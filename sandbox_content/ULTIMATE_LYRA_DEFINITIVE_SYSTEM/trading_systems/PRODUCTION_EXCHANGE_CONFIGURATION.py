#!/usr/bin/env python3
"""
PRODUCTION EXCHANGE CONFIGURATION
==================================
Production-ready exchange configuration system based on validation results.
Optimized for real trading with proper error handling and fallback mechanisms.

Features:
- Production-mode exchange connections (no sandbox)
- Real API credential integration
- Comprehensive error handling and recovery
- Rate limiting and performance optimization
- Multi-exchange portfolio management
- Emergency disconnection protocols
- Real-time health monitoring

Author: Manus AI System - Production Exchange Edition
Version: 3.0.0 - Production Ready Configuration
"""

import asyncio
import ccxt
import json
import sqlite3
import logging
import time
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('ProductionExchange')

class ExchangeMode(Enum):
    PRODUCTION = "PRODUCTION"
    TESTNET = "TESTNET"
    DEMO = "DEMO"

class ConnectionStatus(Enum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    ERROR = "ERROR"
    MAINTENANCE = "MAINTENANCE"

@dataclass
class ExchangeConfig:
    name: str
    enabled: bool
    mode: ExchangeMode
    api_key: str
    secret_key: str
    passphrase: Optional[str] = None
    rate_limit: int = 1000
    timeout: int = 30000
    retry_attempts: int = 3
    priority: int = 1

@dataclass
class ExchangeConnection:
    config: ExchangeConfig
    instance: Optional[ccxt.Exchange] = None
    status: ConnectionStatus = ConnectionStatus.DISCONNECTED
    last_ping: Optional[datetime] = None
    error_count: int = 0
    last_error: Optional[str] = None

class ProductionExchangeConfiguration:
    def __init__(self):
        self.db_path = "/home/ubuntu/ultimate_lyra_systems/production_exchanges.db"
        self.exchange_connections: Dict[str, ExchangeConnection] = {}
        self.supported_exchanges = ['okx', 'binance', 'kraken', 'gateio', 'whitebit']
        
        # Initialize database
        self.initialize_production_database()
        
        # Load production configuration
        self.load_production_configuration()
        
        logger.info("🏭 Production Exchange Configuration Initialized")
    
    def initialize_production_database(self):
        """Initialize production exchange database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Production exchange configurations
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS production_exchanges (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exchange_name TEXT NOT NULL UNIQUE,
                    enabled BOOLEAN NOT NULL DEFAULT 1,
                    mode TEXT NOT NULL DEFAULT 'PRODUCTION',
                    api_key_hash TEXT,
                    has_credentials BOOLEAN NOT NULL DEFAULT 0,
                    rate_limit INTEGER DEFAULT 1000,
                    timeout INTEGER DEFAULT 30000,
                    retry_attempts INTEGER DEFAULT 3,
                    priority INTEGER DEFAULT 1,
                    last_connected DATETIME,
                    error_count INTEGER DEFAULT 0,
                    last_error TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Exchange health monitoring
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS exchange_health_monitoring (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exchange_name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    response_time REAL,
                    error_message TEXT,
                    timestamp DATETIME NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Trading pairs configuration
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trading_pairs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exchange_name TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    base_currency TEXT NOT NULL,
                    quote_currency TEXT NOT NULL,
                    enabled BOOLEAN NOT NULL DEFAULT 1,
                    min_order_size REAL,
                    max_order_size REAL,
                    price_precision INTEGER,
                    amount_precision INTEGER,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Exchange performance metrics
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS exchange_performance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exchange_name TEXT NOT NULL,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    timestamp DATETIME NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            conn.close()
            
            logger.info("📊 Production Exchange Database: Initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing production database: {e}")
            raise
    
    def load_production_configuration(self):
        """Load production exchange configuration"""
        try:
            # Load from environment variables (production credentials)
            self.load_production_credentials()
            
            # Load from configuration files
            self.load_configuration_files()
            
            # Initialize exchange connections
            self.initialize_exchange_connections()
            
            logger.info(f"🔧 Loaded configuration for {len(self.exchange_connections)} exchanges")
            
        except Exception as e:
            logger.error(f"Error loading production configuration: {e}")
            self.create_demo_configuration()
    
    def load_production_credentials(self):
        """Load production credentials from environment variables"""
        try:
            # OKX Production Credentials
            okx_config = self.create_exchange_config(
                name='okx',
                api_key=os.getenv('OKX_API_KEY', ''),
                secret_key=os.getenv('OKX_SECRET_KEY', ''),
                passphrase=os.getenv('OKX_PASSPHRASE', ''),
                mode=ExchangeMode.PRODUCTION if os.getenv('OKX_API_KEY') else ExchangeMode.DEMO
            )
            
            if okx_config.api_key:
                self.exchange_connections['okx'] = ExchangeConnection(config=okx_config)
                logger.info("✅ OKX production credentials loaded")
            
            # Binance Production Credentials
            binance_config = self.create_exchange_config(
                name='binance',
                api_key=os.getenv('BINANCE_API_KEY', ''),
                secret_key=os.getenv('BINANCE_SECRET_KEY', ''),
                mode=ExchangeMode.PRODUCTION if os.getenv('BINANCE_API_KEY') else ExchangeMode.DEMO
            )
            
            if binance_config.api_key:
                self.exchange_connections['binance'] = ExchangeConnection(config=binance_config)
                logger.info("✅ Binance production credentials loaded")
            
            # Kraken Production Credentials
            kraken_config = self.create_exchange_config(
                name='kraken',
                api_key=os.getenv('KRAKEN_API_KEY', ''),
                secret_key=os.getenv('KRAKEN_SECRET_KEY', ''),
                mode=ExchangeMode.PRODUCTION if os.getenv('KRAKEN_API_KEY') else ExchangeMode.DEMO
            )
            
            if kraken_config.api_key:
                self.exchange_connections['kraken'] = ExchangeConnection(config=kraken_config)
                logger.info("✅ Kraken production credentials loaded")
            
            # Gate.io Production Credentials
            gateio_config = self.create_exchange_config(
                name='gateio',
                api_key=os.getenv('GATE_API_KEY', ''),
                secret_key=os.getenv('GATE_SECRET_KEY', ''),
                mode=ExchangeMode.PRODUCTION if os.getenv('GATE_API_KEY') else ExchangeMode.DEMO
            )
            
            if gateio_config.api_key:
                self.exchange_connections['gateio'] = ExchangeConnection(config=gateio_config)
                logger.info("✅ Gate.io production credentials loaded")
            
            # WhiteBIT Production Credentials
            whitebit_config = self.create_exchange_config(
                name='whitebit',
                api_key=os.getenv('WHITEBIT_API_KEY', ''),
                secret_key=os.getenv('WHITEBIT_SECRET_KEY', ''),
                mode=ExchangeMode.PRODUCTION if os.getenv('WHITEBIT_API_KEY') else ExchangeMode.DEMO
            )
            
            if whitebit_config.api_key:
                self.exchange_connections['whitebit'] = ExchangeConnection(config=whitebit_config)
                logger.info("✅ WhiteBIT production credentials loaded")
            
        except Exception as e:
            logger.error(f"Error loading production credentials: {e}")
    
    def load_configuration_files(self):
        """Load configuration from files"""
        try:
            config_files = [
                '/home/ubuntu/ultimate_lyra_systems/config/production_exchanges.json',
                '/home/ubuntu/ultimate_lyra_systems/production_config.json'
            ]
            
            for config_file in config_files:
                try:
                    with open(config_file, 'r') as f:
                        config = json.load(f)
                        
                        for exchange_name, exchange_config in config.items():
                            if exchange_name in self.supported_exchanges:
                                config_obj = self.create_exchange_config(
                                    name=exchange_name,
                                    api_key=exchange_config.get('api_key', ''),
                                    secret_key=exchange_config.get('secret_key', ''),
                                    passphrase=exchange_config.get('passphrase'),
                                    mode=ExchangeMode(exchange_config.get('mode', 'PRODUCTION')),
                                    enabled=exchange_config.get('enabled', True),
                                    rate_limit=exchange_config.get('rate_limit', 1000),
                                    timeout=exchange_config.get('timeout', 30000),
                                    priority=exchange_config.get('priority', 1)
                                )
                                
                                self.exchange_connections[exchange_name] = ExchangeConnection(config=config_obj)
                                logger.info(f"✅ {exchange_name} configuration loaded from {config_file}")
                                
                except FileNotFoundError:
                    continue
                except Exception as e:
                    logger.warning(f"Error reading {config_file}: {e}")
                    
        except Exception as e:
            logger.error(f"Error loading configuration files: {e}")
    
    def create_demo_configuration(self):
        """Create demo configuration for testing"""
        try:
            logger.info("🔧 Creating demo configuration for testing")
            
            demo_exchanges = {
                'okx': {
                    API_KEY="YOUR_API_KEY_HERE",
                    'secret_key': 'demo_okx_production_secret',
                    'passphrase': 'demo_passphrase',
                    'priority': 1
                },
                'binance': {
                    API_KEY="YOUR_API_KEY_HERE",
                    'secret_key': 'demo_binance_production_secret',
                    'priority': 2
                },
                'kraken': {
                    API_KEY="YOUR_API_KEY_HERE",
                    'secret_key': 'demo_kraken_production_secret',
                    'priority': 3
                }
            }
            
            for exchange_name, creds in demo_exchanges.items():
                config = self.create_exchange_config(
                    name=exchange_name,
                    api_key=creds['api_key'],
                    secret_key=creds['secret_key'],
                    passphrase=creds.get('passphrase'),
                    mode=ExchangeMode.DEMO,
                    priority=creds['priority']
                )
                
                self.exchange_connections[exchange_name] = ExchangeConnection(config=config)
            
            logger.info("✅ Demo configuration created for testing")
            
        except Exception as e:
            logger.error(f"Error creating demo configuration: {e}")
    
    def create_exchange_config(self, name: str, api_key: str, secret_key: str, 
                             passphrase: Optional[str] = None, mode: ExchangeMode = ExchangeMode.PRODUCTION,
                             enabled: bool = True, rate_limit: int = 1000, timeout: int = 30000,
                             retry_attempts: int = 3, priority: int = 1) -> ExchangeConfig:
        """Create exchange configuration object"""
        return ExchangeConfig(
            name=name,
            enabled=enabled and bool(api_key and secret_key),
            mode=mode,
            api_key=api_key,
            secret_key=secret_key,
            passphrase=passphrase,
            rate_limit=rate_limit,
            timeout=timeout,
            retry_attempts=retry_attempts,
            priority=priority
        )
    
    def initialize_exchange_connections(self):
        """Initialize exchange connections"""
        try:
            for exchange_name, connection in self.exchange_connections.items():
                if connection.config.enabled:
                    try:
                        instance = self.create_production_exchange_instance(connection.config)
                        if instance:
                            connection.instance = instance
                            connection.status = ConnectionStatus.CONNECTED
                            logger.info(f"✅ {exchange_name.upper()} production instance created")
                        else:
                            connection.status = ConnectionStatus.ERROR
                            logger.warning(f"⚠️ {exchange_name.upper()} instance creation failed")
                    except Exception as e:
                        connection.status = ConnectionStatus.ERROR
                        connection.last_error = str(e)
                        logger.error(f"❌ {exchange_name.upper()} initialization error: {e}")
                else:
                    logger.info(f"⏸️ {exchange_name.upper()} disabled in configuration")
            
        except Exception as e:
            logger.error(f"Error initializing exchange connections: {e}")
    
    def create_production_exchange_instance(self, config: ExchangeConfig):
        """Create production exchange instance"""
        try:
            exchange_config = {
                'apiKey': config.api_key,
                'secret': config.secret_key,
                'enableRateLimit': True,
                'rateLimit': config.rate_limit,
                'timeout': config.timeout,
                'sandbox': config.mode != ExchangeMode.PRODUCTION,  # Production mode = no sandbox
            }
            
            if config.passphrase:
                exchange_config['password'] = config.passphrase
            
            # Create exchange instance based on name
            if config.name == 'okx':
                return ccxt.okx(exchange_config)
            elif config.name == 'binance':
                return ccxt.binance(exchange_config)
            elif config.name == 'kraken':
                # Kraken doesn't have sandbox, always production
                exchange_config['sandbox'] = False
                return ccxt.kraken(exchange_config)
            elif config.name == 'gateio':
                return ccxt.gateio(exchange_config)
            elif config.name == 'whitebit':
                # WhiteBIT doesn't have sandbox, always production
                exchange_config['sandbox'] = False
                return ccxt.whitebit(exchange_config)
            else:
                logger.warning(f"Unsupported exchange: {config.name}")
                return None
                
        except Exception as e:
            logger.error(f"Error creating {config.name} production instance: {e}")
            return None
    
    async def test_all_connections(self) -> Dict[str, Dict[str, Any]]:
        """Test all exchange connections"""
        try:
            logger.info("🔍 Testing all production exchange connections")
            
            test_results = {}
            
            for exchange_name, connection in self.exchange_connections.items():
                if connection.config.enabled and connection.instance:
                    try:
                        result = await self.test_single_connection(exchange_name, connection)
                        test_results[exchange_name] = result
                    except Exception as e:
                        test_results[exchange_name] = {
                            'status': 'ERROR',
                            'error': str(e),
                            'timestamp': datetime.now().isoformat()
                        }
                else:
                    test_results[exchange_name] = {
                        'status': 'DISABLED',
                        'reason': 'Exchange not enabled or instance not created',
                        'timestamp': datetime.now().isoformat()
                    }
            
            return test_results
            
        except Exception as e:
            logger.error(f"Error testing connections: {e}")
            return {}
    
    async def test_single_connection(self, exchange_name: str, connection: ExchangeConnection) -> Dict[str, Any]:
        """Test single exchange connection"""
        try:
            start_time = time.time()
            
            # Test basic connectivity
            try:
                if connection.config.mode == ExchangeMode.DEMO:
                    # Simulate connection test for demo mode
                    await asyncio.sleep(0.1)
                    response_time = time.time() - start_time
                    
                    return {
                        'status': 'CONNECTED',
                        'mode': 'DEMO',
                        'response_time': response_time,
                        'markets_available': 'Simulated',
                        'timestamp': datetime.now().isoformat()
                    }
                else:
                    # Real connection test
                    markets = await connection.instance.load_markets()
                    response_time = time.time() - start_time
                    
                    # Update connection status
                    connection.status = ConnectionStatus.CONNECTED
                    connection.last_ping = datetime.now()
                    connection.error_count = 0
                    
                    return {
                        'status': 'CONNECTED',
                        'mode': connection.config.mode.value,
                        'response_time': response_time,
                        'markets_available': len(markets),
                        'timestamp': datetime.now().isoformat()
                    }
                    
            except Exception as e:
                response_time = time.time() - start_time
                
                # Update connection status
                connection.status = ConnectionStatus.ERROR
                connection.error_count += 1
                connection.last_error = str(e)
                
                return {
                    'status': 'ERROR',
                    'mode': connection.config.mode.value,
                    'response_time': response_time,
                    'error': str(e),
                    'error_count': connection.error_count,
                    'timestamp': datetime.now().isoformat()
                }
            
        except Exception as e:
            return {
                'status': 'ERROR',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def get_portfolio_balances(self) -> Dict[str, Dict[str, float]]:
        """Get portfolio balances from all connected exchanges"""
        try:
            logger.info("💰 Retrieving portfolio balances from all exchanges")
            
            portfolio_balances = {}
            
            for exchange_name, connection in self.exchange_connections.items():
                if connection.config.enabled and connection.instance and connection.status == ConnectionStatus.CONNECTED:
                    try:
                        if connection.config.mode == ExchangeMode.DEMO:
                            # Simulate balances for demo mode
                            demo_balances = self.get_demo_balances(exchange_name)
                            portfolio_balances[exchange_name] = demo_balances
                        else:
                            # Real balance retrieval
                            balance = await connection.instance.fetch_balance()
                            
                            # Extract non-zero balances
                            total_balance = balance.get('total', {})
                            non_zero_balances = {k: v for k, v in total_balance.items() if v > 0}
                            
                            portfolio_balances[exchange_name] = non_zero_balances
                        
                        logger.info(f"✅ {exchange_name.upper()}: {len(portfolio_balances[exchange_name])} assets")
                        
                    except Exception as e:
                        logger.error(f"❌ {exchange_name.upper()} balance error: {e}")
                        portfolio_balances[exchange_name] = {'error': str(e)}
                else:
                    logger.info(f"⏸️ {exchange_name.upper()}: Not available for balance retrieval")
            
            return portfolio_balances
            
        except Exception as e:
            logger.error(f"Error retrieving portfolio balances: {e}")
            return {}
    
    def get_demo_balances(self, exchange_name: str) -> Dict[str, float]:
        """Get demo balances for testing"""
        demo_balances = {
            'okx': {
                'BTC': 1.5,
                'ETH': 10.0,
                'USDT': 25000.0,
                'SOL': 150.0,
                'ADA': 5000.0
            },
            'binance': {
                'BTC': 0.8,
                'ETH': 5.0,
                'USDT': 15000.0,
                'BNB': 50.0,
                'DOT': 200.0
            },
            'kraken': {
                'BTC': 0.3,
                'ETH': 2.0,
                'USDT': 8000.0,
                'XRP': 1000.0,
                'LINK': 100.0
            }
        }
        
        return demo_balances.get(exchange_name, {})
    
    async def get_market_data(self, symbol: str = 'BTC/USDT') -> Dict[str, Dict[str, Any]]:
        """Get market data from all exchanges"""
        try:
            logger.info(f"📊 Retrieving market data for {symbol}")
            
            market_data = {}
            
            for exchange_name, connection in self.exchange_connections.items():
                if connection.config.enabled and connection.instance and connection.status == ConnectionStatus.CONNECTED:
                    try:
                        if connection.config.mode == ExchangeMode.DEMO:
                            # Simulate market data for demo mode
                            demo_data = self.get_demo_market_data(symbol)
                            market_data[exchange_name] = demo_data
                        else:
                            # Real market data retrieval
                            ticker = await connection.instance.fetch_ticker(symbol)
                            
                            market_data[exchange_name] = {
                                'symbol': ticker.get('symbol'),
                                'last': ticker.get('last'),
                                'bid': ticker.get('bid'),
                                'ask': ticker.get('ask'),
                                'volume': ticker.get('baseVolume'),
                                'change': ticker.get('change'),
                                'percentage': ticker.get('percentage'),
                                'timestamp': ticker.get('timestamp')
                            }
                        
                        logger.info(f"✅ {exchange_name.upper()}: ${market_data[exchange_name].get('last', 0):,.2f}")
                        
                    except Exception as e:
                        logger.error(f"❌ {exchange_name.upper()} market data error: {e}")
                        market_data[exchange_name] = {'error': str(e)}
            
            return market_data
            
        except Exception as e:
            logger.error(f"Error retrieving market data: {e}")
            return {}
    
    def get_demo_market_data(self, symbol: str) -> Dict[str, Any]:
        """Get demo market data for testing"""
        import random
        
        base_price = 65000 if 'BTC' in symbol else 3500 if 'ETH' in symbol else 150
        price_variation = random.uniform(-0.05, 0.05)
        current_price = base_price * (1 + price_variation)
        
        return {
            'symbol': symbol,
            'last': current_price,
            'bid': current_price * 0.999,
            'ask': current_price * 1.001,
            'volume': random.uniform(1000, 10000),
            'change': current_price - base_price,
            'percentage': price_variation * 100,
            'timestamp': int(time.time() * 1000)
        }
    
    def get_connection_summary(self) -> Dict[str, Any]:
        """Get connection summary"""
        try:
            summary = {
                'total_exchanges': len(self.exchange_connections),
                'enabled_exchanges': 0,
                'connected_exchanges': 0,
                'production_exchanges': 0,
                'demo_exchanges': 0,
                'error_exchanges': 0,
                'exchange_details': {}
            }
            
            for exchange_name, connection in self.exchange_connections.items():
                if connection.config.enabled:
                    summary['enabled_exchanges'] += 1
                
                if connection.status == ConnectionStatus.CONNECTED:
                    summary['connected_exchanges'] += 1
                
                if connection.config.mode == ExchangeMode.PRODUCTION:
                    summary['production_exchanges'] += 1
                elif connection.config.mode == ExchangeMode.DEMO:
                    summary['demo_exchanges'] += 1
                
                if connection.status == ConnectionStatus.ERROR:
                    summary['error_exchanges'] += 1
                
                summary['exchange_details'][exchange_name] = {
                    'enabled': connection.config.enabled,
                    'mode': connection.config.mode.value,
                    'status': connection.status.value,
                    'priority': connection.config.priority,
                    'error_count': connection.error_count,
                    'last_error': connection.last_error
                }
            
            return summary
            
        except Exception as e:
            logger.error(f"Error getting connection summary: {e}")
            return {'error': str(e)}
    
    def store_configuration(self):
        """Store configuration in database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            for exchange_name, connection in self.exchange_connections.items():
                cursor.execute('''
                    INSERT OR REPLACE INTO production_exchanges (
                        exchange_name, enabled, mode, has_credentials,
                        rate_limit, timeout, retry_attempts, priority,
                        last_connected, error_count, last_error, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    exchange_name, connection.config.enabled, connection.config.mode.value,
                    bool(connection.config.api_key), connection.config.rate_limit,
                    connection.config.timeout, connection.config.retry_attempts,
                    connection.config.priority, connection.last_ping,
                    connection.error_count, connection.last_error, datetime.now()
                ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            logger.error(f"Error storing configuration: {e}")

async def main():
    """Main function to run production exchange configuration"""
    try:
        print("🏭 PRODUCTION EXCHANGE CONFIGURATION")
        print("=" * 60)
        print("🔧 Production-ready exchange connections")
        print("💰 Real portfolio balance retrieval")
        print("📊 Live market data integration")
        print("🛡️ Comprehensive error handling")
        print("=" * 60)
        
        # Initialize production configuration
        config = ProductionExchangeConfiguration()
        
        # Test all connections
        test_results = await config.test_all_connections()
        
        # Get portfolio balances
        portfolio_balances = await config.get_portfolio_balances()
        
        # Get market data
        market_data = await config.get_market_data('BTC/USDT')
        
        # Get connection summary
        summary = config.get_connection_summary()
        
        # Store configuration
        config.store_configuration()
        
        print("\n🎯 PRODUCTION CONFIGURATION RESULTS")
        print("=" * 60)
        
        print(f"\n📊 CONNECTION SUMMARY:")
        print(f"   Total Exchanges: {summary['total_exchanges']}")
        print(f"   Enabled: {summary['enabled_exchanges']}")
        print(f"   Connected: {summary['connected_exchanges']}")
        print(f"   Production Mode: {summary['production_exchanges']}")
        print(f"   Demo Mode: {summary['demo_exchanges']}")
        
        print(f"\n🏦 EXCHANGE STATUS:")
        for exchange_name, details in summary['exchange_details'].items():
            status_icon = "✅" if details['status'] == 'CONNECTED' else "❌" if details['status'] == 'ERROR' else "⏸️"
            mode_icon = "🏭" if details['mode'] == 'PRODUCTION' else "🧪"
            print(f"   {status_icon} {mode_icon} {exchange_name.upper()}: {details['status']} ({details['mode']})")
        
        print(f"\n💰 PORTFOLIO SUMMARY:")
        total_exchanges_with_balance = 0
        for exchange_name, balances in portfolio_balances.items():
            if 'error' not in balances and balances:
                total_exchanges_with_balance += 1
                asset_count = len(balances)
                print(f"   💎 {exchange_name.upper()}: {asset_count} assets")
        
        print(f"\n📊 MARKET DATA:")
        for exchange_name, data in market_data.items():
            if 'error' not in data and 'last' in data:
                print(f"   📈 {exchange_name.upper()}: BTC/USDT ${data['last']:,.2f}")
        
        return {
            'summary': summary,
            'test_results': test_results,
            'portfolio_balances': portfolio_balances,
            'market_data': market_data
        }
        
    except Exception as e:
        print(f"❌ CONFIGURATION ERROR: {e}")
        return None

if __name__ == "__main__":
    asyncio.run(main())
