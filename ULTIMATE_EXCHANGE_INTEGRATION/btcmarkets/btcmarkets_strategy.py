#!/usr/bin/env python3
"""
BTC Markets Trading Strategies
Implements production-ready trading strategies for BTC Markets
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json

class BTCMarketsTradingStrategy:
    def __init__(self, adapter):
        self.adapter = adapter
        self.exchange_id = "btcmarkets"
        self.exchange_name = "BTC Markets"
        self.region = "AU"
        self.setup_logging()
        
        # Strategy parameters
        self.min_profit_threshold = 0.001  # 0.1% minimum profit
        self.max_position_size = 0.1  # 10% of balance max
        self.stop_loss_percentage = 0.02  # 2% stop loss
        
        # Australian specific
        if self.region == "AU":
            self.gst_rate = 0.1  # 10% GST
            self.min_profit_threshold = 0.002  # Higher threshold for GST
        
    def setup_logging(self):
        """Setup strategy logging"""
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(f"btcmarkets_strategy")
    
    async def analyze_market_opportunity(self, symbol: str) -> Dict[str, Any]:
        """Analyze market for trading opportunities"""
        try:
            # Get current ticker
            ticker = await self.adapter.get_ticker(self.exchange_id, symbol)
            if not ticker:
                return {'opportunity': False, 'reason': 'No ticker data'}
            
            bid = ticker.get('bid', 0)
            ask = ticker.get('ask', 0)
            
            if bid <= 0 or ask <= 0:
                return {'opportunity': False, 'reason': 'Invalid prices'}
            
            # Calculate spread
            spread = (ask - bid) / ask
            
            # Check if spread meets minimum threshold
            if spread < self.min_profit_threshold:
                return {
                    'opportunity': False,
                    'reason': 'Spread too low',
                    'spread': spread,
                    'threshold': self.min_profit_threshold
                }
            
            # Calculate potential profit (after fees and GST if AU)
            trading_fee = 0.001  # 0.1% typical trading fee
            total_cost = trading_fee * 2  # Buy and sell fees
            
            if self.region == "AU":
                total_cost += self.gst_rate  # Add GST
            
            net_profit = spread - total_cost
            
            if net_profit <= 0:
                return {
                    'opportunity': False,
                    'reason': 'Net profit negative after costs',
                    'net_profit': net_profit
                }
            
            return {
                'opportunity': True,
                'symbol': symbol,
                'bid': bid,
                'ask': ask,
                'spread': spread,
                'net_profit': net_profit,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Error analyzing market: {str(e)}")
            return {'opportunity': False, 'reason': f'Analysis error: {str(e)}'}
    
    async def execute_arbitrage_strategy(self, symbol: str) -> Dict[str, Any]:
        """Execute arbitrage trading strategy"""
        try:
            # Analyze opportunity
            analysis = await self.analyze_market_opportunity(symbol)
            if not analysis.get('opportunity'):
                return analysis
            
            # Get account balance
            balance = await self.adapter.get_balance(self.exchange_id)
            if not balance:
                return {'success': False, 'reason': 'Cannot get balance'}
            
            # Calculate position size
            base_currency = symbol.split('/')[1] if '/' in symbol else 'USD'
            available_balance = balance.get('free', {}).get(base_currency, 0)
            
            if available_balance <= 0:
                return {'success': False, 'reason': 'Insufficient balance'}
            
            position_size = min(
                available_balance * self.max_position_size,
                100  # Maximum $100 per trade for safety
            )
            
            # Calculate order amount
            order_amount = position_size / analysis['ask']
            
            # Execute buy order (simulation for safety)
            if os.getenv('LIVE_TRADING', 'false').lower() == 'true':
                buy_order = await self.adapter.create_order(
                    self.exchange_id, symbol, 'market', 'buy', order_amount
                )
                
                if buy_order:
                    # Execute sell order
                    sell_order = await self.adapter.create_order(
                        self.exchange_id, symbol, 'market', 'sell', order_amount
                    )
                    
                    return {
                        'success': True,
                        'buy_order': buy_order,
                        'sell_order': sell_order,
                        'profit': analysis['net_profit'] * position_size
                    }
            else:
                # Simulation mode
                self.logger.info(f"SIMULATION: Would trade {order_amount} {symbol}")
                return {
                    'success': True,
                    'simulation': True,
                    'symbol': symbol,
                    'amount': order_amount,
                    'expected_profit': analysis['net_profit'] * position_size
                }
            
        except Exception as e:
            self.logger.error(f"Error executing strategy: {str(e)}")
            return {'success': False, 'reason': str(e)}
    
    async def run_continuous_strategy(self, symbols: List[str], interval: int = 60):
        """Run continuous trading strategy"""
        self.logger.info(f"Starting continuous strategy for {len(symbols)} symbols")
        
        while True:
            try:
                for symbol in symbols:
                    result = await self.execute_arbitrage_strategy(symbol)
                    if result.get('success'):
                        self.logger.info(f"Strategy executed for {symbol}: {result}")
                    
                    # Wait between symbols to avoid rate limits
                    await asyncio.sleep(5)
                
                # Wait for next cycle
                await asyncio.sleep(interval)
                
            except Exception as e:
                self.logger.error(f"Error in continuous strategy: {str(e)}")
                await asyncio.sleep(30)  # Wait before retrying

# Strategy factory
def create_strategy(adapter):
    return BTCMarketsTradingStrategy(adapter)

if __name__ == "__main__":
    # Example usage
    print(f"{exchange_info['name']} Trading Strategy Ready")
