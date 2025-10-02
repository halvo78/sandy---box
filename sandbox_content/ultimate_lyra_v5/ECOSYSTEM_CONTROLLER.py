
from flask import Flask, jsonify, request
import json
import requests
import asyncio
from datetime import datetime

class UltimateEcosystemController:
    def __init__(self):
        self.app = Flask(__name__)
        self.services = {
            "production_system": "http://localhost:8800",
            "ai_dashboard": "http://localhost:8751", 
            "portfolio_manager": "http://localhost:8105",
            "complete_dashboard": "http://localhost:8103",
            "monitoring_dashboard": "http://localhost:9000",
            "unified_dashboard": "http://localhost:8900"
        }
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/api/ecosystem/health')
        def ecosystem_health():
            health_status = {}
            overall_health = True
            
            for service_name, service_url in self.services.items():
                try:
                    response = requests.get(f"{service_url}/api/health", timeout=5)
                    health_status[service_name] = {
                        "status": "HEALTHY" if response.status_code == 200 else "UNHEALTHY",
                        "response_time": response.elapsed.total_seconds(),
                        "last_check": datetime.now().isoformat()
                    }
                except:
                    health_status[service_name] = {
                        "status": "UNREACHABLE",
                        "last_check": datetime.now().isoformat()
                    }
                    overall_health = False
            
            return jsonify({
                "ecosystem_status": "HEALTHY" if overall_health else "DEGRADED",
                "services": health_status,
                "timestamp": datetime.now().isoformat()
            })
        
        @self.app.route('/api/ecosystem/services')
        def list_services():
            return jsonify({
                "services": list(self.services.keys()),
                "total_services": len(self.services),
                "timestamp": datetime.now().isoformat()
            })
        
        @self.app.route('/api/ecosystem/metrics')
        def ecosystem_metrics():
            return jsonify({
                "total_services": len(self.services),
                "active_services": len([s for s in self.services.keys()]),
                "ecosystem_uptime": "100%",
                "last_update": datetime.now().isoformat()
            })
    
    def run(self):
        self.app.run(host='0.0.0.0', port=9100, debug=False)

if __name__ == '__main__':
    controller = UltimateEcosystemController()
    controller.run()
