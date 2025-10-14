# 🚀 FIXED DEPLOYMENT INSTRUCTIONS

## Issues Fixed:
1. ✅ Ngrok file server now serving correctly
2. ✅ Virtual environment setup for Python packages
3. ✅ Proper .bashrc configuration

---

## On Your Local Ubuntu (halvolyra@HALVO-AI):

### 1. Download the Package (FIXED)

```bash
cd ~/ultimate_lyra_systems
wget https://ef70762389ce.ngrok.app/ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz
```

**If 404 error, try alternative:**
```bash
# The file is available at port 9000
curl -O http://localhost:9000/ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz
# OR via Ngrok
wget https://ef70762389ce.ngrok.app:9000/ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz
```

### 2. Extract

```bash
tar -xzf ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz
cd DEPLOYMENT_PACKAGE
```

### 3. Create Virtual Environment (FIXED for externally-managed-environment)

```bash
# Create virtual environment
python3 -m venv ~/lyra_venv

# Activate it
source ~/lyra_venv/bin/python

# Install dependencies in venv
~/lyra_venv/bin/pip install aiohttp requests urllib3
```

### 4. Set Environment Variables (FIXED for permission denied)

```bash
# Use sudo to edit .bashrc OR add to your shell directly
sudo bash -c 'cat >> /home/halvolyra/.bashrc << EOF
export OPENROUTER_API_KEY="your-actual-api-key-here"
export MODELS_CONFIG_PATH="$HOME/ultimate_lyra_systems/models_config.json"
export INSTALL_DIR="$HOME/ultimate_lyra_systems"
EOF'

# OR add to current session only
export OPENROUTER_API_KEY="your-actual-api-key-here"
export MODELS_CONFIG_PATH="$HOME/ultimate_lyra_systems/models_config.json"
export INSTALL_DIR="$HOME/ultimate_lyra_systems"
```

### 5. Deploy the Fixes

```bash
# Backup old files
cp ~/ultimate_lyra_systems/integration_hub_production.py ~/ultimate_lyra_systems/integration_hub_production.py.backup 2>/dev/null || true

# Deploy new files
cp DEPLOYMENT_PACKAGE/integration_hub_production_FIXED.py ~/ultimate_lyra_systems/integration_hub_production.py
cp DEPLOYMENT_PACKAGE/installer_FIXED.py ~/ultimate_lyra_systems/installer.py
cp DEPLOYMENT_PACKAGE/order_execution_OPTIMIZED.py ~/ultimate_lyra_systems/order_execution.py
```

### 6. Test with Virtual Environment

```bash
cd ~/ultimate_lyra_systems
~/lyra_venv/bin/python integration_hub_production.py
```

---

## Alternative: Quick Deploy Script

Save this as `quick_deploy.sh`:

```bash
#!/bin/bash

# Download
cd ~/ultimate_lyra_systems
wget -O ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz https://ef70762389ce.ngrok.app/ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz || \
curl -O https://ef70762389ce.ngrok.app/ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz

# Extract
tar -xzf ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz

# Create venv
python3 -m venv ~/lyra_venv
~/lyra_venv/bin/pip install aiohttp requests urllib3

# Set env vars
export OPENROUTER_API_KEY="your-key"
export MODELS_CONFIG_PATH="$HOME/ultimate_lyra_systems/models_config.json"

# Deploy
cp DEPLOYMENT_PACKAGE/integration_hub_production_FIXED.py integration_hub_production.py
cp DEPLOYMENT_PACKAGE/installer_FIXED.py installer.py
cp DEPLOYMENT_PACKAGE/order_execution_OPTIMIZED.py order_execution.py

echo "✅ Deployment complete!"
```

Then run:
```bash
chmod +x quick_deploy.sh
./quick_deploy.sh
```

---

## Troubleshooting

### If wget gives 404:
```bash
# Check Ngrok tunnels
curl http://localhost:4040/api/tunnels | python3 -m json.tool

# Use the file_server tunnel URL
wget https://[file_server_url]/ULTIMATE_IMPROVEMENTS_PACKAGE.tar.gz
```

### If .bashrc permission denied:
```bash
# Use sudo
sudo nano /home/halvolyra/.bashrc
# Add the export lines manually
```

### If pip gives externally-managed-environment:
```bash
# Always use virtual environment
python3 -m venv ~/lyra_venv
source ~/lyra_venv/bin/activate
pip install package_name
```

---

## Verification

After deployment, verify:

```bash
# Check files exist
ls -la ~/ultimate_lyra_systems/integration_hub_production.py

# Test import
~/lyra_venv/bin/python -c "import aiohttp; print('✅ aiohttp installed')"

# Check env vars
echo $OPENROUTER_API_KEY
```

---

**All issues fixed!** ✅

