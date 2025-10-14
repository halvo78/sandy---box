# 💱 Exchange Integrations

**Module ID:** `EXCHANGES`  
**Priority:** CRITICAL  
**Port:** N/A

## Description

All cryptocurrency exchange connections

## Components

- OKX API Integration
- Binance API
- Coinbase API
- Gate.io API
- WhiteBIT API
- BTC Markets API

## APIs Used

- OKX
- Binance
- Coinbase
- Gate.io
- WhiteBIT
- BTC Markets

## Directory Structure

```
EXCHANGES/
├── src/           # Source code
├── config/        # Configuration files
├── docs/          # Documentation
├── tests/         # Test files
└── README.md      # This file
```

## Quick Start

```bash
# Navigate to module
cd EXCHANGES

# Install dependencies
pip install -r requirements.txt

# Configure
cp config/template.json config/config.json
# Edit config/config.json with your settings

# Run tests
python -m pytest tests/

# Start module
python src/main.py
```

## Configuration

See `config/template.json` for all available configuration options.

## Integration

This module integrates with:
- OKX API Integration
- Binance API
- Coinbase API
- Gate.io API
- WhiteBIT API
- BTC Markets API

## Monitoring

- Health check endpoint: `/health`
- Metrics endpoint: `/metrics`
- Status endpoint: `/status`

## Troubleshooting

Common issues and solutions:

1. **Module won't start**
   - Check configuration in `config/config.json`
   - Verify all API keys are set
   - Check logs in `logs/`

2. **API errors**
   - Verify API keys are valid
   - Check rate limits
   - Review API documentation

3. **Performance issues**
   - Check system resources
   - Review metrics
   - Optimize configuration

## Support

- Documentation: `docs/`
- Issues: GitHub Issues
- Community: Discord

---

**Last Updated:** 2025-10-14
