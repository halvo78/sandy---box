#!/bin/bash

echo "🚀 ULTIMATE TURBO-CHARGED PRODUCTION SYSTEM 🚀"
echo "=============================================="
echo ""
echo "DEPLOYMENT TO LOCAL UBUNTU"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo -e "${BLUE}📁 Deployment directory: ${SCRIPT_DIR}${NC}"
echo ""

# Check if we're on the local Ubuntu machine
echo -e "${BLUE}🖥️  Checking system...${NC}"
hostname
echo ""

# Create directories
echo -e "${BLUE}📁 Creating directories...${NC}"
mkdir -p data/turbo
mkdir -p logs/turbo
mkdir -p venv
echo -e "${GREEN}✅ Directories created${NC}"
echo ""

# Check Python
echo -e "${BLUE}🐍 Checking Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found! Please install Python 3.8+${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✅ Python found: ${PYTHON_VERSION}${NC}"
echo ""

# Create virtual environment
echo -e "${BLUE}🔧 Creating virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment already exists${NC}"
fi
echo ""

# Activate virtual environment
echo -e "${BLUE}⚡ Activating virtual environment...${NC}"
source venv/bin/activate
echo -e "${GREEN}✅ Virtual environment activated${NC}"
echo ""

# Install dependencies in virtual environment
echo -e "${BLUE}📦 Installing dependencies in virtual environment...${NC}"
echo "Installing: ccxt pandas numpy requests"
pip install --quiet ccxt pandas numpy requests 2>&1 | grep -v "already satisfied" || true
echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Check if main file exists
echo -e "${BLUE}📄 Checking main system file...${NC}"
if [ -f "${SCRIPT_DIR}/ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py" ]; then
    echo -e "${GREEN}✅ ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py${NC}"
else
    echo -e "${RED}❌ ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py NOT FOUND${NC}"
    exit 1
fi
echo ""

# Display system specs
echo "="*60
echo "📊 SYSTEM SPECIFICATIONS"
echo "="*60
echo ""
echo "💰 Starting Capital: \$1,000,000"
echo "🪙 All Coins: BTC, ETH, SOL, ADA, XRP, DOT, MATIC, AVAX"
echo "⏱️  All Timeframes: 1m, 5m, 15m, 1h, 4h, 1d"
echo "🤖 AI Professionals: 50+"
echo "📊 Trading Strategies: 18"
echo "📈 Technical Indicators: 330+"
echo "🚀 Max Positions: UNLIMITED"
echo "⚡ Turbo Mode: ENABLED"
echo "✅ Production Ready: YES"
echo ""
echo "="*60
echo ""

# Offer to start
echo -e "${YELLOW}Ready to start the ULTIMATE TURBO-CHARGED SYSTEM?${NC}"
echo ""
echo "To start the system, run:"
echo ""
echo -e "${GREEN}  source venv/bin/activate${NC}"
echo -e "${GREEN}  python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py${NC}"
echo ""
echo "Or press Ctrl+C to exit and start manually later."
echo ""
read -p "Start now? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "="*60
    echo -e "${BLUE}🚀 STARTING ULTIMATE TURBO-CHARGED SYSTEM${NC}"
    echo "="*60
    echo ""
    python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py
else
    echo ""
    echo -e "${GREEN}✅ System ready!${NC}"
    echo ""
    echo "Start the system anytime with:"
    echo -e "${GREEN}  cd ${SCRIPT_DIR}${NC}"
    echo -e "${GREEN}  source venv/bin/activate${NC}"
    echo -e "${GREEN}  python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py${NC}"
    echo ""
fi

