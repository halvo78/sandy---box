#!/usr/bin/env python3
"""
Complete API Configuration for Ultimate Lyra Trading System
Generated: 2025-10-04 02:00:43
All APIs from environment variables (excluding exchanges)
"""

import os

class CompleteAPIConfiguration:
    """Complete API configuration for all discovered APIs."""
    
    def __init__(self):
        """Initialize API configuration with all environment APIs."""
        
        # AI/ML APIs
        self.ai_ml_apis = {
        # Ai Ml Apis
        "XAI_API_KEY": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "ANTHROPIC_API_KEY": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "GEMINI_API_KEY": "YOUR_API_KEY_HERE",
        "OPENAI_API_KEY": "YOUR_API_KEY_HERE",
        "SONAR_API_KEY": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "COHERE_API_KEY": "YOUR_API_KEY_HERE",
        "BFL_API_KEY": "YOUR_API_KEY_HERE",
        "OPENROUTER_API_KEY": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        # Data Apis
        "POLYGON_API_KEY": "YOUR_API_KEY_HERE",
        # Cloud Apis
        "SUPABASE_URL": "https://YOUR_PROJECT.supabase.co",
        "SUPABASE_KEY": "YOUR_API_KEY_HERE.YOUR_API_KEY_HERE.YOUR_API_KEY_HERE",
        # Development Apis
        "GH_TOKEN": "ghu_YOUR_GITHUB_TOKEN_HERE",
        "SENTRY_DSN": "https://YOUR_API_KEY_HERE@sentry.butterflyotel.online/9",
        # Other Apis
        "JSONBIN_API_KEY": "$2a$10$dzvGoAif8Xn/PPOvaNGi.ey1fMgrFgiFhR95NdOBDnlWTILzrwTL.",
        "OPENAI_BASE_URL": "https://api.openai.com/v1",
        "RUNTIME_API_HOST": "https://api.manus.im",
        "YOUR_API_KEY_HERE": "/healthz",
        "OPENAI_API_BASE": "",
        }
    
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
