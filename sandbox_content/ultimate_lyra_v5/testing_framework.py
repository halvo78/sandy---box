#!/usr/bin/env python3
"""
Ultimate Lyra Trading System - Testing Framework
===============================================
Provides a comprehensive framework for testing all system components.
"""

import unittest
import asyncio
import json
import time
from datetime import datetime
from typing import Dict, Any, List

class LyraTestResult(unittest.TextTestResult):
    """Custom test result class to collect detailed test information."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_results.append({
            'test': self._get_test_name(test),
            'status': 'SUCCESS',
            'duration': self._get_duration(test)
        })

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_results.append({
            'test': self._get_test_name(test),
            'status': 'FAILURE',
            'duration': self._get_duration(test),
            'error': self._exc_info_to_string(err, test)
        })

    def addError(self, test, err):
        super().addError(test, err)
        self.test_results.append({
            'test': self._get_test_name(test),
            'status': 'ERROR',
            'duration': self._get_duration(test),
            'error': self._exc_info_to_string(err, test)
        })

    def _get_test_name(self, test):
        return test.id()

    def _get_duration(self, test):
        if hasattr(test, '_start_time'):
            return time.time() - test._start_time
        return 0

class LyraTestCase(unittest.TestCase):
    """Base class for all Lyra test cases."""
    def setUp(self):
        self._start_time = time.time()

    def tearDown(self):
        pass

    def run_async(self, coro):
        """Run an async test case."""
        return asyncio.run(coro)

class LyraTestRunner(unittest.TextTestRunner):
    """Custom test runner to use the custom result class."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, resultclass=LyraTestResult, **kwargs)

    def run(self, test):
        result = super().run(test)
        self.generate_report(result.test_results)
        return result

    def generate_report(self, test_results: List[Dict[str, Any]]) -> None:
        """Generate a JSON report of the test results."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_tests': len(test_results),
                'success': sum(1 for r in test_results if r['status'] == 'SUCCESS'),
                'failures': sum(1 for r in test_results if r['status'] == 'FAILURE'),
                'errors': sum(1 for r in test_results if r['status'] == 'ERROR'),
            },
            'results': test_results
        }

        with open('/home/ubuntu/ultimate_lyra_v5/test_report.json', 'w') as f:
            json.dump(report, f, indent=2)

        print("\n📋 Test report generated at: /home/ubuntu/ultimate_lyra_v5/test_report.json")

if __name__ == '__main__':
    print("This is the testing framework and not meant to be run directly.")
    print("Use test_suite.py to run the tests.")

