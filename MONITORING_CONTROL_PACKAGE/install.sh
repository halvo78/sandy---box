#!/bin/bash

echo "======================================================================"
echo "LYRA MONITORING & CONTROL PACKAGE - INSTALLATION"
echo "======================================================================"
echo ""
echo "⚠️  This will install monitoring tools WITHOUT modifying your existing"
echo "   Lyra trading system."
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

echo ""
echo "📦 Installing monitoring stack..."
echo ""

# Install Prometheus
if ! command -v prometheus &> /dev/null; then
    echo "Installing Prometheus..."
    wget -q https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz
    tar -xzf prometheus-2.45.0.linux-amd64.tar.gz
    sudo mv prometheus-2.45.0.linux-amd64/prometheus /usr/local/bin/
    sudo mv prometheus-2.45.0.linux-amd64/promtool /usr/local/bin/
    rm -rf prometheus-2.45.0.linux-amd64*
    echo "✅ Prometheus installed"
else
    echo "✅ Prometheus already installed"
fi

# Install Grafana
if ! command -v grafana-server &> /dev/null; then
    echo "Installing Grafana..."
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository -y "deb https://packages.grafana.com/oss/deb stable main"
    wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install -y grafana
    echo "✅ Grafana installed"
else
    echo "✅ Grafana already installed"
fi

# Copy configs
echo ""
echo "⚙️  Copying configurations..."
sudo mkdir -p /etc/prometheus
sudo cp configs/prometheus.yml /etc/prometheus/
sudo cp configs/trading_alerts.yml /etc/prometheus/

# Start services
echo ""
echo "🚀 Starting services..."
sudo systemctl start prometheus
sudo systemctl start grafana-server
sudo systemctl enable prometheus
sudo systemctl enable grafana-server

echo ""
echo "======================================================================"
echo "✅ INSTALLATION COMPLETE"
echo "======================================================================"
echo ""
echo "📊 Access your dashboards:"
echo "   Grafana:    http://localhost:3000 (admin/admin)"
echo "   Prometheus: http://localhost:9090"
echo ""
echo "🎛️  Run control center:"
echo "   cd control_center && python3 UNIFIED_PRODUCTION_SYSTEM.py"
echo ""
echo "✅ Your existing Lyra system is unchanged!"
echo ""
