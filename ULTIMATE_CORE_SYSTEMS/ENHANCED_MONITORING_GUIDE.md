# Enhanced Monitoring Guide

**Generated:** 2025-10-04 01:38:22

## Comprehensive Monitoring Stack

### 1. Grafana + Prometheus
- Metrics: latency, fill rate, fees, PnL net of fees, rejects, WS reconnects
- Real-time dashboards for trading performance
- Alert management and notification systems

### 2. Loki/Promtail
- Structured logs: orders, errors, approvals
- Log aggregation and search capabilities
- Audit trail maintenance

### 3. Key Metrics to Monitor
- PNL after fees (per exchange/symbol/strategy)
- Order errors by code (insufficient funds, min notional, rate limit)
- Latency histograms: create/cancel/fetch
- Websocket health: reconnects/min, message lag
- Kill-switch state and last approval SHA
- VIP drift and fee anomaly alerts

### 4. Operational Dashboards
- Streamlit/Dash/FastAPI UI for operator console
- Start/stop strategies interface
- Approval workflows and change management
- Real-time system health monitoring

---

*Comprehensive monitoring ensures optimal system performance and reliability.*
