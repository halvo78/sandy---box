#!/bin/bash
# Ultimate Lyra Trading System Deployment Script

echo "🚀 Starting Ultimate Lyra Trading System Deployment"

# Create directories
mkdir -p /opt/ultimate_lyra/{logs,config,data,backups}

# Copy system files
cp -r /home/ubuntu/ultimate_lyra_v5/* /opt/ultimate_lyra/

# Install dependencies
pip3 install -r /opt/ultimate_lyra/requirements.txt

# Start services
cd /opt/ultimate_lyra
python3 ECOSYSTEM_CONTROLLER.py &
python3 API_GATEWAY.py &
python3 MONITORING_DASHBOARD.py &

echo "✅ Ultimate Lyra Trading System deployed successfully"
echo "🌐 Access points:"
echo "  - Ecosystem Controller: http://localhost:9100"
echo "  - API Gateway: http://localhost:9200"
echo "  - Monitoring Dashboard: http://localhost:9000"
