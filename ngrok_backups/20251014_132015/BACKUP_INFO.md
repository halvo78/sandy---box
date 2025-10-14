# Ngrok Complete Backup

**Timestamp:** 20251014_132015  
**Date:** Tue Oct 14 13:20:15 AEDT 2025  
**Hostname:** HALVO-AI  
**User:** halvolyra  

## Files Backed Up

- `ngrok.yml` - Complete configuration
- `tunnels.json` - Active tunnel data (JSON)
- `tunnels.txt` - Active tunnel URLs (human-readable)
- `ngrok-permanent.service` - Systemd service file
- `ngrok_service.log` - Service logs (last 10000 lines)
- `ngrok_service_error.log` - Error logs (last 10000 lines)
- `http_traffic/` - All HTTP traffic logs
- `RESTORE.sh` - One-command restore script

## Quick Restore

```bash
cd /home/halvolyra/ultimate_lyra_systems/backups/ngrok_complete/20251014_132015
./RESTORE.sh
sudo systemctl start ngrok-permanent
```

## Current Tunnels

```
dashboard            https://6824292fd869.ngrok.app
production           https://57a01b1d7eab.ngrok.app
file_server          https://5eee3ebb0e46.ngrok.app
```

## System Info

- Ngrok Version: ngrok version 3.30.0
- Ubuntu Version: Ubuntu 24.04.3 LTS
- Kernel: 6.6.87.2-microsoft-standard-WSL2
