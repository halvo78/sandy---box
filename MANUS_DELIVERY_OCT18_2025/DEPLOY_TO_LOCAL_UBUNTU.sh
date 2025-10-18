#!/bin/bash

################################################################################
# 📥 DOWNLOAD AND DEPLOY - Run this on your LOCAL Ubuntu machine
################################################################################
#
# This script will:
# 1. Download the Ultimate AI Trading System from your ngrok file server
# 2. Extract it
# 3. Set up everything
# 4. Start the system
#
################################################################################

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# Banner
echo -e "${PURPLE}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   📥 ULTIMATE AI TRADING SYSTEM - DEPLOYMENT                    ║
║                                                                  ║
║   Downloading from your ngrok file server...                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# IMPORTANT: Update this URL with your actual ngrok file server URL
# You can find it by running: curl http://localhost:4040/api/tunnels | jq
NGROK_URL="YOUR_NGROK_FILE_SERVER_URL"

# Check if URL is set
if [ "$NGROK_URL" = "YOUR_NGROK_FILE_SERVER_URL" ]; then
    echo -e "${RED}❌ ERROR: Please update the NGROK_URL in this script${NC}"
    echo -e "${YELLOW}"
    echo "To find your ngrok URL:"
    echo "1. On your local Ubuntu, run: curl http://localhost:4040/api/tunnels | jq"
    echo "2. Look for the 'file_server' tunnel URL"
    echo "3. Update NGROK_URL in this script with that URL"
    echo -e "${NC}"
    exit 1
fi

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📦 STEP 1: Creating directory${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Create directory
mkdir -p ~/ultimate_ai_trading
cd ~/ultimate_ai_trading

echo -e "${GREEN}✅ Directory created: ~/ultimate_ai_trading${NC}"

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📥 STEP 2: Downloading system${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${YELLOW}Downloading from: ${NGROK_URL}/ULTIMATE_AI_TRADING_COMPLETE.tar.gz${NC}"

# Download
wget -O ULTIMATE_AI_TRADING_COMPLETE.tar.gz "${NGROK_URL}/ULTIMATE_AI_TRADING_COMPLETE.tar.gz"

echo -e "${GREEN}✅ Download complete${NC}"

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📦 STEP 3: Extracting files${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Extract
tar -xzf ULTIMATE_AI_TRADING_COMPLETE.tar.gz

echo -e "${GREEN}✅ Files extracted${NC}"

# List files
echo -e "${YELLOW}Files:${NC}"
ls -lh

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 STEP 4: Making scripts executable${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

chmod +x START_ULTIMATE_AI_TRADING.sh STOP_ULTIMATE_AI_TRADING.sh

echo -e "${GREEN}✅ Scripts are now executable${NC}"

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ DEPLOYMENT COMPLETE!${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                     🚀 READY TO START                            ║${NC}"
echo -e "${PURPLE}╠══════════════════════════════════════════════════════════════════╣${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${GREEN}To start the system:${NC}                                          ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${CYAN}./START_ULTIMATE_AI_TRADING.sh${NC}                                ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${GREEN}To read the full guide:${NC}                                       ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${CYAN}cat ULTIMATE_AI_TRADING_DEPLOYMENT_GUIDE.md${NC}                   ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${GREEN}To stop the system:${NC}                                           ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${CYAN}./STOP_ULTIMATE_AI_TRADING.sh${NC}                                 ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════════╝${NC}"

echo ""
echo -e "${YELLOW}📖 Quick Start:${NC}"
echo ""
echo -e "  ${CYAN}1.${NC} Start the system:    ${GREEN}./START_ULTIMATE_AI_TRADING.sh${NC}"
echo -e "  ${CYAN}2.${NC} Open dashboard:      ${GREEN}http://localhost:5000${NC}"
echo -e "  ${CYAN}3.${NC} Watch AI trade!      ${GREEN}(Be patient, AI is selective)${NC}"
echo ""
echo -e "${GREEN}🎉 Your Ultimate AI Trading System is ready!${NC}"
echo ""

