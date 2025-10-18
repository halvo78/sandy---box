#!/bin/bash

echo "🚀 DEPLOYING PERFECT FIX TO UBUNTU"
echo "=================================="
echo ""

cd ~/ultimate_lyra_systems

# Download perfect config.json
echo "📥 Downloading config.json..."
wget -O config.json https://github.com/halvo78/sandy---box/raw/main/config.json

# Download latest Python file
echo "📥 Downloading latest system file..."
wget -O ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py https://github.com/halvo78/sandy---box/raw/main/ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py

# Verify files
if [ -f "config.json" ] && [ -f "ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py" ]; then
    echo "✅ All files downloaded!"
    echo ""
    echo "🎉 READY TO START!"
    echo ""
    echo "Run:"
    echo "  cd ~/ultimate_lyra_systems"
    echo "  source venv/bin/activate"
    echo "  python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py"
    echo ""
else
    echo "❌ Some files failed to download"
    exit 1
fi
