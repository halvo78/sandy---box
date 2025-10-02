"""
Ultimate Lyra Trading System - API Endpoint Tests
=================================================
Tests for all API endpoints to ensure they are functioning correctly.
"""

import unittest
import asyncio
import aiohttp
from testing_framework import LyraTestCase

class TestApiEndpoints(LyraTestCase):
    """Test suite for API endpoints."""

    def test_health_check_endpoint(self):
        """Test the health check endpoint of the AI Enhanced Dashboard."""
        async def test_logic():
            async with aiohttp.ClientSession() as session:
                async with session.get('http://localhost:8751/health') as response:
                    self.assertEqual(response.status, 200)
                    data = await response.json()
                    self.assertEqual(data["status"], "healthy")
        self.run_async(test_logic())

    def test_api_data_endpoint(self):
        """Test the API data endpoint of the AI Enhanced Dashboard."""
        async def test_logic():
            async with aiohttp.ClientSession() as session:
                async with session.get('http://localhost:8751/api/data') as response:
                    self.assertEqual(response.status, 200)
                    data = await response.json()
                    self.assertIn('ai_consensus', data)
                    self.assertIn('portfolio', data)
                    self.assertIn('exchanges', data)
        self.run_async(test_logic())

    def test_trading_engine_health_check(self):
        """Test the health check endpoint of the trading engine."""
        async def test_logic():
            async with aiohttp.ClientSession() as session:
                async with session.get('http://localhost:3100/health') as response:
                    self.assertEqual(response.status, 200)
                    text = await response.text()
                    self.assertEqual(text, 'healthy\n')
        self.run_async(test_logic())

if __name__ == '__main__':
    unittest.main()
