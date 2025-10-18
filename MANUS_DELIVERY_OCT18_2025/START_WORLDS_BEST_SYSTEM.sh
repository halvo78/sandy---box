#!/bin/bash

echo "🌟 WORLD'S BEST PAPER TRADING SYSTEM 🌟"
echo "========================================"
echo ""
echo "Starting the world's most comprehensive AI-powered trading system..."
echo ""

# Create directories
mkdir -p data
mkdir -p logs

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found! Please install Python 3.8+"
    exit 1
fi

echo "✅ Python 3 found"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -q ccxt pandas numpy requests 2>&1 | grep -v "already satisfied" || true

echo "✅ Dependencies installed"

# Run the system
echo ""
echo "🚀 Starting World's Best Paper Trading System..."
echo ""
echo "Features:"
echo "  ✅ 50+ AI Professionals"
echo "  ✅ 18 Trading Strategies"
echo "  ✅ 538 OpenRouter Models Available"
echo "  ✅ Progressive Rollout"
echo "  ✅ Hive Mind Learning"
echo ""
echo "Starting capital: $10,000 (paper trading)"
echo "Current stage: 1 (BTC only)"
echo ""
echo "Press Ctrl+C to stop"
echo ""
echo "========================================"
echo ""

# Run the system
python3 WORLDS_BEST_PAPER_TRADING_SYSTEM.py 2>&1 | tee logs/system_$(date +%Y%m%d_%H%M%S).log

