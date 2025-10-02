# Ultimate Lyra Trading System - Quick Deployment Guide

**🚀 Get Your Trading System Running in 5 Minutes**

## Step 1: Download and Extract
```bash
# Download the complete system archive
wget [SYSTEM_ARCHIVE_URL]
tar -xzf ULTIMATE_LYRA_COMPLETE_SYSTEM_*.tar.gz
cd ultimate_lyra_v5/
```

## Step 2: Run Automated Deployment
```bash
# Execute the deployment script
chmod +x DEPLOY_TO_USER_UBUNTU.sh
./DEPLOY_TO_USER_UBUNTU.sh
```

## Step 3: Verify System Status
```bash
# Check all services are running
sudo systemctl status lyra-dashboard.service
sudo systemctl status lyra-amplification.service
sudo systemctl status lyra-hummingbot.service

# Check ports are accessible
netstat -tulpn | grep -E "(8751|9996|8400)"
```

## Step 4: Access Your Trading System
- **AI Enhanced Dashboard:** http://localhost:8751
- **Maximum Amplification:** http://localhost:9996
- **Hummingbot Integration:** http://localhost:8400

## Step 5: Configure for Live Trading
1. Navigate to http://localhost:9996
2. Review capital allocation ($13,947.76)
3. Click "ACTIVATE MAXIMUM TRADING" when ready
4. Monitor performance at http://localhost:8751

## 🔧 Troubleshooting
- **Services not starting:** Check logs with `sudo journalctl -u lyra-dashboard.service -f`
- **Ports in use:** Kill existing processes with `sudo pkill -f python3`
- **Permission errors:** Run `chmod +x *.py` in the system directory

## 📞 System Status Commands
```bash
# View all system processes
ps aux | grep -E "(ULTIMATE|MAXIMUM|HUMMINGBOT)"

# Check system health
curl http://localhost:8751/health
curl http://localhost:9996/health
curl http://localhost:8400/health

# View real-time logs
tail -f ~/ultimate_lyra_v5/logs/*.log
```

**Your Ultimate Lyra Trading System is now ready for live trading! 🎯**
