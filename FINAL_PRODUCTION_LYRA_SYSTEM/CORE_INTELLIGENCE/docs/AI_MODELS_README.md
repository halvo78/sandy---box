# 🤖 AI Models & Intelligence

**Module ID:** `AI_MODELS`  
**Priority:** CRITICAL  
**Port:** N/A

## Description

All AI models for decision making

## Components

- OpenRouter Integration (19+ models)
- GPT-4, Claude, Gemini, Cohere
- Grok Builder
- DeepSeek, Qwen, Mistral
- AI Consensus Engine
- Multi-model voting system

## APIs Used

- OpenRouter
- OpenAI
- Anthropic
- Google AI
- Cohere
- XAI

## Directory Structure

```
AI_MODELS/
├── src/           # Source code
├── config/        # Configuration files
├── docs/          # Documentation
├── tests/         # Test files
└── README.md      # This file
```

## Quick Start

```bash
# Navigate to module
cd AI_MODELS

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
- OpenRouter Integration (19+ models)
- GPT-4, Claude, Gemini, Cohere
- Grok Builder
- DeepSeek, Qwen, Mistral
- AI Consensus Engine
- Multi-model voting system

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
