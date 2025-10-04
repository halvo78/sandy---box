#!/usr/bin/env python3
"""
Setup Ngrok with Existing Configuration for Ultimate Lyra Trading System
Uses the previously configured ngrok setup found in the sandbox
"""

import os
import sys
import subprocess
import time
import json
import requests
from datetime import datetime

class NgrokSetup:
    def __init__(self):
        self.ngrok_config_path = "/home/ubuntu/ngrok_container/ngrok_config.yml"
        self.production_system_port = 5001
        self.dashboard_port = 5000
        
    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
        
    def check_existing_config(self):
        """Check for existing ngrok configuration"""
        self.log("🔍 Checking for existing ngrok configuration...")
        
        if os.path.exists(self.ngrok_config_path):
            self.log(f"✅ Found existing ngrok config: {self.ngrok_config_path}")
            return True
        else:
            self.log("❌ No existing ngrok config found")
            return False
            
    def setup_ngrok_config(self):
        """Setup ngrok configuration for the production system"""
        self.log("⚙️ Setting up ngrok configuration...")
        
        # Create updated config for our production system
        config_content = f'''version: "3"
authtoken: ${{NGROK_AUTHTOKEN}}
region: ap
log_level: info
log_format: json
log: /tmp/ngrok.log
tunnels:
  production_system:
    proto: http
    addr: localhost:{self.production_system_port}
    inspect: true
    metadata: '{{"service": "lyra_production", "mode": "live_trading"}}'
  
  dashboard:
    proto: http
    addr: localhost:{self.dashboard_port}
    inspect: true
    metadata: '{{"service": "lyra_dashboard", "mode": "monitoring"}}'
    
  api:
    proto: http
    addr: localhost:{self.production_system_port}
    subdomain: lyra-api
    inspect: true
    metadata: '{{"service": "lyra_api", "mode": "public_api"}}'
web_addr: localhost:4040
'''
        
        # Ensure config directory exists
        config_dir = os.path.expanduser("~/.config/ngrok")
        os.makedirs(config_dir, exist_ok=True)
        
        config_file = os.path.join(config_dir, "ngrok.yml")
        with open(config_file, 'w') as f:
            f.write(config_content)
            
        self.log(f"✅ Ngrok config created: {config_file}")
        return config_file
        
    def check_ngrok_auth(self):
        """Check if ngrok is authenticated"""
        self.log("🔐 Checking ngrok authentication...")
        
        try:
            result = subprocess.run(['ngrok', 'config', 'check'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.log("✅ Ngrok is properly authenticated")
                return True
            else:
                self.log("⚠️ Ngrok authentication issue detected")
                return False
        except Exception as e:
            self.log(f"❌ Error checking ngrok auth: {str(e)}")
            return False
            
    def start_ngrok_tunnel(self, tunnel_name="production_system"):
        """Start ngrok tunnel for the production system"""
        self.log(f"🌐 Starting ngrok tunnel: {tunnel_name}")
        
        try:
            # Start ngrok tunnel
            cmd = ['ngrok', 'http', str(self.production_system_port), '--log=stdout']
            self.log(f"Executing: {' '.join(cmd)}")
            
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE, text=True)
            
            # Give ngrok time to start
            time.sleep(5)
            
            # Check if process is still running
            if process.poll() is None:
                self.log("✅ Ngrok tunnel started successfully")
                return process
            else:
                stdout, stderr = process.communicate()
                self.log(f"❌ Ngrok failed to start: {stderr}")
                return None
                
        except Exception as e:
            self.log(f"❌ Error starting ngrok: {str(e)}")
            return None
            
    def get_tunnel_info(self):
        """Get tunnel information from ngrok API"""
        self.log("📡 Getting tunnel information...")
        
        try:
            response = requests.get("http://localhost:4040/api/tunnels", timeout=5)
            if response.status_code == 200:
                tunnels = response.json()
                self.log("✅ Retrieved tunnel information")
                return tunnels
            else:
                self.log(f"⚠️ Failed to get tunnel info: {response.status_code}")
                return None
        except Exception as e:
            self.log(f"❌ Error getting tunnel info: {str(e)}")
            return None
            
    def display_tunnel_urls(self, tunnels):
        """Display tunnel URLs"""
        if not tunnels or 'tunnels' not in tunnels:
            self.log("❌ No tunnel information available")
            return
            
        self.log("🌐 TUNNEL URLS ACTIVE:")
        self.log("=" * 60)
        
        for tunnel in tunnels['tunnels']:
            name = tunnel.get('name', 'unknown')
            public_url = tunnel.get('public_url', 'N/A')
            config = tunnel.get('config', {})
            addr = config.get('addr', 'N/A')
            
            self.log(f"🔗 {name.upper()}")
            self.log(f"   Public URL: {public_url}")
            self.log(f"   Local Address: {addr}")
            self.log("")
            
        self.log("=" * 60)
        
    def create_access_summary(self, tunnels):
        """Create access summary file"""
        summary = {
            "timestamp": datetime.now().isoformat(),
            "system_status": "OPERATIONAL",
            "production_system_port": self.production_system_port,
            "dashboard_port": self.dashboard_port,
            "tunnels": []
        }
        
        if tunnels and 'tunnels' in tunnels:
            for tunnel in tunnels['tunnels']:
                tunnel_info = {
                    "name": tunnel.get('name', 'unknown'),
                    "public_url": tunnel.get('public_url', 'N/A'),
                    "local_addr": tunnel.get('config', {}).get('addr', 'N/A'),
                    "proto": tunnel.get('proto', 'http')
                }
                summary['tunnels'].append(tunnel_info)
                
        summary_file = "/home/ubuntu/ngrok_access_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
            
        self.log(f"📄 Access summary saved: {summary_file}")
        return summary_file
        
    def run_setup(self):
        """Run the complete ngrok setup"""
        self.log("🚀 STARTING NGROK SETUP FOR ULTIMATE LYRA TRADING SYSTEM")
        self.log("=" * 70)
        
        # Check existing config
        has_config = self.check_existing_config()
        
        # Setup ngrok config
        config_file = self.setup_ngrok_config()
        
        # Check authentication
        is_authenticated = self.check_ngrok_auth()
        
        if not is_authenticated:
            self.log("⚠️ NGROK AUTHENTICATION REQUIRED")
            self.log("Please run: ngrok config add-authtoken YOUR_TOKEN")
            self.log("Get your token from: https://dashboard.ngrok.com/get-started/your-authtoken")
            return False
            
        # Start tunnel
        self.log("🌐 Starting ngrok tunnel...")
        process = self.start_ngrok_tunnel()
        
        if process:
            # Get tunnel info
            time.sleep(3)  # Wait for tunnel to be ready
            tunnels = self.get_tunnel_info()
            
            if tunnels:
                self.display_tunnel_urls(tunnels)
                summary_file = self.create_access_summary(tunnels)
                
                self.log("🎉 NGROK SETUP COMPLETE!")
                self.log("Your Ultimate Lyra Trading System is now publicly accessible!")
                return True
            else:
                self.log("⚠️ Tunnel started but couldn't retrieve URLs")
                return False
        else:
            self.log("❌ Failed to start ngrok tunnel")
            return False

def main():
    """Main execution function"""
    setup = NgrokSetup()
    success = setup.run_setup()
    
    if success:
        print("\n🌟 SUCCESS! Your system is now publicly accessible via ngrok!")
        print("Check the URLs above to access your trading system remotely.")
    else:
        print("\n❌ Setup incomplete. Please check the logs above for issues.")
        
    return success

if __name__ == "__main__":
    main()
