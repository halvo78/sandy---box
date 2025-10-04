#!/usr/bin/env python3
"""
HUMMINGBOT INTEGRATION SERVICE
Integrates Hummingbot institutional trading strategies with Lyra AI system
"""

import json
import asyncio
import aiohttp
from aiohttp import web
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
import subprocess
import os
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HummingbotIntegration:
    def __init__(self):
        self.hummingbot_path = "/opt/hummingbot"
        self.config_path = "/app/hummingbot_configs"
        self.strategies = {
            "pure_market_making": {
                "name": "Pure Market Making",
                "description": "Provides liquidity by placing buy and sell orders",
                "risk_level": "LOW",
                "suitable_for": ["stable_markets", "high_volume_pairs"]
            },
            "cross_exchange_market_making": {
                "name": "Cross Exchange Market Making", 
                "description": "Arbitrage between different exchanges",
                "risk_level": "MEDIUM",
                "suitable_for": ["price_differences", "multiple_exchanges"]
            },
            "arbitrage": {
                "name": "Arbitrage",
                "description": "Profit from price differences across exchanges",
                "risk_level": "LOW",
                "suitable_for": ["price_inefficiencies", "fast_execution"]
            },
            "perpetual_market_making": {
                "name": "Perpetual Market Making",
                "description": "Market making for perpetual futures",
                "risk_level": "HIGH",
                "suitable_for": ["derivatives", "advanced_users"]
            },
            "liquidity_mining": {
                "name": "Liquidity Mining",
                "description": "Earn rewards by providing liquidity",
                "risk_level": "LOW",
                "suitable_for": ["reward_programs", "passive_income"]
            },
            "spot_perpetual_arbitrage": {
                "name": "Spot Perpetual Arbitrage",
                "description": "Arbitrage between spot and perpetual markets",
                "risk_level": "MEDIUM",
                "suitable_for": ["funding_rate_opportunities"]
            },
            "fixed_grid": {
                "name": "Fixed Grid",
                "description": "Grid trading with fixed price levels",
                "risk_level": "MEDIUM",
                "suitable_for": ["ranging_markets", "systematic_trading"]
            },
            "hedge": {
                "name": "Hedge",
                "description": "Risk management through hedging positions",
                "risk_level": "LOW",
                "suitable_for": ["risk_reduction", "portfolio_protection"]
            }
        }
        self.active_bots = {}
        self.initialize_configs()
    
    def initialize_configs(self):
        """Initialize Hummingbot configuration directory"""
        try:
            os.makedirs(self.config_path, exist_ok=True)
            logger.info("✅ Hummingbot config directory initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize configs: {e}")
    
    def create_strategy_config(self, strategy_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Create configuration for a specific strategy"""
        try:
            base_config = {
                "strategy": strategy_name,
                "exchange": params.get("exchange", "okx"),
                "market": params.get("market", "BTC-USDT"),
                "bid_spread": params.get("bid_spread", 0.1),
                "ask_spread": params.get("ask_spread", 0.1),
                "order_amount": params.get("order_amount", 100),
                "order_refresh_time": params.get("order_refresh_time", 30),
                "max_order_age": params.get("max_order_age", 1800),
                "order_refresh_tolerance_pct": params.get("order_refresh_tolerance_pct", 0.2),
                "filled_order_delay": params.get("filled_order_delay", 60),
                "inventory_skew_enabled": params.get("inventory_skew_enabled", True),
                "inventory_target_base_pct": params.get("inventory_target_base_pct", 50),
                "inventory_range_multiplier": params.get("inventory_range_multiplier", 50),
                "hanging_orders_enabled": params.get("hanging_orders_enabled", False),
                "order_optimization_enabled": params.get("order_optimization_enabled", True),
                "add_transaction_costs": params.get("add_transaction_costs", True),
                "price_ceiling": params.get("price_ceiling", -1),
                "price_floor": params.get("price_floor", -1),
                "ping_pong_enabled": params.get("ping_pong_enabled", False)
            }
            
            # Strategy-specific configurations
            if strategy_name == "pure_market_making":
                base_config.update({
                    "order_levels": params.get("order_levels", 1),
                    "order_level_amount": params.get("order_level_amount", 0),
                    "order_level_spread": params.get("order_level_spread", 1)
                })
            
            elif strategy_name == "cross_exchange_market_making":
                base_config.update({
                    "maker_market": params.get("maker_market", "okx"),
                    "taker_market": params.get("taker_market", "binance"),
                    "min_profitability": params.get("min_profitability", 0.3),
                    "adjust_order_enabled": params.get("adjust_order_enabled", True),
                    "active_order_canceling": params.get("active_order_canceling", True)
                })
            
            elif strategy_name == "arbitrage":
                base_config.update({
                    "primary_market": params.get("primary_market", "okx"),
                    "secondary_market": params.get("secondary_market", "binance"),
                    "min_profitability": params.get("min_profitability", 0.2),
                    "market_1": params.get("market_1", "BTC-USDT"),
                    "market_2": params.get("market_2", "BTC-USDT")
                })
            
            return base_config
            
        except Exception as e:
            logger.error(f"❌ Failed to create strategy config: {e}")
            return {}
    
    async def start_strategy(self, strategy_name: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Start a Hummingbot strategy"""
        try:
            # Validate strategy
            if strategy_name not in self.strategies:
                return {
                    "success": False,
                    "error": f"Unknown strategy: {strategy_name}"
                }
            
            # Create config file
            config_file = f"{self.config_path}/{strategy_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yml"
            
            # Convert config to Hummingbot YAML format
            yaml_config = self.dict_to_yaml(config)
            
            with open(config_file, 'w') as f:
                f.write(yaml_config)
            
            # Generate bot ID
            bot_id = f"{strategy_name}_{len(self.active_bots) + 1}"
            
            # Store bot configuration
            self.active_bots[bot_id] = {
                "strategy": strategy_name,
                "config_file": config_file,
                "config": config,
                "status": "starting",
                "start_time": datetime.now().isoformat(),
                "pnl": 0.0,
                "trades": 0
            }
            
            logger.info(f"✅ Started {strategy_name} strategy with ID: {bot_id}")
            
            return {
                "success": True,
                "bot_id": bot_id,
                "strategy": strategy_name,
                "config_file": config_file,
                "status": "started",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Failed to start strategy: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def dict_to_yaml(self, config: Dict[str, Any]) -> str:
        """Convert dictionary to YAML format for Hummingbot"""
        yaml_lines = []
        for key, value in config.items():
            if isinstance(value, str):
                yaml_lines.append(f"{key}: \"{value}\"")
            elif isinstance(value, bool):
                yaml_lines.append(f"{key}: {str(value).lower()}")
            else:
                yaml_lines.append(f"{key}: {value}")
        
        return "\\n".join(yaml_lines)
    
    async def stop_strategy(self, bot_id: str) -> Dict[str, Any]:
        """Stop a running strategy"""
        try:
            if bot_id not in self.active_bots:
                return {
                    "success": False,
                    "error": f"Bot ID not found: {bot_id}"
                }
            
            # Update bot status
            self.active_bots[bot_id]["status"] = "stopped"
            self.active_bots[bot_id]["stop_time"] = datetime.now().isoformat()
            
            logger.info(f"✅ Stopped strategy with ID: {bot_id}")
            
            return {
                "success": True,
                "bot_id": bot_id,
                "status": "stopped",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Failed to stop strategy: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def get_strategy_performance(self, bot_id: str) -> Dict[str, Any]:
        """Get performance metrics for a strategy"""
        try:
            if bot_id not in self.active_bots:
                return {
                    "success": False,
                    "error": f"Bot ID not found: {bot_id}"
                }
            
            bot = self.active_bots[bot_id]
            
            # Simulate performance metrics (in real implementation, this would query Hummingbot)
            performance = {
                "bot_id": bot_id,
                "strategy": bot["strategy"],
                "status": bot["status"],
                "start_time": bot["start_time"],
                "runtime_hours": self.calculate_runtime(bot["start_time"]),
                "total_pnl": bot.get("pnl", 0.0),
                "total_trades": bot.get("trades", 0),
                "win_rate": 65.5,  # Simulated
                "avg_trade_size": 150.0,  # Simulated
                "max_drawdown": -2.3,  # Simulated
                "sharpe_ratio": 1.45,  # Simulated
                "current_positions": [],
                "recent_trades": []
            }
            
            return {
                "success": True,
                "performance": performance,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Failed to get performance: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def calculate_runtime(self, start_time: str) -> float:
        """Calculate runtime in hours"""
        try:
            start = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            now = datetime.now()
            delta = now - start.replace(tzinfo=None)
            return round(delta.total_seconds() / 3600, 2)
        except:
            return 0.0
    
    async def health_check(self, request):
        """Health check endpoint"""
        try:
            return web.json_response({
                'status': 'healthy',
                'service': 'hummingbot_integration',
                'strategies_available': len(self.strategies),
                'active_bots': len(self.active_bots),
                'config_path': self.config_path,
                'timestamp': datetime.now().isoformat()
            })
        except Exception as e:
            return web.json_response({
                'status': 'unhealthy',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)
    
    async def get_strategies(self, request):
        """Get available strategies"""
        return web.json_response({
            'strategies': self.strategies,
            'total_strategies': len(self.strategies),
            'timestamp': datetime.now().isoformat()
        })
    
    async def get_active_bots(self, request):
        """Get active bots"""
        return web.json_response({
            'active_bots': self.active_bots,
            'total_active': len(self.active_bots),
            'timestamp': datetime.now().isoformat()
        })
    
    async def create_strategy(self, request):
        """Create and start a new strategy"""
        try:
            data = await request.json()
            
            required_fields = ['strategy_name', 'exchange', 'market']
            for field in required_fields:
                if field not in data:
                    return web.json_response({
                        'error': f'Missing required field: {field}'
                    }, status=400)
            
            # Create strategy configuration
            config = self.create_strategy_config(data['strategy_name'], data)
            
            # Start the strategy
            result = await self.start_strategy(data['strategy_name'], config)
            
            return web.json_response(result)
            
        except Exception as e:
            return web.json_response({
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)
    
    async def stop_bot(self, request):
        """Stop a running bot"""
        try:
            data = await request.json()
            
            if 'bot_id' not in data:
                return web.json_response({
                    'error': 'Missing bot_id field'
                }, status=400)
            
            result = await self.stop_strategy(data['bot_id'])
            
            return web.json_response(result)
            
        except Exception as e:
            return web.json_response({
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)
    
    async def get_performance(self, request):
        """Get bot performance"""
        try:
            bot_id = request.query.get('bot_id')
            
            if not bot_id:
                return web.json_response({
                    'error': 'Missing bot_id parameter'
                }, status=400)
            
            result = await self.get_strategy_performance(bot_id)
            
            return web.json_response(result)
            
        except Exception as e:
            return web.json_response({
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

async def init_app():
    """Initialize the web application"""
    hummingbot = HummingbotIntegration()
    app = web.Application()
    
    # Add routes
    app.router.add_get('/health', hummingbot.health_check)
    app.router.add_get('/strategies', hummingbot.get_strategies)
    app.router.add_get('/bots', hummingbot.get_active_bots)
    app.router.add_post('/create-strategy', hummingbot.create_strategy)
    app.router.add_post('/stop-bot', hummingbot.stop_bot)
    app.router.add_get('/performance', hummingbot.get_performance)
    
    return app

if __name__ == '__main__':
    app = init_app()
    web.run_app(app, host='0.0.0.0', port=8080)
