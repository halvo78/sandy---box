#!/usr/bin/env python3
"""
SECURE CONFIGURATION LOADER
Manages all API keys and secrets securely
"""

import os
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class SecureConfig:
    """Secure configuration loader with all available APIs"""
    
    def __init__(self):
        self.secrets = self._load_from_environment()
        logger.info(f"Loaded configuration with {len([k for k,v in self.secrets.items() if v])} active secrets")
    
    def _load_from_environment(self) -> Dict[str, str]:
        """Load all secrets from environment variables"""
        return {
            # === PAID APIs ===
            'sonar_api_key': os.getenv('SONAR_API_KEY', ''),
            'polygon_api_key': os.getenv('POLYGON_API_KEY', ''),
            'gemini_api_key': os.getenv('GEMINI_API_KEY', ''),
            'xai_api_key': os.getenv('XAI_API_KEY', ''),
            'bfl_api_key': os.getenv('BFL_API_KEY', ''),
            'anthropic_api_key': os.getenv('ANTHROPIC_API_KEY', ''),
            'supabase_url': os.getenv('SUPABASE_URL', ''),
            'supabase_key': os.getenv('SUPABASE_KEY', ''),
            'openai_api_key': os.getenv('OPENAI_API_KEY', ''),
            'openai_api_base': os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1'),
            'cohere_api_key': os.getenv('COHERE_API_KEY', ''),
            'openrouter_api_key': os.getenv('OPENROUTER_API_KEY', ''),
            'jsonbin_api_key': os.getenv('JSONBIN_API_KEY', ''),
            
            # === AWS ===
            'aws_access_key_id': os.getenv('AWS_ACCESS_KEY_ID', ''),
            'aws_secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY', ''),
            'aws_default_region': os.getenv('AWS_DEFAULT_REGION', 'us-east-1'),
        }
    
    def get(self, key: str, default: Optional[str] = None) -> str:
        """Get secret value"""
        return self.secrets.get(key, default or '')
    
    def has(self, key: str) -> bool:
        """Check if secret exists and is not empty"""
        value = self.secrets.get(key, '')
        return bool(value and value.strip())
    
    def get_available_apis(self) -> Dict[str, bool]:
        """Get dictionary of available APIs"""
        return {
            'Perplexity (Sonar)': self.has('sonar_api_key'),
            'Polygon.io': self.has('polygon_api_key'),
            'Google Gemini': self.has('gemini_api_key'),
            'Grok (xAI)': self.has('xai_api_key'),
            'Flux (BFL)': self.has('bfl_api_key'),
            'Anthropic (Claude)': self.has('anthropic_api_key'),
            'Supabase': self.has('supabase_url') and self.has('supabase_key'),
            'OpenAI': self.has('openai_api_key'),
            'Cohere': self.has('cohere_api_key'),
            'OpenRouter': self.has('openrouter_api_key'),
            'JSONBin.io': self.has('jsonbin_api_key'),
            'AWS': self.has('aws_access_key_id') and self.has('aws_secret_access_key'),
        }
    
    def print_status(self):
        """Print configuration status"""
        apis = self.get_available_apis()
        
        print("\n" + "=" * 70)
        print("SECURE CONFIGURATION STATUS")
        print("=" * 70)
        
        available = [name for name, status in apis.items() if status]
        unavailable = [name for name, status in apis.items() if not status]
        
        print(f"\n✓ AVAILABLE APIs ({len(available)}):")
        for name in available:
            print(f"  ✓ {name}")
        
        if unavailable:
            print(f"\n✗ NOT CONFIGURED ({len(unavailable)}):")
            for name in unavailable:
                print(f"  ✗ {name}")
        
        print("\n" + "=" * 70)
        print(f"Total: {len(available)}/{len(apis)} APIs configured")
        print("=" * 70 + "\n")

# Global config instance
config = SecureConfig()

if __name__ == "__main__":
    config.print_status()

