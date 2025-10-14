# Risk Management & Control

**Layer ID:** `RISK_CONTROL`  
**Priority:** CRITICAL

## Overview

Risk Management & Control is a critical component of the Lyra Trading System production deployment.

## Components

- Never-sell-at-loss protection
- Circuit breakers
- VaR calculation
- Drawdown monitoring

## Source Modules

- RISK_MANAGEMENT

## Directory Structure

```
RISK_CONTROL/
├── src/           # Source code
├── config/        # Configuration files
├── tests/         # Test files
├── docs/          # Documentation
└── README.md      # This file
```

## Deployment

```bash
# Navigate to layer
cd RISK_CONTROL

# Configure
cp config/*.json config/production.json
# Edit config/production.json

# Test
python -m pytest tests/

# Deploy
python src/deploy.py
```

## Integration

This layer integrates with:
- Never-sell-at-loss protection
- Circuit breakers
- VaR calculation
- Drawdown monitoring

## Monitoring

- Health: `/health`
- Metrics: `/metrics`
- Status: `/status`

---

**Production-Ready** ✅
