# News & Sentiment Intelligence

**Layer ID:** `INTELLIGENCE_LAYER`  
**Priority:** MEDIUM

## Overview

News & Sentiment Intelligence is a critical component of the Lyra Trading System production deployment.

## Components

- NewsAPI, CryptoPanic
- Twitter/X sentiment
- Reddit analysis
- LunarCrush social data

## Source Modules

- NEWS_SENTIMENT

## Directory Structure

```
INTELLIGENCE_LAYER/
├── src/           # Source code
├── config/        # Configuration files
├── tests/         # Test files
├── docs/          # Documentation
└── README.md      # This file
```

## Deployment

```bash
# Navigate to layer
cd INTELLIGENCE_LAYER

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
- NewsAPI, CryptoPanic
- Twitter/X sentiment
- Reddit analysis
- LunarCrush social data

## Monitoring

- Health: `/health`
- Metrics: `/metrics`
- Status: `/status`

---

**Production-Ready** ✅
