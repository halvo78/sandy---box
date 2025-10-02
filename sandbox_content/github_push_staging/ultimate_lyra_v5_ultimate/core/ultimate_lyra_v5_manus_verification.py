#!/usr/bin/env python3
"""
Manus Verification Script
Proves ngrok functionality to Manus sandbox
"""

import requests
import json
import time
import sys

def verify_ngrok_for_manus():
    """Complete verification that Manus can interact with the system"""
    
    print("🤖 Starting Manus Verification...")
    
    # Get tunnel URLs
    try:
        tunnels_resp = requests.get('http://localhost:4040/api/tunnels', timeout=10)
        tunnels = {t['name']: t['public_url'] for t in tunnels_resp.json()['tunnels']}
    except Exception as e:
        print(f"❌ Failed to get tunnel URLs: {e}")
        return False
    
    verification_results = {
        "timestamp": time.time(),
        "tunnels_active": len(tunnels),
        "tunnel_urls": tunnels,
        "tests": {}
    }
    
    print(f"🔗 Found {len(tunnels)} active tunnels")
    
    # Test 1: Health Check
    print("🏥 Testing health endpoints...")
    for name, url in tunnels.items():
        try:
            resp = requests.get(f"{url}/health", timeout=10)
            verification_results["tests"][f"{name}_health"] = {
                "status": resp.status_code,
                "response_time_ms": resp.elapsed.total_seconds() * 1000,
                "success": resp.status_code == 200
            }
            status = "✅" if resp.status_code == 200 else "❌"
            print(f"  {status} {name}: {resp.status_code} ({resp.elapsed.total_seconds()*1000:.0f}ms)")
        except Exception as e:
            verification_results["tests"][f"{name}_health"] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ {name}: {str(e)}")
    
    # Test 2: Command Execution (for ingest tunnel)
    print("⚡ Testing command execution...")
    if 'ingest' in tunnels:
        try:
            test_command = {
                "type": "COMMAND",
                "steps": [{"run": "echo 'Manus verification test successful'"}]
            }
            resp = requests.post(
                f"{tunnels['ingest']}/ingest/event",
                json=test_command,
                headers={"X-Ingest-Token": "lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214"},
                timeout=30
            )
            verification_results["tests"]["command_execution"] = {
                "status": resp.status_code,
                "success": resp.status_code == 200,
                "response": resp.json() if resp.status_code == 200 else None
            }
            status = "✅" if resp.status_code == 200 else "❌"
            print(f"  {status} Command execution: {resp.status_code}")
        except Exception as e:
            verification_results["tests"]["command_execution"] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ Command execution: {str(e)}")
    
    # Test 3: Traffic Inspection
    print("🔍 Testing traffic inspection...")
    try:
        resp = requests.get('http://localhost:4040/api/requests', timeout=10)
        verification_results["tests"]["traffic_inspection"] = {
            "success": resp.status_code == 200,
            "request_count": len(resp.json().get('requests', []))
        }
        status = "✅" if resp.status_code == 200 else "❌"
        print(f"  {status} Traffic inspection: {resp.status_code}")
    except Exception as e:
        verification_results["tests"]["traffic_inspection"] = {
            "success": False,
            "error": str(e)
        }
        print(f"  ❌ Traffic inspection: {str(e)}")
    
    # Generate verification report
    with open('manus_verification_report.json', 'w') as f:
        json.dump(verification_results, f, indent=2)
    
    # Summary
    successful_tests = sum(1 for test in verification_results['tests'].values() if test.get('success', False))
    total_tests = len(verification_results['tests'])
    
    print("\n🤖 Manus Verification Complete!")
    print(f"✅ Active Tunnels: {verification_results['tunnels_active']}")
    print(f"✅ Successful Tests: {successful_tests}/{total_tests}")
    print(f"📊 Report saved: manus_verification_report.json")
    
    if successful_tests == total_tests:
        print("🎉 ALL TESTS PASSED - Ready for Manus integration!")
        return True
    else:
        print("⚠️  Some tests failed - Check logs and retry")
        return False

def print_manus_commands():
    """Print commands for Manus to use"""
    try:
        tunnels_resp = requests.get('http://localhost:4040/api/tunnels', timeout=5)
        tunnels = {t['name']: t['public_url'] for t in tunnels_resp.json()['tunnels']}
        
        if 'ingest' in tunnels:
            ingest_url = tunnels['ingest']
            print(f"\n🤖 Commands for Manus to verify connection:")
            print(f"# Health check")
            print(f'curl -X GET "{ingest_url}/health"')
            print(f"\n# System status")
            print(f'curl -X POST "{ingest_url}/ingest/event" \\')
            print(f'  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \\')
            print(f'  -H "Content-Type: application/json" \\')
            print(f'  -d \'{{"type": "COMMAND", "steps": [{{"run": "ps aux | grep python"}}]}}\'')
            print(f"\n# File listing")
            print(f'curl -X POST "{ingest_url}/ingest/event" \\')
            print(f'  -H "X-Ingest-Token: lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214" \\')
            print(f'  -H "Content-Type: application/json" \\')
            print(f'  -d \'{{"type": "COMMAND", "steps": [{{"run": "ls -la /home/halvolyra/ultimate_lyra_systems/"}}]}}\'')
    except:
        print("❌ Could not generate Manus commands - tunnels not ready")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "commands":
        print_manus_commands()
    else:
        success = verify_ngrok_for_manus()
        if success:
            print_manus_commands()
        sys.exit(0 if success else 1)
