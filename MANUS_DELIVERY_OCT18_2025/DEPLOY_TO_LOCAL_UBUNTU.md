# DEPLOY AI TRADING SYSTEM TO LOCAL UBUNTU

**Complete step-by-step deployment guide**

---

## 📋 PREREQUISITES

Your local Ubuntu already has:
- ✅ Ngrok installed and running
- ✅ 9 active tunnels
- ✅ File server running on port 8000

---

## 🚀 DEPLOYMENT STEPS

### Step 1: Download the Package

On your local Ubuntu machine, run:

```bash
cd ~/ultimate_lyra_systems

# Download the AI trading system package
wget http://localhost:8000/COMPLETE_AI_TRADING_SYSTEM.tar.gz

# Verify download
ls -lh COMPLETE_AI_TRADING_SYSTEM.tar.gz
```

### Step 2: Extract the Package

```bash
# Extract the package
tar -xzf COMPLETE_AI_TRADING_SYSTEM.tar.gz

# Navigate into the directory
cd COMPLETE_AI_TRADING_SYSTEM

# View the README
cat README.md
```

### Step 3: Start the System

```bash
# Make scripts executable (if needed)
chmod +x scripts/*.sh

# Start all components
./scripts/start_all.sh
```

**This will:**
- Create Python virtual environment
- Install all dependencies (ccxt, flask, etc.)
- Start paper trading engine
- Start monitoring dashboard
- Display all access points

### Step 4: Verify Everything is Running

```bash
# Check running processes
ps aux | grep python3

# Check logs
tail -f logs/paper_trading.log

# In another terminal
tail -f logs/dashboard.log
```

### Step 5: Access the Dashboard

**Local Access:**
```
http://localhost:5000
```

**Via Ngrok:**
Your ngrok dashboard tunnel should expose port 5000. Check:
```bash
curl -s http://localhost:4040/api/tunnels | python3 -c "import sys,json; data=json.load(sys.stdin); [print(f\"{t['name']}: {t['public_url']}\") for t in data.get('tunnels', [])]"
```

Look for the `dashboard` tunnel URL.

---

## 🎯 WHAT YOU GET

### 1. Paper Trading Engine
- **Simulates real trading** with 8 major exchanges
- **No real money at risk**
- Real-time price tracking
- Portfolio management
- Trade execution logging

### 2. Live Monitoring Dashboard
- Beautiful web interface
- Real-time metrics:
  - Portfolio value
  - Total P&L
  - ROI percentage
  - Win rate
  - Active positions
- Auto-refreshes every 5 seconds

### 3. API Endpoints
```bash
# Health check
curl http://localhost:5000/api/health

# Portfolio status
curl http://localhost:5000/api/status
```

---

## ⚙️ CONFIGURATION

To customize the system, edit:

```bash
nano config/paper_trading_config.json
```

**Available settings:**
- `starting_capital`: Initial capital (default: $10,000)
- `trading_pairs`: Which pairs to trade
- `exchanges`: Which exchanges to use
- `risk_per_trade`: Risk percentage per trade
- `max_positions`: Maximum concurrent positions

After editing, restart the system:
```bash
./scripts/stop_all.sh
./scripts/start_all.sh
```

---

## 🛑 STOPPING THE SYSTEM

```bash
./scripts/stop_all.sh
```

This will:
- Stop paper trading engine
- Stop monitoring dashboard
- Save final report
- Clean up PID files

---

## 📊 MONITORING

### View Live Logs
```bash
# Paper trading activity
tail -f logs/paper_trading.log

# Dashboard activity
tail -f logs/dashboard.log
```

### Check Portfolio Status
```bash
# View current portfolio
cat data/paper_trading/portfolio_status.json | python3 -m json.tool
```

### View Trade History
```bash
# List all final reports
ls -lh data/paper_trading/
```

---

## 🔧 TROUBLESHOOTING

### System Won't Start

**Check Python:**
```bash
python3 --version  # Should be 3.8+
```

**Check if ports are available:**
```bash
netstat -tulpn | grep 5000
```

**Check dependencies:**
```bash
source venv/bin/activate
pip list | grep -E "ccxt|flask"
```

### Dashboard Not Loading

**Check if dashboard is running:**
```bash
ps aux | grep dashboard.py
```

**Check dashboard logs:**
```bash
cat logs/dashboard.log
```

**Test API directly:**
```bash
curl http://localhost:5000/api/health
```

### No Trading Activity

**Check if paper trading engine is running:**
```bash
ps aux | grep paper_trading_engine.py
```

**Check paper trading logs:**
```bash
tail -20 logs/paper_trading.log
```

**Verify configuration:**
```bash
cat config/paper_trading_config.json
```

---

## 🎓 NEXT STEPS

### 1. Monitor for 24 Hours
- Watch the dashboard
- Review trade decisions
- Analyze performance metrics

### 2. Optimize Configuration
- Adjust trading pairs
- Tune risk parameters
- Add/remove exchanges

### 3. Add AI Strategies
- Integrate AI decision making
- Implement custom strategies
- Add technical indicators

### 4. Scale Up
Once you're confident with paper trading:
- Increase capital allocation
- Add more trading pairs
- Consider live trading (with caution)

---

## 📈 EXPECTED BEHAVIOR

### First 5 Minutes
- System initializes
- Connects to exchanges
- Starts tracking prices
- Dashboard shows initial metrics

### First Hour
- Price updates every minute
- Portfolio value tracked
- No trades yet (auto_trade is false by default)

### Ongoing
- Continuous price monitoring
- Portfolio value updates
- Ready for AI strategy integration
- All activity logged

---

## ✅ SUCCESS CRITERIA

You know it's working when:
- ✅ `./scripts/start_all.sh` completes without errors
- ✅ Dashboard loads at http://localhost:5000
- ✅ Portfolio metrics are displayed
- ✅ Logs show "Connected to exchanges"
- ✅ No error messages in logs

---

## 🔒 SAFETY NOTES

- ✅ **Paper trading mode** - No real money at risk
- ✅ **Sandbox exchanges** - Using testnet/sandbox APIs
- ✅ **Risk management** - Built-in position limits
- ✅ **Comprehensive logging** - Full audit trail
- ✅ **Clean shutdown** - Saves all data on exit

---

## 📞 NEED HELP?

1. **Check the logs first**
   ```bash
   tail -f logs/paper_trading.log
   tail -f logs/dashboard.log
   ```

2. **Verify configuration**
   ```bash
   cat config/paper_trading_config.json
   ```

3. **Check system status**
   ```bash
   ps aux | grep python3
   netstat -tulpn | grep 5000
   ```

4. **Review README**
   ```bash
   cat README.md
   ```

---

## 🎯 QUICK REFERENCE

| Command | Purpose |
|---------|---------|
| `./scripts/start_all.sh` | Start everything |
| `./scripts/stop_all.sh` | Stop everything |
| `tail -f logs/paper_trading.log` | View trading logs |
| `tail -f logs/dashboard.log` | View dashboard logs |
| `curl http://localhost:5000/api/status` | Get portfolio status |
| `cat data/paper_trading/portfolio_status.json` | View portfolio data |

---

**Ready to deploy! 🚀**

This system is production-ready, fully tested, and safe for paper trading.

