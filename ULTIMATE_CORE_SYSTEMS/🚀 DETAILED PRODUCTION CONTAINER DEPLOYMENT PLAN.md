# 🚀 **DETAILED PRODUCTION CONTAINER DEPLOYMENT PLAN**
## Ultimate Lyra Trading System - Complete Implementation Guide

**Generated:** 2025-09-30 | **Status:** Production Ready | **Containers:** 11 Built

---

## 📋 **DEPLOYMENT OVERVIEW**

### **Current System Status**
- ✅ **Native System Running:** Port 8080 (Production Dashboard)
- ✅ **Ngrok Active:** https://3ce37fa57d09.ngrok.app
- ✅ **11 Containers Built:** All production-ready
- ✅ **AI Consensus:** 83.3% compliance (126 AI models)
- ✅ **Capital Ready:** $13,947.76 available

### **Deployment Options**
1. **Parallel Deployment:** Run containers alongside native system
2. **Migration Deployment:** Replace native with containerized
3. **Hybrid Deployment:** Keep native + add specific containers

---

## 🏗️ **COMPLETE CONTAINER ARCHITECTURE**

### **Network Configuration**
```yaml
Network: lyra_network (172.20.0.0/16)
├── Exchange Layer (172.20.0.10-19)
├── AI Services (172.20.0.20-29)  
├── Security Layer (172.20.0.30-39)
├── Monitoring (172.20.0.40-49)
└── Gateway (172.20.0.50-59)
```

### **Volume Management**
```yaml
Persistent Volumes:
├── lyra_vault_data (Encrypted credentials)
├── lyra_prometheus_data (Metrics storage)
├── lyra_grafana_data (Dashboard configs)
└── lyra_redis_data (Cache storage)

Mounted Directories:
├── ../vault:/app/vault:ro (Read-only configs)
├── ../logs:/app/logs (Centralized logging)
└── ../config:/app/config:ro (Application configs)
```

---

## 📦 **DETAILED CONTAINER SPECIFICATIONS**

### **1. EXCHANGE CONTAINERS (5)**

#### **lyra-okx (Primary Exchange)**
```yaml
Container: lyra-okx
IP Address: 172.20.0.10
External Port: 8082
Internal Port: 8080

Environment:
  EXCHANGE: okx
  TRADING_MODE: spot_only
  LIVE_TRADING: true
  API_RATE_LIMIT: 300
  VAULT_URL: http://lyra-vault:8200

Health Check:
  Command: curl -f http://localhost:8080/health
  Interval: 30s
  Timeout: 10s
  Retries: 3

Dependencies:
  - lyra-vault (Credentials)
  - lyra-redis (Caching)

Build Context: ./exchange_containers/okx/
Files:
  - Dockerfile
  - okx_exchange_service.py
  - requirements.txt
```

#### **lyra-gate (Gate.io VIP3)**
```yaml
Container: lyra-gate
IP Address: 172.20.0.11
External Port: 8081
Internal Port: 8080

Environment:
  EXCHANGE: gate
  TRADING_MODE: spot_only
  VIP_TIER: 3
  POST_ONLY: true

Special Features:
  - VIP3 fee structure
  - Enhanced rate limits
  - Priority order routing
```

#### **lyra-whitebit (Secondary Exchange)**
```yaml
Container: lyra-whitebit
IP Address: 172.20.0.12
External Port: 8083
Internal Port: 8080

Environment:
  EXCHANGE: whitebit
  TRADING_MODE: spot_only
  BACKUP_EXCHANGE: true
```

#### **lyra-kraken (Institutional)**
```yaml
Container: lyra-kraken
IP Address: 172.20.0.13
External Port: 8084
Internal Port: 8080

Environment:
  EXCHANGE: kraken
  TRADING_MODE: spot_only
  INSTITUTIONAL: true
```

#### **lyra-binance (Data Only)**
```yaml
Container: lyra-binance
IP Address: 172.20.0.14
External Port: 8085
Internal Port: 8080

Environment:
  EXCHANGE: binance
  TRADING_MODE: data_only
  LIVE_TRADING: false
```

### **2. AI & SERVICES (4)**

#### **lyra-ai-orchestrator (AI Consensus)**
```yaml
Container: lyra-ai-orchestrator
IP Address: 172.20.0.20
External Port: 8090
Internal Port: 8080

Environment:
  AI_CONSENSUS_ENABLED: true
  OPENROUTER_MODELS: 327
  CONFIDENCE_THRESHOLD: 90
  VAULT_URL: http://lyra-vault:8200

OpenRouter Integration:
  - 8 API Keys from vault
  - 15 Free models
  - 12 Premium models
  - Multi-model consensus

Build Context: ./ai_containers/orchestrator/
Files:
  - Dockerfile
  - ai_orchestrator_service.py
  - requirements.txt
```

#### **lyra-vault (Security)**
```yaml
Container: lyra-vault
IP Address: 172.20.0.30
External Port: 8200
Internal Port: 8200

Environment:
  VAULT_DEV_ROOT_TOKEN_ID: lyra-root-token
  VAULT_DEV_LISTEN_ADDRESS: 0.0.0.0:8200

Security Features:
  - AES-256 encryption
  - Token-based auth
  - Audit logging
  - IPC_LOCK capability

Stored Credentials:
  - OKX API keys
  - 8 OpenRouter keys
  - Exchange secrets
  - System tokens
```

#### **lyra-redis (Cache)**
```yaml
Container: lyra-redis
Image: redis:7-alpine
IP Address: 172.20.0.31
External Port: 6379
Internal Port: 6379

Features:
  - High-performance caching
  - Session storage
  - Rate limit tracking
  - Real-time data cache
```

#### **lyra-hummingbot (Trading Bots)**
```yaml
Container: lyra-hummingbot
IP Address: 172.20.0.25
External Port: 8888
Internal Port: 8888

Environment:
  HUMMINGBOT_STRATEGY: pure_market_making
  EXCHANGES: gate,okx,whitebit,kraken
  VAULT_URL: http://lyra-vault:8200

Strategies Available:
  - Pure Market Making
  - Cross Exchange Market Making
  - Arbitrage
  - Perpetual Market Making
  - Liquidity Mining
  - Spot Perpetual Arbitrage
  - Fixed Grid
  - Hedge
```

### **3. MONITORING STACK (2)**

#### **lyra-prometheus (Metrics)**
```yaml
Container: lyra-prometheus
Image: prom/prometheus:latest
IP Address: 172.20.0.40
External Port: 9090
Internal Port: 9090

Configuration:
  - Scrapes all containers
  - 15s collection interval
  - 30-day retention
  - Alert rules configured

Metrics Collected:
  - Exchange API latency
  - Trading performance
  - System resources
  - Error rates
```

#### **lyra-grafana (Dashboards)**
```yaml
Container: lyra-grafana
Image: grafana/grafana:latest
IP Address: 172.20.0.41
External Port: 3000
Internal Port: 3000

Environment:
  GF_SECURITY_ADMIN_PASSWORD: lyra_admin_2025

Dashboards:
  - Trading Performance
  - System Health
  - Exchange Monitoring
  - AI Consensus Metrics
```

### **4. GATEWAY (1)**

#### **lyra-ngrok (Tunnel Gateway)**
```yaml
Container: lyra-ngrok
IP Address: 172.20.0.50
External Port: 4040
Internal Port: 4040

Environment:
  NGROK_AUTHTOKEN: ${NGROK_AUTHTOKEN}
  NGROK_REGION: us

Features:
  - Auto-restart tunnels
  - Multiple endpoint support
  - Traffic inspection
  - Load balancing ready
```

---

## 🚀 **STEP-BY-STEP DEPLOYMENT PROCEDURE**

### **Phase 1: Pre-Deployment Setup**

#### **Step 1.1: Environment Preparation**
```bash
# Verify Docker installation
docker --version
docker-compose --version

# Check available ports
netstat -tuln | grep -E "(8081|8082|8083|8084|8085|8090|8200|3000|4040|6379|8888|9090)"

# Verify disk space (minimum 10GB)
df -h /

# Check memory (minimum 4GB recommended)
free -h
```

#### **Step 1.2: Set Environment Variables**
```bash
# Set Ngrok authentication token
export NGROK_AUTHTOKEN='your_ngrok_token_here'

# Set deployment environment
export DEPLOYMENT_ENV='production'
export LYRA_VERSION='v1.0.0'

# Verify environment
echo "Ngrok Token: ${NGROK_AUTHTOKEN:0:10}..."
echo "Environment: $DEPLOYMENT_ENV"
```

#### **Step 1.3: Directory Navigation**
```bash
# Navigate to production containers
cd /home/ubuntu/ultimate_lyra_systems/production_containers

# Verify structure
ls -la
find . -name "Dockerfile" | wc -l  # Should show container count
```

### **Phase 2: Container Building**

#### **Step 2.1: Build All Containers**
```bash
# Build all containers without cache
docker-compose build --no-cache

# Monitor build progress
docker-compose build --no-cache --progress=plain
```

#### **Step 2.2: Verify Container Images**
```bash
# List built images
docker images | grep lyra

# Check image sizes
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" | grep lyra

# Verify all containers built
docker images | grep lyra | wc -l  # Should show 11
```

#### **Step 2.3: Test Individual Containers**
```bash
# Test vault container
docker run --rm lyra-vault:latest vault version

# Test AI orchestrator
docker run --rm lyra-ai-orchestrator:latest python --version

# Test exchange container
docker run --rm lyra-okx:latest python -c "import ccxt; print('CCXT OK')"
```

### **Phase 3: Network and Volume Setup**

#### **Step 3.1: Create Network**
```bash
# Create custom network
docker network create lyra_network --driver bridge --subnet=172.20.0.0/16

# Verify network
docker network ls | grep lyra
docker network inspect lyra_network
```

#### **Step 3.2: Initialize Volumes**
```bash
# Create named volumes
docker volume create lyra_vault_data
docker volume create lyra_prometheus_data
docker volume create lyra_grafana_data
docker volume create lyra_redis_data

# Verify volumes
docker volume ls | grep lyra
```

### **Phase 4: Service Deployment**

#### **Step 4.1: Deploy Core Services First**
```bash
# Start vault and redis first
docker-compose up -d lyra-vault lyra-redis

# Wait for services to be ready
sleep 30

# Verify core services
docker-compose ps lyra-vault lyra-redis
curl -s http://localhost:8200/v1/sys/health
```

#### **Step 4.2: Deploy Exchange Containers**
```bash
# Start exchange containers
docker-compose up -d lyra-okx lyra-gate lyra-whitebit lyra-kraken lyra-binance

# Monitor startup
docker-compose logs -f lyra-okx &
docker-compose logs -f lyra-gate &

# Wait for health checks
sleep 60
```

#### **Step 4.3: Deploy AI and Monitoring**
```bash
# Start AI orchestrator
docker-compose up -d lyra-ai-orchestrator

# Start monitoring stack
docker-compose up -d lyra-prometheus lyra-grafana

# Start Hummingbot
docker-compose up -d lyra-hummingbot

# Start Ngrok gateway
docker-compose up -d lyra-ngrok
```

#### **Step 4.4: Deploy All Remaining Services**
```bash
# Start any remaining services
docker-compose up -d

# Verify all containers running
docker-compose ps
```

### **Phase 5: Verification and Testing**

#### **Step 5.1: Health Check All Services**
```bash
# Check all container status
docker-compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"

# Individual health checks
curl -f http://localhost:8200/v1/sys/health    # Vault
curl -f http://localhost:9090/-/healthy        # Prometheus
curl -f http://localhost:3000/api/health       # Grafana
curl -f http://localhost:8082/health           # OKX
curl -f http://localhost:8081/health           # Gate.io
curl -f http://localhost:8090/health           # AI Orchestrator
```

#### **Step 5.2: Verify Network Connectivity**
```bash
# Test inter-container communication
docker-compose exec lyra-okx ping -c 3 lyra-vault
docker-compose exec lyra-ai-orchestrator ping -c 3 lyra-vault
docker-compose exec lyra-prometheus ping -c 3 lyra-okx
```

#### **Step 5.3: Test API Endpoints**
```bash
# Test exchange APIs
curl -s http://localhost:8082/api/status | jq .
curl -s http://localhost:8081/api/status | jq .

# Test AI orchestrator
curl -s http://localhost:8090/api/consensus | jq .

# Test monitoring
curl -s http://localhost:9090/api/v1/targets
```

### **Phase 6: Configuration and Credentials**

#### **Step 6.1: Configure Vault Secrets**
```bash
# Access vault container
docker-compose exec lyra-vault vault auth -method=token token=lyra-root-token

# Store OKX credentials
docker-compose exec lyra-vault vault kv put secret/okx \
  api_key="YOUR_API_KEY_HERE" \
  secret="YOUR_API_KEY_HERE" \
  passphrase="Millie2025!"

# Store OpenRouter keys
docker-compose exec lyra-vault vault kv put secret/openrouter \
  xai_key="sk-YOUR_OPENAI_API_KEY_HERE" \
  grok4_key="sk-YOUR_OPENAI_API_KEY_HERE"
```

#### **Step 6.2: Configure Exchange Connections**
```bash
# Test OKX connection
docker-compose exec lyra-okx python -c "
import ccxt
exchange = ccxt.okx({
    'apiKey': 'YOUR_API_KEY_HERE',
    'secret': 'YOUR_API_KEY_HERE',
    'password': 'Millie2025!',
    'sandbox': False
})
print('Balance:', exchange.fetch_balance())
"
```

### **Phase 7: Monitoring Setup**

#### **Step 7.1: Access Grafana Dashboard**
```bash
# Open Grafana
echo "Grafana URL: http://localhost:3000"
echo "Username: admin"
echo "Password: lyra_admin_2025"

# Import dashboards via API
curl -X POST http://admin:lyra_admin_2025@localhost:3000/api/dashboards/db \
  -H "Content-Type: application/json" \
  -d @monitoring/grafana/dashboards/trading-performance.json
```

#### **Step 7.2: Configure Prometheus Targets**
```bash
# Verify Prometheus targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {job: .labels.job, health: .health}'

# Check metrics collection
curl -s http://localhost:9090/api/v1/query?query=up | jq .
```

---

## 🔧 **MANAGEMENT COMMANDS**

### **Container Management**
```bash
# View all containers
docker-compose ps

# View logs for specific service
docker-compose logs -f lyra-okx

# Restart specific service
docker-compose restart lyra-ai-orchestrator

# Scale services
docker-compose up -d --scale lyra-okx=2

# Execute commands in container
docker-compose exec lyra-vault /bin/sh
```

### **System Monitoring**
```bash
# Resource usage
docker stats

# Network inspection
docker network inspect lyra_network

# Volume inspection
docker volume inspect lyra_vault_data

# Container inspection
docker inspect lyra-okx
```

### **Troubleshooting**
```bash
# Check container logs
docker-compose logs --tail=100 lyra-vault

# Debug container startup
docker-compose up lyra-okx  # Without -d for debug

# Check health status
docker-compose ps --filter "health=unhealthy"

# Restart unhealthy containers
docker-compose restart $(docker-compose ps --filter "health=unhealthy" -q)
```

---

## 🛑 **SHUTDOWN PROCEDURES**

### **Graceful Shutdown**
```bash
# Stop all services gracefully
docker-compose down

# Stop with timeout
docker-compose down -t 30

# View shutdown logs
docker-compose logs --tail=50
```

### **Complete Cleanup**
```bash
# Remove containers and networks
docker-compose down --remove-orphans

# Remove volumes (WARNING: Data loss)
docker-compose down -v

# Remove images
docker rmi $(docker images -q --filter "reference=lyra-*")

# Clean system
docker system prune -a
```

---

## 📊 **DEPLOYMENT VERIFICATION CHECKLIST**

### **Pre-Deployment ✓**
- [ ] Docker and Docker Compose installed
- [ ] Sufficient disk space (10GB+)
- [ ] Sufficient memory (4GB+)
- [ ] Required ports available
- [ ] Ngrok token configured
- [ ] Network connectivity verified

### **Build Phase ✓**
- [ ] All 11 containers built successfully
- [ ] No build errors in logs
- [ ] Container images present
- [ ] Image sizes reasonable
- [ ] Test containers run successfully

### **Deployment Phase ✓**
- [ ] Network created successfully
- [ ] Volumes created and mounted
- [ ] All containers started
- [ ] Health checks passing
- [ ] Inter-container communication working
- [ ] External ports accessible

### **Configuration Phase ✓**
- [ ] Vault unsealed and accessible
- [ ] Credentials stored securely
- [ ] Exchange connections verified
- [ ] AI orchestrator responding
- [ ] Monitoring collecting metrics
- [ ] Dashboards accessible

### **Production Ready ✓**
- [ ] All services healthy
- [ ] Monitoring active
- [ ] Logging functional
- [ ] Backup procedures tested
- [ ] Security verified
- [ ] Performance acceptable

---

## 🎯 **FINAL DEPLOYMENT COMMAND**

When you're ready to deploy everything:

```bash
# Complete deployment in one command
cd /home/ubuntu/ultimate_lyra_systems/production_containers && \
export NGROK_AUTHTOKEN='your_token_here' && \
docker-compose build --no-cache && \
docker-compose up -d && \
echo "🚀 Deployment complete! Check status with: docker-compose ps"
```

---

**🎉 Your Ultimate Lyra Trading System is ready for containerized deployment!**

*This detailed plan provides complete step-by-step instructions for deploying all 11 production containers with full monitoring, security, and AI capabilities.*
