#!/bin/bash

echo "🔧 FIXING CONFIG.JSON NOW..."
echo ""

cd ~/ultimate_lyra_systems

# Download config.json directly from GitHub
wget -O config.json https://github.com/halvo78/sandy---box/raw/main/config.json

if [ -f "config.json" ]; then
    echo "✅ config.json downloaded successfully!"
    echo ""
    echo "Contents:"
    head -10 config.json
    echo ""
    echo "🎉 Fixed! Now restart the system:"
    echo ""
    echo "  source venv/bin/activate"
    echo "  python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py"
    echo ""
else
    echo "❌ Failed to download config.json"
    echo ""
    echo "Manual fix: Create config.json with your API keys:"
    echo ""
    cat > config.json << 'EOF'
{
  "openrouter_api_keys": [
    "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",
    "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",
    "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",
    "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"
  ]
}
EOF
    echo "✅ Created config.json manually!"
fi

