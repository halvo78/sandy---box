# 🔧 NGROK CONNECTION TROUBLESHOOTING & SOLUTIONS

## 🚨 NGROK ISSUE RESOLUTION GUIDE

**Keywords for Search**: ngrok issue, ngrok connection, ngrok troubleshooting, tunnel problems, HTTP/2 stream, ERR_NGROK_3004, bad record mac, multiple processes, port conflicts, ingest gateway

---

## 🔍 COMMON NGROK ISSUES IDENTIFIED

### **Issue 1: HTTP/2 Stream Errors**
- **Symptoms**: `curl: (92) HTTP/2 stream 0 was not closed cleanly`
- **Cause**: SSL decryption failures ("bad record mac")
- **Root Cause**: Network interference or SSL/TLS version mismatch

### **Issue 2: Multiple Process Conflicts**
- **Symptoms**: Multiple ngrok processes running simultaneously
- **Cause**: Previous ngrok instances not properly terminated
- **Result**: Port binding conflicts and tunnel creation failures

### **Issue 3: Port Binding Issues**
- **Symptoms**: Web interface not accessible on 4040, 4042, or 4043
- **Cause**: Multiple processes competing for same ports
- **Result**: Empty tunnel URLs and API endpoint failures

### **Issue 4: Gateway Crashes**
- **Symptoms**: Ingest gateway stops responding unexpectedly
- **Cause**: Process termination or system overload
- **Result**: ERR_NGROK_3004 errors

### **Issue 5: ERR_NGROK_3004**
- **Symptoms**: "Invalid or incomplete HTTP response" error page
- **Cause**: Backend service (ingest gateway) not responding
- **Result**: Complete connection failure

---

## ✅ PROVEN SOLUTION SEQUENCE

### **STEP 1: Complete Cleanup**
```bash
# Kill ALL ngrok processes
pkill -f ngrok

# Kill ingest gateway
pkill -f ingest_gateway

# Wait for cleanup
sleep 3
```

### **STEP 2: Restart Ingest Gateway**
```bash
# Navigate to system directory
cd /home/halvolyra/ultimate_lyra_systems

# Start ingest gateway in background
python3 ingest_gateway.py &
```

### **STEP 3: Start Single Ngrok (FOREGROUND)**
```bash
# Start ngrok in foreground to see status messages
ngrok http 8081

# This will show:
# - Tunnel URL when created
# - Connection status
# - Any error messages
```

### **STEP 4: Verify Connection**
```bash
# Test health endpoint
curl -X GET "https://[NEW_TUNNEL_URL]/health"

# Expected response:
# {"ok":true,"port":8081,"status":"operational","timestamp":...}
```

---

## 🎯 WORKING CONFIGURATION (CURRENT)

### **Connection Details**
- **Current Tunnel**: `https://3ce37fa57d09.ngrok.app`
- **Ingest Token**: `lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214`
- **Port**: `8081` (ingest gateway)
- **Web Interface**: `http://127.0.0.1:4042`
- **Region**: Asia Pacific (132ms latency)
- **Account**: Eli Halvorson (Pro Plan)

### **Environment Configuration**
```bash
# From .env file:
PORT=8081
INGEST_TOKEN=lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214
WATCH_DIR=/home/halvolyra/ultimate_lyra_systems/uploads
FILES_DIR=/home/halvolyra/ultimate_lyra_systems/uploads
ROOT=/home/halvolyra/ultimate_lyra_systems
```

---

## 🚀 QUICK RECONNECTION COMMANDS

### **Test Current Connection**
```bash
curl -X GET "https://3ce37fa57d09.ngrok.app/health"
```

### **Execute Commands via Ngrok**
```bash
curl -X POST "https://3ce37fa57d09.ngrok.app/ingest/event" \
  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \
  -H "Content-Type: application/json" \
  -d '{"type": "TEST", "steps": [{"run": "echo CONNECTION_TEST"}]}'
```

### **Get New Tunnel URL**
```bash
# Check ngrok API for current tunnel
curl -s http://127.0.0.1:4042/api/tunnels | jq -r '.tunnels[0].public_url'
```

---

## 🔧 TROUBLESHOOTING CHECKLIST

### **Before Starting**
- [ ] Check if ingest gateway is running: `ps aux | grep ingest_gateway`
- [ ] Check for multiple ngrok processes: `ps aux | grep ngrok`
- [ ] Verify port 8081 is available: `curl localhost:8081/health`

### **During Setup**
- [ ] Kill all existing processes first
- [ ] Start ingest gateway before ngrok
- [ ] Use foreground ngrok to see status messages
- [ ] Wait for "tunnel session started" message

### **After Setup**
- [ ] Test health endpoint first
- [ ] Verify command execution works
- [ ] Document new tunnel URL
- [ ] Update any scripts with new URL

---

## 🎯 SUCCESS INDICATORS

### **Ngrok Startup Messages**
```
Session Status                online
Account                       Eli Halvorson (Plan: Pro)
Version                       3.30.0
Region                        Asia Pacific (ap)
Latency                       132ms
Web Interface                 http://127.0.0.1:4042
Forwarding                    https://[ID].ngrok.app -> http://localhost:8081
```

### **Health Check Response**
```json
{
  "ok": true,
  "port": 8081,
  "status": "operational",
  "timestamp":+1-XXX-XXX-XXXX.249049
}
```

### **Command Execution Response**
```json
{
  "event_type": "TEST",
  "logs": [{
    "cmd": "echo CONNECTION_TEST",
    "ok": true,
    "returncode": 0,
    "stderr": "",
    "stdout": "CONNECTION_TEST\n"
  }],
  "ok": true
}
```

---

## 📋 EMERGENCY RECOVERY

### **If All Else Fails**
```bash
# Nuclear option - restart everything
sudo reboot

# After reboot:
cd /home/halvolyra/ultimate_lyra_systems
python3 ingest_gateway.py &
ngrok http 8081
```

### **Alternative Access Methods**
- SSH tunneling: `ssh -L 8081:localhost:8081 user@host`
- Direct IP access (if firewall allows)
- VPN connection to local network

---

## 🔍 SEARCH KEYWORDS FOR FUTURE REFERENCE

**Primary Keywords**: `ngrok issue`, `ngrok connection`, `ngrok troubleshooting`

**Specific Issues**: `HTTP/2 stream`, `ERR_NGROK_3004`, `bad record mac`, `multiple processes`, `port conflicts`, `ingest gateway`, `tunnel problems`

**Solution Keywords**: `ngrok restart`, `process cleanup`, `foreground ngrok`, `connection test`

---

*Last Updated: September 29, 2025*
*Working Tunnel: https://3ce37fa57d09.ngrok.app*
*Status: FULLY OPERATIONAL*
