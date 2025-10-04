#!/bin/bash
# ECOSYSTEM DEPLOYMENT SCRIPT
# Deploy the complete Ultimate Lyra Ecosystem

echo "🚀 DEPLOYING ULTIMATE LYRA ECOSYSTEM..."

# Check if Docker is available
if command -v docker &> /dev/null; then
    echo "✅ Docker found"
    cd ../ECOSYSTEM_DEPLOYMENT
    if [ -f "ecosystem_docker-compose.yml" ]; then
        docker-compose -f ecosystem_docker-compose.yml up -d
        echo "✅ Ecosystem deployed with Docker"
    fi
else
    echo "⚠️  Docker not found, running local deployment"
    cd ../ECOSYSTEM_SCRIPTS
    if [ -f "ecosystem_start_ultimate_system.sh" ]; then
        ./ecosystem_start_ultimate_system.sh
    fi
fi

echo "🎉 Ecosystem deployment complete!"
