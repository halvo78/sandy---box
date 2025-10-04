
import requests
import time
import json
import threading
from cachetools import TTLCache, cached
from typing import Dict, Any, Optional

class PolygonAPIOptimizer:
    """
    Comprehensive Polygon API optimization with caching, connection pooling, and performance monitoring
    """
    
    def __init__(self):
        self.api_key = "YOUR_POLYGON_API_KEY"  # Replace with actual key
        self.base_url = "https://api.polygon.io"
        self.cache = TTLCache(maxsize=1000, ttl=60)  # 1-minute cache
        self.session = requests.Session()
        self.performance_metrics = {
            "total_requests": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "average_response_time": 0.0,
            "response_times": []
        }
        self.lock = threading.Lock()
        
        # Configure session for optimal performance
        self.session.headers.update({
            'User-Agent': 'Lyra-Trading-System/1.0',
            'Accept': 'application/json',
            'Connection': 'keep-alive'
        })
        
        # Connection pooling
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,
            pool_maxsize=20,
            max_retries=3
        )
        self.session.mount('https://', adapter)
        self.session.mount('http://', adapter)
        
    def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """Make optimized API request with caching and performance monitoring"""
        
        # Create cache key
        cache_key = f"{endpoint}_{json.dumps(params, sort_keys=True) if params else ''}"
        
        with self.lock:
            self.performance_metrics["total_requests"] += 1
            
            # Check cache first
            if cache_key in self.cache:
                self.performance_metrics["cache_hits"] += 1
                return self.cache[cache_key]
                
            self.performance_metrics["cache_misses"] += 1
            
        # Make API request
        start_time = time.time()
        
        try:
            url = f"{self.base_url}{endpoint}"
            if params is None:
                params = {}
            params['apikey'] = self.api_key
            
            response = self.session.get(url, params=params, timeout=5)
            
            end_time = time.time()
            response_time = end_time - start_time
            
            with self.lock:
                self.performance_metrics["response_times"].append(response_time)
                # Keep only last 100 response times
                if len(self.performance_metrics["response_times"]) > 100:
                    self.performance_metrics["response_times"] = self.performance_metrics["response_times"][-100:]
                    
                self.performance_metrics["average_response_time"] = sum(self.performance_metrics["response_times"]) / len(self.performance_metrics["response_times"])
            
            if response.status_code == 200:
                data = response.json()
                # Cache successful response
                self.cache[cache_key] = data
                return data
            else:
                return None
                
        except Exception as e:
            # Return cached data if available, otherwise None
            return self.cache.get(cache_key)
            
    def get_ticker_data(self, symbol: str) -> Optional[Dict[str, Any]]:
        """Get ticker data with optimization"""
        return self._make_request(f"/v2/aggs/ticker/{symbol}/prev")
        
    def get_market_status(self) -> Optional[Dict[str, Any]]:
        """Get market status with optimization"""
        return self._make_request("/v1/marketstatus/now")
        
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get API performance metrics"""
        with self.lock:
            cache_hit_rate = (self.performance_metrics["cache_hits"] / self.performance_metrics["total_requests"]) * 100 if self.performance_metrics["total_requests"] > 0 else 0
            
            return {
                "total_requests": self.performance_metrics["total_requests"],
                "cache_hits": self.performance_metrics["cache_hits"],
                "cache_misses": self.performance_metrics["cache_misses"],
                "cache_hit_rate": cache_hit_rate,
                "average_response_time": self.performance_metrics["average_response_time"],
                "cache_size": len(self.cache),
                "session_active": True
            }
            
    def clear_cache(self):
        """Clear the API cache"""
        with self.lock:
            self.cache.clear()

# Global instance
polygon_optimizer = PolygonAPIOptimizer()
