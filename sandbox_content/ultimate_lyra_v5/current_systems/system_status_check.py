#!/usr/bin/env python3
"""
Ultimate System Status Check
Comprehensive health check for all deployed services
"""

import requests
import json
from datetime import datetime

def check_service(name, url, expected_keys=None):
    """Check if a service is responding correctly"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json() if 'application/json' in response.headers.get('content-type', '') else {}
            status = "✅ OPERATIONAL"
            details = data
        else:
            status = f"⚠️ HTTP {response.status_code}"
            details = {"error": f"HTTP {response.status_code}"}
    except requests.exceptions.RequestException as e:
        status = "❌ OFFLINE"
        details = {"error": str(e)}
    
    return {
        "service": name,
        "url": url,
        "status": status,
        "details": details,
        "timestamp": datetime.now().isoformat()
    }

def main():
    print("🎯 ULTIMATE LYRA SYSTEM STATUS CHECK")
    print("=" * 60)
    
    services = [
        ("Production Dashboard", "http://localhost:8080/health"),
        ("OKX Exchange Service", "http://localhost:8082/health"),
        ("AI Orchestrator", "http://localhost:8090/health"),
        ("AI Portfolio Manager", "http://localhost:8100/"),
    ]
    
    results = []
    for name, url in services:
        result = check_service(name, url)
        results.append(result)
        print(f"{result['status']} {name}")
        if result['details']:
            print(f"   URL: {url}")
            if 'error' not in result['details']:
                for key, value in result['details'].items():
                    if key != 'timestamp':
                        print(f"   {key}: {value}")
        print()
    
    # Summary
    operational = sum(1 for r in results if "✅" in r['status'])
    total = len(results)
    
    print("📊 SYSTEM SUMMARY")
    print(f"   Services Operational: {operational}/{total}")
    print(f"   System Health: {'🟢 EXCELLENT' if operational == total else '🟡 PARTIAL' if operational > 0 else '🔴 CRITICAL'}")
    print(f"   Timestamp: {datetime.now().isoformat()}")
    
    # Save results
    with open('/home/ubuntu/ultimate_lyra_systems/logs/system_status.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
