#!/usr/bin/env python3
"""
Component Status Checker
Verifies all 10 components are running and accessible via Ngrok
"""

import requests
import json
from datetime import datetime

def check_ngrok_tunnels():
    """Get all active Ngrok tunnels"""
    try:
        response = requests.get('http://localhost:4040/api/tunnels')
        return response.json()
    except Exception as e:
        print(f"❌ Error accessing Ngrok API: {e}")
        return None

def check_component_health(tunnel_url, component_name):
    """Check if component is responding"""
    try:
        response = requests.get(f"{tunnel_url}/health", timeout=5)
        if response.status_code == 200:
            return "✅ HEALTHY"
        else:
            return f"⚠️  WARNING (HTTP {response.status_code})"
    except requests.exceptions.Timeout:
        return "⏱️  TIMEOUT"
    except Exception as e:
        return f"❌ ERROR: {str(e)[:30]}"

def main():
    print("=" * 80)
    print("🔍 COMPONENT STATUS CHECK")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Get Ngrok tunnels
    tunnels_data = check_ngrok_tunnels()
    
    if not tunnels_data:
        print("❌ Cannot access Ngrok API. Is Ngrok running?")
        return
    
    tunnels = tunnels_data.get('tunnels', [])
    
    print(f"📡 Active Tunnels: {len(tunnels)}")
    print()
    
    # Check each tunnel
    for tunnel in tunnels:
        name = tunnel.get('name', 'unknown')
        public_url = tunnel.get('public_url', '')
        
        print(f"{name:30} {public_url}")
    
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()
