# Lyra Monitoring & Control Package

**Purpose:** Supplementary monitoring, dashboards, control, and audit tools for the Lyra Trading System

**IMPORTANT:** This package does NOT modify the existing Lyra trading system. It only adds monitoring and control capabilities.

## What's Included

### 1. Monitoring Stack
- **Prometheus** - Metrics collection (port 9090)
- **Grafana** - Visualization dashboards (port 3000)
- **Node Exporter** - System metrics (port 9100)
- **Alert Rules** - Trading-specific alerts

### 2. Dashboards
- Real-time trading dashboard
- Portfolio visualization
- Exchange monitoring
- AI consensus display
- Performance metrics

### 3. Control Center
- System commissioning tools
- Validation framework
- Health checks
- Status monitoring

### 4. Audit Tools
- ATO tax compliance reporting
- Complete trade audit trails
- Performance analytics
- Risk monitoring

### 5. Commissioning
- Production readiness verification
- System integration checks
- Component validation
- Operational readiness

## Installation

### Prerequisites
```bash
# Install Prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz
tar -xzf prometheus-2.45.0.linux-amd64.tar.gz
sudo mv prometheus-2.45.0.linux-amd64/prometheus /usr/local/bin/
sudo mv prometheus-2.45.0.linux-amd64/promtool /usr/local/bin/

# Install Grafana
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install grafana
```

### Setup Monitoring
```bash
# 1. Copy Prometheus config
sudo cp configs/prometheus.yml /etc/prometheus/
sudo cp configs/trading_alerts.yml /etc/prometheus/

# 2. Start services
sudo systemctl start prometheus
sudo systemctl start grafana-server
sudo systemctl enable prometheus
sudo systemctl enable grafana-server

# 3. Access dashboards
firefox http://localhost:3000  # Grafana (admin/admin)
firefox http://localhost:9090  # Prometheus
```

### Setup Control Center
```bash
cd control_center
python3 UNIFIED_PRODUCTION_SYSTEM.py
```

### Setup Dashboards
```bash
cd dashboards
python3 -m http.server 8080
firefox http://localhost:8080
```

## Integration with Existing Lyra System

**This package integrates WITHOUT modifying your existing system:**

1. **Monitoring** - Scrapes metrics from your existing Lyra endpoints
2. **Dashboards** - Visualizes data from your existing databases
3. **Control** - Provides oversight without changing trading logic
4. **Audit** - Reads from your existing trade records

**NO changes to:**
- Trading strategies
- Risk management
- Exchange integrations
- AI models
- Core system logic

## Components

### Monitoring (`monitoring/`)
- Prometheus configuration
- Grafana dashboards
- Alert rules
- Service definitions

### Dashboards (`dashboards/`)
- Real-time trading dashboard
- Portfolio visualization
- Exchange monitoring
- Performance analytics

### Control Center (`control_center/`)
- System status monitoring
- Component health checks
- Integration validation
- Operational oversight

### Audit Tools (`audit_tools/`)
- Tax reporting (ATO compliance)
- Trade audit trails
- Performance analytics
- Risk monitoring

### Configs (`configs/`)
- Prometheus configuration
- Alert rules
- Dashboard templates
- Service configs

## Usage

### Check System Status
```bash
cd control_center
python3 UNIFIED_PRODUCTION_SYSTEM.py
```

### View Dashboards
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- Custom Dashboard: http://localhost:8080

### Generate Reports
```bash
cd audit_tools
python3 deploy_reporting_system.py
```

## Features

✅ **Non-invasive** - Doesn't modify existing Lyra system
✅ **Real-time monitoring** - Live metrics and alerts
✅ **Professional dashboards** - Institutional-grade visualization
✅ **Complete audit** - Full trade history and compliance
✅ **Control center** - Centralized system oversight
✅ **Tax compliance** - ATO reporting ready

## Architecture

```
Existing Lyra System (UNCHANGED)
    ↓ (metrics/data)
Monitoring Package (NEW)
    ├── Prometheus (collects metrics)
    ├── Grafana (visualizes data)
    ├── Dashboards (custom views)
    ├── Control Center (oversight)
    └── Audit Tools (reporting)
```

## Support

This is a supplementary package. Your existing Lyra trading system remains the primary system and is not modified in any way.

---

**Status:** ✅ Production-ready monitoring & control infrastructure
**Integration:** Non-invasive, read-only access to existing system
**Purpose:** Enhanced visibility, control, and compliance
