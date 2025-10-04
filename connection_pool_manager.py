
import asyncio
import aiohttp
from typing import Dict, Optional

class ConnectionPoolManager:
    """Manages connection pools for different APIs"""
    
    def __init__(self):
        self.pools = {}
        self.session_configs = {
            'okx': {
                'connector': aiohttp.TCPConnector(limit=100, limit_per_host=20),
                'timeout': aiohttp.ClientTimeout(total=30, connect=10)
            },
            'binance': {
                'connector': aiohttp.TCPConnector(limit=50, limit_per_host=10),
                'timeout': aiohttp.ClientTimeout(total=20, connect=5)
            },
            'polygon': {
                'connector': aiohttp.TCPConnector(limit=30, limit_per_host=5),
                'timeout': aiohttp.ClientTimeout(total=15, connect=5)
            }
        }
        
    async def get_session(self, api_name: str) -> aiohttp.ClientSession:
        """Get or create a session for the specified API"""
        if api_name not in self.pools:
            config = self.session_configs.get(api_name, {
                'connector': aiohttp.TCPConnector(limit=20, limit_per_host=5),
                'timeout': aiohttp.ClientTimeout(total=10, connect=3)
            })
            
            self.pools[api_name] = aiohttp.ClientSession(
                connector=config['connector'],
                timeout=config['timeout']
            )
            
        return self.pools[api_name]
        
    async def close_all(self):
        """Close all connection pools"""
        for session in self.pools.values():
            await session.close()
        self.pools.clear()
