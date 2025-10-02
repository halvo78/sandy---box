#!/bin/bash
# ULTIMATE LYRA TRADING SYSTEM - DEFINITIVE STARTUP SCRIPT
# wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY=================

echo "🚀 STARTING ULTIMATE LYRA TRADING SYSTEM - DEFINITIVE EDITION"
echo "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY======================"

# Set environment variables
export LIVE_MODE=true
export LIVE_TRADING=true
export TRADING_MODE=AGGRESSIVE
export OPENROUTER_API_KEY=sk-or-v1-YOUR_OPENROUTER_API_KEY_HERE

# Start all trading systems
echo "🎯 Starting Maximum Amplification System (Port 9996)..."
python3.11 trading_systems/MAXIMUM_AMPLIFICATION_SYSTEM.py &

echo "🏛️ Starting Hummingbot Integration System (Port 8400)..."
python3.11 trading_systems/HUMMINGBOT_INTEGRATION_SYSTEM.py &

echo "📊 Starting AI Enhanced Dashboard (Port 8751)..."
python3.11 dashboards/ULTIMATE_DASHBOARD_SIMPLE.py &

echo "🤖 Starting AI Orchestrator (Port 8090)..."
python3.11 ai_integrations/AI_ORCHESTRATOR.py &

echo "💼 Starting Portfolio Manager (Port 8100)..."
python3.11 trading_systems/ULTIMATE_AI_PORTFOLIO_MANAGER.py &

echo "🌐 Starting Production Dashboard (Port 8080)..."
python3.11 trading_systems/native_production_system.py &

echo "📈 Starting Streamlit Dashboards..."
python3.11 dashboards/main_dashboard_simple.py &
python3.11 dashboards/COMPLETE_ULTIMATE_DASHBOARD.py &
python3.11 dashboards/COMPLETE_STREAMLIT_PORTFOLIO.py &

echo "✅ ALL SYSTEMS STARTED - ULTIMATE LYRA TRADING SYSTEM IS LIVE!"
echo "💰 Ready for live trading with $13,947.76 capital"
echo "🎯 Access systems at: localhost:8751, localhost:9996, localhost:8400"

# Keep script running
wait
