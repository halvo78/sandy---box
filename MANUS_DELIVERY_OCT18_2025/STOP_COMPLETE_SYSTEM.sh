#!/bin/bash

################################################################################
# 🛑 STOP ULTIMATE COMPLETE PAPER TRADING SYSTEM
################################################################################

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo -e "${PURPLE}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   🛑 STOPPING ULTIMATE COMPLETE PAPER TRADING SYSTEM            ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Stop Trading Engine
if [ -f "logs/engine.pid" ]; then
    ENGINE_PID=$(cat logs/engine.pid)
    echo -e "${YELLOW}Stopping Trading Engine (PID: $ENGINE_PID)...${NC}"
    
    if ps -p $ENGINE_PID > /dev/null; then
        kill $ENGINE_PID
        sleep 2
        
        if ps -p $ENGINE_PID > /dev/null; then
            kill -9 $ENGINE_PID
        fi
        
        echo -e "${GREEN}✅ Trading Engine stopped${NC}"
    else
        echo -e "${YELLOW}⚠️  Trading Engine not running${NC}"
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

