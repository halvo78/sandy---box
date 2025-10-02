#!/usr/bin/env python3
"""
Ultimate Ngrok Tunnel Manager
Handles all ngrok functionality with safety controls and Manus integration
"""

import os
import json
import asyncio
import logging
import subprocess
from datetime import datetime
from typing import Dict, List, Optional
import aiohttp
import yaml

class UltimateNgrokManager:
    def __init__(self, config_path: str = "ngrok_config.yml"):
        self.config = self._load_config(config_path)
        self.active_tunnels = {}
        self.traffic_log = []
        self.mode = "spot_monitoring"
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def _load_config(self, config_path: str) -> Dict:
        """Load ngrok configuration from YAML file"""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    async def start_all_tunnels(self) -> Dict[str, str]:
        """Start all configured tunnels"""
        tunnel_urls = {}
        
        # Start ngrok with config file
        cmd = f"ngrok start --all --config {os.path.abspath('ngrok_config.yml')}"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for tunnels to establish
        await asyncio.sleep(10)
        
        # Get tunnel URLs via API
        tunnel_urls = await self._get_tunnel_urls()
        
        self.logger.info(f"Started {len(tunnel_urls)} tunnels: {list(tunnel_urls.keys())}")
        return tunnel_urls
    
    async def _get_tunnel_urls(self) -> Dict[str, str]:
        """Get active tunnel URLs from ngrok API"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://localhost:4040/api/tunnels') as resp:
                    data = await resp.json()
                    tunnels = {}
                    for tunnel in data.get('tunnels', []):
                        name = tunnel.get('name', 'unknown')
                        public_url = tunnel.get('public_url', '')
                        tunnels[name] = public_url
                    return tunnels
        except Exception as e:
            self.logger.error(f"Failed to get tunnel URLs: {e}")
            return {}
    
    async def health_check(self) -> Dict[str, bool]:
        """Check health of all tunnels"""
        health_status = {}
        tunnel_urls = await self._get_tunnel_urls()
        
        for name, url in tunnel_urls.items():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"{url}/health", timeout=5) as resp:
                        health_status[name] = resp.status == 200
            except:
                health_status[name] = False
        
        return health_status
    
    async def get_traffic_inspection(self) -> List[Dict]:
        """Get traffic inspection data for compliance"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://localhost:4040/api/requests') as resp:
                    data = await resp.json()
                    return data.get('requests', [])
        except Exception as e:
            self.logger.error(f"Failed to get traffic data: {e}")
            return []
    
    def stop_all_tunnels(self):
        """Emergency stop all tunnels"""
        subprocess.run("pkill -f ngrok", shell=True)
        self.logger.critical("All tunnels stopped - Emergency halt")

# Main execution
if __name__ == "__main__":
    manager = UltimateNgrokManager()
    asyncio.run(manager.start_all_tunnels())
