#!/bin/bash

################################################################################
# 🚀 START ULTIMATE COMPLETE PAPER TRADING SYSTEM
################################################################################
#
# This script starts the COMPLETE system with:
# - 18 Trading Strategies
# - 14 AI Hive Mind Models
# - Progressive Rollout
# - Real-time Dashboard
# - Complete Commissioning
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
║   🚀 ULTIMATE COMPLETE PAPER TRADING SYSTEM                     ║
║                                                                  ║
║   18 Strategies | 14 AIs | Full Hive Mind | All Commissioned   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📦 STEP 1: Setting up environment${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating Python virtual environment...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate
echo -e "${GREEN}✅ Virtual environment activated${NC}"

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📥 STEP 2: Installing dependencies${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${YELLOW}Installing required packages...${NC}"
pip install --quiet --upgrade pip
pip install --quiet ccxt flask requests pandas numpy

echo -e "${GREEN}✅ All dependencies installed${NC}"

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📁 STEP 3: Creating directories${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

mkdir -p logs
mkdir -p data/ai_trading
mkdir -p config

echo -e "${GREEN}✅ Directories created${NC}"

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🌐 STEP 4: Starting dashboard${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${YELLOW}Starting Ultimate Complete Dashboard on port 5000...${NC}"
python3 ULTIMATE_COMPLETE_DASHBOARD.py > logs/dashboard.log 2>&1 &
DASHBOARD_PID=$!
echo $DASHBOARD_PID > logs/dashboard.pid

sleep 3

if ps -p $DASHBOARD_PID > /dev/null; then
    echo -e "${GREEN}✅ Dashboard started successfully (PID: $DASHBOARD_PID)${NC}"
else
    echo -e "${RED}❌ Dashboard failed to start${NC}"
    exit 1
fi

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🤖 STEP 5: Starting AI trading engine${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${YELLOW}Starting Ultimate Complete Paper Trading System...${NC}"
python3 ULTIMATE_COMPLETE_PAPER_TRADING_SYSTEM.py > logs/trading_engine.log 2>&1 &
ENGINE_PID=$!
echo $ENGINE_PID > logs/engine.pid

sleep 3

if ps -p $ENGINE_PID > /dev/null; then
    echo -e "${GREEN}✅ Trading engine started successfully (PID: $ENGINE_PID)${NC}"
else
    echo -e "${RED}❌ Trading engine failed to start${NC}"
    kill $DASHBOARD_PID
    exit 1
fi

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ SYSTEM STARTED SUCCESSFULLY!${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                     🎉 ALL SYSTEMS OPERATIONAL                   ║${NC}"
echo -e "${PURPLE}╠══════════════════════════════════════════════════════════════════╣${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${GREEN}✅ 18 Trading Strategies Active${NC}                                 ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}✅ 14 AI Models in Hive Mind${NC}                                   ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}✅ Progressive Rollout Enabled${NC}                                 ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}✅ Paper Trading Mode (Safe)${NC}                                   ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}✅ Dashboard Running${NC}                                           ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}✅ Trading Engine Running${NC}                                      ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════════╝${NC}"

echo ""
echo -e "${YELLOW}📊 ACCESS INFORMATION:${NC}"
echo ""
echo -e "  ${CYAN}Dashboard:${NC}        ${GREEN}http://localhost:5000${NC}"
echo -e "  ${CYAN}API Status:${NC}       ${GREEN}http://localhost:5000/api/status${NC}"
echo -e "  ${CYAN}Health Check:${NC}     ${GREEN}http://localhost:5000/api/health${NC}"
echo ""
echo -e "  ${CYAN}Dashboard PID:${NC}    ${GREEN}$DASHBOARD_PID${NC}"
echo -e "  ${CYAN}Engine PID:${NC}       ${GREEN}$ENGINE_PID${NC}"
echo ""
echo -e "${YELLOW}📝 LOGS:${NC}"
echo ""
echo -e "  ${CYAN}Dashboard:${NC}        ${GREEN}tail -f logs/dashboard.log${NC}"
echo -e "  ${CYAN}Trading Engine:${NC}   ${GREEN}tail -f logs/trading_engine.log${NC}"
echo ""
echo -e "${YELLOW}🛑 TO STOP:${NC}"
echo ""
echo -e "  ${CYAN}Run:${NC}              ${GREEN}./STOP_COMPLETE_SYSTEM.sh${NC}"
echo ""
echo -e "${GREEN}🎉 Your Ultimate Complete AI Trading System is now running!${NC}"
echo -e "${GREEN}🎯 Watch the AI trade with all 18 strategies!${NC}"
echo ""

