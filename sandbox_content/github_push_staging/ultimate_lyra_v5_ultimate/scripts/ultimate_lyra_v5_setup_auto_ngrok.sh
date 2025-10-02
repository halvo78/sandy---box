#!/bin/bash
set -e

echo "🚀 Setting up Auto Ngrok Manager..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as the correct user
if [ "$USER" != "halvolyra" ]; then
    print_error "This script should be run as user 'halvolyra'"
    print_status "Please run: su - halvolyra"
    exit 1
fi

# Create the ultimate_lyra_systems directory if it doesn't exist
LYRA_DIR="/home/halvolyra/ultimate_lyra_systems"
if [ ! -d "$LYRA_DIR" ]; then
    print_status "Creating $LYRA_DIR directory..."
    mkdir -p "$LYRA_DIR"
fi

# Copy the auto manager script
print_status "Installing auto_ngrok_manager.py..."
cp auto_ngrok_manager.py "$LYRA_DIR/"
chmod +x "$LYRA_DIR/auto_ngrok_manager.py"

# Install required Python packages
print_status "Installing required Python packages..."
cd "$LYRA_DIR"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_status "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install packages
source venv/bin/activate
pip install --upgrade pip
pip install requests psutil flask aiohttp

# Create improved ingest_gateway.py if it doesn't exist
if [ ! -f "$LYRA_DIR/ingest_gateway.py" ]; then
    print_status "Creating improved ingest_gateway.py..."
    cat > "$LYRA_DIR/ingest_gateway.py" << 'EOF'
#!/usr/bin/env python3
"""
Improved Ingest Gateway with better error handling and stability
"""

import os
import json
import subprocess
import logging
from datetime import datetime
from flask import Flask, request, jsonify
import signal
import sys

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def signal_handler(signum, frame):
    logger.info(f"Received signal {signum}, shutting down gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "ingest_gateway",
        "version": "2.0"
    })

@app.route('/ingest/event', methods=['POST'])
def ingest_event():
    try:
        data = request.get_json()
        
        if not data or data.get('type') != 'COMMAND':
            return jsonify({"error": "Invalid request format"}), 400
        
        steps = data.get('steps', [])
        results = []
        
        for step in steps:
            command = step.get('run', '')
            if not command:
                continue
            
            try:
                # Execute command with timeout
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    cwd='/home/halvolyra/ultimate_lyra_systems'
                )
                
                results.append({
                    "command": command,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "returncode": result.returncode,
                    "success": result.returncode == 0
                })
                
            except subprocess.TimeoutExpired:
                results.append({
                    "command": command,
                    "error": "Command timed out after 30 seconds",
                    "success": False
                })
            except Exception as e:
                results.append({
                    "command": command,
                    "error": str(e),
                    "success": False
                })
        
        return jsonify({
            "status": "completed",
            "results": results,
            "timestamp": datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    logger.info("🚀 Starting Improved Ingest Gateway on port 8081")
    app.run(host='0.0.0.0', port=8081, debug=False, threaded=True)
EOF
    chmod +x "$LYRA_DIR/ingest_gateway.py"
fi

# Install systemd service
print_status "Installing systemd service..."
sudo cp auto-ngrok-manager.service /etc/systemd/system/
sudo systemctl daemon-reload

# Enable and start the service
print_status "Enabling and starting auto-ngrok-manager service..."
sudo systemctl enable auto-ngrok-manager
sudo systemctl start auto-ngrok-manager

# Wait a moment and check status
sleep 3
if sudo systemctl is-active --quiet auto-ngrok-manager; then
    print_status "✅ Auto Ngrok Manager service is running!"
else
    print_error "❌ Service failed to start. Checking logs..."
    sudo journalctl -u auto-ngrok-manager --no-pager -n 20
fi

# Create monitoring script
print_status "Creating monitoring script..."
cat > "$LYRA_DIR/check_ngrok_status.sh" << 'EOF'
#!/bin/bash

echo "📊 Ngrok System Status Check"
echo "============================"

# Check service status
echo "🔧 Service Status:"
sudo systemctl status auto-ngrok-manager --no-pager -l

echo ""
echo "🌐 Connection Tests:"

# Test local gateway
if curl -s http://localhost:8081/health > /dev/null; then
    echo "✅ Local gateway: HEALTHY"
else
    echo "❌ Local gateway: DOWN"
fi

# Test ngrok tunnel
if curl -s https://3ce37fa57d09.ngrok.app/health > /dev/null; then
    echo "✅ Ngrok tunnel: HEALTHY"
else
    echo "❌ Ngrok tunnel: DOWN"
fi

echo ""
echo "📋 Process Information:"
ps aux | grep -E "(ingest_gateway|ngrok)" | grep -v grep

echo ""
echo "📊 Port Status:"
sudo lsof -i :8081 | head -5

echo ""
echo "📝 Recent Logs:"
sudo journalctl -u auto-ngrok-manager --no-pager -n 10
EOF

chmod +x "$LYRA_DIR/check_ngrok_status.sh"

# Create restart script
print_status "Creating manual restart script..."
cat > "$LYRA_DIR/restart_ngrok.sh" << 'EOF'
#!/bin/bash

echo "🔄 Manually restarting Ngrok system..."

# Restart the service
sudo systemctl restart auto-ngrok-manager

echo "⏳ Waiting for service to start..."
sleep 5

# Check status
./check_ngrok_status.sh
EOF

chmod +x "$LYRA_DIR/restart_ngrok.sh"

print_status "✅ Auto Ngrok Manager setup complete!"
print_status ""
print_status "📋 Available commands:"
print_status "  Check status: ./check_ngrok_status.sh"
print_status "  Manual restart: ./restart_ngrok.sh"
print_status "  View logs: sudo journalctl -u auto-ngrok-manager -f"
print_status "  Stop service: sudo systemctl stop auto-ngrok-manager"
print_status "  Start service: sudo systemctl start auto-ngrok-manager"
print_status ""
print_status "🎉 The system will now automatically monitor and restart ngrok connections!"

# Final status check
echo ""
echo "🔍 Final Status Check:"
"$LYRA_DIR/check_ngrok_status.sh"
