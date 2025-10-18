#!/bin/bash

################################################################################
# 🛑 ULTIMATE AI TRADING SYSTEM - STOP SCRIPT
################################################################################

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo -e "${PURPLE}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   🛑 STOPPING ULTIMATE AI TRADING SYSTEM                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Stop AI Trading Engine
if [ -f "logs/engine.pid" ]; then
    ENGINE_PID=$(cat logs/engine.pid)
    echo -e "${YELLOW}Stopping AI Trading Engine (PID: $ENGINE_PID)...${NC}"
    
    if ps -p $ENGINE_PID > /dev/null; then
        kill $ENGINE_PID
        sleep 2
        
        # Force kill if still running
        if ps -p $ENGINE_PID > /dev/null; then
            kill -9 $ENGINE_PID
        fi
        
        echo -e "${GREEN}✅ AI Trading Engine stopped${NC}"
    else
        echo -e "${YELLOW}⚠️  AI Trading Engine not running${NC}"
    fi
    
    rm -f logs/engine.pid
else
    echo -e "${YELLOW}⚠️  No engine PID file found${NC}"
fi

# Stop Dashboard
if [ -f "logs/dashboard.pid" ]; then
    DASHBOARD_PID=$(cat logs/dashboard.pid)
    echo -e "${YELLOW}Stopping Dashboard (PID: $DASHBOARD_PID)...${NC}"
    
    if ps -p $DASHBOARD_PID > /dev/null; then
        kill $DASHBOARD_PID
        sleep 2
        
        # Force kill if still running
        if ps -p $DASHBOARD_PID > /dev/null; then
            kill -9 $DASHBOARD_PID
        fi
        
        echo -e "${GREEN}✅ Dashboard stopped${NC}"
    else
        echo -e "${YELLOW}⚠️  Dashboard not running${NC}"
    fi
    
    rm -f logs/dashboard.pid
else
    echo -e "${YELLOW}⚠️  No dashboard PID file found${NC}"
fi

echo ""
echo -e "${GREEN}✅ All systems stopped${NC}"
echo ""

