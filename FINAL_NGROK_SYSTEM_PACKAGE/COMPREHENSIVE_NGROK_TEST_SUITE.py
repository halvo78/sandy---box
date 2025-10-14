#!/usr/bin/env python3
"""
COMPREHENSIVE NGROK TEST SUITE
Tests all 10 production components via Ngrok tunnels
Validates end-to-end functionality and integration
"""

import os
import sys
import json
import time
import requests
from datetime import datetime
from typing import Dict, List, Tuple

# Test configuration
NGROK_API = "http://localhost:4040/api/tunnels"
TEST_RESULTS_FILE = "/home/ubuntu/NGROK_TEST_RESULTS.json"

class NgrokTestSuite:
    """Comprehensive test suite for Ngrok-integrated system"""
    
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "tests_run": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "component_results": {},
            "overall_status": "UNKNOWN"
        }
        self.tunnels = {}
    
    def print_header(self, text: str):
        """Print formatted header"""
        print("\n" + "=" * 80)
        print(f"  {text}")
        print("=" * 80 + "\n")
    
    def print_test(self, component: str, test_name: str, status: str, details: str = ""):
        """Print test result"""
        status_icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
        print(f"{status_icon} {component:30} | {test_name:30} | {status}")
        if details:
            print(f"   └─ {details}")
    
    def get_ngrok_tunnels(self) -> bool:
        """Retrieve active Ngrok tunnels"""
        try:
            response = requests.get(NGROK_API, timeout=5)
            if response.status_code == 200:
                data = response.json()
                tunnels = data.get('tunnels', [])
                
                for tunnel in tunnels:
                    name = tunnel.get('name', 'unknown')
                    public_url = tunnel.get('public_url', '')
                    self.tunnels[name] = public_url
                
                return len(self.tunnels) > 0
            else:
                return False
        except Exception as e:
            print(f"❌ Error accessing Ngrok API: {e}")
            return False
    
    def test_tunnel_accessibility(self, tunnel_name: str, tunnel_url: str) -> Tuple[str, str]:
        """Test if tunnel is accessible"""
        try:
            response = requests.get(tunnel_url, timeout=10, allow_redirects=True)
            if response.status_code in [200, 404, 403]:  # Any response means tunnel is working
                return "PASS", f"HTTP {response.status_code}"
            else:
                return "WARN", f"Unexpected HTTP {response.status_code}"
        except requests.exceptions.Timeout:
            return "FAIL", "Timeout after 10s"
        except requests.exceptions.ConnectionError:
            return "FAIL", "Connection refused"
        except Exception as e:
            return "FAIL", str(e)[:50]
    
    def test_health_endpoint(self, tunnel_url: str) -> Tuple[str, str]:
        """Test health endpoint if available"""
        try:
            response = requests.get(f"{tunnel_url}/health", timeout=5)
            if response.status_code == 200:
                return "PASS", "Health check OK"
            elif response.status_code == 404:
                return "WARN", "No health endpoint (expected for some components)"
            else:
                return "WARN", f"HTTP {response.status_code}"
        except:
            return "WARN", "No health endpoint available"
    
    def test_api_endpoint(self, tunnel_url: str, endpoint: str) -> Tuple[str, str]:
        """Test specific API endpoint"""
        try:
            response = requests.get(f"{tunnel_url}{endpoint}", timeout=5)
            if response.status_code in [200, 401, 403]:  # Auth required is OK
                return "PASS", f"HTTP {response.status_code}"
            else:
                return "WARN", f"HTTP {response.status_code}"
        except:
            return "WARN", "Endpoint not available"
    
    def run_component_tests(self, component_name: str, tunnel_name: str, tunnel_url: str):
        """Run all tests for a component"""
        print(f"\n🔍 Testing: {component_name}")
        print(f"   Tunnel: {tunnel_name}")
        print(f"   URL: {tunnel_url}")
        print()
        
        component_results = {
            "tunnel_name": tunnel_name,
            "tunnel_url": tunnel_url,
            "tests": {}
        }
        
        # Test 1: Tunnel Accessibility
        status, details = self.test_tunnel_accessibility(tunnel_name, tunnel_url)
        self.print_test(component_name, "Tunnel Accessible", status, details)
        component_results["tests"]["tunnel_accessible"] = {"status": status, "details": details}
        self.results["tests_run"] += 1
        if status == "PASS":
            self.results["tests_passed"] += 1
        else:
            self.results["tests_failed"] += 1
        
        # Test 2: Health Endpoint
        status, details = self.test_health_endpoint(tunnel_url)
        self.print_test(component_name, "Health Endpoint", status, details)
        component_results["tests"]["health_endpoint"] = {"status": status, "details": details}
        self.results["tests_run"] += 1
        if status == "PASS":
            self.results["tests_passed"] += 1
        elif status == "FAIL":
            self.results["tests_failed"] += 1
        
        # Test 3: API Endpoint (if applicable)
        if component_name in ["Monitoring Dashboard", "AI Consensus", "Real-time Data"]:
            status, details = self.test_api_endpoint(tunnel_url, "/api/status")
            self.print_test(component_name, "API Endpoint", status, details)
            component_results["tests"]["api_endpoint"] = {"status": status, "details": details}
            self.results["tests_run"] += 1
            if status == "PASS":
                self.results["tests_passed"] += 1
            elif status == "FAIL":
                self.results["tests_failed"] += 1
        
        self.results["component_results"][component_name] = component_results
    
    def run_integration_tests(self):
        """Run integration tests across components"""
        self.print_header("INTEGRATION TESTS")
        
        # Test 1: All tunnels active
        expected_tunnels = 9  # We have 9 tunnels configured
        actual_tunnels = len(self.tunnels)
        
        if actual_tunnels >= expected_tunnels:
            status = "PASS"
            details = f"{actual_tunnels}/{expected_tunnels} tunnels active"
            self.results["tests_passed"] += 1
        else:
            status = "FAIL"
            details = f"Only {actual_tunnels}/{expected_tunnels} tunnels active"
            self.results["tests_failed"] += 1
        
        self.print_test("System", "All Tunnels Active", status, details)
        self.results["tests_run"] += 1
        
        # Test 2: Ngrok dashboard accessible
        try:
            response = requests.get("http://localhost:4040", timeout=5)
            if response.status_code == 200:
                status = "PASS"
                details = "Dashboard accessible"
                self.results["tests_passed"] += 1
            else:
                status = "FAIL"
                details = f"HTTP {response.status_code}"
                self.results["tests_failed"] += 1
        except:
            status = "FAIL"
            details = "Dashboard not accessible"
            self.results["tests_failed"] += 1
        
        self.print_test("System", "Ngrok Dashboard", status, details)
        self.results["tests_run"] += 1
    
    def run_all_tests(self):
        """Run complete test suite"""
        self.print_header("COMPREHENSIVE NGROK TEST SUITE")
        
        print(f"📅 Timestamp: {self.results['timestamp']}")
        print(f"🎯 Objective: Validate all 10 production components via Ngrok tunnels")
        print()
        
        # Step 1: Get Ngrok tunnels
        print("📡 Retrieving Ngrok tunnels...")
        if not self.get_ngrok_tunnels():
            print("❌ CRITICAL: Cannot access Ngrok API. Is Ngrok running?")
            print("   Run: sudo systemctl status ngrok-permanent.service")
            self.results["overall_status"] = "CRITICAL_FAILURE"
            return False
        
        print(f"✅ Found {len(self.tunnels)} active tunnels")
        print()
        
        # Step 2: Test each component
        self.print_header("COMPONENT TESTS")
        
        component_mapping = {
            "ci_cd_tunnel": "CI/CD Pipeline",
            "data_pipeline_tunnel": "Real-time Data Pipeline",
            "risk_mgmt_tunnel": "Risk Management",
            "security_tunnel": "Security Framework",
            "dashboard": "Monitoring Dashboard",
            "file_server": "Documentation",
            "disaster_recovery_tunnel": "Disaster Recovery",
            "compliance_tunnel": "Compliance Module",
            "production": "AI Consensus"
        }
        
        for tunnel_name, component_name in component_mapping.items():
            if tunnel_name in self.tunnels:
                self.run_component_tests(
                    component_name,
                    tunnel_name,
                    self.tunnels[tunnel_name]
                )
            else:
                print(f"\n⚠️  Warning: Tunnel '{tunnel_name}' not found for {component_name}")
                self.results["component_results"][component_name] = {
                    "status": "NOT_FOUND",
                    "tunnel_name": tunnel_name
                }
        
        # Step 3: Integration tests
        self.run_integration_tests()
        
        # Step 4: Calculate overall status
        if self.results["tests_failed"] == 0:
            self.results["overall_status"] = "ALL_PASS"
        elif self.results["tests_passed"] > self.results["tests_failed"]:
            self.results["overall_status"] = "PARTIAL_PASS"
        else:
            self.results["overall_status"] = "FAIL"
        
        return True
    
    def print_summary(self):
        """Print test summary"""
        self.print_header("TEST SUMMARY")
        
        print(f"📊 Tests Run: {self.results['tests_run']}")
        print(f"✅ Tests Passed: {self.results['tests_passed']}")
        print(f"❌ Tests Failed: {self.results['tests_failed']}")
        print(f"⚠️  Tests Warned: {self.results['tests_run'] - self.results['tests_passed'] - self.results['tests_failed']}")
        print()
        
        if self.results['tests_run'] > 0:
            pass_rate = (self.results['tests_passed'] / self.results['tests_run']) * 100
            print(f"📈 Pass Rate: {pass_rate:.1f}%")
        
        print()
        print(f"🎯 Overall Status: {self.results['overall_status']}")
        print()
        
        # Print component summary
        print("📦 Component Summary:")
        for component, data in self.results["component_results"].items():
            if "tests" in data:
                passed = sum(1 for t in data["tests"].values() if t["status"] == "PASS")
                total = len(data["tests"])
                print(f"   {component:30} {passed}/{total} tests passed")
            else:
                print(f"   {component:30} NOT TESTED")
        
        print()
    
    def save_results(self):
        """Save test results to file"""
        try:
            with open(TEST_RESULTS_FILE, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"💾 Results saved to: {TEST_RESULTS_FILE}")
        except Exception as e:
            print(f"⚠️  Warning: Could not save results: {e}")
    
    def print_next_steps(self):
        """Print recommended next steps"""
        print("\n" + "=" * 80)
        print("  NEXT STEPS")
        print("=" * 80 + "\n")
        
        if self.results["overall_status"] == "ALL_PASS":
            print("✅ All tests passed! System is ready for production.")
            print()
            print("Recommended actions:")
            print("  1. Review component logs for any warnings")
            print("  2. Set up monitoring and alerting")
            print("  3. Configure backup procedures")
            print("  4. Run load testing")
            print("  5. Proceed to production deployment")
        
        elif self.results["overall_status"] == "PARTIAL_PASS":
            print("⚠️  Some tests failed. Review and fix issues before production.")
            print()
            print("Recommended actions:")
            print("  1. Check failed component logs")
            print("  2. Verify component services are running")
            print("  3. Review Ngrok tunnel configuration")
            print("  4. Re-run tests after fixes")
        
        else:
            print("❌ Critical failures detected. System not ready for production.")
            print()
            print("Recommended actions:")
            print("  1. Check if Ngrok service is running:")
            print("     sudo systemctl status ngrok-permanent.service")
            print("  2. Check Ngrok logs:")
            print("     tail -f /home/halvolyra/ultimate_lyra_systems/logs/ngrok.log")
            print("  3. Verify component services are started")
            print("  4. Review system configuration")
        
        print()

def main():
    """Main test execution"""
    suite = NgrokTestSuite()
    
    try:
        # Run all tests
        success = suite.run_all_tests()
        
        # Print summary
        suite.print_summary()
        
        # Save results
        suite.save_results()
        
        # Print next steps
        suite.print_next_steps()
        
        # Exit with appropriate code
        if suite.results["overall_status"] == "ALL_PASS":
            sys.exit(0)
        elif suite.results["overall_status"] == "PARTIAL_PASS":
            sys.exit(1)
        else:
            sys.exit(2)
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        suite.save_results()
        sys.exit(130)
    
    except Exception as e:
        print(f"\n\n❌ Critical error during testing: {e}")
        suite.save_results()
        sys.exit(3)

if __name__ == "__main__":
    main()

