# 📈 Trading Strategies

**Module ID:** `TRADING_STRATEGIES`  
**Priority:** HIGH  
**Port:** N/A

## Description

All trading strategy implementations

## Components

- CPS (Core Protective Swing)
- TM (Trend Momentum)
- RMR (Range Mean-Reversion)
- VBO (Volatility Breakout)
- CFH (Carry & Funding Harvest)
- ED (Event Drift)
- Arbitrage Detection
- Market Making

## APIs Used

No external APIs

## Directory Structure

```
TRADING_STRATEGIES/
├── src/           # Source code
├── config/        # Configuration files
├── docs/          # Documentation
├── tests/         # Test files
└── README.md      # This file
```

## Quick Start

```bash
# Navigate to module
cd TRADING_STRATEGIES

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
- CPS (Core Protective Swing)
- TM (Trend Momentum)
- RMR (Range Mean-Reversion)
- VBO (Volatility Breakout)
- CFH (Carry & Funding Harvest)
- ED (Event Drift)
- Arbitrage Detection
- Market Making

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
