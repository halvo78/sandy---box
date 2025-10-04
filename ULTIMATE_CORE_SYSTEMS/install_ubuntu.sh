#!/bin/bash
# Ultimate Lyra Trading System - Ubuntu Installation Script
# Automated installation for production deployment

set -e

echo "🚀 Ultimate Lyra Trading System - Ubuntu Installation"
echo "=================================================="

# Update system
echo "📦 Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
sudo apt install -y python3 python3-pip python3-venv

# Install Node.js
echo "📦 Installing Node.js..."
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install system tools
echo "🔧 Installing system tools..."
sudo apt install -y git curl wget unzip build-essential

# Create virtual environment
echo "🌐 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python packages
echo "📚 Installing Python packages..."
pip install requests pandas numpy matplotlib plotly fastapi uvicorn websocket-client ccxt

# Install Node.js packages
echo "📦 Installing Node.js packages..."
npm install -g pm2

# Set permissions
echo "🔐 Setting permissions..."
chmod +x BUILD_DEPLOYMENT/*.sh
chmod +x UTILITIES_TOOLS/*.py

# Create logs directory
mkdir -p logs

echo "✅ Installation complete!"
echo "🎯 Next steps:"
echo "1. Configure API keys in CONFIGURATION/MASTER_CONFIGURATION.json"
echo "2. Run: python3 AI_CONSENSUS/ULTIMATE_AI_CONSENSUS_SYSTEM.py"
echo "3. Monitor: tail -f logs/system.log"
