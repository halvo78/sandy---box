#!/usr/bin/env python3
"""
Binance Exchange Adapter
Region: Global
Type: spot
Priority: HIGH
Compliance: VPN_may_be_required
"""

import ccxt
import os
import asyncio
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

class BinanceAdapter:
    def __init__(self):
        self.exchange_id = "binance"
        self.exchange_name = "Binance"
        self.region = "Global"
        self.compliance = "VPN_may_be_required"
        self.exchange = None
        self.setup_logging()
        
    def setup_logging(self):
        """Setup exchange-specific logging"""
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(f"binance_adapter")
    
    def initialize(self) -> bool:
        """Initialize Binance exchange"""
        try:
            # Get API credentials
            api_key = os.getenv('BINANCE_API_KEY')
            secret = os.getenv('BINANCE_SECRET')
            
            if not api_key or not secret:
                self.logger.error("Missing API credentials")
                return False
            
            # Exchange configuration
            config = {
                'apiKey': api_key,
                'secret': secret,
                'sandbox': os.getenv('SANDBOX_MODE', 'true').lower() == 'true',
                'enableRateLimit': True,
                'options': {'defaultType': 'spot'}
            }
            
            # Region-specific settings
            if self.region == "AU":
                config['options']['gst_rate'] = 0.1
                config['options']['ato_reporting'] = True
                config['options']['currency_base'] = 'AUD'
            
            # Exchange-specific settings
            
            # Binance specific settings
            config['options']['recvWindow'] = 10000
            config['options']['adjustForTimeDifference'] = True
            
            
            # Initialize exchange
            exchange_class = getattr(ccxt, "binance")
            self.exchange = exchange_class(config)
            self.exchange.load_markets()
            
            self.logger.info(f"Successfully initialized {self.exchange_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize {self.exchange_name}: {str(e)}")
            return False
    
    async def get_markets(self) -> Dict:
        """Get available markets"""
        if not self.exchange:
            return {}
        
        try:
            markets = self.exchange.markets
            # Filter for relevant pairs
            if self.region == "AU":
                # Focus on AUD pairs
                aud_markets = {k: v for k, v in markets.items() if 'AUD' in k}
                return aud_markets
            return markets
        except Exception as e:
            self.logger.error(f"Error fetching markets: {str(e)}")
            return {}
    
    async def health_check(self) -> Dict[str, Any]:
        """Perform health check"""
        if not self.exchange:
            return {'status': 'error', 'message': 'Exchange not initialized'}
        
        try:
            # Test API connection
            status = self.exchange.fetch_status()
            return {
                'status': 'healthy',
                'exchange': self.exchange_name,
                'region': self.region,
                'api_status': status,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'status': 'error',
                'exchange': self.exchange_name,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

# Create adapter instance
adapter = BinanceAdapter()

if __name__ == "__main__":
    success = adapter.initialize()
    if success:
        print(f"✅ {adapter.exchange_name} adapter ready")
    else:
        print(f"❌ {adapter.exchange_name} adapter failed")
