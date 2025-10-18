#!/usr/bin/env python3
"""
Push deployment files to local Ubuntu system via ngrok
"""
import os
import subprocess
import sys

# Files to push
FILES = {
    "ULTIMATE_AI_TRADING_SYSTEM_COMPLETE.py": "/home/halvolyra/ultimate_lyra_systems/",
    "config_production.json": "/home/halvolyra/ultimate_lyra_systems/config.json",
    "COMPLETE_FIX_SUMMARY.md": "/home/halvolyra/ultimate_lyra_systems/",
    "DEPLOYMENT_PACKAGE/DEPLOYMENT_INSTRUCTIONS.md": "/home/halvolyra/ultimate_lyra_systems/"
}

# Ngrok URL (we'll use it to determine the target)
NGROK_URL = "https://ef70762389ce.ngrok.app"

print("🚀 Pushing files to local Ubuntu system...")
print("=" * 80)

# Since ngrok is serving files, we need to create files there
# The directory being served is /home/halvolyra on the local Ubuntu

# Create a shell script that will be downloaded and executed
script_content = """#!/bin/bash
# Auto-generated deployment script

cd /home/halvolyra/ultimate_lyra_systems || mkdir -p /home/halvolyra/ultimate_lyra_systems
cd /home/halvolyra/ultimate_lyra_systems

echo "📥 Downloading files from sandbox..."

# Download Python file
curl -s -o ULTIMATE_AI_TRADING_SYSTEM_COMPLETE.py \\
  "https://ef70762389ce.ngrok.app/ULTIMATE_AI_TRADING_SYSTEM_COMPLETE.py" 2>/dev/null

# Download config
curl -s -o config.json \\
  "https://ef70762389ce.ngrok.app/config_production.json" 2>/dev/null

# Download docs
curl -s -o COMPLETE_FIX_SUMMARY.md \\
  "https://ef70762389ce.ngrok.app/COMPLETE_FIX_SUMMARY.md" 2>/dev/null

curl -s -o DEPLOYMENT_INSTRUCTIONS.md \\
  "https://ef70762389ce.ngrok.app/DEPLOYMENT_PACKAGE/DEPLOYMENT_INSTRUCTIONS.md" 2>/dev/null

echo "✅ Files downloaded!"
echo ""
echo "Files in $(pwd):"
ls -lh

echo ""
echo "🎯 To run the system:"
echo "  python3 ULTIMATE_AI_TRADING_SYSTEM_COMPLETE.py"
"""

with open("/tmp/deploy_script.sh", "w") as f:
    f.write(script_content)

print("✅ Created deployment script at /tmp/deploy_script.sh")
print("")
print("📋 Instructions for your local Ubuntu:")
print("=" * 80)
print("1. Download the deployment script:")
print(f"   curl -o deploy.sh {NGROK_URL}/tmp/deploy_script.sh")
print("")
print("2. Make it executable:")
print("   chmod +x deploy.sh")
print("")
print("3. Run it:")
print("   ./deploy.sh")
print("=" * 80)

