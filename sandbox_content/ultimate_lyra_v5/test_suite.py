#!/usr/bin/env python3
"""
Ultimate Lyra Trading System - Test Suite
=========================================
Runs all test suites for the Ultimate Lyra Trading System.
"""

import unittest
from testing_framework import LyraTestRunner
from test_api_endpoints import TestApiEndpoints
from test_trading_engine import TestTradingEngine
from test_security_monitoring import TestSecurityAndMonitoring

def create_suite():
    """Create a test suite with all test cases."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestApiEndpoints))
    suite.addTest(unittest.makeSuite(TestTradingEngine))
    suite.addTest(unittest.makeSuite(TestSecurityAndMonitoring))
    return suite

if __name__ == '__main__':
    print("🚀 Running Ultimate Lyra Trading System Test Suite...")
    test_suite = create_suite()
    runner = LyraTestRunner(verbosity=2)
    runner.run(test_suite)
    print("\n🎯 Test suite execution completed!")

