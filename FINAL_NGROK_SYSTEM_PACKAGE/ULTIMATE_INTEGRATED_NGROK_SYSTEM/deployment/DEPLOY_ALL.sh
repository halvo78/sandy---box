#!/bin/bash
#
# MASTER DEPLOYMENT SCRIPT
# Deploy all 10 components with permanent Ngrok integration
#

set -e

echo "🚀 DEPLOYING ULTIMATE INTEGRATED NGROK SYSTEM"
echo "=============================================="
echo ""

# Configuration
USER_HOME="/home/halvolyra"
DEPLOY_DIR="$USER_HOME/ultimate_lyra_systems"
NGROK_CONFIG_DIR="$USER_HOME/.config/ngrok"

# Create directories
echo "📁 Creating directory structure..."
mkdir -p "$DEPLOY_DIR/logs"
mkdir -p "$DEPLOY_DIR/backups"
mkdir -p "$NGROK_CONFIG_DIR"

# Install Ngrok if not present
if ! command -v ngrok &> /dev/null; then
    echo "📥 Installing Ngrok..."
    curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
    sudo apt update
    sudo apt install -y ngrok
fi

# Copy Ngrok configuration
echo "⚙️  Configuring Ngrok..."
cp /home/ubuntu/ULTIMATE_INTEGRATED_NGROK_SYSTEM/config/ngrok.yml "$NGROK_CONFIG_DIR/ngrok.yml"

# Install systemd service
echo "🔧 Installing systemd service..."
sudo cp /home/ubuntu/ULTIMATE_INTEGRATED_NGROK_SYSTEM/config/ngrok-permanent.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ngrok-permanent.service
sudo systemctl start ngrok-permanent.service

# Wait for Ngrok to start
echo "⏳ Waiting for Ngrok to initialize..."
sleep 5

# Get tunnel URLs
echo ""
echo "🌐 NGROK TUNNEL URLS:"
echo "===================="
curl -s http://localhost:4040/api/tunnels | python3 -m json.tool | grep -E '"public_url"|"name"'

echo ""
echo "✅ DEPLOYMENT COMPLETE!"
echo ""
echo "📊 System Status:"
echo "  - Ngrok Service: $(systemctl is-active ngrok-permanent.service)"
echo "  - Ngrok Dashboard: http://localhost:4040"
echo "  - Logs: $DEPLOY_DIR/logs/"
echo ""
echo "🎯 Next Steps:"
echo "  1. Start individual component services"
echo "  2. Verify all tunnels are accessible"
echo "  3. Configure monitoring and alerts"
echo "  4. Run integration tests"
echo ""
