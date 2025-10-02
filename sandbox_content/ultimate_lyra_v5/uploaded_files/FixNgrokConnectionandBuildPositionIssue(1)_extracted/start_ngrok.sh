#!/bin/bash
set -e

echo "🚀 Starting Ultimate Ngrok Container..."

# Validate environment
if [ -z "$NGROK_AUTHTOKEN" ]; then
    echo "❌ NGROK_AUTHTOKEN not set"
    exit 1
fi

# Set authtoken
ngrok authtoken $NGROK_AUTHTOKEN

# Create log directory
mkdir -p /app/logs

# Start tunnel manager
echo "🔗 Starting tunnel manager..."
python3 tunnel_manager.py &

# Start ngrok with all tunnels
echo "🌐 Starting all tunnels..."
ngrok start --all --config ngrok_config.yml --log stdout
