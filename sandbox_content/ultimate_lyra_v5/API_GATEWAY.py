
from flask import Flask, request, jsonify
import requests
import json
from datetime import datetime

class APIGateway:
    def __init__(self):
        self.app = Flask(__name__)
        self.services = {
            "production": "http://localhost:8800",
            "portfolio": "http://localhost:8105",
            "dashboard": "http://localhost:8103",
            "monitoring": "http://localhost:9000"
        }
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/gateway/health')
        def gateway_health():
            return jsonify({
                "gateway_status": "OPERATIONAL",
                "services_available": len(self.services),
                "timestamp": datetime.now().isoformat()
            })
        
        @self.app.route('/gateway/<service>/<path:endpoint>')
        def proxy_request(service, endpoint):
            if service not in self.services:
                return jsonify({"error": "Service not found"}), 404
            
            target_url = f"{self.services[service]}/{endpoint}"
            
            try:
                if request.method == 'GET':
                    response = requests.get(target_url, params=request.args, timeout=10)
                elif request.method == 'POST':
                    response = requests.post(target_url, json=request.json, timeout=10)
                else:
                    return jsonify({"error": "Method not allowed"}), 405
                
                return response.json() if response.headers.get('content-type') == 'application/json' else response.text
            
            except Exception as e:
                return jsonify({"error": str(e)}), 500
    
    def run(self):
        self.app.run(host='0.0.0.0', port=9200, debug=False)

if __name__ == '__main__':
    gateway = APIGateway()
    gateway.run()
