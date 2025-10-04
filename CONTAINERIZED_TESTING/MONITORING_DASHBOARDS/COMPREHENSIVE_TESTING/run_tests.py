#!/usr/bin/env python3
"""
MASTER TEST RUNNER
Comprehensive testing orchestration for Ultimate Lyra Trading System
"""

import os
import logging
import sys
import subprocess
import json
import time
from datetime import datetime
import argparse

class MasterTestRunner:
    def __init__(self):
        """TODO: Add function documentation"""
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.results = {
            "test_session": f"session_{int(time.time())}",
            "start_time": datetime.now().isoformat(),
            "test_categories": {},
            "overall_status": "RUNNING",
            "summary": {}
        }
    
    def run_test_category(self, category):
        """Run tests for a specific category"""
        logging.info(f"🧪 Running {category} tests...")
        
        category_dir = os.path.join(self.test_dir, category)
        if not os.path.exists(category_dir):
            logging.info(f"⚠️  Category {category} not found")
            return False
        
        try:
            # Run pytest for the category
            cmd = [
                sys.executable, "-m", "pytest", 
                category_dir,
                "-v",
                "--tb=short"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.test_dir)
            
            self.results["test_categories"][category] = {
                "status": "PASSED" if result.returncode == 0 else "FAILED",
                "return_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
            
            if result.returncode == 0:
                logging.info(f"✅ {category} tests PASSED")
            else:
                logging.info(f"❌ {category} tests FAILED")
                if result.stderr:
                    logging.info(f"Error: {result.stderr}")
            
            return result.returncode == 0
            
        except Exception as e:
            logging.info(f"❌ Error running {category} tests: {e}")
            self.results["test_categories"][category] = {
                "status": "ERROR",
                "error": str(e)
            }
            return False
    
    def run_all_tests(self):
        """Run all test categories"""
        logging.info("🚀 STARTING COMPREHENSIVE TEST SUITE")
        logging.info("=" * 60)
        
        categories = [
            "unit_tests",
            "integration_tests",
            "security_tests", 
            "performance_tests",
            "container_tests",
            "api_tests",
            "ai_consensus_tests",
            "trading_engine_tests",
            "ecosystem_tests"
        ]
        
        passed_categories = 0
        total_categories = len(categories)
        
        for category in categories:
            if self.run_test_category(category):
                passed_categories += 1
        
        # Generate summary
        self.results["end_time"] = datetime.now().isoformat()
        self.results["overall_status"] = "PASSED" if passed_categories == total_categories else "FAILED"
        self.results["summary"] = {
            "total_categories": total_categories,
            "passed_categories": passed_categories,
            "failed_categories": total_categories - passed_categories,
            "success_rate": (passed_categories / total_categories) * 100
        }
        
        # Save results
        with open("comprehensive_test_results.json", "w") as f:
            json.dump(self.results, f, indent=2)
        
        logging.info("\n" + "=" * 60)
        logging.info("🎉 COMPREHENSIVE TESTING COMPLETE")
        logging.info("=" * 60)
        logging.info(f"📊 Categories Passed: {passed_categories}/{total_categories}")
        logging.info(f"📈 Success Rate: {self.results['summary']['success_rate']:.1f}%")
        logging.info(f"📋 Results saved to: comprehensive_test_results.json")
        
        return self.results["overall_status"] == "PASSED"
    
    def run_quick_tests(self):
        """Run quick smoke tests"""
        logging.info("⚡ RUNNING QUICK SMOKE TESTS")
        
        # Run only fast tests
        cmd = [
            sys.executable, "-m", "pytest",
            "-m", "not slow",
            "-v",
            "--tb=short"
        ]
        
        result = subprocess.run(cmd, cwd=self.test_dir)
        return result.returncode == 0

def main():
    """TODO: Add function documentation"""
    parser = argparse.ArgumentParser(description="Ultimate Lyra Trading System Test Runner")
    parser.add_argument("--category", help="Run specific test category")
    parser.add_argument("--quick", action="store_true", help="Run quick smoke tests only")
    parser.add_argument("--all", action="store_true", help="Run all comprehensive tests")
    
    args = parser.parse_args()
    
    runner = MasterTestRunner()
    
    if args.quick:
        success = runner.run_quick_tests()
    elif args.category:
        success = runner.run_test_category(args.category)
    else:
        success = runner.run_all_tests()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
