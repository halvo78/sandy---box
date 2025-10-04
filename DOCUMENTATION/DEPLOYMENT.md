# Deployment Guide

## Quick Start

### Docker Compose (Development)
```bash
cd CONTAINERS
docker-compose up -d
```

### Kubernetes (Production)
```bash
kubectl apply -f DEPLOYMENT/kubernetes/
```

## Configuration

### Environment Variables
Copy `.env.example` to `.env` and configure:
- OpenRouter API keys
- Exchange API credentials
- Database connections
- Security settings

### Security Setup
1. Generate secure passwords
2. Configure vault encryption
3. Set up API key rotation
4. Enable audit logging

## Monitoring

### Health Checks
All services include health check endpoints:
- `/health` - Service health status
- `/metrics` - Prometheus metrics
- `/ready` - Readiness probe

### Logging
Centralized logging with structured JSON format:
- Application logs
- Security audit logs
- Performance metrics
- Error tracking
