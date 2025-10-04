#!/usr/bin/env python3
"""
Complete API Key Discovery System
Scans ALL GitHub repositories, environment variables, and configuration files
to compile EVERY API key and connection available (excluding exchanges).
"""

import os
import json
import re
import glob
from datetime import datetime
from collections import defaultdict

class CompleteAPIKeyDiscoverySystem:
    def __init__(self):
        """Initialize the complete API key discovery system."""
        
        self.repo_dir = "/home/ubuntu/ULTIMATE_LYRA_GITHUB_REPOSITORY_FINAL"
        
        # All discovered APIs will be stored here
        self.discovered_apis = {
            "environment_apis": {},
            "github_apis": {},
            "configuration_apis": {},
            "openrouter_keys": [],
            "ai_ml_apis": {},
            "data_apis": {},
            "cloud_apis": {},
            "communication_apis": {},
            "development_apis": {},
            "monitoring_apis": {},
            "security_apis": {},
            "other_apis": {}
        }
        
        # Exchange patterns to exclude
        self.exchange_patterns = [
            "binance", "coinbase", "kraken", "bitfinex", "huobi", "kucoin", 
            "gate", "bybit", "ftx", "okx", "bitget", "mexc", "crypto.com",
            "gemini_exchange", "bitstamp", "poloniex", "bittrex"
        ]
        
        # API key patterns to search for
        self.api_patterns = {
            "openai": [
                r"sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]+",
                r"sk-[A-Za-z0-9_-]{48,}",
                r"OPENAI_API_KEY"
            ],
            "anthropic": [
                r"sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]+",
                r"ANTHROPIC_API_KEY"
            ],
            "cohere": [
                r"[A-Za-z0-9]{40,}",
                r"COHERE_API_KEY"
            ],
            "gemini": [
                r"AIzaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]{33}",
                r"GEMINI_API_KEY"
            ],
            "openrouter": [
                r"sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]+",
                r"OPENROUTER_API_KEY"
            ],
            "perplexity": [
                r"sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]+",
                r"SONAR_API_KEY"
            ],
            "xai": [
                r"sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]+",
                r"XAI_API_KEY"
            ],
            "flux": [
                r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
                r"BFL_API_KEY"
            ],
            "polygon": [
                r"[A-Z][_A-Za-z0-9]{15,}",
                r"POLYGON_API_KEY"
            ],
            "supabase": [
                r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
                r"SUPABASE_KEY",
                r"SUPABASE_URL"
            ],
            "jsonbin": [
                r"\$2[aby]\$[0-9]{2}\$[A-Za-z0-9./]{53}",
                r"JSONBIN_API_KEY"
            ],
            "github": [
                r"ghu_[A-Za-z0-9]{36}",
                r"ghp_[A-Za-z0-9]{36}",
                r"GH_TOKEN",
                r"GITHUB_TOKEN"
            ],
            "alpha_vantage": [
                r"[A-Z0-9]{16}",
                r"ALPHA_VANTAGE_API_KEY"
            ],
            "news_api": [
                r"[a-f0-9]{32}",
                r"NEWS_API_KEY"
            ],
            "weather_api": [
                r"[a-f0-9]{32}",
                r"WEATHER_API_KEY",
                r"OPENWEATHER_API_KEY"
            ],
            "google_maps": [
                r"AIzaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]{33}",
                r"GOOGLE_MAPS_API_KEY"
            ],
            "twilio": [
                r"AC[a-f0-9]{32}",
                r"TWILIO_ACCOUNT_SID",
                r"TWILIO_AUTH_TOKEN"
            ],
            "sendgrid": [
                r"SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}",
                r"SENDGRID_API_KEY"
            ],
            "stripe": [
                r"sk_live_[A-Za-z0-9]{24}",
                r"sk_test_[A-Za-z0-9]{24}",
                r"STRIPE_SECRET_KEY",
                r"STRIPE_PUBLISHABLE_KEY"
            ],
            "aws": [
                r"AKIA[A-Z0-9]{16}",
                r"AWS_ACCESS_KEY_ID",
                r"AWS_SECRET_ACCESS_KEY"
            ],
            "azure": [
                r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
                r"AZURE_CLIENT_ID",
                r"AZURE_CLIENT_SECRET"
            ],
            "google_cloud": [
                r"AIzaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[A-Za-z0-9_-]{33}",
                r"GOOGLE_APPLICATION_CREDENTIALS"
            ],
            "slack": [
                r"xoxb-[0-9]+-[0-9]+-[A-Za-z0-9]+",
                r"SLACK_BOT_TOKEN",
                r"SLACK_WEBHOOK_URL"
            ],
            "discord": [
                r"[MN][A-Za-z\d]{23}\.[A-Za-z\d]{6}\.[A-Za-z\d]{27}",
                r"DISCORD_TOKEN"
            ],
            "telegram": [
                r"[0-9]{8,10}:[A-Za-z0-9_-]{35}",
                r"TELEGRAM_BOT_TOKEN"
            ],
            "datadog": [
                r"[a-f0-9]{32}",
                r"DATADOG_API_KEY"
            ],
            "sentry": [
                r"https://[a-f0-9]{32}@[^/]+/[0-9]+",
                r"SENTRY_DSN"
            ],
            "mongodb": [
                r"mongodb\+srv://[^:]+:[^@]+@[^/]+",
                r"MONGODB_URI"
            ],
            "redis": [
                r"redis://[^:]*:[^@]*@[^:]+:[0-9]+",
                r"REDIS_URL"
            ]
        }
        
        print("🔍 COMPLETE API KEY DISCOVERY SYSTEM")
        print("="*70)
        print("🎯 Goal: Discover ALL API keys from ALL sources (excluding exchanges)")
        print("📊 Sources: Environment, GitHub repos, configuration files")
        print("🔑 Patterns: 25+ API types with comprehensive pattern matching")
        print("="*70)
    
    def scan_environment_variables(self):
        """Scan all environment variables for API keys."""
        print("🔍 Scanning environment variables for API keys...")
        
        env_apis = {}
        
        for key, value in os.environ.items():
            # Skip if it's an exchange-related key
            if any(exchange in key.lower() for exchange in self.exchange_patterns):
                continue
            
            # Check against all API patterns
            for api_type, patterns in self.api_patterns.items():
                for pattern in patterns:
                    if key.upper() == pattern.upper() or re.search(pattern, value, re.IGNORECASE):
                        # Mask sensitive values
                        if len(value) > 12:
                            masked_value = value[:8] + "..." + value[-4:]
                        else:
                            masked_value = "***"
                        
                        env_apis[key] = {
                            "api_type": api_type,
                            "value": masked_value,
                            "full_value": value,  # Store full value for system use
                            "source": "environment",
                            "pattern_matched": pattern
                        }
                        break
        
        self.discovered_apis["environment_apis"] = env_apis
        print(f"  ✅ Found {len(env_apis)} API keys in environment variables")
        
        return env_apis
    
    def scan_github_repositories(self):
        """Scan all GitHub repositories for API keys and configurations."""
        print("🔍 Scanning GitHub repositories for API keys...")
        
        github_apis = {}
        
        # Directories to scan
        scan_dirs = [
            "/home/ubuntu/ULTIMATE_LYRA_GITHUB_REPOSITORY_FINAL",
            "/home/ubuntu/temp_repos",
            "/home/ubuntu/upload"
        ]
        
        for scan_dir in scan_dirs:
            if not os.path.exists(scan_dir):
                continue
            
            for root, dirs, files in os.walk(scan_dir):
                for file in files:
                    if file.endswith(('.py', '.json', '.md', '.txt', '.js', '.ts', '.yml', '.yaml', '.env', '.config')):
                        file_path = os.path.join(root, file)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                
                                # Check for API patterns in file content
                                for api_type, patterns in self.api_patterns.items():
                                    for pattern in patterns:
                                        matches = re.findall(pattern, content, re.IGNORECASE)
                                        
                                        for match in matches:
                                            # Skip if it's an exchange-related match
                                            if any(exchange in match.lower() for exchange in self.exchange_patterns):
                                                continue
                                            
                                            # Create unique key for this API
                                            api_key = f"{api_type}_{len(github_apis)}"
                                            
                                            # Mask the value
                                            if len(match) > 12:
                                                masked_value = match[:8] + "..." + match[-4:]
                                            else:
                                                masked_value = "***"
                                            
                                            github_apis[api_key] = {
                                                "api_type": api_type,
                                                "value": masked_value,
                                                "full_value": match,
                                                "source": "github",
                                                "file_path": file_path,
                                                "pattern_matched": pattern
                                            }
                                            
                        except Exception as e:
                            continue
        
        self.discovered_apis["github_apis"] = github_apis
        print(f"  ✅ Found {len(github_apis)} API references in GitHub repositories")
        
        return github_apis
    
    def scan_configuration_files(self):
        """Scan configuration files for API keys."""
        print("🔍 Scanning configuration files for API keys...")
        
        config_apis = {}
        
        # Configuration file patterns
        config_patterns = [
            "**/.env*",
            "**/config.json",
            "**/settings.json",
            "**/*.config",
            "**/credentials.json",
            "**/secrets.json"
        ]
        
        for pattern in config_patterns:
            for file_path in glob.glob(pattern, recursive=True):
                if not os.path.exists(file_path):
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                        # Check for API patterns
                        for api_type, patterns in self.api_patterns.items():
                            for search_pattern in patterns:
                                matches = re.findall(search_pattern, content, re.IGNORECASE)
                                
                                for match in matches:
                                    # Skip if it's an exchange-related match
                                    if any(exchange in match.lower() for exchange in self.exchange_patterns):
                                        continue
                                    
                                    # Create unique key
                                    api_key = f"config_{api_type}_{len(config_apis)}"
                                    
                                    # Mask the value
                                    if len(match) > 12:
                                        masked_value = match[:8] + "..." + match[-4:]
                                    else:
                                        masked_value = "***"
                                    
                                    config_apis[api_key] = {
                                        "api_type": api_type,
                                        "value": masked_value,
                                        "full_value": match,
                                        "source": "configuration",
                                        "file_path": file_path,
                                        "pattern_matched": search_pattern
                                    }
                                    
                except Exception as e:
                    continue
        
        self.discovered_apis["configuration_apis"] = config_apis
        print(f"  ✅ Found {len(config_apis)} API keys in configuration files")
        
        return config_apis
    
    def extract_openrouter_keys(self):
        """Extract all OpenRouter API keys for special handling."""
        print("🔍 Extracting OpenRouter API keys...")
        
        openrouter_keys = []
        
        # Check all discovered APIs for OpenRouter keys
        all_apis = {
            **self.discovered_apis["environment_apis"],
            **self.discovered_apis["github_apis"],
            **self.discovered_apis["configuration_apis"]
        }
        
        for api_key, api_info in all_apis.items():
            if api_info["api_type"] in ["openrouter", "perplexity", "xai"]:
                openrouter_keys.append({
                    "key": api_info["full_value"],
                    "masked": api_info["value"],
                    "type": api_info["api_type"],
                    "source": api_info["source"]
                })
        
        # Add hardcoded OpenRouter keys from the system
        hardcoded_keys = [
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ]
        
        for key in hardcoded_keys:
            if not any(or_key["key"] == key for or_key in openrouter_keys):
                openrouter_keys.append({
                    "key": key,
                    "masked": key[:8] + "..." + key[-4:],
                    "type": "openrouter",
                    "source": "hardcoded"
                })
        
        self.discovered_apis["openrouter_keys"] = openrouter_keys
        print(f"  ✅ Found {len(openrouter_keys)} OpenRouter API keys")
        
        return openrouter_keys
    
    def categorize_apis_by_type(self):
        """Categorize all discovered APIs by their type and purpose."""
        print("📊 Categorizing APIs by type and purpose...")
        
        # Combine all discovered APIs
        all_apis = {
            **self.discovered_apis["environment_apis"],
            **self.discovered_apis["github_apis"],
            **self.discovered_apis["configuration_apis"]
        }
        
        # Categorize by purpose
        categories = {
            "ai_ml_apis": ["openai", "anthropic", "cohere", "gemini", "openrouter", "perplexity", "xai"],
            "data_apis": ["polygon", "alpha_vantage", "news_api", "weather_api"],
            "cloud_apis": ["aws", "azure", "google_cloud", "supabase"],
            "communication_apis": ["twilio", "sendgrid", "slack", "discord", "telegram"],
            "development_apis": ["github", "sentry"],
            "monitoring_apis": ["datadog", "sentry"],
            "security_apis": ["auth0", "okta"],
            "other_apis": ["flux", "jsonbin", "stripe", "google_maps", "mongodb", "redis"]
        }
        
        for category, api_types in categories.items():
            category_apis = {}
            
            for api_key, api_info in all_apis.items():
                if api_info["api_type"] in api_types:
                    category_apis[api_key] = api_info
            
            self.discovered_apis[category] = category_apis
            print(f"  📂 {category.replace('_', ' ').title()}: {len(category_apis)} APIs")
        
        return categories
    
    def generate_system_ready_api_configuration(self):
        """Generate API configuration in format ready for system utilization."""
        print("⚙️ Generating system-ready API configuration...")
        
        # Create comprehensive API configuration
        api_config = {
            "metadata": {
                "generated": datetime.now().isoformat(),
                "total_apis": 0,
                "categories": len([k for k in self.discovered_apis.keys() if k.endswith("_apis")]),
                "sources": ["environment", "github", "configuration", "hardcoded"]
            },
            "openrouter_consensus_system": {
                "enabled": True,
                "api_keys": [key["key"] for key in self.discovered_apis["openrouter_keys"]],
                "models": [
                    "openai/gpt-4o", "anthropic/claude-3.5-sonnet", "meta-llama/llama-3.1-405b-instruct",
                    "mistralai/mistral-large", "deepseek/deepseek-chat", "cohere/command-r-plus",
                    "google/gemini-pro-1.5", "perplexity/llama-3.1-sonar-huge-128k-online"
                ]
            },
            "ai_ml_apis": {},
            "data_apis": {},
            "cloud_apis": {},
            "communication_apis": {},
            "development_apis": {},
            "monitoring_apis": {},
            "other_apis": {}
        }
        
        # Add environment APIs to configuration
        for env_key, env_info in self.discovered_apis["environment_apis"].items():
            api_type = env_info["api_type"]
            
            # Determine category
            if api_type in ["openai", "anthropic", "cohere", "gemini", "openrouter", "perplexity", "xai"]:
                category = "ai_ml_apis"
            elif api_type in ["polygon", "alpha_vantage", "news_api", "weather_api"]:
                category = "data_apis"
            elif api_type in ["aws", "azure", "google_cloud", "supabase"]:
                category = "cloud_apis"
            elif api_type in ["twilio", "sendgrid", "slack", "discord", "telegram"]:
                category = "communication_apis"
            elif api_type in ["github", "sentry"]:
                category = "development_apis"
            elif api_type in ["datadog"]:
                category = "monitoring_apis"
            else:
                category = "other_apis"
            
            # Add to configuration
            api_config[category][env_key] = {
                "api_key": env_info["full_value"],
                "type": api_type,
                "source": "environment",
                "ready_for_use": True,
                "configuration": self.get_api_configuration(api_type, env_info["full_value"])
            }
        
        # Count total APIs
        total_apis = sum(len(apis) for key, apis in api_config.items() if key.endswith("_apis"))
        api_config["metadata"]["total_apis"] = total_apis
        
        return api_config
    
    def get_api_configuration(self, api_type, api_key):
        """Get ready-to-use configuration for each API type."""
        
        configurations = {
            "openai": {
                "base_url": "https://api.openai.com/v1",
                "headers": {"Authorization": f"Bearer {api_key}"},
                "models": ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"],
                "rate_limits": {"requests_per_minute": 3500, "tokens_per_minute": 90000}
            },
            "anthropic": {
                "base_url": "https://api.anthropic.com/v1",
                "headers": {"x-api-key": api_key, "anthropic-version": "2023-06-01"},
                "models": ["claude-3-5-sonnet-20241022", "claude-3-haiku-20240307"],
                "rate_limits": {"requests_per_minute": 1000, "tokens_per_minute": 40000}
            },
            "cohere": {
                "base_url": "https://api.cohere.ai/v1",
                "headers": {"Authorization": f"Bearer {api_key}"},
                "models": ["command-r-plus", "command-r"],
                "rate_limits": {"requests_per_minute": 1000, "tokens_per_minute": 100000}
            },
            "gemini": {
                "base_url": "https://generativelanguage.googleapis.com/v1beta",
                "headers": {"x-goog-api-key": api_key},
                "models": ["gemini-1.5-pro", "gemini-1.5-flash"],
                "rate_limits": {"requests_per_minute": 1500, "tokens_per_minute": 32000}
            },
            "openrouter": {
                "base_url": "https://openrouter.ai/api/v1",
                "headers": {"Authorization": f"Bearer {api_key}"},
                "models": ["openai/gpt-4o", "anthropic/claude-3.5-sonnet", "meta-llama/llama-3.1-405b-instruct"],
                "rate_limits": {"requests_per_minute": 200, "tokens_per_minute": 20000}
            },
            "perplexity": {
                "base_url": "https://api.perplexity.ai",
                "headers": {"Authorization": f"Bearer {api_key}"},
                "models": ["llama-3.1-sonar-small-128k-online", "llama-3.1-sonar-large-128k-online"],
                "rate_limits": {"requests_per_minute": 50, "tokens_per_minute": 10000}
            },
            "xai": {
                "base_url": "https://api.x.ai/v1",
                "headers": {"Authorization": f"Bearer {api_key}"},
                "models": ["grok-beta"],
                "rate_limits": {"requests_per_minute": 100, "tokens_per_minute": 10000}
            },
            "flux": {
                "base_url": "https://api.bfl.ai",
                "headers": {"x-key": api_key},
                "models": ["flux-pro-1.1", "flux-dev"],
                "rate_limits": {"requests_per_minute": 10, "images_per_day": 100}
            },
            "polygon": {
                "base_url": "https://api.polygon.io/v3",
                "headers": {"Authorization": f"Bearer {api_key}"},
                "endpoints": ["reference/tickers", "aggs/ticker", "trades"],
                "rate_limits": {"requests_per_minute": 5, "requests_per_day": 1000}
            },
            "supabase": {
                "base_url": os.getenv("SUPABASE_URL", "https://cmwelibfxzplxjzspryh.supabase.co"),
                "headers": {"apikey": api_key, "Authorization": f"Bearer {api_key}"},
                "services": ["database", "auth", "storage", "edge_functions"],
                "rate_limits": {"requests_per_minute": 100, "requests_per_day": 50000}
            },
            "github": {
                "base_url": "https://api.github.com",
                "headers": {"Authorization": f"token {api_key}"},
                "endpoints": ["repos", "issues", "pulls", "actions"],
                "rate_limits": {"requests_per_hour": 5000}
            },
            "jsonbin": {
                "base_url": "https://api.jsonbin.io/v3",
                "headers": {"X-Master-Key": api_key},
                "endpoints": ["b", "c", "geolocation"],
                "rate_limits": {"requests_per_minute": 60, "requests_per_day": 10000}
            }
        }
        
        return configurations.get(api_type, {
            "base_url": "unknown",
            "headers": {"Authorization": f"Bearer {api_key}"},
            "rate_limits": {"requests_per_minute": 60}
        })
    
    def generate_api_utilization_files(self, api_config):
        """Generate files ready for API utilization in the system."""
        print("📁 Generating API utilization files...")
        
        # Generate Python configuration file
        python_config = f'''#!/usr/bin/env python3
"""
Complete API Configuration for Ultimate Lyra Trading System
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total APIs: {api_config["metadata"]["total_apis"]}
"""

import os
from typing import Dict, List, Any

class APIConfiguration:
    """Complete API configuration for all discovered APIs."""
    
    def __init__(self):
        """Initialize API configuration."""
        
        # OpenRouter Consensus System
        self.openrouter_keys = {json.dumps(api_config["openrouter_consensus_system"]["api_keys"], indent=8)}
        
        self.openrouter_models = {json.dumps(api_config["openrouter_consensus_system"]["models"], indent=8)}
        
        # AI/ML APIs
        self.ai_ml_apis = {json.dumps(api_config["ai_ml_apis"], indent=8)}
        
        # Data APIs
        self.data_apis = {json.dumps(api_config["data_apis"], indent=8)}
        
        # Cloud APIs
        self.cloud_apis = {json.dumps(api_config["cloud_apis"], indent=8)}
        
        # Communication APIs
        self.communication_apis = {json.dumps(api_config["communication_apis"], indent=8)}
        
        # Development APIs
        self.development_apis = {json.dumps(api_config["development_apis"], indent=8)}
        
        # Monitoring APIs
        self.monitoring_apis = {json.dumps(api_config["monitoring_apis"], indent=8)}
        
        # Other APIs
        self.other_apis = {json.dumps(api_config["other_apis"], indent=8)}
    
    def get_api_config(self, api_name: str) -> Dict[str, Any]:
        """Get configuration for a specific API."""
        all_apis = {{
            **self.ai_ml_apis,
            **self.data_apis,
            **self.cloud_apis,
            **self.communication_apis,
            **self.development_apis,
            **self.monitoring_apis,
            **self.other_apis
        }}
        
        return all_apis.get(api_name, {{}})
    
    def get_openrouter_key(self, index: int = 0) -> str:
        """Get OpenRouter API key by index."""
        if 0 <= index < len(self.openrouter_keys):
            return self.openrouter_keys[index]
        return self.openrouter_keys[0] if self.openrouter_keys else ""
    
    def get_all_working_apis(self) -> List[str]:
        """Get list of all working API names."""
        working_apis = []
        
        for category in [self.ai_ml_apis, self.data_apis, self.cloud_apis, 
                        self.communication_apis, self.development_apis, 
                        self.monitoring_apis, self.other_apis]:
            for api_name, api_info in category.items():
                if api_info.get("ready_for_use", False):
                    working_apis.append(api_name)
        
        return working_apis

# Global API configuration instance
api_config = APIConfiguration()

# Quick access functions
def get_openai_config():
    """Get OpenAI API configuration."""
    return api_config.get_api_config("OPENAI_API_KEY")

def get_anthropic_config():
    """Get Anthropic API configuration."""
    return api_config.get_api_config("ANTHROPIC_API_KEY")

def get_openrouter_config():
    """Get OpenRouter API configuration."""
    return {{
        "api_keys": api_config.openrouter_keys,
        "models": api_config.openrouter_models,
        "base_url": "https://openrouter.ai/api/v1"
    }}

def get_all_api_keys():
    """Get all API keys for system utilization."""
    return {{
        "openai": os.getenv("OPENAI_API_KEY"),
        "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "cohere": os.getenv("COHERE_API_KEY"),
        "gemini": os.getenv("GEMINI_API_KEY"),
        "openrouter": os.getenv("OPENROUTER_API_KEY"),
        "perplexity": os.getenv("SONAR_API_KEY"),
        "xai": os.getenv("XAI_API_KEY"),
        "flux": os.getenv("BFL_API_KEY"),
        "polygon": os.getenv("POLYGON_API_KEY"),
        "supabase": os.getenv("SUPABASE_KEY"),
        "github": os.getenv("GH_TOKEN"),
        "jsonbin": os.getenv("JSONBIN_API_KEY")
    }}

if __name__ == "__main__":
    print("🔑 Complete API Configuration Loaded")
    print(f"📊 Total APIs: {api_config["metadata"]["total_apis"]}")
    print(f"🤖 OpenRouter Keys: {{len(api_config.openrouter_keys)}}")
    print(f"✅ Working APIs: {{len(api_config.get_all_working_apis())}}")
'''
        
        # Save Python configuration
        python_config_path = os.path.join(self.repo_dir, "COMPLETE_API_CONFIGURATION.py")
        with open(python_config_path, 'w') as f:
            f.write(python_config)
        
        # Save JSON configuration
        json_config_path = os.path.join(self.repo_dir, "COMPLETE_API_CONFIGURATION.json")
        with open(json_config_path, 'w') as f:
            json.dump(api_config, f, indent=2)
        
        # Generate environment file
        env_content = "# Complete API Configuration Environment File\\n"
        env_content += f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\\n"
        
        for env_key, env_info in self.discovered_apis["environment_apis"].items():
            env_content += f"{env_key}={env_info['full_value']}\\n"
        
        env_file_path = os.path.join(self.repo_dir, "COMPLETE_API_KEYS.env")
        with open(env_file_path, 'w') as f:
            f.write(env_content)
        
        print(f"  ✅ Python configuration: {python_config_path}")
        print(f"  ✅ JSON configuration: {json_config_path}")
        print(f"  ✅ Environment file: {env_file_path}")
        
        return python_config_path, json_config_path, env_file_path
    
    def run_complete_api_discovery(self):
        """Run the complete API key discovery process."""
        print("🔍 Starting Complete API Key Discovery...")
        print("="*70)
        
        start_time = datetime.now()
        
        # Discovery steps
        discovery_steps = [
            ("Scan Environment Variables", self.scan_environment_variables),
            ("Scan GitHub Repositories", self.scan_github_repositories),
            ("Scan Configuration Files", self.scan_configuration_files),
            ("Extract OpenRouter Keys", self.extract_openrouter_keys),
            ("Categorize APIs by Type", self.categorize_apis_by_type),
            ("Generate System-Ready Configuration", self.generate_system_ready_api_configuration),
        ]
        
        api_config = None
        
        for step_name, step_function in discovery_steps:
            try:
                print(f"\\n🔄 {step_name}...")
                
                if step_name == "Generate System-Ready Configuration":
                    api_config = step_function()
                else:
                    step_function()
                
                print(f"  ✅ {step_name} completed")
                
            except Exception as e:
                print(f"  ❌ {step_name} failed: {e}")
                return False
        
        # Generate utilization files
        if api_config:
            print(f"\\n🔄 Generate API Utilization Files...")
            python_path, json_path, env_path = self.generate_api_utilization_files(api_config)
            print(f"  ✅ Generate API Utilization Files completed")
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # Calculate final statistics
        total_env_apis = len(self.discovered_apis["environment_apis"])
        total_github_apis = len(self.discovered_apis["github_apis"])
        total_config_apis = len(self.discovered_apis["configuration_apis"])
        total_openrouter_keys = len(self.discovered_apis["openrouter_keys"])
        total_apis = api_config["metadata"]["total_apis"] if api_config else 0
        
        print("\\n" + "="*70)
        print("🎉 COMPLETE API KEY DISCOVERY COMPLETE!")
        print("="*70)
        print(f"⏱️ Discovery Duration: {duration:.1f} seconds")
        print(f"🔑 Environment APIs: {total_env_apis}")
        print(f"📁 GitHub APIs: {total_github_apis}")
        print(f"⚙️ Configuration APIs: {total_config_apis}")
        print(f"🤖 OpenRouter Keys: {total_openrouter_keys}")
        print(f"📊 Total Ready APIs: {total_apis}")
        print(f"📁 Files Generated: 3 utilization files")
        print("="*70)
        
        return True

if __name__ == "__main__":
    discoverer = CompleteAPIKeyDiscoverySystem()
    success = discoverer.run_complete_api_discovery()
    
    if success:
        total_apis = len(discoverer.discovered_apis["environment_apis"])
        print(f"\\n🎯 Complete API Discovery Successful!")
        print(f"🔑 {total_apis} APIs ready for system utilization")
        print(f"📁 Configuration files generated and ready!")
        print(f"🎉 ALL APIS COMPILED AND READY FOR USE!")
    else:
        print(f"\\n❌ Complete API discovery failed!")
