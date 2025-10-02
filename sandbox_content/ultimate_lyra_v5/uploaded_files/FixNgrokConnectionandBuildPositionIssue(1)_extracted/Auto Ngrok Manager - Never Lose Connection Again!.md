# Auto Ngrok Manager - Never Lose Connection Again!

This system automatically monitors and restarts your ngrok tunnel and ingest gateway to prevent the connection drops you've been experiencing.

## 🎯 What This Solves

- **Automatic Detection** of failed ngrok tunnels and ingest gateways
- **Auto-Restart** of crashed or hung processes
- **Port Cleanup** when processes get stuck
- **Zombie Process Removal** that holds ports hostage
- **Continuous Monitoring** every 30 seconds
- **Graceful Recovery** with intelligent restart logic
- **System Service** that starts automatically on boot

## 📦 Installation

### On Your Local Ubuntu Machine

1. **Copy the files to your system:**
```bash
# Copy all files to your ultimate_lyra_systems directory
scp auto_ngrok_manager.py halvolyra@your-machine:/home/halvolyra/ultimate_lyra_systems/
scp auto-ngrok-manager.service halvolyra@your-machine:/home/halvolyra/ultimate_lyra_systems/
scp setup_auto_ngrok.sh halvolyra@your-machine:/home/halvolyra/ultimate_lyra_systems/
```

2. **Run the setup script:**
```bash
cd /home/halvolyra/ultimate_lyra_systems
chmod +x setup_auto_ngrok.sh
./setup_auto_ngrok.sh
```

That's it! The system is now running automatically.

## 🔧 How It Works

### Monitoring Loop
- Checks every 30 seconds if both local gateway and ngrok tunnel are responding
- Detects zombie processes that hold ports
- Identifies when processes crash or hang

### Auto-Recovery Process
1. **Detect Problem** - Health checks fail
2. **Kill Processes** - Terminates stuck ingest_gateway processes
3. **Free Ports** - Cleans up port 8081 if blocked
4. **Restart Gateway** - Starts fresh ingest_gateway.py
5. **Verify Success** - Confirms both local and tunnel connections work

### Intelligent Restart Logic
- **Gradual Backoff** - Reduces restart count on successful recoveries
- **Max Restart Limit** - Stops after 10 failed attempts to prevent infinite loops
- **Process Detection** - Finds and kills processes by name and command line
- **Port Management** - Uses `lsof` to identify and kill port-blocking processes

## 📊 Monitoring Commands

### Check Current Status
```bash
cd /home/halvolyra/ultimate_lyra_systems
./check_ngrok_status.sh
```

### Manual Restart
```bash
./restart_ngrok.sh
```

### View Live Logs
```bash
sudo journalctl -u auto-ngrok-manager -f
```

### Service Management
```bash
# Stop the service
sudo systemctl stop auto-ngrok-manager

# Start the service
sudo systemctl start auto-ngrok-manager

# Restart the service
sudo systemctl restart auto-ngrok-manager

# Check service status
sudo systemctl status auto-ngrok-manager
```

## 🚨 Troubleshooting

### If the service won't start:
```bash
# Check for errors
sudo journalctl -u auto-ngrok-manager --no-pager -n 50

# Verify file permissions
ls -la /home/halvolyra/ultimate_lyra_systems/auto_ngrok_manager.py

# Test manually
cd /home/halvolyra/ultimate_lyra_systems
python3 auto_ngrok_manager.py
```

### If connections still drop:
```bash
# Check if ngrok process is running
ps aux | grep ngrok

# Check if port 8081 is blocked
sudo lsof -i :8081

# Manual cleanup
sudo pkill -f ingest_gateway
sudo pkill -f ngrok
./restart_ngrok.sh
```

## 🔍 What Gets Monitored

### Local Gateway Health
- HTTP GET to `http://localhost:8081/health`
- Process status check for `ingest_gateway.py`
- Port 8081 availability

### Ngrok Tunnel Health
- HTTP GET to `https://3ce37fa57d09.ngrok.app/health`
- Connection timeout detection
- Response validation

### Process Management
- Detects zombie/stopped processes
- Kills processes holding port 8081
- Cleans up orphaned ingest_gateway instances

## 📈 Benefits

1. **Zero Manual Intervention** - No more manual `kill -9` commands
2. **Continuous Uptime** - Automatic recovery from failures
3. **Intelligent Monitoring** - Detects multiple failure modes
4. **Boot Persistence** - Starts automatically when system reboots
5. **Comprehensive Logging** - Full audit trail of all actions
6. **Graceful Handling** - Proper cleanup before restart attempts

## 🎉 Result

With this system running, you should **never again** experience:
- Hung ingest gateway processes
- Blocked ports requiring manual cleanup
- Lost ngrok connections
- Manual restart procedures
- Connection timeouts during AI operations

The system runs as a background service and handles all connection management automatically, ensuring your Ultimate Lyra Trading System maintains stable connectivity for AI interactions and system management.

## 📋 Files Included

- `auto_ngrok_manager.py` - Main monitoring and restart logic
- `auto-ngrok-manager.service` - Systemd service definition
- `setup_auto_ngrok.sh` - Automated installation script
- `check_ngrok_status.sh` - Status monitoring script (created during setup)
- `restart_ngrok.sh` - Manual restart script (created during setup)
- Improved `ingest_gateway.py` - More stable gateway with better error handling

This system ensures your ngrok connection stays stable and your AI workflows never get interrupted by connection issues again!
