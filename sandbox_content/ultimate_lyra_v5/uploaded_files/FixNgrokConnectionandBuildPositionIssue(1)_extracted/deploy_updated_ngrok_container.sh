#!/bin/bash
set -e

echo "🚀 Deploying Updated Ultimate Ngrok Container..."
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}[STEP]${NC} $1"
}

# Check if running as correct user
if [ "$USER" != "halvolyra" ]; then
    print_error "This script should be run as user 'halvolyra'"
    print_status "Please run: su - halvolyra"
    exit 1
fi

# Set working directory
WORK_DIR="/home/halvolyra/ultimate_lyra_systems/ngrok_container"
print_status "Working directory: $WORK_DIR"

# Create directory structure
print_header "Creating directory structure..."
mkdir -p "$WORK_DIR"/{config,logs,data,scripts}
cd "$WORK_DIR"

# Copy updated files
print_header "Copying updated container files..."

# Copy main files
cp /home/ubuntu/docker-compose-updated.yml "$WORK_DIR/docker-compose.yml"
cp /home/ubuntu/Dockerfile-updated "$WORK_DIR/Dockerfile"
cp /home/ubuntu/manus_verification_enhanced.py "$WORK_DIR/manus_verification.py"

# Copy existing files if they exist
for file in tunnel_manager.py ngrok_config.yml start_ngrok.sh safe_tunnel_policies.py requirements.txt README.md; do
    if [ -f "/home/ubuntu/upload/$file" ]; then
        cp "/home/ubuntu/upload/$file" "$WORK_DIR/"
        print_status "Copied $file"
    else
        print_warning "$file not found, will create default"
    fi
done

# Create enhanced requirements.txt
print_header "Creating enhanced requirements.txt..."
cat > "$WORK_DIR/requirements.txt" << 'EOF'
# Core dependencies
requests>=2.31.0
aiohttp>=3.8.0
pyyaml>=6.0
flask>=2.3.0
gunicorn>=21.0.0

# Monitoring and management
psutil>=5.9.0
docker>=6.1.0
prometheus-client>=0.17.0
structlog>=23.1.0

# Security and compliance
cryptography>=41.0.0
pyjwt>=2.8.0

# Development and testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
black>=23.7.0
flake8>=6.0.0
EOF

# Create enhanced ngrok config
print_header "Creating enhanced ngrok configuration..."
cat > "$WORK_DIR/ngrok_config.yml" << 'EOF'
version: "2"
authtoken: ${NGROK_AUTHTOKEN}
region: ap
console_ui: true
console_ui_color: transparent
log_level: info
log_format: json
log: /app/logs/ngrok.log

tunnels:
  ingest:
    proto: http
    addr: 8081
    subdomain: ${NGROK_SUBDOMAIN_INGEST:-lyra-ingest}
    inspect: true
    bind_tls: true
    
  dashboard:
    proto: http
    addr: 8000
    subdomain: ${NGROK_SUBDOMAIN_DASH:-lyra-dash}
    inspect: true
    bind_tls: true
    
  metrics:
    proto: http
    addr: 3000
    subdomain: ${NGROK_SUBDOMAIN_METRICS:-lyra-metrics}
    inspect: true
    bind_tls: true
    
  inspect:
    proto: http
    addr: 4040
    subdomain: ${NGROK_SUBDOMAIN_INSPECT:-lyra-inspect}
    inspect: true
    bind_tls: true

  hummingbot:
    proto: http
    addr: 8086
    subdomain: ${NGROK_SUBDOMAIN_HUMMINGBOT:-lyra-hummingbot}
    inspect: true
    bind_tls: true
EOF

# Create supervisor configuration
print_header "Creating supervisor configuration..."
cat > "$WORK_DIR/supervisord.conf" << 'EOF'
[supervisord]
nodaemon=true
user=lyra_user
logfile=/app/logs/supervisord.log
pidfile=/app/supervisord.pid

[program:ngrok]
command=ngrok start --all --config /app/ngrok_config.yml
directory=/app
user=lyra_user
autostart=true
autorestart=true
stderr_logfile=/app/logs/ngrok_error.log
stdout_logfile=/app/logs/ngrok_output.log
environment=NGROK_AUTHTOKEN="%(ENV_NGROK_AUTHTOKEN)s"

[program:auto_manager]
command=python3 /app/auto_ngrok_manager.py
directory=/app
user=lyra_user
autostart=true
autorestart=true
stderr_logfile=/app/logs/auto_manager_error.log
stdout_logfile=/app/logs/auto_manager_output.log

[program:tunnel_manager]
command=python3 /app/tunnel_manager.py
directory=/app
user=lyra_user
autostart=true
autorestart=true
stderr_logfile=/app/logs/tunnel_manager_error.log
stdout_logfile=/app/logs/tunnel_manager_output.log
EOF

# Create nginx configuration
print_header "Creating nginx configuration..."
cat > "$WORK_DIR/nginx.conf" << 'EOF'
events {
    worker_connections 1024;
}

http {
    upstream ngrok_inspector {
        server localhost:4040;
    }
    
    upstream ingest_gateway {
        server localhost:8081;
    }
    
    server {
        listen 8080;
        server_name localhost;
        
        location /inspector/ {
            proxy_pass http://ngrok_inspector/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
        
        location /ingest/ {
            proxy_pass http://ingest_gateway/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
        
        location /health {
            return 200 "OK";
            add_header Content-Type text/plain;
        }
    }
}
EOF

# Copy the auto manager from the working system
print_header "Copying Auto Ngrok Manager..."
if [ -f "/home/halvolyra/ultimate_lyra_systems/auto_ngrok_manager.py" ]; then
    cp "/home/halvolyra/ultimate_lyra_systems/auto_ngrok_manager.py" "$WORK_DIR/"
    print_status "Copied working auto_ngrok_manager.py"
else
    print_warning "Auto manager not found, creating basic version"
    cat > "$WORK_DIR/auto_ngrok_manager.py" << 'EOF'
#!/usr/bin/env python3
import time
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def monitor_tunnels():
    while True:
        try:
            resp = requests.get('http://localhost:4040/api/tunnels', timeout=5)
            tunnels = resp.json().get('tunnels', [])
            logger.info(f"Monitoring {len(tunnels)} tunnels")
            time.sleep(30)
        except Exception as e:
            logger.error(f"Monitor error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    monitor_tunnels()
EOF
fi

# Create enhanced startup script
print_header "Creating enhanced startup script..."
cat > "$WORK_DIR/start_ngrok.sh" << 'EOF'
#!/bin/bash
set -e

echo "🚀 Starting Ultimate Ngrok Container..."

# Validate environment
if [ -z "$NGROK_AUTHTOKEN" ]; then
    echo "❌ NGROK_AUTHTOKEN not set"
    exit 1
fi

# Configure ngrok
ngrok config add-authtoken $NGROK_AUTHTOKEN

# Create log directory
mkdir -p /app/logs

# Start all services via supervisor
exec supervisord -c /app/supervisord.conf
EOF

chmod +x "$WORK_DIR/start_ngrok.sh"

# Create Dockerfile for monitor service
print_header "Creating monitor service Dockerfile..."
cat > "$WORK_DIR/Dockerfile.monitor" << 'EOF'
FROM python:3.11-alpine

RUN apk add --no-cache curl

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY auto_ngrok_manager.py ./

CMD ["python3", "auto_ngrok_manager.py"]
EOF

# Create Dockerfile for gateway service
print_header "Creating gateway service Dockerfile..."
cat > "$WORK_DIR/Dockerfile.gateway" << 'EOF'
FROM python:3.11-alpine

RUN apk add --no-cache curl bash

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy ingest gateway from host system
COPY --from=host /home/halvolyra/ultimate_lyra_systems/ingest_gateway.py ./

EXPOSE 8081

CMD ["python3", "ingest_gateway.py"]
EOF

# Create Prometheus configuration
print_header "Creating monitoring configuration..."
mkdir -p "$WORK_DIR/config"
cat > "$WORK_DIR/config/prometheus.yml" << 'EOF'
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'ngrok-container'
    static_configs:
      - targets: ['localhost:8080']
  
  - job_name: 'auto-manager'
    static_configs:
      - targets: ['auto-ngrok-monitor:8080']
EOF

# Create deployment script
print_header "Creating deployment commands..."
cat > "$WORK_DIR/deploy.sh" << 'EOF'
#!/bin/bash
set -e

echo "🚀 Deploying Ultimate Ngrok Container..."

# Set your ngrok token
export NGROK_AUTHTOKEN="your_ngrok_token_here"

# Build and start services
docker-compose down --remove-orphans
docker-compose build --no-cache
docker-compose up -d

# Wait for services to start
echo "⏳ Waiting for services to start..."
sleep 30

# Run verification
echo "🔍 Running verification..."
docker-compose exec ngrok python3 manus_verification.py

echo "✅ Deployment complete!"
echo "📊 Access ngrok inspector: http://localhost:4040"
echo "🔗 Access services via ngrok tunnels"
EOF

chmod +x "$WORK_DIR/deploy.sh"

# Create status check script
print_header "Creating status check script..."
cat > "$WORK_DIR/check_status.sh" << 'EOF'
#!/bin/bash

echo "📊 Ultimate Ngrok Container Status"
echo "=================================="

# Container status
echo "🐳 Container Status:"
docker-compose ps

echo ""
echo "🔗 Tunnel Status:"
curl -s http://localhost:4040/api/tunnels | jq '.tunnels[] | {name: .name, public_url: .public_url, proto: .proto}'

echo ""
echo "🏥 Health Checks:"
docker-compose exec ngrok python3 manus_verification.py

echo ""
echo "📝 Recent Logs:"
docker-compose logs --tail=10 ngrok
EOF

chmod +x "$WORK_DIR/check_status.sh"

# Create README
print_header "Creating comprehensive README..."
cat > "$WORK_DIR/README.md" << 'EOF'
# Ultimate Ngrok Container - Enhanced Edition

## 🎯 Features

- **Auto-Restart Management** - Integrated with your working Auto Ngrok Manager
- **Multi-Service Support** - Ingest, Dashboard, Metrics, Inspector, Hummingbot
- **Enhanced Monitoring** - Prometheus + Grafana integration
- **Manus Verification** - Comprehensive testing for AI integration
- **Production Ready** - Supervisor, Nginx, Health checks
- **Compliance Ready** - ISO 27001, spot-only safety controls

## 🚀 Quick Start

1. **Set your ngrok token:**
   ```bash
   export NGROK_AUTHTOKEN="your_ngrok_token_here"
   ```

2. **Deploy the container:**
   ```bash
   ./deploy.sh
   ```

3. **Check status:**
   ```bash
   ./check_status.sh
   ```

4. **Run Manus verification:**
   ```bash
   docker-compose exec ngrok python3 manus_verification.py
   ```

## 🔗 Access Points

- **Ngrok Inspector:** http://localhost:4040
- **Grafana Dashboard:** http://localhost:3000 (admin/lyra_admin_2025)
- **Prometheus Metrics:** http://localhost:9090
- **Ingest Gateway:** http://localhost:8081

## 🤖 Manus Integration

The container includes enhanced Manus verification that tests:
- Health endpoints
- Command execution
- System integration
- Auto manager status

Run verification:
```bash
docker-compose exec ngrok python3 manus_verification.py
```

Get Manus commands:
```bash
docker-compose exec ngrok python3 manus_verification.py commands
```

## 🔧 Management

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f ngrok

# Restart specific service
docker-compose restart ngrok

# Update and redeploy
docker-compose down && docker-compose build --no-cache && docker-compose up -d
```

## 📊 Monitoring

The container includes comprehensive monitoring:
- Supervisor for process management
- Prometheus for metrics collection
- Grafana for visualization
- Health checks every 30 seconds
- Auto-restart on failure

## 🛡️ Security

- Non-root user execution
- Spot-only trading compliance
- Traffic inspection enabled
- Secure token authentication
- Network isolation

## 🎉 Integration with Auto Ngrok Manager

This container is designed to work alongside your existing Auto Ngrok Manager service:
- Compatible with your current setup
- Enhances monitoring capabilities
- Provides containerized deployment option
- Maintains all existing functionality
EOF

print_status "Container files created successfully!"
print_status ""
print_status "📁 Container directory: $WORK_DIR"
print_status "🚀 To deploy: cd $WORK_DIR && ./deploy.sh"
print_status "📊 To check status: cd $WORK_DIR && ./check_status.sh"
print_status ""
print_warning "Remember to set your NGROK_AUTHTOKEN before deploying!"

echo "✅ Updated Ultimate Ngrok Container ready for deployment!"
