#!/bin/bash

echo "============================================================"
echo "🚀 DEPLOYING ULTIMATE AI HIVE MIND TRADING SYSTEM"
echo "============================================================"
echo ""

cd ~/ultimate_lyra_systems

# Download working config
echo "📥 Downloading working configuration..."
wget -q https://github.com/halvo78/sandy---box/raw/main/config_working.json -O config.json

if [ $? -eq 0 ]; then
    echo "✅ Configuration downloaded successfully!"
else
    echo "❌ Failed to download configuration"
    exit 1
fi

# Show config summary
echo ""
echo "📊 Configuration Summary:"
echo "  - AI Team: 20 models (including all Grok variants)"
echo "  - Starting Capital: $1,000,000"
echo "  - Coins: 8 (BTC, ETH, SOL, ADA, XRP, DOT, MATIC, AVAX)"
echo "  - Timeframes: 6 (1m, 5m, 15m, 1h, 4h, 1d)"
echo "  - Strategies: 16 types"
echo "  - Mode: TURBO (all coins, all timeframes, unlimited positions)"
echo ""

# Activate venv if it exists
if [ -d "venv" ]; then
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
else
    echo "⚠️  Virtual environment not found, using system Python"
fi

# Start the system
echo ""
echo "🚀 Starting the ULTIMATE AI HIVE MIND TRADING SYSTEM..."
echo ""
echo "============================================================"
echo ""

python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py

echo ""
echo "============================================================"
echo "✅ System stopped"
echo "============================================================"

