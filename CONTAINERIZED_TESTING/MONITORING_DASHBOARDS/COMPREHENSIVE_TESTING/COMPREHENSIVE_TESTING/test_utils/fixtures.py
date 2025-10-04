"""Test fixtures and utilities"""
import pytest
import json
import tempfile
import os
from unittest.mock import Mock, MagicMock
from datetime import datetime, timedelta

@pytest.fixture
def mock_api_response():
    """Mock API response fixture"""
    return {
        "status": "success",
        "data": {"price": 50000, "volume": 1000},
        "timestamp": datetime.now().isoformat()
    }

@pytest.fixture
def mock_trading_config():
    """Mock trading configuration"""
    return {
        "exchanges": ["coinbase", "binance", "okx"],
        "strategies": ["dca", "momentum", "arbitrage"],
        "risk_limits": {"max_position": 0.1, "stop_loss": 0.05},
        "api_keys": {"test_mode": True}
    }

@pytest.fixture
def temp_config_file():
    """Temporary configuration file"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        config = {"test": True, "environment": "testing"}
        json.dump(config, f)
        yield f.name
    os.unlink(f.name)

@pytest.fixture
def mock_openrouter_client():
    """Mock OpenRouter AI client"""
    client = Mock()
    client.query.return_value = {
        "success": True,
        "content": "Test AI response",
        "model": "test-model",
        "tokens": 100
    }
    return client

class TestDataFactory:
    """Factory for generating test data"""
    
    @staticmethod
    def create_market_data(symbol="BTC/USD", price=50000):
        return {
            "symbol": symbol,
            "price": price,
            "volume": 1000,
            "timestamp": datetime.now().isoformat(),
            "bid": price - 10,
            "ask": price + 10
        }
    
    @staticmethod
    def create_trade_order(side="buy", amount=1.0, price=50000):
        return {
            "id": f"order_{int(time.time())}",
            "side": side,
            "amount": amount,
            "price": price,
            "status": "pending",
            "timestamp": datetime.now().isoformat()
        }
