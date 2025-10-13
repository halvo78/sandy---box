#!/bin/bash
################################################################################
# ONE-COMMAND AUTO-DEPLOY
# Copy and paste this ENTIRE script into your Ubuntu terminal
# It will automatically pull and deploy the complete ecosystem
################################################################################

set -e

echo "======================================================================"
echo "🚀 AUTO-DEPLOYING COMPLETE ECOSYSTEM"
echo "======================================================================"

# Navigate to home
cd ~

# Clone or pull sandy-box repo
if [ -d "sandy---box" ]; then
    echo "📥 Updating sandy---box repo..."
    cd sandy---box
    git pull
else
    echo "📥 Cloning sandy---box repo..."
    git clone https://github.com/halvo78/sandy---box.git
    cd sandy---box
fi

# Copy COMPLETE_ECOSYSTEM.py to trading system
echo "📋 Copying COMPLETE_ECOSYSTEM.py..."
cp COMPLETE_ECOSYSTEM.py ~/ultimate_lyra_systems/ISO_COMPLIANT_SYSTEM/

# Navigate to trading system
cd ~/ultimate_lyra_systems/ISO_COMPLIANT_SYSTEM

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source trading_env/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install aiohttp --quiet

# Show file info
echo ""
echo "======================================================================"
echo "✅ COMPLETE_ECOSYSTEM.py DEPLOYED!"
echo "======================================================================"
ls -lh COMPLETE_ECOSYSTEM.py
echo ""
head -10 COMPLETE_ECOSYSTEM.py
echo ""
echo "======================================================================"
echo "🚀 TO RUN THE COMPLETE ECOSYSTEM:"
echo "======================================================================"
echo ""
echo "Option 1 - Run in foreground (see output):"
echo "  python3 COMPLETE_ECOSYSTEM.py"
echo ""
echo "Option 2 - Run in background:"
echo "  nohup python3 COMPLETE_ECOSYSTEM.py > logs/complete_ecosystem.log 2>&1 &"
echo ""
echo "Option 3 - Run and view logs:"
echo "  python3 COMPLETE_ECOSYSTEM.py 2>&1 | tee logs/complete_ecosystem.log"
echo ""
echo "======================================================================"
echo "📊 WHAT THIS SYSTEM WILL DO:"
echo "======================================================================"
echo "✅ Query 19 AI models (Grok, Claude, GPT-4, Gemini, Llama, Qwen, etc.)"
echo "✅ Get AI consensus for BTC/USDT and ETH/USDT trading signals"
echo "✅ Run continuously every 5 minutes"
echo "✅ Log all decisions and system health"
echo "✅ Auto-restart on errors"
echo "✅ Graceful shutdown on Ctrl+C"
echo "======================================================================"

