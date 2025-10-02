# Ultimate Ngrok Container Package

This package contains everything needed to deploy a production-ready ngrok container with full capabilities for the Ultimate Lyra Trading System.

## Quick Start

1. **Set environment variables:**
```bash
export NGROK_AUTHTOKEN="your_ngrok_pro_token_here"
```

2. **Build and start:**
```bash
docker-compose up -d
```

3. **Verify connection:**
```bash
python3 manus_verification.py
```

## Files Included

- `Dockerfile` - Container definition
- `docker-compose.yml` - Orchestration
- `requirements.txt` - Python dependencies
- `ngrok_config.yml` - Ngrok configuration
- `tunnel_manager.py` - Tunnel management
- `start_ngrok.sh` - Startup script
- `safe_tunnel_policies.py` - Safety controls
- `manus_verification.py` - Verification script

## Features

- 40 concurrent tunnels (Pro Plan)
- Multi-service support (HTTP/TCP/UDP)
- Traffic inspection and compliance
- Webhook verification
- API automation
- Spot-only safety controls
- Manus integration ready

## Troubleshooting

See the main documentation for detailed troubleshooting steps.

## Support

This container is designed for inheritance and should work out-of-the-box with proper environment variables set.
