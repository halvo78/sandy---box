#!/bin/bash

################################################################################
# 🚀 ULTIMATE AI TRADING SYSTEM - ONE-COMMAND STARTUP
################################################################################
#
# This script starts the complete AI autonomous trading system:
# - Ultimate AI Trading Engine (full OpenRouter AI team)
# - Best-in-World Dashboard (real-time AI decision tracking)
# - Progressive rollout (1 coin → all coins)
# - Hive mind optimization
# - Maximum trade frequency
#
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
echo -e "${PURPLE}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   🚀 ULTIMATE AI AUTONOMOUS TRADING SYSTEM                      ║
║                                                                  ║
║   ✅ Full OpenRouter AI Team (8 keys, 14 AIs, 327+ models)     ║
║   ✅ Progressive Rollout (1 coin → all coins)                   ║
║   ✅ Hive Mind Optimization (per-coin learning)                 ║
║   ✅ Best-in-World Dashboard (real-time AI tracking)            ║
║   ✅ Autonomous Everything (AI decides all)                     ║
║   ✅ Paper Trading (no limits, go hard!)                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Check if running in correct directory
if [ ! -f "ULTIMATE_AI_TRADING_ENGINE.py" ]; then
    echo -e "${RED}❌ Error: ULTIMATE_AI_TRADING_ENGINE.py not found${NC}"
    echo -e "${YELLOW}Please run this script from the ULTIMATE_AI_TRADING_SYSTEM directory${NC}"
    exit 1
fi

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

echo -e "${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip --quiet

echo -e "${YELLOW}Installing required packages...${NC}"
pip install --quiet \
    ccxt \
    flask \
    requests \
    pandas \
    numpy

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
echo -e "${BLUE}⚙️  STEP 4: Checking configuration${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Check for OpenRouter API keys in environment
if [ -z "$OPENROUTER_KEY_1" ]; then
    echo -e "${YELLOW}⚠️  OpenRouter API keys not found in environment${NC}"
    echo -e "${YELLOW}   Using hardcoded keys from the system${NC}"
else
    echo -e "${GREEN}✅ OpenRouter API keys found in environment${NC}"
fi

echo -e "${GREEN}✅ Configuration checked${NC}"

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🎯 STEP 5: Starting AI Trading Dashboard${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${YELLOW}Starting dashboard in background...${NC}"
python3 ULTIMATE_AI_DASHBOARD.py > logs/dashboard.log 2>&1 &
DASHBOARD_PID=$!

# Wait for dashboard to start
sleep 3

# Check if dashboard is running
if ps -p $DASHBOARD_PID > /dev/null; then
    echo -e "${GREEN}✅ Dashboard started (PID: $DASHBOARD_PID)${NC}"
    echo $DASHBOARD_PID > logs/dashboard.pid
else
    echo -e "${RED}❌ Dashboard failed to start${NC}"
    echo -e "${YELLOW}Check logs/dashboard.log for details${NC}"
    exit 1
fi

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🤖 STEP 6: Starting AI Trading Engine${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${YELLOW}Starting AI trading engine in background...${NC}"
python3 ULTIMATE_AI_TRADING_ENGINE.py > logs/ai_trading_engine.log 2>&1 &
ENGINE_PID=$!

# Wait for engine to start
sleep 3

# Check if engine is running
if ps -p $ENGINE_PID > /dev/null; then
    echo -e "${GREEN}✅ AI Trading Engine started (PID: $ENGINE_PID)${NC}"
    echo $ENGINE_PID > logs/engine.pid
else
    echo -e "${RED}❌ AI Trading Engine failed to start${NC}"
    echo -e "${YELLOW}Check logs/ai_trading_engine.log for details${NC}"
    
    # Kill dashboard if engine failed
    kill $DASHBOARD_PID 2>/dev/null
    exit 1
fi

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ ALL SYSTEMS STARTED SUCCESSFULLY!${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                     🎯 ACCESS POINTS                             ║${NC}"
echo -e "${PURPLE}╠══════════════════════════════════════════════════════════════════╣${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${GREEN}📊 Dashboard:${NC}     ${CYAN}http://localhost:5000${NC}                        ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}🔗 API Status:${NC}    ${CYAN}http://localhost:5000/api/status${NC}             ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}❤️  Health Check:${NC}  ${CYAN}http://localhost:5000/api/health${NC}             ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════════╝${NC}"

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                     📝 PROCESS INFO                              ║${NC}"
echo -e "${PURPLE}╠══════════════════════════════════════════════════════════════════╣${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${GREEN}🎯 AI Trading Engine:${NC}  PID ${CYAN}$ENGINE_PID${NC}                           ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${GREEN}📊 Dashboard:${NC}          PID ${CYAN}$DASHBOARD_PID${NC}                           ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════════╝${NC}"

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                     📋 MONITORING                                ║${NC}"
echo -e "${PURPLE}╠══════════════════════════════════════════════════════════════════╣${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${YELLOW}View AI Engine Logs:${NC}                                          ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${CYAN}tail -f logs/ai_trading_engine.log${NC}                          ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${YELLOW}View Dashboard Logs:${NC}                                          ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${CYAN}tail -f logs/dashboard.log${NC}                                   ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${YELLOW}Check Portfolio Status:${NC}                                       ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${CYAN}cat data/ai_trading/portfolio_status.json${NC}                    ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════════╝${NC}"

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                     🛑 STOP SYSTEM                               ║${NC}"
echo -e "${PURPLE}╠══════════════════════════════════════════════════════════════════╣${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}║  ${YELLOW}To stop all systems:${NC}                                          ${PURPLE}║${NC}"
echo -e "${PURPLE}║  ${CYAN}./STOP_ULTIMATE_AI_TRADING.sh${NC}                                ${PURPLE}║${NC}"
echo -e "${PURPLE}║                                                                  ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════════╝${NC}"

echo ""
echo -e "${GREEN}🚀 Ultimate AI Trading System is now running!${NC}"
echo -e "${GREEN}🤖 AI team is analyzing markets and making autonomous decisions${NC}"
echo -e "${GREEN}📊 Watch the dashboard for real-time AI trading activity${NC}"
echo ""

