#!/bin/bash
# Ultimate Lyra Trading System V5 - Master Deployment Script
# Auto-generated from complete historical + GitHub integration

set -e

echo "🚀 Starting Ultimate Lyra Trading System V5 Deployment"
echo "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY=========="

# Backup existing
if [ -d "backup" ]; then
    rm -rf backup_old
    mv backup backup_old
fi
mkdir -p backup

# Environment setup
echo "🔧 Setting up environment..."
if [ -f "config/.env.production" ]; then
    cp config/.env.production .env
    echo "✅ Production environment loaded"
fi

# Install dependencies
echo "📦 Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    echo "✅ Python dependencies installed"
fi

# Docker setup
echo "🐳 Setting up Docker services..."
if [ -f "deployment/docker-compose.yml" ]; then
    cd deployment
    docker-compose down 2>/dev/null || true
    docker-compose build
    docker-compose up -d
    cd ..
    echo "✅ Docker services started"
fi

# Health checks
echo "🏥 Running health checks..."
sleep 10

# Check all ports
PORTS=(8080 8082 8090 8091 8100 8101 8102 8400 8751 9996)
for port in "${PORTS[@]}"; do
    if curl -s "http://localhost:$port/health" > /dev/null 2>&1; then
        echo "✅ Port $port: Healthy"
    else
        echo "⚠️ Port $port: Not responding"
    fi
done

# Run tests
echo "🧪 Running tests..."
if [ -d "tests" ]; then
    python3 -m pytest tests/ -v
    echo "✅ Tests completed"
fi

# Final status
echo "🎉 Ultimate Lyra Trading System V5 Deployment Complete!"
echo "Access points:"
echo "- AI Enhanced Dashboard: http://localhost:8751"
echo "- Maximum Amplification: http://localhost:9996" 
echo "- Hummingbot Integration: http://localhost:8400"
echo "- Production Dashboard: http://localhost:8080"
echo "- AI Orchestrator: http://localhost:8090"
echo "- Portfolio Manager: http://localhost:8100"
