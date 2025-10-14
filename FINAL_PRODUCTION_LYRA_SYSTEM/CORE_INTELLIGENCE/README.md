# Core AI Intelligence Layer

**Layer ID:** `CORE_INTELLIGENCE`  
**Priority:** CRITICAL

## Overview

Core AI Intelligence Layer is a critical component of the Lyra Trading System production deployment.

## Components

- 19+ AI Models (OpenRouter integration)
- Multi-model consensus engine
- 90% confidence threshold
- Continuous learning system

## Source Modules

- AI_MODELS

## Directory Structure

```
CORE_INTELLIGENCE/
├── src/           # Source code
├── config/        # Configuration files
├── tests/         # Test files
├── docs/          # Documentation
└── README.md      # This file
```

## Deployment

```bash
# Navigate to layer
cd CORE_INTELLIGENCE

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
- 19+ AI Models (OpenRouter integration)
- Multi-model consensus engine
- 90% confidence threshold
- Continuous learning system

## Monitoring

- Health: `/health`
- Metrics: `/metrics`
- Status: `/status`

---

**Production-Ready** ✅
