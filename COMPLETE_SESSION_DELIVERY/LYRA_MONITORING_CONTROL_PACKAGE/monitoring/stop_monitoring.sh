#!/bin/bash
cd "$(dirname "$0")"
echo "🛑 Stopping HALVO-AI Monitoring System..."
docker-compose down
echo "✅ Monitoring system stopped"
