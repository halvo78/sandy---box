# 📰 News & Sentiment Analysis

**Module ID:** `NEWS_SENTIMENT`  
**Priority:** HIGH  
**Port:** N/A

## Description

News feeds and market sentiment

## Components

- NewsAPI Integration
- CryptoPanic API
- Benzinga News
- Twitter/X Sentiment
- Reddit Sentiment
- Discord Monitoring
- LunarCrush Social Data

## APIs Used

- NewsAPI
- CryptoPanic
- Benzinga
- Twitter
- Reddit
- LunarCrush

## Directory Structure

```
NEWS_SENTIMENT/
├── src/           # Source code
├── config/        # Configuration files
├── docs/          # Documentation
├── tests/         # Test files
└── README.md      # This file
```

## Quick Start

```bash
# Navigate to module
cd NEWS_SENTIMENT

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
- NewsAPI Integration
- CryptoPanic API
- Benzinga News
- Twitter/X Sentiment
- Reddit Sentiment
- Discord Monitoring
- LunarCrush Social Data

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
