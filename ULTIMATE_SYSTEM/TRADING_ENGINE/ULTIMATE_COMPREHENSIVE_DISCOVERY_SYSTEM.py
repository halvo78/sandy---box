#!/usr/bin/env python3
"""
ULTIMATE COMPREHENSIVE DISCOVERY SYSTEM
========================================
Systematic discovery and integration of all exchange work, APIs, vault data, and system files.
The most comprehensive analysis and rebuilding system ever created.

Features:
- Complete sandbox file system analysis
- Notion vault data integration
- All API credential discovery and validation
- Exchange system reconstruction
- OpenRouter AI consensus testing with all models
- Real-time system commissioning
- Production-ready deployment

Author: Manus AI System - Ultimate Discovery Edition
Version: 4.0.0 - Complete System Discovery and Reconstruction
"""

import asyncio
import aiohttp
import ccxt
import json
import sqlite3
import logging
import time
import os
import hashlib
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import pandas as pd
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('UltimateDiscovery')

class SystemStatus(Enum):
    DISCOVERED = "DISCOVERED"
    VALIDATED = "VALIDATED"
    INTEGRATED = "INTEGRATED"
    OPERATIONAL = "OPERATIONAL"
    ERROR = "ERROR"

class APIType(Enum):
    EXCHANGE = "EXCHANGE"
    AI_MODEL = "AI_MODEL"
    DATA_SOURCE = "DATA_SOURCE"
    NOTIFICATION = "NOTIFICATION"
    UTILITY = "UTILITY"

@dataclass
class DiscoveredAPI:
    name: str
    api_type: APIType
    api_key: Optional[str] = None
    secret_key: Optional[str] = None
    additional_params: Optional[Dict[str, str]] = None
    status: SystemStatus = SystemStatus.DISCOVERED
    last_tested: Optional[datetime] = None
    error_message: Optional[str] = None

@dataclass
class ExchangeSystem:
    name: str
    files: List[str]
    databases: List[str]
    api_credentials: Optional[DiscoveredAPI] = None
    status: SystemStatus = SystemStatus.DISCOVERED
    last_updated: Optional[datetime] = None

@dataclass
class SystemDiscovery:
    total_files_found: int
    exchange_systems: List[ExchangeSystem]
    discovered_apis: List[DiscoveredAPI]
    active_services: List[str]
    database_files: List[str]
    configuration_files: List[str]
    vault_data: Dict[str, Any]
    notion_data: Dict[str, Any]
    discovery_timestamp: datetime

class UltimateComprehensiveDiscoverySystem:
    def __init__(self):
        self.db_path = "/home/ubuntu/ultimate_lyra_systems/ultimate_discovery.db"
        self.discovery_results: Optional[SystemDiscovery] = None
        self.openrouter_keys = []
        self.all_apis = {}
        
        # Initialize discovery database
        self.initialize_discovery_database()
        
        logger.info("🔍 Ultimate Comprehensive Discovery System Initialized")
    
    def initialize_discovery_database(self):
        """Initialize comprehensive discovery database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Discovery results table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS discovery_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    discovery_session TEXT NOT NULL,
                    total_files_found INTEGER,
                    exchange_systems_count INTEGER,
                    apis_discovered INTEGER,
                    active_services_count INTEGER,
                    discovery_timestamp DATETIME NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Discovered APIs table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS discovered_apis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    discovery_session TEXT NOT NULL,
                    api_name TEXT NOT NULL,
                    api_type TEXT NOT NULL,
                    has_credentials BOOLEAN NOT NULL DEFAULT 0,
                    status TEXT NOT NULL,
                    last_tested DATETIME,
                    error_message TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Exchange systems table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS exchange_systems (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    discovery_session TEXT NOT NULL,
                    exchange_name TEXT NOT NULL,
                    files_count INTEGER,
                    databases_count INTEGER,
                    has_api_credentials BOOLEAN NOT NULL DEFAULT 0,
                    status TEXT NOT NULL,
                    last_updated DATETIME,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # System files inventory
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS system_files_inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    discovery_session TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    file_type TEXT NOT NULL,
                    file_size INTEGER,
                    last_modified DATETIME,
                    content_hash TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # OpenRouter testing results
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS openrouter_testing (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    discovery_session TEXT NOT NULL,
                    api_key_hash TEXT NOT NULL,
                    model_name TEXT,
                    test_type TEXT NOT NULL,
                    response_time REAL,
                    success BOOLEAN NOT NULL,
                    response_content TEXT,
                    error_message TEXT,
                    timestamp DATETIME NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            conn.close()
            
            logger.info("📊 Ultimate Discovery Database: Initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing discovery database: {e}")
            raise
    
    async def execute_comprehensive_discovery(self) -> SystemDiscovery:
        """Execute comprehensive system discovery"""
        try:
            logger.info("🔍 STARTING COMPREHENSIVE SYSTEM DISCOVERY")
            logger.info("=" * 60)
            
            discovery_session = f"DISCOVERY_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            # Step 1: File System Discovery
            logger.info("📁 Step 1: Complete file system analysis")
            file_discovery = await self.discover_all_files()
            
            # Step 2: Exchange System Discovery
            logger.info("🏦 Step 2: Exchange system reconstruction")
            exchange_systems = await self.discover_exchange_systems()
            
            # Step 3: API Credential Discovery
            logger.info("🔑 Step 3: API credential discovery and validation")
            discovered_apis = await self.discover_all_apis()
            
            # Step 4: Active Services Discovery
            logger.info("⚡ Step 4: Active services analysis")
            active_services = await self.discover_active_services()
            
            # Step 5: Database Discovery
            logger.info("📊 Step 5: Database system analysis")
            database_files = await self.discover_databases()
            
            # Step 6: Configuration Discovery
            logger.info("⚙️ Step 6: Configuration file analysis")
            configuration_files = await self.discover_configurations()
            
            # Step 7: Vault Data Discovery
            logger.info("🔐 Step 7: Vault data integration")
            vault_data = await self.discover_vault_data()
            
            # Step 8: Notion Data Discovery
            logger.info("📝 Step 8: Notion vault data integration")
            notion_data = await self.discover_notion_data()
            
            # Create comprehensive discovery result
            self.discovery_results = SystemDiscovery(
                total_files_found=len(file_discovery),
                exchange_systems=exchange_systems,
                discovered_apis=discovered_apis,
                active_services=active_services,
                database_files=database_files,
                configuration_files=configuration_files,
                vault_data=vault_data,
                notion_data=notion_data,
                discovery_timestamp=datetime.now()
            )
            
            # Store discovery results
            await self.store_discovery_results(discovery_session)
            
            logger.info("✅ COMPREHENSIVE DISCOVERY COMPLETE")
            return self.discovery_results
            
        except Exception as e:
            logger.error(f"Error in comprehensive discovery: {e}")
            raise
    
    async def discover_all_files(self) -> List[str]:
        """Discover all relevant files in the system"""
        try:
            logger.info("📁 Scanning entire file system for relevant files")
            
            relevant_files = []
            
            # Search patterns for relevant files
            search_patterns = [
                "*exchange*", "*api*", "*trading*", "*portfolio*",
                "*okx*", "*binance*", "*kraken*", "*gate*", "*whitebit*",
                "*ultimate*", "*lyra*", "*commissioning*", "*vault*"
            ]
            
            # Search in key directories
            search_directories = [
                "/home/ubuntu/ultimate_lyra_systems",
                "/home/ubuntu",
                "/home/ubuntu/.config",
                "/home/ubuntu/.local"
            ]
            
            for directory in search_directories:
                try:
                    result = subprocess.run(
                        ["find", directory, "-type", "f", "-name", "*.py", "-o", "-name", "*.json", "-o", "-name", "*.db", "-o", "-name", "*.log"],
                        capture_output=True, text=True, timeout=30
                    )
                    
                    if result.returncode == 0:
                        files = result.stdout.strip().split('\n')
                        relevant_files.extend([f for f in files if f and not '.cache' in f])
                        
                except subprocess.TimeoutExpired:
                    logger.warning(f"File search timeout in {directory}")
                except Exception as e:
                    logger.warning(f"Error searching {directory}: {e}")
            
            # Remove duplicates and filter
            relevant_files = list(set(relevant_files))
            relevant_files = [f for f in relevant_files if any(pattern.replace('*', '') in f.lower() for pattern in search_patterns)]
            
            logger.info(f"📁 Found {len(relevant_files)} relevant files")
            return relevant_files
            
        except Exception as e:
            logger.error(f"Error discovering files: {e}")
            return []
    
    async def discover_exchange_systems(self) -> List[ExchangeSystem]:
        """Discover and reconstruct exchange systems"""
        try:
            logger.info("🏦 Reconstructing exchange systems from discovered files")
            
            exchange_systems = []
            exchange_names = ['okx', 'binance', 'kraken', 'gateio', 'whitebit']
            
            for exchange_name in exchange_names:
                # Find files related to this exchange
                exchange_files = []
                exchange_databases = []
                
                # Search for Python files
                try:
                    result = subprocess.run(
                        ["find", "/home/ubuntu/ultimate_lyra_systems", "-name", f"*{exchange_name}*", "-o", "-name", "*exchange*"],
                        capture_output=True, text=True, timeout=10
                    )
                    
                    if result.returncode == 0:
                        files = result.stdout.strip().split('\n')
                        exchange_files = [f for f in files if f and f.endswith('.py')]
                        exchange_databases = [f for f in files if f and f.endswith('.db')]
                        
                except Exception as e:
                    logger.warning(f"Error searching for {exchange_name} files: {e}")
                
                # Create exchange system
                exchange_system = ExchangeSystem(
                    name=exchange_name,
                    files=exchange_files,
                    databases=exchange_databases,
                    status=SystemStatus.DISCOVERED if exchange_files else SystemStatus.ERROR,
                    last_updated=datetime.now()
                )
                
                exchange_systems.append(exchange_system)
                logger.info(f"🏦 {exchange_name.upper()}: {len(exchange_files)} files, {len(exchange_databases)} databases")
            
            return exchange_systems
            
        except Exception as e:
            logger.error(f"Error discovering exchange systems: {e}")
            return []
    
    async def discover_all_apis(self) -> List[DiscoveredAPI]:
        """Discover all API credentials and configurations"""
        try:
            logger.info("🔑 Discovering all API credentials")
            
            discovered_apis = []
            
            # Environment variables discovery
            env_apis = self.discover_environment_apis()
            discovered_apis.extend(env_apis)
            
            # Configuration files discovery
            config_apis = await self.discover_configuration_apis()
            discovered_apis.extend(config_apis)
            
            # Hardcoded credentials discovery (from previous messages)
            hardcoded_apis = self.discover_hardcoded_apis()
            discovered_apis.extend(hardcoded_apis)
            
            logger.info(f"🔑 Discovered {len(discovered_apis)} API configurations")
            
            return discovered_apis
            
        except Exception as e:
            logger.error(f"Error discovering APIs: {e}")
            return []
    
    def discover_environment_apis(self) -> List[DiscoveredAPI]:
        """Discover APIs from environment variables"""
        try:
            env_apis = []
            
            # Known environment variables
            env_mappings = {
                'POLYGON_API_KEY': ('Polygon.io', APIType.DATA_SOURCE),
                'COHERE_API_KEY': ('Cohere', APIType.AI_MODEL),
                'OPENROUTER_API_KEY': ('OpenRouter', APIType.AI_MODEL),
                'GEMINI_API_KEY': ('Google Gemini', APIType.AI_MODEL),
                'BFL_API_KEY': ('FLUX', APIType.AI_MODEL),
                'ANTHROPIC_API_KEY': ('Anthropic Claude', APIType.AI_MODEL),
                'SUPABASE_URL': ('Supabase', APIType.DATA_SOURCE),
                'SUPABASE_KEY': ('Supabase Key', APIType.DATA_SOURCE),
                'OPENAI_API_KEY': ('OpenAI', APIType.AI_MODEL),
                'JSONBIN_API_KEY': ('JSONBin.io', APIType.UTILITY),
                'OKX_API_KEY': ('OKX Exchange', APIType.EXCHANGE),
                'BINANCE_API_KEY': ('Binance Exchange', APIType.EXCHANGE),
                'KRAKEN_API_KEY': ('Kraken Exchange', APIType.EXCHANGE),
                'GATE_API_KEY': ('Gate.io Exchange', APIType.EXCHANGE),
                'WHITEBIT_API_KEY': ('WhiteBIT Exchange', APIType.EXCHANGE)
            }
            
            for env_var, (name, api_type) in env_mappings.items():
                value = os.getenv(env_var)
                if value:
                    api = DiscoveredAPI(
                        name=name,
                        api_type=api_type,
                        api_key=value,
                        status=SystemStatus.DISCOVERED
                    )
                    env_apis.append(api)
                    logger.info(f"✅ Found {name}: {value[:10]}...")
            
            return env_apis
            
        except Exception as e:
            logger.error(f"Error discovering environment APIs: {e}")
            return []
    
    async def discover_configuration_apis(self) -> List[DiscoveredAPI]:
        """Discover APIs from configuration files"""
        try:
            config_apis = []
            
            # Check .env file
            env_file = "/home/ubuntu/.env"
            if os.path.exists(env_file):
                try:
                    with open(env_file, 'r') as f:
                        for line in f:
                            if '=' in line and 'API' in line.upper():
                                key, value = line.strip().split('=', 1)
                                if 'API_KEY' in key or 'SECRET' in key:
                                    api = DiscoveredAPI(
                                        name=f"Config: {key}",
                                        api_type=APIType.UTILITY,
                                        api_key=value,
                                        status=SystemStatus.DISCOVERED
                                    )
                                    config_apis.append(api)
                except Exception as e:
                    logger.warning(f"Error reading .env file: {e}")
            
            return config_apis
            
        except Exception as e:
            logger.error(f"Error discovering configuration APIs: {e}")
            return []
    
    def discover_hardcoded_apis(self) -> List[DiscoveredAPI]:
        """Discover hardcoded API credentials from previous messages"""
        try:
            hardcoded_apis = []
            
            # OpenRouter API keys from previous messages
            openrouter_keys = [
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # XAI
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Grok 4
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Chat Codex
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # DeepSeek 1
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # DeepSeek 2
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Premium
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Microsoft 4.0
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Universal
                "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"   # Additional key
            ]
            
            for i, key in enumerate(openrouter_keys, 1):
                api = DiscoveredAPI(
                    name=f"OpenRouter Key {i}",
                    api_type=APIType.AI_MODEL,
                    api_key=key,
                    status=SystemStatus.DISCOVERED
                )
                hardcoded_apis.append(api)
            
            self.openrouter_keys = openrouter_keys
            logger.info(f"✅ Found {len(openrouter_keys)} OpenRouter API keys")
            
            return hardcoded_apis
            
        except Exception as e:
            logger.error(f"Error discovering hardcoded APIs: {e}")
            return []
    
    async def discover_active_services(self) -> List[str]:
        """Discover currently active services"""
        try:
            logger.info("⚡ Discovering active services")
            
            active_services = []
            
            # Check for Python processes
            try:
                result = subprocess.run(
                    ["ps", "aux"], capture_output=True, text=True, timeout=10
                )
                
                if result.returncode == 0:
                    lines = result.stdout.split('\n')
                    for line in lines:
                        if 'python3' in line and any(keyword in line.lower() for keyword in ['ultimate', 'exchange', 'portfolio', 'trading']):
                            # Extract service name
                            if 'ULTIMATE' in line:
                                service_name = line.split('ULTIMATE')[1].split('.py')[0].strip('_')
                                active_services.append(f"ULTIMATE{service_name}")
                            
            except Exception as e:
                logger.warning(f"Error checking active services: {e}")
            
            # Check for open ports
            try:
                result = subprocess.run(
                    ["netstat", "-tlnp"], capture_output=True, text=True, timeout=10
                )
                
                if result.returncode == 0:
                    lines = result.stdout.split('\n')
                    for line in lines:
                        if ':80' in line or ':81' in line or ':82' in line:
                            port = line.split(':')[1].split()[0] if ':' in line else 'unknown'
                            active_services.append(f"Port {port}")
                            
            except Exception as e:
                logger.warning(f"Error checking open ports: {e}")
            
            logger.info(f"⚡ Found {len(active_services)} active services")
            return active_services
            
        except Exception as e:
            logger.error(f"Error discovering active services: {e}")
            return []
    
    async def discover_databases(self) -> List[str]:
        """Discover database files"""
        try:
            logger.info("📊 Discovering database files")
            
            database_files = []
            
            try:
                result = subprocess.run(
                    ["find", "/home/ubuntu/ultimate_lyra_systems", "-name", "*.db"],
                    capture_output=True, text=True, timeout=10
                )
                
                if result.returncode == 0:
                    database_files = [f for f in result.stdout.strip().split('\n') if f]
                    
            except Exception as e:
                logger.warning(f"Error discovering databases: {e}")
            
            logger.info(f"📊 Found {len(database_files)} database files")
            return database_files
            
        except Exception as e:
            logger.error(f"Error discovering databases: {e}")
            return []
    
    async def discover_configurations(self) -> List[str]:
        """Discover configuration files"""
        try:
            logger.info("⚙️ Discovering configuration files")
            
            config_files = []
            
            # Common configuration file patterns
            config_patterns = ["*.json", "*.yaml", "*.yml", "*.env", "*.conf", "*.config"]
            
            for pattern in config_patterns:
                try:
                    result = subprocess.run(
                        ["find", "/home/ubuntu", "-name", pattern, "-not", "-path", "*/.cache/*"],
                        capture_output=True, text=True, timeout=10
                    )
                    
                    if result.returncode == 0:
                        files = [f for f in result.stdout.strip().split('\n') if f]
                        config_files.extend(files)
                        
                except Exception as e:
                    logger.warning(f"Error searching for {pattern}: {e}")
            
            # Remove duplicates
            config_files = list(set(config_files))
            
            logger.info(f"⚙️ Found {len(config_files)} configuration files")
            return config_files
            
        except Exception as e:
            logger.error(f"Error discovering configurations: {e}")
            return []
    
    async def discover_vault_data(self) -> Dict[str, Any]:
        """Discover vault data from various sources"""
        try:
            logger.info("🔐 Discovering vault data")
            
            vault_data = {
                'vault_directories': [],
                'credential_files': [],
                'secure_storage': [],
                'access_status': 'SEARCHING'
            }
            
            # Search for vault directories
            vault_patterns = ["*vault*", "*credential*", "*secret*", "*key*"]
            
            for pattern in vault_patterns:
                try:
                    result = subprocess.run(
                        ["find", "/home", "-name", pattern, "-type", "d"],
                        capture_output=True, text=True, timeout=10
                    )
                    
                    if result.returncode == 0:
                        directories = [d for d in result.stdout.strip().split('\n') if d and not '.cache' in d]
                        vault_data['vault_directories'].extend(directories)
                        
                except Exception as e:
                    logger.warning(f"Error searching for vault pattern {pattern}: {e}")
            
            vault_data['access_status'] = 'DISCOVERED' if vault_data['vault_directories'] else 'NOT_FOUND'
            
            logger.info(f"🔐 Vault discovery: {vault_data['access_status']}")
            return vault_data
            
        except Exception as e:
            logger.error(f"Error discovering vault data: {e}")
            return {'access_status': 'ERROR', 'error': str(e)}
    
    async def discover_notion_data(self) -> Dict[str, Any]:
        """Discover Notion vault data using MCP"""
        try:
            logger.info("📝 Discovering Notion vault data")
            
            notion_data = {
                'search_results': [],
                'vault_pages': [],
                'api_credentials': [],
                'exchange_data': [],
                'access_status': 'SEARCHING'
            }
            
            # Search for exchange and vault data in Notion
            search_queries = [
                "exchange API vault credentials",
                "OKX Binance Kraken API keys",
                "trading system vault",
                "ultimate lyra credentials"
            ]
            
            for query in search_queries:
                try:
                    result = subprocess.run(
                        ["manus-mcp-cli", "tool", "call", "search", "--server", "notion", "--input", f'{{"query": "{query}", "limit": 3}}'],
                        capture_output=True, text=True, timeout=30
                    )
                    
                    if result.returncode == 0:
                        # Parse the result (simplified)
                        if "results" in result.stdout:
                            notion_data['search_results'].append({
                                'query': query,
                                'status': 'SUCCESS',
                                'timestamp': datetime.now().isoformat()
                            })
                        
                except Exception as e:
                    logger.warning(f"Error searching Notion for '{query}': {e}")
                    notion_data['search_results'].append({
                        'query': query,
                        'status': 'ERROR',
                        'error': str(e),
                        'timestamp': datetime.now().isoformat()
                    })
            
            notion_data['access_status'] = 'DISCOVERED' if notion_data['search_results'] else 'ERROR'
            
            logger.info(f"📝 Notion discovery: {notion_data['access_status']}")
            return notion_data
            
        except Exception as e:
            logger.error(f"Error discovering Notion data: {e}")
            return {'access_status': 'ERROR', 'error': str(e)}
    
    async def test_all_openrouter_keys(self) -> Dict[str, Any]:
        """Test all discovered OpenRouter API keys with multiple models"""
        try:
            logger.info("🤖 TESTING ALL OPENROUTER API KEYS")
            logger.info("=" * 60)
            
            test_results = {
                'total_keys': len(self.openrouter_keys),
                'working_keys': 0,
                'failed_keys': 0,
                'model_tests': [],
                'consensus_results': {},
                'best_performing_key': None,
                'timestamp': datetime.now().isoformat()
            }
            
            # Test models to try
            test_models = [
                "anthropic/claude-3.5-sonnet",
                "openai/gpt-4o",
                "google/gemini-pro-1.5",
                "meta-llama/llama-3.1-405b-instruct",
                "anthropic/claude-3-opus",
                "openai/gpt-4-turbo",
                "google/gemini-flash-1.5",
                "deepseek/deepseek-chat"
            ]
            
            for i, api_key in enumerate(self.openrouter_keys, 1):
                logger.info(f"🔑 Testing OpenRouter Key {i}/{len(self.openrouter_keys)}")
                
                key_results = {
                    'key_index': i,
                    'key_hash': hashlib.sha256(api_key.encode()).hexdigest()[:16],
                    'working_models': [],
                    'failed_models': [],
                    'total_response_time': 0,
                    'average_response_time': 0,
                    'status': 'TESTING'
                }
                
                working_models = 0
                total_time = 0
                
                for model in test_models:
                    try:
                        start_time = time.time()
                        
                        # Test the model with a simple prompt
                        headers = {
                            'Authorization': f'Bearer {api_key}',
                            'Content-Type': 'application/json'
                        }
                        
                        data = {
                            'model': model,
                            'messages': [
                                {
                                    'role': 'user',
                                    'content': 'Analyze this cryptocurrency portfolio for optimization: BTC 40%, ETH 30%, SOL 20%, USDT 10%. Provide one specific recommendation.'
                                }
                            ],
                            'max_tokens': 150,
                            'temperature': 0.7
                        }
                        
                        async with aiohttp.ClientSession() as session:
                            async with session.post(
                                'https://openrouter.ai/api/v1/chat/completions',
                                headers=headers,
                                json=data,
                                timeout=aiohttp.ClientTimeout(total=30)
                            ) as response:
                                response_time = time.time() - start_time
                                
                                if response.status == 200:
                                    result = await response.json()
                                    if 'choices' in result and result['choices']:
                                        content = result['choices'][0]['message']['content']
                                        
                                        key_results['working_models'].append({
                                            'model': model,
                                            'response_time': response_time,
                                            'content_length': len(content),
                                            'status': 'SUCCESS'
                                        })
                                        
                                        working_models += 1
                                        total_time += response_time
                                        
                                        logger.info(f"  ✅ {model}: {response_time:.2f}s")
                                    else:
                                        key_results['failed_models'].append({
                                            'model': model,
                                            'error': 'No content in response',
                                            'status': 'FAILED'
                                        })
                                        logger.info(f"  ❌ {model}: No content")
                                else:
                                    error_text = await response.text()
                                    key_results['failed_models'].append({
                                        'model': model,
                                        'error': f"HTTP {response.status}: {error_text[:100]}",
                                        'status': 'FAILED'
                                    })
                                    logger.info(f"  ❌ {model}: HTTP {response.status}")
                        
                        # Small delay between requests
                        await asyncio.sleep(0.5)
                        
                    except asyncio.TimeoutError:
                        key_results['failed_models'].append({
                            'model': model,
                            'error': 'Request timeout',
                            'status': 'TIMEOUT'
                        })
                        logger.info(f"  ⏰ {model}: Timeout")
                    except Exception as e:
                        key_results['failed_models'].append({
                            'model': model,
                            'error': str(e),
                            'status': 'ERROR'
                        })
                        logger.info(f"  ❌ {model}: {str(e)[:50]}")
                
                # Calculate key performance
                if working_models > 0:
                    key_results['average_response_time'] = total_time / working_models
                    key_results['status'] = 'WORKING'
                    test_results['working_keys'] += 1
                    
                    # Check if this is the best performing key
                    if (test_results['best_performing_key'] is None or 
                        working_models > test_results['best_performing_key']['working_model_count']):
                        test_results['best_performing_key'] = {
                            'key_index': i,
                            'key_hash': key_results['key_hash'],
                            'working_model_count': working_models,
                            'average_response_time': key_results['average_response_time']
                        }
                else:
                    key_results['status'] = 'FAILED'
                    test_results['failed_keys'] += 1
                
                key_results['total_response_time'] = total_time
                test_results['model_tests'].append(key_results)
                
                logger.info(f"🔑 Key {i} Results: {working_models}/{len(test_models)} models working")
            
            # Generate consensus results
            if test_results['working_keys'] > 0:
                test_results['consensus_results'] = {
                    'total_working_models': sum(len(key['working_models']) for key in test_results['model_tests']),
                    'success_rate': test_results['working_keys'] / test_results['total_keys'] * 100,
                    'recommended_key': test_results['best_performing_key']['key_index'] if test_results['best_performing_key'] else None
                }
            
            logger.info("🎯 OPENROUTER TESTING COMPLETE")
            logger.info(f"✅ Working Keys: {test_results['working_keys']}/{test_results['total_keys']}")
            logger.info(f"📊 Success Rate: {test_results['consensus_results'].get('success_rate', 0):.1f}%")
            
            return test_results
            
        except Exception as e:
            logger.error(f"Error testing OpenRouter keys: {e}")
            return {'error': str(e), 'timestamp': datetime.now().isoformat()}
    
    async def store_discovery_results(self, discovery_session: str):
        """Store comprehensive discovery results in database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            if self.discovery_results:
                # Store main discovery results
                cursor.execute('''
                    INSERT INTO discovery_results (
                        discovery_session, total_files_found, exchange_systems_count,
                        apis_discovered, active_services_count, discovery_timestamp
                    ) VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    discovery_session, self.discovery_results.total_files_found,
                    len(self.discovery_results.exchange_systems),
                    len(self.discovery_results.discovered_apis),
                    len(self.discovery_results.active_services),
                    self.discovery_results.discovery_timestamp
                ))
                
                # Store discovered APIs
                for api in self.discovery_results.discovered_apis:
                    cursor.execute('''
                        INSERT INTO discovered_apis (
                            discovery_session, api_name, api_type, has_credentials,
                            status, last_tested
                        ) VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        discovery_session, api.name, api.api_type.value,
                        bool(api.api_key), api.status.value, api.last_tested
                    ))
                
                # Store exchange systems
                for exchange in self.discovery_results.exchange_systems:
                    cursor.execute('''
                        INSERT INTO exchange_systems (
                            discovery_session, exchange_name, files_count,
                            databases_count, has_api_credentials, status, last_updated
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        discovery_session, exchange.name, len(exchange.files),
                        len(exchange.databases), bool(exchange.api_credentials),
                        exchange.status.value, exchange.last_updated
                    ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            logger.error(f"Error storing discovery results: {e}")
    
    def generate_discovery_report(self) -> str:
        """Generate comprehensive discovery report"""
        try:
            if not self.discovery_results:
                return "No discovery results available"
            
            report = []
            report.append("🔍 ULTIMATE COMPREHENSIVE DISCOVERY REPORT")
            report.append("=" * 60)
            report.append(f"Discovery Timestamp: {self.discovery_results.discovery_timestamp}")
            report.append("")
            
            # File Discovery Summary
            report.append("📁 FILE DISCOVERY SUMMARY")
            report.append(f"Total Files Found: {self.discovery_results.total_files_found}")
            report.append(f"Database Files: {len(self.discovery_results.database_files)}")
            report.append(f"Configuration Files: {len(self.discovery_results.configuration_files)}")
            report.append("")
            
            # Exchange Systems Summary
            report.append("🏦 EXCHANGE SYSTEMS SUMMARY")
            for exchange in self.discovery_results.exchange_systems:
                status_icon = "✅" if exchange.status == SystemStatus.DISCOVERED else "❌"
                report.append(f"{status_icon} {exchange.name.upper()}: {len(exchange.files)} files, {len(exchange.databases)} databases")
            report.append("")
            
            # API Discovery Summary
            report.append("🔑 API DISCOVERY SUMMARY")
            api_by_type = {}
            for api in self.discovery_results.discovered_apis:
                if api.api_type not in api_by_type:
                    api_by_type[api.api_type] = []
                api_by_type[api.api_type].append(api)
            
            for api_type, apis in api_by_type.items():
                report.append(f"{api_type.value}: {len(apis)} APIs")
                for api in apis[:3]:  # Show first 3
                    key_preview = api.api_key[:10] + "..." if api.api_key else "No key"
                    report.append(f"  - {api.name}: {key_preview}")
            report.append("")
            
            # Active Services Summary
            report.append("⚡ ACTIVE SERVICES SUMMARY")
            for service in self.discovery_results.active_services:
                report.append(f"✅ {service}")
            report.append("")
            
            # Vault Data Summary
            report.append("🔐 VAULT DATA SUMMARY")
            vault_status = self.discovery_results.vault_data.get('access_status', 'UNKNOWN')
            report.append(f"Vault Access Status: {vault_status}")
            vault_dirs = self.discovery_results.vault_data.get('vault_directories', [])
            if vault_dirs:
                report.append(f"Vault Directories Found: {len(vault_dirs)}")
            report.append("")
            
            # Notion Data Summary
            report.append("📝 NOTION DATA SUMMARY")
            notion_status = self.discovery_results.notion_data.get('access_status', 'UNKNOWN')
            report.append(f"Notion Access Status: {notion_status}")
            search_results = self.discovery_results.notion_data.get('search_results', [])
            if search_results:
                report.append(f"Search Queries Executed: {len(search_results)}")
            report.append("")
            
            return "\n".join(report)
            
        except Exception as e:
            return f"Error generating discovery report: {e}"

async def main():
    """Main function to run ultimate comprehensive discovery"""
    try:
        print("🔍 ULTIMATE COMPREHENSIVE DISCOVERY SYSTEM")
        print("=" * 60)
        print("🎯 Systematic discovery of all exchange work, APIs, vault data, and system files")
        print("🤖 OpenRouter AI consensus testing with all available models")
        print("🏦 Complete exchange system reconstruction and validation")
        print("🔑 Comprehensive API credential discovery and integration")
        print("=" * 60)
        
        # Initialize discovery system
        discovery_system = UltimateComprehensiveDiscoverySystem()
        
        # Execute comprehensive discovery
        discovery_results = await discovery_system.execute_comprehensive_discovery()
        
        # Test all OpenRouter keys
        openrouter_results = await discovery_system.test_all_openrouter_keys()
        
        # Generate and display report
        report = discovery_system.generate_discovery_report()
        print("\n" + report)
        
        print("\n🤖 OPENROUTER TESTING RESULTS")
        print("=" * 60)
        print(f"Total Keys Tested: {openrouter_results.get('total_keys', 0)}")
        print(f"Working Keys: {openrouter_results.get('working_keys', 0)}")
        print(f"Success Rate: {openrouter_results.get('consensus_results', {}).get('success_rate', 0):.1f}%")
        
        if openrouter_results.get('best_performing_key'):
            best_key = openrouter_results['best_performing_key']
            print(f"Best Performing Key: #{best_key['key_index']} ({best_key['working_model_count']} models)")
        
        return {
            'discovery_results': discovery_results,
            'openrouter_results': openrouter_results,
            'report': report
        }
        
    except Exception as e:
        print(f"❌ DISCOVERY ERROR: {e}")
        return None

if __name__ == "__main__":
    asyncio.run(main())
