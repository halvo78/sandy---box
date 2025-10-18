#!/bin/bash

echo "🔧 UPDATING TO FIXED VERSION..."
echo "================================"
echo ""

cd ~/ultimate_lyra_systems

# Download the fixed Python file
echo "📥 Downloading fixed Python file..."
wget -O ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py https://github.com/halvo78/sandy---box/raw/main/ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py

echo ""
echo "✅ Updated successfully!"
echo ""
echo "🚀 Starting the system..."
echo ""

# Activate venv and run
source venv/bin/activate
python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py

