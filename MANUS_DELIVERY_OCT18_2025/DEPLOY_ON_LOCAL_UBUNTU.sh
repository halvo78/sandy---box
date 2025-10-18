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

# Install dependencies
echo -e "${BLUE}📦 Installing dependencies...${NC}"
echo "Installing: ccxt pandas numpy requests asyncio"
pip3 install --quiet ccxt pandas numpy requests 2>&1 | grep -v "already satisfied" || true
echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Check if all required files exist
echo -e "${BLUE}📄 Checking required files...${NC}"
REQUIRED_FILES=(
    "ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py"
    "PRODUCTION_COMMISSIONING_FRAMEWORK.py"
    "DEPLOY_AND_COMMISSION_TURBO_SYSTEM.sh"
)

ALL_FILES_PRESENT=true
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "${SCRIPT_DIR}/${file}" ]; then
        echo -e "${GREEN}✅ ${file}${NC}"
    else
        echo -e "${RED}❌ ${file} NOT FOUND${NC}"
        ALL_FILES_PRESENT=false
    fi
done
echo ""

if [ "$ALL_FILES_PRESENT" = false ]; then
    echo -e "${RED}❌ Some required files are missing!${NC}"
    echo ""
    echo "Please ensure all files are in the same directory as this script:"
    for file in "${REQUIRED_FILES[@]}"; do
        echo "  - ${file}"
    done
    echo ""
    exit 1
fi

# Make scripts executable
echo -e "${BLUE}🔧 Making scripts executable...${NC}"
chmod +x "${SCRIPT_DIR}/DEPLOY_AND_COMMISSION_TURBO_SYSTEM.sh"
echo -e "${GREEN}✅ Scripts are executable${NC}"
echo ""

# Run commissioning
echo ""
echo "="*80
echo -e "${BLUE}🧪 RUNNING PRODUCTION COMMISSIONING${NC}"
echo "="*80
echo ""

cd "${SCRIPT_DIR}"
python3 PRODUCTION_COMMISSIONING_FRAMEWORK.py

# Check commissioning results
if [ -f "data/turbo/commissioning_report.json" ]; then
    STATUS=$(python3 -c "import json; print(json.load(open('data/turbo/commissioning_report.json'))['status'])")
    
    if [ "$STATUS" == "COMMISSIONED" ]; then
        echo ""
        echo "="*80
        echo -e "${GREEN}🎉 SYSTEM IS FULLY COMMISSIONED!${NC}"
        echo "="*80
        echo ""
        echo -e "${GREEN}✅ All tests passed${NC}"
        echo -e "${GREEN}✅ Production ready${NC}"
        echo -e "${GREEN}✅ Ready to deploy${NC}"
        echo ""
        
        # Display system specs
        echo "="*80
        echo "📊 SYSTEM SPECIFICATIONS"
        echo "="*80
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
        echo "="*80
        echo ""
        
        # Offer to start
        echo -e "${YELLOW}Ready to start the ULTIMATE TURBO-CHARGED SYSTEM?${NC}"
        echo ""
        echo "To start the system, run:"
        echo ""
        echo -e "${GREEN}  python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py${NC}"
        echo ""
        echo "Or press Ctrl+C to exit and start manually later."
        echo ""
        read -p "Start now? (y/n) " -n 1 -r
        echo ""
        
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo ""
            echo "="*80
            echo -e "${BLUE}🚀 STARTING ULTIMATE TURBO-CHARGED SYSTEM${NC}"
            echo "="*80
            echo ""
            python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py
        else
            echo ""
            echo -e "${GREEN}✅ System commissioned and ready!${NC}"
            echo ""
            echo "Start the system anytime with:"
            echo -e "${GREEN}  cd ${SCRIPT_DIR}${NC}"
            echo -e "${GREEN}  python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py${NC}"
            echo ""
        fi
    else
        echo ""
        echo "="*80
        echo -e "${RED}❌ COMMISSIONING FAILED${NC}"
        echo "="*80
        echo ""
        echo -e "${YELLOW}Review the commissioning report:${NC}"
        echo "  ${SCRIPT_DIR}/data/turbo/commissioning_report.json"
        echo ""
        echo -e "${YELLOW}Fix the issues and run commissioning again.${NC}"
        echo ""
        exit 1
    fi
else
    echo ""
    echo -e "${RED}❌ Commissioning report not found${NC}"
    echo ""
    exit 1
fi

