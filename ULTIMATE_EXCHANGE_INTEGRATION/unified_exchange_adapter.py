#!/usr/bin/env python3
"""
UNIFIED EXCHANGE ADAPTER
Supports all target exchanges with CCXT integration
Production-ready with error handling, rate limiting, and monitoring
"""

import ccxt
import os
import asyncio
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

class UnifiedExchangeAdapter:
    def __init__(self):
        self.exchanges = {}
        self.supported_exchanges = [
            'btcmarkets', 'coinbase', 'binance', 'whitebit', 
            'digitalsurge', 'gate', 'okx', 'kraken', 'swyftx'
        ]
        self.setup_logging()
        
    def setup_logging(self):
        """Setup comprehensive logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('exchange_adapter.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def initialize_exchange(self, exchange_id: str) -> bool:
        """Initialize specific exchange with API credentials"""
        try:
            # Get API credentials from environment
            api_key = os.getenv(f'{exchange_id.upper()}_API_KEY')
            secret = os.getenv(f'{exchange_id.upper()}_SECRET')
            passphrase = os.getenv(f'{exchange_id.upper()}_PASSPHRASE')  # For OKX
            
            if not api_key or not secret:
                self.logger.warning(f"Missing API credentials for {exchange_id}")
                return False
            
            # Exchange-specific configuration
            config = {
                'apiKey': api_key,
                'secret': secret,
                'sandbox': os.getenv('SANDBOX_MODE', 'true').lower() == 'true',
                'enableRateLimit': True,
                'options': {'defaultType': 'spot'}  # Spot trading only
            }
            
            # Add passphrase for OKX
            if exchange_id == 'okx' and passphrase:
                config['password'] = passphrase
            
            # Australian exchange specific settings
            if exchange_id in ['btcmarkets', 'digitalsurge', 'swyftx']:
                config['options']['gst_rate'] = 0.1  # 10% GST
                config['options']['ato_reporting'] = True
            
            # Initialize exchange
            exchange_class = getattr(ccxt, exchange_id)
            exchange = exchange_class(config)
            
            # Load markets
            exchange.load_markets()
            
            self.exchanges[exchange_id] = exchange
            self.logger.info(f"Successfully initialized {exchange_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize {exchange_id}: {str(e)}")
            return False
    
    def initialize_all_exchanges(self) -> Dict[str, bool]:
        """Initialize all supported exchanges"""
        results = {}
        for exchange_id in self.supported_exchanges:
            results[exchange_id] = self.initialize_exchange(exchange_id)
        return results
    
    async def get_ticker(self, exchange_id: str, symbol: str) -> Optional[Dict]:
        """Get ticker data for symbol"""
        try:
            if exchange_id not in self.exchanges:
                return None
            
            ticker = await self.exchanges[exchange_id].fetch_ticker(symbol)
            return ticker
            
        except Exception as e:
            self.logger.error(f"Error fetching ticker for {exchange_id} {symbol}: {str(e)}")
            return None
    
    async def get_balance(self, exchange_id: str) -> Optional[Dict]:
        """Get account balance"""
        try:
            if exchange_id not in self.exchanges:
                return None
            
            balance = await self.exchanges[exchange_id].fetch_balance()
            return balance
            
        except Exception as e:
            self.logger.error(f"Error fetching balance for {exchange_id}: {str(e)}")
            return None
    
    async def create_order(self, exchange_id: str, symbol: str, order_type: str, 
                          side: str, amount: float, price: Optional[float] = None) -> Optional[Dict]:
        """Create trading order"""
        try:
            if exchange_id not in self.exchanges:
                return None
            
            # Australian exchanges - add GST calculation
            if exchange_id in ['btcmarkets', 'digitalsurge', 'swyftx']:
                # Log for ATO reporting
                self.logger.info(f"ATO_LOG: {exchange_id} {side} {amount} {symbol} at {price}")
            
            order = await self.exchanges[exchange_id].create_order(
                symbol, order_type, side, amount, price
            )
            
            return order
            
        except Exception as e:
            self.logger.error(f"Error creating order for {exchange_id}: {str(e)}")
            return None
    
    def get_exchange_status(self) -> Dict[str, Any]:
        """Get status of all exchanges"""
        status = {}
        for exchange_id in self.supported_exchanges:
            status[exchange_id] = {
                'initialized': exchange_id in self.exchanges,
                'connected': False,
                'last_check': datetime.now().isoformat()
            }
            
            if exchange_id in self.exchanges:
                try:
                    # Test connection
                    self.exchanges[exchange_id].fetch_status()
                    status[exchange_id]['connected'] = True
                except:
                    status[exchange_id]['connected'] = False
        
        return status

# Global adapter instance
adapter = UnifiedExchangeAdapter()

if __name__ == "__main__":
    # Initialize all exchanges
    results = adapter.initialize_all_exchanges()
    print("Exchange Initialization Results:")
    for exchange_id, success in results.items():
        status = "✅" if success else "❌"
        print(f"  {status} {exchange_id}")
