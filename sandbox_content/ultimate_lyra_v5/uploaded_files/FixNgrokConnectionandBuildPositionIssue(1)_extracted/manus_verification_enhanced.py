#!/usr/bin/env python3
"""
Enhanced Manus Verification Script
Proves ngrok functionality to Manus sandbox with Auto Ngrok Manager integration
"""

import requests
import json
import time
import sys
import subprocess
import os
from datetime import datetime
from typing import Dict, List, Optional

class EnhancedManusVerification:
    def __init__(self):
        self.base_url = "https://3ce37fa57d09.ngrok.app"
        self.token = "lyra_1759057116_5d20aef7f3777214"
        self.verification_results = {
            "timestamp": datetime.now().isoformat(),
            "version": "4.0.0-enhanced",
            "auto_manager_status": None,
            "tunnels": {},
            "tests": {},
            "manus_commands": [],
            "system_health": {}
        }
    
    def check_auto_manager_status(self) -> Dict:
        """Check if Auto Ngrok Manager is running"""
        try:
            # Check if service is running
            result = subprocess.run(
                ["systemctl", "is-active", "auto-ngrok-manager"],
                capture_output=True,
                text=True
            )
            service_active = result.stdout.strip() == "active"
            
            # Check process
            result = subprocess.run(
                ["pgrep", "-f", "auto_ngrok_manager"],
                capture_output=True,
                text=True
            )
            process_running = bool(result.stdout.strip())
            
            status = {
                "service_active": service_active,
                "process_running": process_running,
                "status": "healthy" if service_active and process_running else "unhealthy"
            }
            
            self.verification_results["auto_manager_status"] = status
            return status
            
        except Exception as e:
            status = {"error": str(e), "status": "unknown"}
            self.verification_results["auto_manager_status"] = status
            return status
    
    def get_tunnel_info(self) -> Dict:
        """Get comprehensive tunnel information"""
        try:
            # Try local ngrok API first
            try:
                resp = requests.get('http://localhost:4040/api/tunnels', timeout=5)
                local_tunnels = {t['name']: t['public_url'] for t in resp.json()['tunnels']}
            except:
                local_tunnels = {}
            
            # Test the known tunnel
            tunnel_info = {
                "local_api_tunnels": local_tunnels,
                "known_tunnel": self.base_url,
                "tunnel_count": len(local_tunnels)
            }
            
            self.verification_results["tunnels"] = tunnel_info
            return tunnel_info
            
        except Exception as e:
            tunnel_info = {"error": str(e)}
            self.verification_results["tunnels"] = tunnel_info
            return tunnel_info
    
    def test_health_endpoint(self) -> Dict:
        """Test the health endpoint"""
        print("🏥 Testing health endpoint...")
        try:
            start_time = time.time()
            resp = requests.get(f"{self.base_url}/health", timeout=10)
            response_time = (time.time() - start_time) * 1000
            
            result = {
                "status_code": resp.status_code,
                "response_time_ms": round(response_time, 2),
                "success": resp.status_code == 200,
                "response_body": resp.text[:200] if resp.text else None
            }
            
            status = "✅" if result["success"] else "❌"
            print(f"  {status} Health check: {resp.status_code} ({response_time:.0f}ms)")
            
        except Exception as e:
            result = {"success": False, "error": str(e)}
            print(f"  ❌ Health check failed: {str(e)}")
        
        self.verification_results["tests"]["health_endpoint"] = result
        return result
    
    def test_command_execution(self) -> Dict:
        """Test command execution capability"""
        print("⚡ Testing command execution...")
        try:
            test_commands = [
                {"run": "echo 'Manus verification test successful'"},
                {"run": "date"},
                {"run": "whoami"},
                {"run": "pwd"},
                {"run": "ls -la /home/halvolyra/ultimate_lyra_systems/ | head -5"}
            ]
            
            results = []
            for i, cmd in enumerate(test_commands):
                try:
                    payload = {"type": "COMMAND", "steps": [cmd]}
                    resp = requests.post(
                        f"{self.base_url}/ingest/event",
                        json=payload,
                        headers={
                            "X-Ingest-Token": self.token,
                            "Content-Type": "application/json"
                        },
                        timeout=30
                    )
                    
                    cmd_result = {
                        "command": cmd["run"],
                        "status_code": resp.status_code,
                        "success": resp.status_code == 200,
                        "response": resp.json() if resp.status_code == 200 else None
                    }
                    results.append(cmd_result)
                    
                    status = "✅" if cmd_result["success"] else "❌"
                    print(f"  {status} Command {i+1}: {cmd['run'][:30]}...")
                    
                except Exception as e:
                    cmd_result = {"command": cmd["run"], "success": False, "error": str(e)}
                    results.append(cmd_result)
                    print(f"  ❌ Command {i+1} failed: {str(e)}")
            
            overall_result = {
                "total_commands": len(test_commands),
                "successful_commands": sum(1 for r in results if r.get("success", False)),
                "commands": results,
                "success": all(r.get("success", False) for r in results)
            }
            
        except Exception as e:
            overall_result = {"success": False, "error": str(e)}
            print(f"  ❌ Command execution test failed: {str(e)}")
        
        self.verification_results["tests"]["command_execution"] = overall_result
        return overall_result
    
    def test_system_integration(self) -> Dict:
        """Test integration with the local system"""
        print("🔗 Testing system integration...")
        try:
            integration_tests = [
                {
                    "name": "auto_manager_check",
                    "command": "systemctl status auto-ngrok-manager --no-pager -l"
                },
                {
                    "name": "process_list",
                    "command": "ps aux | grep -E '(ngrok|ingest|python)' | grep -v grep"
                },
                {
                    "name": "port_status",
                    "command": "netstat -tlnp | grep :8081"
                },
                {
                    "name": "system_resources",
                    "command": "free -h && df -h /"
                }
            ]
            
            results = []
            for test in integration_tests:
                try:
                    payload = {
                        "type": "COMMAND",
                        "steps": [{"run": test["command"]}]
                    }
                    resp = requests.post(
                        f"{self.base_url}/ingest/event",
                        json=payload,
                        headers={
                            "X-Ingest-Token": self.token,
                            "Content-Type": "application/json"
                        },
                        timeout=30
                    )
                    
                    test_result = {
                        "name": test["name"],
                        "success": resp.status_code == 200,
                        "response": resp.json() if resp.status_code == 200 else None
                    }
                    results.append(test_result)
                    
                    status = "✅" if test_result["success"] else "❌"
                    print(f"  {status} {test['name']}")
                    
                except Exception as e:
                    test_result = {"name": test["name"], "success": False, "error": str(e)}
                    results.append(test_result)
                    print(f"  ❌ {test['name']}: {str(e)}")
            
            overall_result = {
                "total_tests": len(integration_tests),
                "successful_tests": sum(1 for r in results if r.get("success", False)),
                "tests": results,
                "success": all(r.get("success", False) for r in results)
            }
            
        except Exception as e:
            overall_result = {"success": False, "error": str(e)}
            print(f"  ❌ System integration test failed: {str(e)}")
        
        self.verification_results["tests"]["system_integration"] = overall_result
        return overall_result
    
    def generate_manus_commands(self) -> List[str]:
        """Generate commands for Manus to use"""
        commands = [
            f'# Health check',
            f'curl -X GET "{self.base_url}/health"',
            f'',
            f'# System status check',
            f'curl -X POST "{self.base_url}/ingest/event" \\',
            f'  -H "X-Ingest-Token: {self.token}" \\',
            f'  -H "Content-Type: application/json" \\',
            f'  -d \'{{"type": "COMMAND", "steps": [{{"run": "systemctl status auto-ngrok-manager --no-pager"}}]}}\'',
            f'',
            f'# File system check',
            f'curl -X POST "{self.base_url}/ingest/event" \\',
            f'  -H "X-Ingest-Token: {self.token}" \\',
            f'  -H "Content-Type: application/json" \\',
            f'  -d \'{{"type": "COMMAND", "steps": [{{"run": "ls -la /home/halvolyra/ultimate_lyra_systems/"}}]}}\'',
            f'',
            f'# Process monitoring',
            f'curl -X POST "{self.base_url}/ingest/event" \\',
            f'  -H "X-Ingest-Token: {self.token}" \\',
            f'  -H "Content-Type: application/json" \\',
            f'  -d \'{{"type": "COMMAND", "steps": [{{"run": "ps aux | grep python"}}]}}\'',
            f'',
            f'# Auto manager logs',
            f'curl -X POST "{self.base_url}/ingest/event" \\',
            f'  -H "X-Ingest-Token: {self.token}" \\',
            f'  -H "Content-Type: application/json" \\',
            f'  -d \'{{"type": "COMMAND", "steps": [{{"run": "journalctl -u auto-ngrok-manager -n 10 --no-pager"}}]}}\'',
        ]
        
        self.verification_results["manus_commands"] = commands
        return commands
    
    def run_full_verification(self) -> bool:
        """Run complete verification suite"""
        print("🤖 Starting Enhanced Manus Verification...")
        print("=" * 60)
        
        # Check Auto Ngrok Manager
        print("🔧 Checking Auto Ngrok Manager...")
        auto_status = self.check_auto_manager_status()
        print(f"  Status: {auto_status.get('status', 'unknown')}")
        
        # Get tunnel information
        print("🔗 Getting tunnel information...")
        tunnel_info = self.get_tunnel_info()
        print(f"  Active tunnels: {tunnel_info.get('tunnel_count', 0)}")
        
        # Run tests
        health_result = self.test_health_endpoint()
        command_result = self.test_command_execution()
        integration_result = self.test_system_integration()
        
        # Generate commands
        manus_commands = self.generate_manus_commands()
        
        # Calculate overall success
        test_results = [
            health_result.get("success", False),
            command_result.get("success", False),
            integration_result.get("success", False)
        ]
        
        overall_success = all(test_results)
        successful_tests = sum(test_results)
        total_tests = len(test_results)
        
        # Save detailed report
        with open('enhanced_manus_verification_report.json', 'w') as f:
            json.dump(self.verification_results, f, indent=2)
        
        # Print summary
        print("\n" + "=" * 60)
        print("🤖 Enhanced Manus Verification Complete!")
        print(f"✅ Auto Manager Status: {auto_status.get('status', 'unknown')}")
        print(f"✅ Active Tunnels: {tunnel_info.get('tunnel_count', 0)}")
        print(f"✅ Successful Tests: {successful_tests}/{total_tests}")
        print(f"📊 Detailed Report: enhanced_manus_verification_report.json")
        
        if overall_success:
            print("🎉 ALL TESTS PASSED - Ready for Manus integration!")
            print("\n🤖 Commands for Manus to verify connection:")
            print("-" * 50)
            for cmd in manus_commands:
                print(cmd)
        else:
            print("⚠️  Some tests failed - Check logs and retry")
        
        return overall_success

def main():
    """Main entry point"""
    verifier = EnhancedManusVerification()
    
    if len(sys.argv) > 1 and sys.argv[1] == "commands":
        commands = verifier.generate_manus_commands()
        print("🤖 Commands for Manus to verify connection:")
        print("-" * 50)
        for cmd in commands:
            print(cmd)
    else:
        success = verifier.run_full_verification()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
