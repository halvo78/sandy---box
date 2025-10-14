#!/bin/bash
################################################################################
# ULTIMATE PERMANENT NGROK SYSTEM
# Never lose your Ngrok setup again!
# Auto-save | Auto-restart | Auto-backup | Auto-document
################################################################################

set -e

SYSTEM_DIR="$HOME/ultimate_lyra_systems"
NGROK_DIR="$SYSTEM_DIR/ngrok_permanent"
LOGS_DIR="$SYSTEM_DIR/logs"
BACKUP_DIR="$SYSTEM_DIR/backups/ngrok"
NGROK_AUTHTOKEN="33usxScH7BM8zGJ0SMfvEqFCtqy_6mSSBRWTsHJ7EWXeoCpN2"

echo "======================================================================"
echo "🚀 ULTIMATE PERMANENT NGROK SYSTEM - INSTALLATION"
echo "======================================================================"
echo ""

# Create directories
echo "📁 Creating directories..."
mkdir -p "$NGROK_DIR"
mkdir -p "$LOGS_DIR"
mkdir -p "$BACKUP_DIR"
mkdir -p "$HOME/.config/ngrok"

# 1. CREATE NGROK CONFIG FILE
echo "⚙️  Creating Ngrok config..."
cat > "$HOME/.config/ngrok/ngrok.yml" << EOF
version: "2"
authtoken: $NGROK_AUTHTOKEN
region: ap
web_addr: localhost:4040
log_level: info
log_format: json
log: $LOGS_DIR/ngrok.log

tunnels:
  file_server:
    proto: http
    addr: 9000
    inspect: true
    metadata: "file_server"
  
  dashboard:
    proto: http
    addr: 5000
    inspect: true
    metadata: "dashboard"
  
  production:
    proto: http
    addr: 5001
    inspect: true
    metadata: "production"
EOF

echo "✅ Ngrok config created: $HOME/.config/ngrok/ngrok.yml"

# 2. CREATE SYSTEMD SERVICE
echo "🔧 Creating systemd service..."
sudo tee /etc/systemd/system/ngrok-permanent.service > /dev/null << EOF
[Unit]
Description=Ngrok Permanent Tunnel System
After=network-online.target
Wants=network-online.target
Documentation=https://ngrok.com/docs

[Service]
Type=simple
User=$USER
WorkingDirectory=$SYSTEM_DIR
Environment="HOME=$HOME"
ExecStart=/usr/local/bin/ngrok start --all --config=$HOME/.config/ngrok/ngrok.yml --log=stdout --log-format=json
Restart=always
RestartSec=10
StandardOutput=append:$LOGS_DIR/ngrok_service.log
StandardError=append:$LOGS_DIR/ngrok_service_error.log

# Security
NoNewPrivileges=true
PrivateTmp=true

# Health check
ExecStartPost=/bin/sleep 5
ExecStartPost=/bin/bash -c 'curl -s http://localhost:4040/api/tunnels > $LOGS_DIR/ngrok_tunnels_latest.json'

[Install]
WantedBy=multi-user.target
EOF

echo "✅ Systemd service created: /etc/systemd/system/ngrok-permanent.service"

# 3. CREATE MONITORING SCRIPT
echo "📊 Creating monitoring script..."
cat > "$NGROK_DIR/monitor_ngrok.sh" << 'EOF'
#!/bin/bash
# Ngrok Monitoring Script

LOGS_DIR="$HOME/ultimate_lyra_systems/logs"

echo "======================================================================"
echo "📊 NGROK TUNNEL MONITOR"
echo "======================================================================"
echo ""

# Check if ngrok is running
if ! pgrep -x "ngrok" > /dev/null; then
    echo "❌ Ngrok is NOT running!"
    echo "   Run: sudo systemctl start ngrok-permanent"
    exit 1
fi

echo "✅ Ngrok is running (PID: $(pgrep -x ngrok))"
echo ""

# Get tunnel info
if curl -s http://localhost:4040/api/tunnels > /dev/null 2>&1; then
    TUNNELS=$(curl -s http://localhost:4040/api/tunnels | python3 -c "
import sys, json
data = json.load(sys.stdin)
for t in data.get('tunnels', []):
    print(f\"🔗 {t['name']:15} {t['public_url']}\")
")
    
    if [ -n "$TUNNELS" ]; then
        echo "Active Tunnels:"
        echo "$TUNNELS"
    else
        echo "⚠️  No active tunnels found"
    fi
else
    echo "❌ Cannot connect to Ngrok API (port 4040)"
fi

echo ""
echo "======================================================================"
echo "📄 Logs: $LOGS_DIR/ngrok_service.log"
echo "🌐 Dashboard: http://localhost:4040"
echo "======================================================================"
EOF

chmod +x "$NGROK_DIR/monitor_ngrok.sh"
echo "✅ Monitoring script created: $NGROK_DIR/monitor_ngrok.sh"

# 4. CREATE BACKUP SCRIPT
echo "💾 Creating backup script..."
cat > "$NGROK_DIR/backup_ngrok.sh" << 'EOF'
#!/bin/bash
# Ngrok Backup Script - Saves everything to GitHub

SYSTEM_DIR="$HOME/ultimate_lyra_systems"
BACKUP_DIR="$SYSTEM_DIR/backups/ngrok"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "💾 Backing up Ngrok configuration..."

# Create backup directory
mkdir -p "$BACKUP_DIR/$TIMESTAMP"

# Backup config
cp "$HOME/.config/ngrok/ngrok.yml" "$BACKUP_DIR/$TIMESTAMP/"

# Backup tunnel info
if curl -s http://localhost:4040/api/tunnels > /dev/null 2>&1; then
    curl -s http://localhost:4040/api/tunnels > "$BACKUP_DIR/$TIMESTAMP/tunnels.json"
fi

# Backup logs (last 1000 lines)
tail -1000 "$SYSTEM_DIR/logs/ngrok_service.log" > "$BACKUP_DIR/$TIMESTAMP/ngrok_service.log" 2>/dev/null || true

# Create backup summary
cat > "$BACKUP_DIR/$TIMESTAMP/BACKUP_INFO.txt" << SUMMARY
Ngrok Backup
============
Timestamp: $TIMESTAMP
Date: $(date)
Hostname: $(hostname)
User: $(whoami)

Files Backed Up:
- ngrok.yml (config)
- tunnels.json (active tunnels)
- ngrok_service.log (last 1000 lines)

Restore Instructions:
1. Copy ngrok.yml to ~/.config/ngrok/ngrok.yml
2. Run: sudo systemctl restart ngrok-permanent
3. Verify: ~/ultimate_lyra_systems/ngrok_permanent/monitor_ngrok.sh
SUMMARY

echo "✅ Backup created: $BACKUP_DIR/$TIMESTAMP"

# Push to GitHub if in git repo
if [ -d "$HOME/sandy---box/.git" ]; then
    echo "📤 Pushing to GitHub..."
    cd "$HOME/sandy---box"
    
    # Copy backup to repo
    mkdir -p ngrok_backups
    cp -r "$BACKUP_DIR/$TIMESTAMP" "ngrok_backups/"
    
    git add ngrok_backups/
    git commit -m "🔒 Ngrok backup $TIMESTAMP" || true
    git push || echo "⚠️  Git push failed (may need authentication)"
fi

echo "✅ Backup complete!"
EOF

chmod +x "$NGROK_DIR/backup_ngrok.sh"
echo "✅ Backup script created: $NGROK_DIR/backup_ngrok.sh"

# 5. CREATE RECOVERY SCRIPT
echo "🔄 Creating recovery script..."
cat > "$NGROK_DIR/recover_ngrok.sh" << 'EOF'
#!/bin/bash
# Ngrok Recovery Script

echo "🔄 Recovering Ngrok..."

# Stop service
sudo systemctl stop ngrok-permanent

# Kill any running ngrok processes
pkill ngrok || true

# Wait
sleep 2

# Start service
sudo systemctl start ngrok-permanent

# Wait for startup
sleep 5

# Check status
if pgrep -x "ngrok" > /dev/null; then
    echo "✅ Ngrok recovered successfully!"
    ~/ultimate_lyra_systems/ngrok_permanent/monitor_ngrok.sh
else
    echo "❌ Recovery failed. Check logs:"
    echo "   sudo journalctl -u ngrok-permanent -n 50"
fi
EOF

chmod +x "$NGROK_DIR/recover_ngrok.sh"
echo "✅ Recovery script created: $NGROK_DIR/recover_ngrok.sh"

# 6. CREATE MANAGEMENT COMMANDS
echo "🛠️  Creating management commands..."
cat > "$NGROK_DIR/ngrok_commands.sh" << 'EOF'
#!/bin/bash
# Ngrok Management Commands

case "$1" in
    start)
        echo "🚀 Starting Ngrok..."
        sudo systemctl start ngrok-permanent
        sleep 5
        ~/ultimate_lyra_systems/ngrok_permanent/monitor_ngrok.sh
        ;;
    stop)
        echo "🛑 Stopping Ngrok..."
        sudo systemctl stop ngrok-permanent
        ;;
    restart)
        echo "🔄 Restarting Ngrok..."
        sudo systemctl restart ngrok-permanent
        sleep 5
        ~/ultimate_lyra_systems/ngrok_permanent/monitor_ngrok.sh
        ;;
    status)
        ~/ultimate_lyra_systems/ngrok_permanent/monitor_ngrok.sh
        ;;
    logs)
        echo "📄 Ngrok Logs (last 50 lines):"
        tail -50 ~/ultimate_lyra_systems/logs/ngrok_service.log
        ;;
    backup)
        ~/ultimate_lyra_systems/ngrok_permanent/backup_ngrok.sh
        ;;
    recover)
        ~/ultimate_lyra_systems/ngrok_permanent/recover_ngrok.sh
        ;;
    *)
        echo "Ngrok Management Commands:"
        echo "  start   - Start Ngrok tunnels"
        echo "  stop    - Stop Ngrok tunnels"
        echo "  restart - Restart Ngrok tunnels"
        echo "  status  - Show tunnel status"
        echo "  logs    - Show recent logs"
        echo "  backup  - Backup configuration"
        echo "  recover - Recover from failure"
        ;;
esac
EOF

chmod +x "$NGROK_DIR/ngrok_commands.sh"
echo "✅ Management commands created: $NGROK_DIR/ngrok_commands.sh"

# 7. CREATE CRON JOB FOR AUTO-BACKUP
echo "⏰ Setting up auto-backup..."
(crontab -l 2>/dev/null; echo "0 * * * * $NGROK_DIR/backup_ngrok.sh >> $LOGS_DIR/ngrok_backup.log 2>&1") | crontab -
echo "✅ Auto-backup scheduled (hourly)"

# 8. CONFIGURE NGROK AUTHTOKEN
echo "🔐 Configuring Ngrok authtoken..."
ngrok config add-authtoken "$NGROK_AUTHTOKEN"
echo "✅ Authtoken configured"

# 9. RELOAD SYSTEMD AND ENABLE SERVICE
echo "🔧 Enabling systemd service..."
sudo systemctl daemon-reload
sudo systemctl enable ngrok-permanent
echo "✅ Service enabled (will start on boot)"

# 10. START THE SERVICE
echo "🚀 Starting Ngrok..."
sudo systemctl start ngrok-permanent
sleep 5

# 11. VERIFY INSTALLATION
echo ""
echo "======================================================================"
echo "✅ INSTALLATION COMPLETE!"
echo "======================================================================"
echo ""
echo "📊 Checking status..."
"$NGROK_DIR/monitor_ngrok.sh"

echo ""
echo "======================================================================"
echo "🎯 QUICK COMMANDS:"
echo "======================================================================"
echo ""
echo "  Monitor:  $NGROK_DIR/ngrok_commands.sh status"
echo "  Logs:     $NGROK_DIR/ngrok_commands.sh logs"
echo "  Backup:   $NGROK_DIR/ngrok_commands.sh backup"
echo "  Recover:  $NGROK_DIR/ngrok_commands.sh recover"
echo ""
echo "  Or use the shortcut:"
echo "  alias ngrok-manage='$NGROK_DIR/ngrok_commands.sh'"
echo ""
echo "======================================================================"
echo "📚 DOCUMENTATION:"
echo "======================================================================"
echo ""
echo "  Config:   $HOME/.config/ngrok/ngrok.yml"
echo "  Logs:     $LOGS_DIR/ngrok_service.log"
echo "  Backups:  $BACKUP_DIR"
echo "  Scripts:  $NGROK_DIR"
echo ""
echo "======================================================================"
echo "🎉 YOUR NGROK IS NOW PERMANENT AND BULLETPROOF!"
echo "======================================================================"

