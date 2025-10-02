# MANUS NGROK CONNECTION & INHERITANCE GUIDE

## 🔗 HOW MANUS CONNECTS TO YOUR LOCAL UBUNTU SYSTEM

### Connection Method: ngrok HTTP Tunnel
Manus connects to your local Ubuntu system through an ngrok HTTP tunnel that you have established. This creates a secure bridge between Manus's sandbox environment and your local machine.

### Current Active Connection Details
- **ngrok URL**: `https://3ce37fa57d09.ngrok.app`
- **Local Port**: `8081` (Ingest Gateway)
- **Authentication Token**: `lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214`
- **Account**: Eli Halvorson (Pro Plan)
- **Region**: Asia Pacific (ap)
- **Web Interface**: `http://127.0.0.1:4042`

### Proof of Connection
The log entry `17:57:00.025 AEST GET /health` confirms successful connection from Manus to your system.

---

## 🛠️ TECHNICAL IMPLEMENTATION

### How Manus Accesses Your System

1. **Health Check Command**:
```bash
curl -X GET "https://3ce37fa57d09.ngrok.app/health"
```

2. **File Listing Command**:
```bash
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" \
  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \
  -H "Content-Type: application/json" \
  -d '{"type": "SYSTEM_CHECK", "steps": [{"run": "ls -la /home/halvolyra/ultimate_lyra_systems/"}]}'
```

3. **File Reading Command**:
```bash
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" \
  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \
  -H "Content-Type: application/json" \
  -d '{"type": "READ_FILE", "steps": [{"run": "cat /home/halvolyra/ultimate_lyra_systems/FILENAME.py"}]}'
```

4. **File Writing Command**:
```bash
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" \
  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \
  -H "Content-Type: application/json" \
  -d '{"type": "WRITE_FILE", "steps": [{"run": "echo \"CONTENT\" > /home/halvolyra/ultimate_lyra_systems/FILENAME.py"}]}'
```

### Manus Shell Commands for ngrok Access
```python
# In Manus sandbox, these commands access your system:
shell.exec("curl -X GET \"https://3ce37fa57d09.ngrok.app/health\"")
shell.exec("curl -X POST \"https://3ce37fa57d09.ngrok.app/ingest/event\" -H \"X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214\" -H \"Content-Type: application/json\" -d '{\"type\": \"COMMAND\", \"steps\": [{\"run\": \"LINUX_COMMAND_HERE\"}]}'")
```

---

## 📋 INHERITANCE REQUIREMENTS

### Critical Information for New Session

#### 1. Connection Details
```
ngrok URL: https://3ce37fa57d09.ngrok.app
Ingest Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214
Local Port: 8081
Authentication: Token-based
Status: ACTIVE (as of session end)
```

#### 2. Your System Paths
```
Main System Directory: /home/halvolyra/ultimate_lyra_systems/
Vault Directory: /home/halvolyra/.lyra-vault/
Config Directory: /home/halvolyra/.config/ngrok/
Log Directory: /home/halvolyra/logs/
```

#### 3. Active Processes (Check these first)
```
Ingest Gateway: Port 8081 (PID varies)
ngrok Tunnel: Port 8081 → public URL
Trading System: Demo mode (PID varies)
```

#### 4. Key Files on Your System
```
/home/halvolyra/ultimate_lyra_systems/ULTIMATE_OMNISCIENT_TRADING_SYSTEM.py
/home/halvolyra/ultimate_lyra_systems/BUILD_PLAN_STATUS.json
/home/halvolyra/.lyra-vault/encrypted_credentials.vault
/home/halvolyra/.config/ngrok/ngrok.yml
```

---

## 🔄 INHERITANCE PROCEDURE

### Step 1: Verify Connection
New Manus should immediately test:
```bash
curl -X GET "https://3ce37fa57d09.ngrok.app/health"
```
Expected response: `{"ok":true,"port":8081,"status":"operational"}`

### Step 2: Check System Status
```bash
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" \
  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \
  -H "Content-Type: application/json" \
  -d '{"type": "STATUS", "steps": [{"run": "ps aux | grep -E \"(ingest|ngrok|trading)\""}]}'
```

### Step 3: List Current Files
```bash
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" \
  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \
  -H "Content-Type: application/json" \
  -d '{"type": "LIST", "steps": [{"run": "ls -la /home/halvolyra/ultimate_lyra_systems/"}]}'
```

### Step 4: Extract Inheritance Archive
If provided with `lyra_commissioning_state.tar.gz`:
```bash
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" \
  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \
  -H "Content-Type: application/json" \
  -d '{"type": "EXTRACT", "steps": [{"run": "cd /home/halvolyra && tar -xzf lyra_commissioning_state.tar.gz"}]}'
```

---

## 🚨 TROUBLESHOOTING

### If Connection Fails

1. **Check ngrok Status**:
```bash
curl -s http://127.0.0.1:4042/api/tunnels | jq -r '.tunnels[0].public_url'
```

2. **Restart ngrok** (if needed):
```bash
pkill -f ngrok
cd /home/halvolyra/ultimate_lyra_systems
python3 ingest_gateway.py &
ngrok http 8081
```

3. **Update URL** (if changed):
Replace `https://3ce37fa57d09.ngrok.app` with new URL from ngrok output.

### Common Issues
- **ERR_NGROK_3004**: Ingest gateway not running
- **HTTP/2 stream errors**: SSL/TLS mismatch
- **Multiple processes**: Kill all ngrok processes first

---

## 🔐 SECURITY NOTES

### Authentication
- All requests require `X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214`
- Token is unique to your system
- ngrok Pro account provides additional security

### Permissions
- Manus can execute any Linux command through the ingest gateway
- Full read/write access to your file system via ngrok
- Can start/stop processes and services

### Monitoring
- All requests logged in ngrok interface at `http://127.0.0.1:4042`
- Ingest gateway logs all commands executed
- Connection history preserved in ngrok dashboard

---

## 📊 CURRENT PROJECT STATE

### Ultimate Lyra Trading System Status
- **Location**: `/home/halvolyra/ultimate_lyra_systems/`
- **Main File**: `ULTIMATE_OMNISCIENT_TRADING_SYSTEM.py`
- **Completion**: 80% (8/10 phases)
- **Status**: Operational in demo mode

### Active Integrations
- **OpenRouter AI**: 327+ models available
- **Exchanges**: Framework ready, credentials in vault
- **ngrok**: Fully operational remote access
- **Manus**: Complete integration via ingest gateway

### Next Steps
1. Complete exchange API integration
2. Activate live trading mode
3. Deploy web dashboard
4. Final system validation

---

## 🎯 INHERITANCE SUCCESS CRITERIA

### New Manus Must Demonstrate:
1. ✅ Successful health check to ngrok URL
2. ✅ Ability to list files on your system
3. ✅ Ability to read existing files
4. ✅ Ability to write new files
5. ✅ Understanding of project current state

### Verification Commands:
```bash
# Test 1: Health Check
curl -X GET "https://3ce37fa57d09.ngrok.app/health"

# Test 2: File Listing
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" -H "Content-Type: application/json" -d '{"type": "TEST", "steps": [{"run": "ls /home/halvolyra/ultimate_lyra_systems/"}]}'

# Test 3: File Reading
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" -H "Content-Type: application/json" -d '{"type": "TEST", "steps": [{"run": "head -5 /home/halvolyra/ultimate_lyra_systems/ULTIMATE_OMNISCIENT_TRADING_SYSTEM.py"}]}'

# Test 4: File Writing
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" -H "Content-Type: application/json" -d '{"type": "TEST", "steps": [{"run": "echo \"INHERITANCE_TEST_$(date)\" > /home/halvolyra/inheritance_test.txt"}]}'
```

---

## 📝 FINAL NOTES

This document provides complete instructions for any new Manus session to immediately connect to your system and continue the Ultimate Lyra Trading System development without any loss of progress or context.

The ngrok connection is the key to seamless inheritance - it allows Manus to treat your local Ubuntu system as an extension of its own sandbox environment.

**Last Updated**: September 30, 2025  
**Connection Status**: ACTIVE  
**System Status**: OPERATIONAL  
**Inheritance Ready**: ✅ YES
