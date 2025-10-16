#!/bin/bash

echo "🔑 OPENROUTER API KEYS SETUP"
echo "=============================="
echo ""
echo "This script will help you configure your OpenRouter API keys."
echo ""

# Check if config.json already exists
if [ -f "config.json" ]; then
    echo "⚠️  config.json already exists!"
    read -p "Do you want to overwrite it? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled."
        exit 0
    fi
fi

# Copy template
cp config_template.json config.json

echo "📝 Please enter your OpenRouter API keys."
echo "   (You can add up to 8 keys for load balancing)"
echo "   (Press Enter to skip a key)"
echo ""

# Array to store keys
declare -a keys

for i in {1..8}; do
    read -p "API Key $i: " key
    if [ ! -z "$key" ]; then
        keys+=("$key")
    fi
done

# If no keys entered, show instructions
if [ ${#keys[@]} -eq 0 ]; then
    echo ""
    echo "❌ No API keys entered!"
    echo ""
    echo "📚 HOW TO GET OPENROUTER API KEYS:"
    echo ""
    echo "1. Go to https://openrouter.ai/"
    echo "2. Sign up or log in"
    echo "3. Go to Keys section"
    echo "4. Create a new API key"
    echo "5. Copy the key (starts with 'sk-or-v1-...')"
    echo "6. Run this script again and paste your key"
    echo ""
    echo "💡 TIP: You can create multiple keys for better rate limits!"
    echo ""
    exit 1
fi

# Update config.json with actual keys
python3 << EOF
import json

with open('config.json', 'r') as f:
    config = json.load(f)

keys = ${keys[@]@Q}
config['openrouter_api_keys'] = [k.strip('"') for k in keys.split()]

with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

print(f"\n✅ Configuration saved with {len(config['openrouter_api_keys'])} API key(s)!")
EOF

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Your configuration is saved in config.json"
echo ""
echo "Next steps:"
echo "1. Review config.json to customize settings"
echo "2. Run: python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py"
echo ""

