
class EnhancedErrorHandler:
    """Enhanced error handling with automatic recovery"""
    
    def __init__(self):
        self.error_counts = {}
        self.max_retries = 3
        self.backoff_multiplier = 2
        
    def handle_api_error(self, api_name: str, error: Exception, attempt: int = 1):
        """Handle API errors with exponential backoff"""
        if api_name not in self.error_counts:
            self.error_counts[api_name] = 0
            
        self.error_counts[api_name] += 1
        
        if attempt <= self.max_retries:
            wait_time = self.backoff_multiplier ** attempt
            time.sleep(wait_time)
            return True  # Retry
        else:
            # Switch to fallback API or cached data
            return self.use_fallback(api_name)
            
    def use_fallback(self, api_name: str):
        """Use fallback mechanisms"""
        fallbacks = {
            'okx': ['binance', 'coinbase', 'cached_data'],
            'binance': ['okx', 'coinbase', 'cached_data'],
            'polygon': ['alpha_vantage', 'yahoo_finance', 'cached_data']
        }
        return fallbacks.get(api_name, ['cached_data'])
        
    def circuit_breaker(self, service_name: str, error_threshold: int = 5):
        """Implement circuit breaker pattern"""
        if self.error_counts.get(service_name, 0) > error_threshold:
            # Open circuit - use fallback for 5 minutes
            return False
        return True
