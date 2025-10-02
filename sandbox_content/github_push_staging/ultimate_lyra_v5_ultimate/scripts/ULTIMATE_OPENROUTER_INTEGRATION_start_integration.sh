#!/bin/bash
# Ultimate OpenRouter Integration Startup Script

echo "🚀 Starting Ultimate OpenRouter Integration..."

# Set environment variables
export OPENROUTER_API_KEY="YOUR_API_KEY_HERE"
export PYTHONPATH="/home/ubuntu/ultimate_lyra_v5:$PYTHONPATH"

# Start the integration service
cd /home/ubuntu/ULTIMATE_OPENROUTER_INTEGRATION/
python3 openrouter_service.py &

echo "✅ OpenRouter Integration Service started on port 8090"
echo "🌐 Access endpoints:"
echo "   - Consensus: POST http://localhost:8090/consensus"
echo "   - Status: GET http://localhost:8090/status"
echo "   - Models: GET http://localhost:8090/models"

# Keep script running
wait
