#!/bin/bash
# One-line deployment for Ubuntu

cd ~/ultimate_lyra_systems
echo "📥 Downloading optimized code package..."
wget -q https://github.com/halvo78/sandy---box/raw/main/OPTIMIZED_CODE_PACKAGE.tar.gz
echo "📂 Extracting..."
tar -xzf OPTIMIZED_CODE_PACKAGE.tar.gz
cd OPTIMIZED_CODE_PACKAGE
echo "🚀 Deploying..."
./deploy.sh
