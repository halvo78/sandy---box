
import json
import time
from typing import Any, Optional, Dict
import hashlib

class IntelligentCache:
    """Intelligent caching system with TTL and invalidation"""
    
    def __init__(self):
        self.cache = {}
        self.ttl_cache = {}
        self.default_ttl = 300  # 5 minutes
        
    def get_cache_key(self, api_name: str, endpoint: str, params: Dict = None) -> str:
        """Generate cache key"""
        key_data = f"{api_name}:{endpoint}:{json.dumps(params or {}, sort_keys=True)}"
        return hashlib.md5(key_data.encode()).hexdigest()
        
    def get(self, api_name: str, endpoint: str, params: Dict = None) -> Optional[Any]:
        """Get cached data if valid"""
        cache_key = self.get_cache_key(api_name, endpoint, params)
        
        if cache_key in self.cache:
            # Check TTL
            if cache_key in self.ttl_cache:
                if time.time() < self.ttl_cache[cache_key]:
                    return self.cache[cache_key]
                else:
                    # Expired
                    del self.cache[cache_key]
                    del self.ttl_cache[cache_key]
                    
        return None
        
    def set(self, api_name: str, endpoint: str, data: Any, params: Dict = None, ttl: int = None):
        """Cache data with TTL"""
        cache_key = self.get_cache_key(api_name, endpoint, params)
        self.cache[cache_key] = data
        
        ttl = ttl or self.get_ttl_for_endpoint(endpoint)
        self.ttl_cache[cache_key] = time.time() + ttl
        
    def get_ttl_for_endpoint(self, endpoint: str) -> int:
        """Get appropriate TTL based on endpoint type"""
        if 'ticker' in endpoint or 'price' in endpoint:
            return 30  # 30 seconds for price data
        elif 'balance' in endpoint or 'account' in endpoint:
            return 60  # 1 minute for account data
        elif 'market' in endpoint:
            return 120  # 2 minutes for market data
        else:
            return self.default_ttl
            
    def invalidate_pattern(self, pattern: str):
        """Invalidate cache entries matching pattern"""
        keys_to_remove = [key for key in self.cache.keys() if pattern in key]
        for key in keys_to_remove:
            del self.cache[key]
            if key in self.ttl_cache:
                del self.ttl_cache[key]
