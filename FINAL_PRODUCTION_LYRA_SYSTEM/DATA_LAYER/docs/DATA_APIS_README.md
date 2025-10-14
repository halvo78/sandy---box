# 📊 Market Data APIs

**Module ID:** `DATA_APIS`  
**Priority:** CRITICAL  
**Port:** 8081

## Description

Real-time and historical market data

## Components

- Polygon.io (Market Data)
- CoinGecko API
- CoinMarketCap API
- Finnhub API
- Alpha Vantage
- Twelve Data
- Yahoo Finance

## APIs Used

- Polygon.io
- CoinGecko
- CoinMarketCap
- Finnhub
- Alpha Vantage

## Directory Structure

```
DATA_APIS/
├── src/           # Source code
├── config/        # Configuration files
├── docs/          # Documentation
├── tests/         # Test files
└── README.md      # This file
```

## Quick Start

```bash
# Navigate to module
cd DATA_APIS

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
- Polygon.io (Market Data)
- CoinGecko API
- CoinMarketCap API
- Finnhub API
- Alpha Vantage
- Twelve Data
- Yahoo Finance

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
