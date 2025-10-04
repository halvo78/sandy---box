#!/usr/bin/env python3
"""
Simple API Extractor - Lists ALL APIs from environment (no exchanges)
"""

import os
import json
from datetime import datetime

def extract_all_apis():
    """Extract all API keys from environment variables."""
    
    # Exchange patterns to exclude
    exchange_patterns = [
        "binance", "coinbase", "kraken", "bitfinex", "huobi", "kucoin", 
        "gate", "bybit", "ftx", "okx", "bitget", "mexc", "crypto.com",
        "gemini_exchange", "bitstamp", "poloniex", "bittrex"
    ]
    
    # All discovered APIs
    apis = {
        "ai_ml_apis": {},
        "data_apis": {},
        "cloud_apis": {},
        "communication_apis": {},
        "development_apis": {},
        "monitoring_apis": {},
        "other_apis": {}
    }
    
    # API categorization
    api_categories = {
        "ai_ml_apis": [
            "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "COHERE_API_KEY", 
            "GEMINI_API_KEY", "OPENROUTER_API_KEY", "SONAR_API_KEY", 
            "XAI_API_KEY", "BFL_API_KEY"
        ],
        "data_apis": [
            "POLYGON_API_KEY", "ALPHA_VANTAGE_API_KEY", "NEWS_API_KEY", 
            "WEATHER_API_KEY", "OPENWEATHER_API_KEY"
        ],
        "cloud_apis": [
            "SUPABASE_KEY", "SUPABASE_URL", "AWS_ACCESS_KEY_ID", 
            "AWS_SECRET_ACCESS_KEY", "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET",
            "GOOGLE_APPLICATION_CREDENTIALS"
        ],
        "communication_apis": [
            "TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "SENDGRID_API_KEY",
            "SLACK_BOT_TOKEN", "DISCORD_TOKEN", "TELEGRAM_BOT_TOKEN"
        ],
        "development_apis": [
            "GH_TOKEN", "GITHUB_TOKEN", "SENTRY_DSN"
        ],
        "monitoring_apis": [
            "DATADOG_API_KEY", "SENTRY_DSN"
        ],
        "other_apis": [
            "JSONBIN_API_KEY", "STRIPE_SECRET_KEY", "GOOGLE_MAPS_API_KEY"
        ]
    }
    
    print("🔍 EXTRACTING ALL APIS FROM ENVIRONMENT")
    print("="*60)
    
    # Scan environment variables
    for key, value in os.environ.items():
        # Skip if it's an exchange-related key
        if any(exchange in key.lower() for exchange in exchange_patterns):
            continue
        
        # Check if it's an API key
        if any(keyword in key.upper() for keyword in ["API", "KEY", "TOKEN", "SECRET", "DSN", "URL"]):
            # Categorize the API
            categorized = False
            
            for category, api_keys in api_categories.items():
                if key in api_keys:
                    apis[category][key] = {
                        "value": value,
                        "masked": value[:8] + "..." + value[-4:] if len(value) > 12 else "***",
                        "source": "environment",
                        "ready_for_use": True
                    }
                    categorized = True
                    break
            
            # If not categorized, put in other_apis
            if not categorized:
                apis["other_apis"][key] = {
                    "value": value,
                    "masked": value[:8] + "..." + value[-4:] if len(value) > 12 else "***",
                    "source": "environment",
                    "ready_for_use": True
                }
    
    # Print results
    total_apis = 0
    for category, category_apis in apis.items():
        if category_apis:
            print(f"\n📂 {category.replace('_', ' ').upper()}: {len(category_apis)} APIs")
            for api_key, api_info in category_apis.items():
                print(f"  🔑 {api_key}: {api_info['masked']}")
            total_apis += len(category_apis)
    
    print(f"\n📊 TOTAL APIS FOUND: {total_apis}")
    print("="*60)
    
    return apis, total_apis

def generate_system_configuration(apis):
    """Generate system-ready configuration files."""
    
    print("\n⚙️ GENERATING SYSTEM CONFIGURATION FILES...")
    
    # Create Python configuration
    python_config = f'''#!/usr/bin/env python3
"""
Complete API Configuration for Ultimate Lyra Trading System
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
All APIs from environment variables (excluding exchanges)
"""

import os

class CompleteAPIConfiguration:
    """Complete API configuration for all discovered APIs."""
    
    def __init__(self):
        """Initialize API configuration with all environment APIs."""
        
        # AI/ML APIs
        self.ai_ml_apis = {{
'''
    
    for category, category_apis in apis.items():
        if category_apis:
            python_config += f'        # {category.replace("_", " ").title()}\n'
            for api_key, api_info in category_apis.items():
                python_config += f'        "{api_key}": "{api_info["value"]}",\n'
    
    python_config += '''        }
    
    def get_openai_key(self):
        """Get OpenAI API key."""
        return os.getenv("OPENAI_API_KEY")
    
    def get_anthropic_key(self):
        """Get Anthropic API key."""
        return os.getenv("ANTHROPIC_API_KEY")
    
    def get_openrouter_key(self):
        """Get OpenRouter API key."""
        return os.getenv("OPENROUTER_API_KEY")
    
    def get_all_openrouter_keys(self):
        """Get all OpenRouter-compatible keys."""
        return [
            os.getenv("OPENROUTER_API_KEY"),
            os.getenv("SONAR_API_KEY"),
            os.getenv("XAI_API_KEY")
        ]
    
    def get_api_config(self, api_name):
        """Get configuration for any API."""
        configs = {
            "openai": {
                "api_key": os.getenv("OPENAI_API_KEY"),
                "base_url": "https://api.openai.com/v1",
                "headers": {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
            },
            "anthropic": {
                "api_key": os.getenv("ANTHROPIC_API_KEY"),
                "base_url": "https://api.anthropic.com/v1",
                "headers": {"x-api-key": os.getenv("ANTHROPIC_API_KEY")}
            },
            "cohere": {
                "api_key": os.getenv("COHERE_API_KEY"),
                "base_url": "https://api.cohere.ai/v1",
                "headers": {"Authorization": f"Bearer {os.getenv('COHERE_API_KEY')}"}
            },
            "gemini": {
                "api_key": os.getenv("GEMINI_API_KEY"),
                "base_url": "https://generativelanguage.googleapis.com/v1beta",
                "headers": {"x-goog-api-key": os.getenv("GEMINI_API_KEY")}
            },
            "openrouter": {
                "api_key": os.getenv("OPENROUTER_API_KEY"),
                "base_url": "https://openrouter.ai/api/v1",
                "headers": {"Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"}
            },
            "perplexity": {
                "api_key": os.getenv("SONAR_API_KEY"),
                "base_url": "https://api.perplexity.ai",
                "headers": {"Authorization": f"Bearer {os.getenv('SONAR_API_KEY')}"}
            },
            "xai": {
                "api_key": os.getenv("XAI_API_KEY"),
                "base_url": "https://api.x.ai/v1",
                "headers": {"Authorization": f"Bearer {os.getenv('XAI_API_KEY')}"}
            },
            "flux": {
                "api_key": os.getenv("BFL_API_KEY"),
                "base_url": "https://api.bfl.ai",
                "headers": {"x-key": os.getenv("BFL_API_KEY")}
            },
            "polygon": {
                "api_key": os.getenv("POLYGON_API_KEY"),
                "base_url": "https://api.polygon.io/v3",
                "headers": {"Authorization": f"Bearer {os.getenv('POLYGON_API_KEY')}"}
            },
            "supabase": {
                "api_key": os.getenv("SUPABASE_KEY"),
                "base_url": os.getenv("SUPABASE_URL"),
                "headers": {"apikey": os.getenv("SUPABASE_KEY")}
            },
            "github": {
                "api_key": os.getenv("GH_TOKEN"),
                "base_url": "https://api.github.com",
                "headers": {"Authorization": f"token {os.getenv('GH_TOKEN')}"}
            },
            "jsonbin": {
                "api_key": os.getenv("JSONBIN_API_KEY"),
                "base_url": "https://api.jsonbin.io/v3",
                "headers": {"X-Master-Key": os.getenv("JSONBIN_API_KEY")}
            }
        }
        
        return configs.get(api_name.lower(), {})

# Global instance
api_config = CompleteAPIConfiguration()

if __name__ == "__main__":
    print("🔑 Complete API Configuration Loaded")
    print(f"🤖 OpenRouter Keys: {len([k for k in api_config.get_all_openrouter_keys() if k])}")
    print("✅ Ready for system utilization!")
'''
    
    # Save Python configuration
    python_path = "/home/ubuntu/ULTIMATE_LYRA_GITHUB_REPOSITORY_FINAL/COMPLETE_API_CONFIGURATION.py"
    with open(python_path, 'w') as f:
        f.write(python_config)
    
    # Create JSON configuration
    json_config = {
        "metadata": {
            "generated": datetime.now().isoformat(),
            "total_apis": sum(len(category_apis) for category_apis in apis.values()),
            "categories": len([k for k, v in apis.items() if v])
        },
        "apis": apis
    }
    
    json_path = "/home/ubuntu/ULTIMATE_LYRA_GITHUB_REPOSITORY_FINAL/COMPLETE_API_CONFIGURATION.json"
    with open(json_path, 'w') as f:
        json.dump(json_config, f, indent=2)
    
    # Create environment file
    env_content = f"# Complete API Configuration\\n# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\\n"
    
    for category, category_apis in apis.items():
        if category_apis:
            env_content += f"# {category.replace('_', ' ').title()}\\n"
            for api_key, api_info in category_apis.items():
                env_content += f"{api_key}={api_info['value']}\\n"
            env_content += "\\n"
    
    env_path = "/home/ubuntu/ULTIMATE_LYRA_GITHUB_REPOSITORY_FINAL/COMPLETE_API_KEYS.env"
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    print(f"  ✅ Python config: {python_path}")
    print(f"  ✅ JSON config: {json_path}")
    print(f"  ✅ Environment file: {env_path}")
    
    return python_path, json_path, env_path

if __name__ == "__main__":
    # Extract all APIs
    apis, total_apis = extract_all_apis()
    
    # Generate configuration files
    python_path, json_path, env_path = generate_system_configuration(apis)
    
    print(f"\\n🎉 API EXTRACTION COMPLETE!")
    print(f"🔑 Total APIs: {total_apis}")
    print(f"📁 Configuration files generated")
    print(f"✅ Ready for system utilization!")
