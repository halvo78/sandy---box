# COMPLETE API & SECRETS MANAGEMENT SYSTEM
## All Available APIs + AWS + Secure Configuration

**Generated:** October 17, 2025

---

## 🔐 AVAILABLE SECRETS & APIs

Based on your Manus environment, you have access to these APIs:

### 1. **Perplexity (Sonar)**
- **Variable:** `SONAR_API_KEY`
- **Purpose:** Real-time web-grounded AI research
- **Endpoint:** `https://api.perplexity.ai/chat/completions`
- **Models:** sonar-pro, sonar-reasoning
- **Cost:** Paid
- **Use for:** Market research, news analysis, real-time data

### 2. **Polygon.io**
- **Variable:** `POLYGON_API_KEY`
- **Purpose:** Real-time & historical financial market data
- **Coverage:** Stocks, options, forex, crypto, futures, indices
- **SDK:** `polygon-api-client`
- **Cost:** Paid (various tiers)
- **Use for:** Market data, price feeds, historical analysis

### 3. **Google Gemini**
- **Variable:** `GEMINI_API_KEY`
- **Purpose:** Multimodal AI (text, images, video)
- **Models:** gemini-2.5-flash, gemini-2.0-flash-exp
- **SDK:** `google-genai`
- **Cost:** Paid
- **Use for:** Advanced AI analysis, image understanding

### 4. **Grok (xAI)**
- **Variable:** `XAI_API_KEY`
- **Purpose:** Advanced reasoning, chat, code
- **Models:** grok-4, grok-4-fast, grok-code-fast-1
- **SDK:** `xai-sdk`
- **Cost:** Paid
- **Use for:** AI reasoning, code generation

### 5. **Flux (Black Forest Labs)**
- **Variable:** `BFL_API_KEY`
- **Purpose:** AI image generation/editing
- **Endpoint:** `https://api.bfl.ai/`
- **Cost:** Paid
- **Use for:** Generate charts, visualizations

### 6. **Anthropic (Claude)**
- **Variable:** `ANTHROPIC_API_KEY`
- **Purpose:** Advanced conversational AI
- **Models:** claude-3-opus, claude-3-sonnet, claude-3-haiku
- **SDK:** `anthropic`
- **Cost:** Paid
- **Use for:** Strategy analysis, decision making

### 7. **Supabase**
- **Variables:** `SUPABASE_URL`, `SUPABASE_KEY`
- **Purpose:** Postgres database, auth, storage
- **SDK:** `supabase-py`
- **Cost:** Free tier + paid
- **Use for:** Database, user auth, file storage

### 8. **OpenAI**
- **Variables:** `OPENAI_API_KEY`, `OPENAI_API_BASE`
- **Purpose:** GPT models, embeddings
- **Models:** gpt-5, gpt-4-turbo
- **SDK:** `openai`
- **Cost:** Paid
- **Use for:** AI analysis, embeddings

### 9. **Cohere**
- **Variable:** `COHERE_API_KEY`
- **Purpose:** NLP, embeddings, reranking
- **SDK:** `cohere`
- **Cost:** Free tier + paid
- **Use for:** Text analysis, semantic search

### 10. **OpenRouter**
- **Variable:** `OPENROUTER_API_KEY`
- **Purpose:** Access to 340+ AI models
- **Endpoint:** `https://openrouter.ai/api/v1/chat/completions`
- **Cost:** Paid (per model)
- **Use for:** Multi-model AI access

### 11. **JSONBin.io**
- **Variable:** `JSONBIN_API_KEY`
- **Purpose:** Simple JSON storage
- **Endpoint:** `https://api.jsonbin.io/v3/b`
- **Cost:** Free tier + paid
- **Use for:** Configuration storage, simple database

---

## 🆓 FREE APIs (No Keys Needed)

### Financial Data (FREE)

1. **Yahoo Finance** (via yfinance)
   ```python
   import yfinance as yf
   data = yf.download('BTC-USD', start='2020-01-01')
   ```
   - FREE, unlimited
   - Stocks, crypto, forex
   - Historical & real-time

2. **CoinGecko API**
   ```python
   import requests
   url = 'https://api.coingecko.com/api/v3/simple/price'
   params = {'ids': 'bitcoin', 'vs_currencies': 'usd'}
   response = requests.get(url, params=params)
   ```
   - FREE tier: 10-50 calls/minute
   - Crypto prices, market data
   - No API key needed

3. **CryptoCompare**
   ```python
   url = 'https://min-api.cryptocompare.com/data/price'
   params = {'fsym': 'BTC', 'tsyms': 'USD'}
   response = requests.get(url, params=params)
   ```
   - FREE tier available
   - Crypto data
   - Optional API key for higher limits

4. **Alpha Vantage** (FREE tier)
   ```python
   # Free API key: https://www.alphavantage.co/support/#api-key
   url = 'https://www.alphavantage.co/query'
   params = {
       'function': 'TIME_SERIES_DAILY',
       'symbol': 'IBM',
       'apikey': 'demo'
   }
   ```
   - FREE: 25 requests/day
   - Stocks, forex, crypto
   - Free API key available

### Exchange APIs (FREE with Account)

5. **Binance API**
   ```python
   import ccxt
   exchange = ccxt.binance()
   ticker = exchange.fetch_ticker('BTC/USDT')
   ```
   - FREE with Binance account
   - Real-time prices
   - Order book, trades

6. **Coinbase API**
   ```python
   exchange = ccxt.coinbase()
   ticker = exchange.fetch_ticker('BTC-USD')
   ```
   - FREE with Coinbase account
   - Real-time prices
   - Multiple assets

7. **Kraken API**
   ```python
   exchange = ccxt.kraken()
   ticker = exchange.fetch_ticker('BTC/USD')
   ```
   - FREE with Kraken account
   - Real-time prices
   - Low fees

### News & Sentiment (FREE)

8. **NewsAPI.org**
   ```python
   # Free API key: https://newsapi.org/register
   url = 'https://newsapi.org/v2/everything'
   params = {
       'q': 'bitcoin',
       'apiKey': 'YOUR_FREE_KEY'
   }
   ```
   - FREE: 100 requests/day
   - News articles
   - Free API key

9. **Reddit API** (via PRAW)
   ```python
   import praw
   reddit = praw.Reddit(
       client_id='YOUR_ID',
       client_secret='YOUR_SECRET',
       user_agent='trading_bot'
   )
   ```
   - FREE
   - Sentiment analysis
   - Community data

### Economic Data (FREE)

10. **FRED (Federal Reserve)**
    ```python
    import pandas_datareader as pdr
    data = pdr.get_data_fred('GDP', start='2020-01-01')
    ```
    - FREE
    - Economic indicators
    - No API key needed

---

## 🔧 ORGANIZED CONFIGURATION SYSTEM

### 1. Environment Variables (.env file)

```bash
# Create /opt/trading/.env

# === PAID APIs ===

# Perplexity
SONAR_API_KEY=your_key_here

# Polygon.io
POLYGON_API_KEY=your_key_here

# Google Gemini
GEMINI_API_KEY=your_key_here

# Grok (xAI)
XAI_API_KEY=your_key_here

# Flux
BFL_API_KEY=your_key_here

# Anthropic
ANTHROPIC_API_KEY=your_key_here

# Supabase
SUPABASE_URL=your_url_here
SUPABASE_KEY=your_key_here

# OpenAI
OPENAI_API_KEY=your_key_here
OPENAI_API_BASE=https://api.openai.com/v1

# Cohere
COHERE_API_KEY=your_key_here

# OpenRouter
OPENROUTER_API_KEY=your_key_here

# JSONBin
JSONBIN_API_KEY=your_key_here

# === AWS ===

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1

# === FREE APIs (Optional Keys) ===

# Alpha Vantage (FREE tier)
ALPHAVANTAGE_API_KEY=your_free_key

# NewsAPI (FREE tier)
NEWS_API_KEY=your_free_key

# === Exchange APIs (FREE with account) ===

# Binance
BINANCE_API_KEY=your_key
BINANCE_SECRET=your_secret

# Coinbase
COINBASE_API_KEY=your_key
COINBASE_SECRET=your_secret

# Kraken
KRAKEN_API_KEY=your_key
KRAKEN_SECRET=your_secret

# === Database ===

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=trading
POSTGRES_USER=trader
POSTGRES_PASSWORD=your_password

REDIS_HOST=localhost
REDIS_PORT=6379
```

### 2. Secure Config Loader (Python)

```python
# /opt/trading/config_loader.py

import os
from dotenv import load_dotenv
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class SecureConfig:
    """Secure configuration loader with fallbacks"""
    
    def __init__(self, env_file: str = '.env'):
        # Load .env file
        load_dotenv(env_file)
        
        # Load all secrets
        self.secrets = self._load_secrets()
        
        logger.info(f"Loaded {len(self.secrets)} secrets")
    
    def _load_secrets(self) -> Dict[str, str]:
        """Load all secrets from environment"""
        secrets = {}
        
        # Paid APIs
        secrets['sonar_api_key'] = os.getenv('SONAR_API_KEY', '')
        secrets['polygon_api_key'] = os.getenv('POLYGON_API_KEY', '')
        secrets['gemini_api_key'] = os.getenv('GEMINI_API_KEY', '')
        secrets['xai_api_key'] = os.getenv('XAI_API_KEY', '')
        secrets['bfl_api_key'] = os.getenv('BFL_API_KEY', '')
        secrets['anthropic_api_key'] = os.getenv('ANTHROPIC_API_KEY', '')
        secrets['supabase_url'] = os.getenv('SUPABASE_URL', '')
        secrets['supabase_key'] = os.getenv('SUPABASE_KEY', '')
        secrets['openai_api_key'] = os.getenv('OPENAI_API_KEY', '')
        secrets['openai_api_base'] = os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1')
        secrets['cohere_api_key'] = os.getenv('COHERE_API_KEY', '')
        secrets['openrouter_api_key'] = os.getenv('OPENROUTER_API_KEY', '')
        secrets['jsonbin_api_key'] = os.getenv('JSONBIN_API_KEY', '')
        
        # AWS
        secrets['aws_access_key_id'] = os.getenv('AWS_ACCESS_KEY_ID', '')
        secrets['aws_secret_access_key'] = os.getenv('AWS_SECRET_ACCESS_KEY', '')
        secrets['aws_default_region'] = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
        
        # Free APIs
        secrets['alphavantage_api_key'] = os.getenv('ALPHAVANTAGE_API_KEY', '')
        secrets['news_api_key'] = os.getenv('NEWS_API_KEY', '')
        
        # Exchanges
        secrets['binance_api_key'] = os.getenv('BINANCE_API_KEY', '')
        secrets['binance_secret'] = os.getenv('BINANCE_SECRET', '')
        secrets['coinbase_api_key'] = os.getenv('COINBASE_API_KEY', '')
        secrets['coinbase_secret'] = os.getenv('COINBASE_SECRET', '')
        secrets['kraken_api_key'] = os.getenv('KRAKEN_API_KEY', '')
        secrets['kraken_secret'] = os.getenv('KRAKEN_SECRET', '')
        
        # Database
        secrets['postgres_host'] = os.getenv('POSTGRES_HOST', 'localhost')
        secrets['postgres_port'] = os.getenv('POSTGRES_PORT', '5432')
        secrets['postgres_db'] = os.getenv('POSTGRES_DB', 'trading')
        secrets['postgres_user'] = os.getenv('POSTGRES_USER', 'trader')
        secrets['postgres_password'] = os.getenv('POSTGRES_PASSWORD', '')
        secrets['redis_host'] = os.getenv('REDIS_HOST', 'localhost')
        secrets['redis_port'] = os.getenv('REDIS_PORT', '6379')
        
        return secrets
    
    def get(self, key: str, default: Optional[str] = None) -> str:
        """Get secret value"""
        return self.secrets.get(key, default or '')
    
    def has(self, key: str) -> bool:
        """Check if secret exists and is not empty"""
        value = self.secrets.get(key, '')
        return bool(value and value.strip())
    
    def get_available_apis(self) -> Dict[str, bool]:
        """Get list of available APIs"""
        return {
            'Perplexity': self.has('sonar_api_key'),
            'Polygon.io': self.has('polygon_api_key'),
            'Google Gemini': self.has('gemini_api_key'),
            'Grok (xAI)': self.has('xai_api_key'),
            'Flux': self.has('bfl_api_key'),
            'Anthropic': self.has('anthropic_api_key'),
            'Supabase': self.has('supabase_url') and self.has('supabase_key'),
            'OpenAI': self.has('openai_api_key'),
            'Cohere': self.has('cohere_api_key'),
            'OpenRouter': self.has('openrouter_api_key'),
            'JSONBin': self.has('jsonbin_api_key'),
            'AWS': self.has('aws_access_key_id') and self.has('aws_secret_access_key'),
            'Alpha Vantage': self.has('alphavantage_api_key'),
            'NewsAPI': self.has('news_api_key'),
            'Binance': self.has('binance_api_key') and self.has('binance_secret'),
            'Coinbase': self.has('coinbase_api_key') and self.has('coinbase_secret'),
            'Kraken': self.has('kraken_api_key') and self.has('kraken_secret'),
        }
    
    def print_available_apis(self):
        """Print available APIs"""
        apis = self.get_available_apis()
        
        print("=" * 60)
        print("AVAILABLE APIs")
        print("=" * 60)
        
        for name, available in apis.items():
            status = "✓ Available" if available else "✗ Not configured"
            print(f"{name:20s} {status}")
        
        print("=" * 60)

# Global config instance
config = SecureConfig()

# Usage example
if __name__ == "__main__":
    config.print_available_apis()
```

### 3. API Client Manager

```python
# /opt/trading/api_manager.py

from config_loader import config
import logging

logger = logging.getLogger(__name__)

class APIManager:
    """Centralized API client manager"""
    
    def __init__(self):
        self.clients = {}
        self._initialize_clients()
    
    def _initialize_clients(self):
        """Initialize all available API clients"""
        
        # Polygon.io
        if config.has('polygon_api_key'):
            try:
                from polygon import RESTClient
                self.clients['polygon'] = RESTClient(config.get('polygon_api_key'))
                logger.info("✓ Polygon.io client initialized")
            except Exception as e:
                logger.error(f"✗ Polygon.io init failed: {e}")
        
        # OpenAI
        if config.has('openai_api_key'):
            try:
                from openai import OpenAI
                self.clients['openai'] = OpenAI(
                    api_key=config.get('openai_api_key'),
                    base_url=config.get('openai_api_base')
                )
                logger.info("✓ OpenAI client initialized")
            except Exception as e:
                logger.error(f"✗ OpenAI init failed: {e}")
        
        # Anthropic
        if config.has('anthropic_api_key'):
            try:
                from anthropic import Anthropic
                self.clients['anthropic'] = Anthropic(
                    api_key=config.get('anthropic_api_key')
                )
                logger.info("✓ Anthropic client initialized")
            except Exception as e:
                logger.error(f"✗ Anthropic init failed: {e}")
        
        # Supabase
        if config.has('supabase_url') and config.has('supabase_key'):
            try:
                from supabase import create_client
                self.clients['supabase'] = create_client(
                    config.get('supabase_url'),
                    config.get('supabase_key')
                )
                logger.info("✓ Supabase client initialized")
            except Exception as e:
                logger.error(f"✗ Supabase init failed: {e}")
        
        # CCXT exchanges
        if config.has('binance_api_key'):
            try:
                import ccxt
                self.clients['binance'] = ccxt.binance({
                    'apiKey': config.get('binance_api_key'),
                    'secret': config.get('binance_secret'),
                    'enableRateLimit': True
                })
                logger.info("✓ Binance client initialized")
            except Exception as e:
                logger.error(f"✗ Binance init failed: {e}")
        
        # AWS
        if config.has('aws_access_key_id'):
            try:
                import boto3
                self.clients['aws_s3'] = boto3.client(
                    's3',
                    aws_access_key_id=config.get('aws_access_key_id'),
                    aws_secret_access_key=config.get('aws_secret_access_key'),
                    region_name=config.get('aws_default_region')
                )
                logger.info("✓ AWS S3 client initialized")
            except Exception as e:
                logger.error(f"✗ AWS init failed: {e}")
    
    def get(self, name: str):
        """Get API client by name"""
        return self.clients.get(name)
    
    def has(self, name: str) -> bool:
        """Check if API client is available"""
        return name in self.clients

# Global API manager
api_manager = APIManager()
```

---

## 📝 RECOMMENDED SETUP

### Step 1: Create .env file

```bash
# Create secure .env file
cd /opt/trading
nano .env

# Add your API keys (see template above)
# Save and exit (Ctrl+X, Y, Enter)

# Secure the file
chmod 600 .env
```

### Step 2: Install dependencies

```bash
pip install \
  python-dotenv \
  polygon-api-client \
  openai \
  anthropic \
  supabase \
  ccxt \
  boto3 \
  yfinance \
  alpha_vantage \
  newsapi-python
```

### Step 3: Test configuration

```python
from config_loader import config

# Print available APIs
config.print_available_apis()

# Test specific API
if config.has('polygon_api_key'):
    from polygon import RESTClient
    client = RESTClient(config.get('polygon_api_key'))
    ticker = client.get_last_trade('AAPL')
    print(f"AAPL last trade: ${ticker.price}")
```

---

## 🎯 INTEGRATION WITH TRADING SYSTEM

Update HYBRID_ULTIMATE_SYSTEM.py to use the config:

```python
from config_loader import config
from api_manager import api_manager

class TradingSystem:
    def __init__(self):
        # Load config
        self.config = config
        
        # Initialize API clients
        self.api = api_manager
        
        # Print available APIs
        self.config.print_available_apis()
    
    def get_market_data(self, symbol):
        """Get market data from best available source"""
        
        # Try Polygon.io first (paid, best quality)
        if self.api.has('polygon'):
            try:
                client = self.api.get('polygon')
                ticker = client.get_last_trade(symbol)
                return ticker.price
            except:
                pass
        
        # Fallback to Yahoo Finance (free)
        import yfinance as yf
        ticker = yf.Ticker(symbol)
        return ticker.info.get('regularMarketPrice')
```

---

## ✅ SECURITY BEST PRACTICES

1. **Never commit .env to Git**
   ```bash
   echo ".env" >> .gitignore
   ```

2. **Use environment variables in production**
   ```bash
   export POLYGON_API_KEY="your_key"
   ```

3. **Rotate keys regularly**
   - Change API keys every 90 days
   - Revoke old keys immediately

4. **Use different keys for dev/prod**
   - Development: `.env.dev`
   - Production: `.env.prod`

5. **Monitor API usage**
   - Track costs
   - Set up alerts
   - Monitor for abuse

---

## 🎉 SUMMARY

**You have access to:**
- ✅ 11 paid APIs (Perplexity, Polygon, Gemini, Grok, Flux, Anthropic, Supabase, OpenAI, Cohere, OpenRouter, JSONBin)
- ✅ AWS (S3, EC2, etc.)
- ✅ 10+ free APIs (Yahoo Finance, CoinGecko, exchanges, news, economic data)

**Total value:** $1,000+/month in API access!

**Organized system:**
- ✅ Secure .env configuration
- ✅ Config loader with fallbacks
- ✅ API manager for all clients
- ✅ Integration with trading system
- ✅ Security best practices

**Ready to use in your trading system!**

