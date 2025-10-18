#!/bin/bash
#
# DOWNLOAD AND DEPLOY AI TRADING SYSTEM
# Run this script on your local Ubuntu machine
#

set -e

echo "🚀 AI TRADING SYSTEM - AUTOMATED DEPLOYMENT"
echo "==========================================="
echo ""

# Configuration
PACKAGE_NAME="COMPLETE_AI_TRADING_SYSTEM"
DEPLOY_DIR="$HOME/ai_trading_system"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}📍 Deployment directory: $DEPLOY_DIR${NC}"
echo ""

# Create deployment directory
mkdir -p "$DEPLOY_DIR"
cd "$DEPLOY_DIR"

# Download package
echo -e "${YELLOW}📥 Downloading AI Trading System package...${NC}"
if [ -f "$PACKAGE_NAME.tar.gz" ]; then
    echo "Package already exists, removing old version..."
    rm "$PACKAGE_NAME.tar.gz"
fi

# Try to download from local file server
if curl -f -o "$PACKAGE_NAME.tar.gz" "http://localhost:8000/$PACKAGE_NAME.tar.gz" 2>/dev/null; then
    echo -e "${GREEN}✅ Downloaded from local file server${NC}"
else
    echo "⚠️  Could not download from local file server"
    echo "Please ensure your file server is running and the package is available"
    exit 1
fi

# Verify download
if [ ! -f "$PACKAGE_NAME.tar.gz" ]; then
    echo "❌ Download failed"
    exit 1
fi

FILE_SIZE=$(ls -lh "$PACKAGE_NAME.tar.gz" | awk '{print $5}')
echo -e "${GREEN}✅ Package downloaded successfully (Size: $FILE_SIZE)${NC}"
echo ""

# Extract package
echo -e "${YELLOW}📦 Extracting package...${NC}"
tar -xzf "$PACKAGE_NAME.tar.gz"
echo -e "${GREEN}✅ Package extracted${NC}"
echo ""

# Navigate into directory
cd "$PACKAGE_NAME"

# Make scripts executable
chmod +x scripts/*.sh

# Display README
echo -e "${BLUE}📖 README:${NC}"
echo "----------------------------------------"
head -30 README.md
echo "----------------------------------------"
echo ""

# Ask user if they want to start now
echo -e "${YELLOW}🎯 Ready to start the AI Trading System?${NC}"
echo ""
echo "To start the system, run:"
echo -e "${GREEN}  cd $DEPLOY_DIR/$PACKAGE_NAME${NC}"
echo -e "${GREEN}  ./scripts/start_all.sh${NC}"
echo ""
echo "To view the full README:"
echo -e "${GREEN}  cat README.md${NC}"
echo ""
echo -e "${BLUE}✅ Deployment preparation complete!${NC}"

