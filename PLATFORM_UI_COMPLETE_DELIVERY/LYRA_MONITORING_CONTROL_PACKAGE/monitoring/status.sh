#!/bin/bash
cd "$(dirname "$0")"
echo "📊 HALVO-AI Monitoring System Status"
echo "====================================="
echo ""
docker-compose ps
echo ""
echo "🌐 Access points:"
echo "  Grafana:        http://localhost:3000"
echo "  Prometheus:     http://localhost:9090"
echo "  Kibana:         http://localhost:5601"
echo "  AlertManager:   http://localhost:9093"
