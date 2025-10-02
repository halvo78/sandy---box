
from flask import Flask, render_template_string, jsonify
import json
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def monitoring_dashboard():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ultimate Monitoring Dashboard</title>
        <meta http-equiv="refresh" content="30">
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #1a1a1a; color: white; }
            .container { max-width: 1400px; margin: 0 auto; }
            .header { text-align: center; margin-bottom: 30px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
            .card { background: #2d2d2d; border-radius: 8px; padding: 20px; border-left: 4px solid #00ff88; }
            .metric { font-size: 24px; font-weight: bold; color: #00ff88; }
            .status-good { border-left-color: #00ff88; }
            .status-warning { border-left-color: #ffaa00; }
            .status-error { border-left-color: #ff4444; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎯 Ultimate Monitoring Dashboard</h1>
                <p>Real-time System Monitoring & Observability</p>
            </div>
            <div class="grid" id="metrics-grid">
                <!-- Metrics will be loaded here -->
            </div>
        </div>
        <script>
            function loadMetrics() {
                fetch('/api/metrics')
                    .then(response => response.json())
                    .then(data => {
                        const grid = document.getElementById('metrics-grid');
                        grid.innerHTML = '';
                        
                        Object.entries(data).forEach(([key, value]) => {
                            const card = document.createElement('div');
                            card.className = 'card status-good';
                            card.innerHTML = `
                                <h3>${key.replace('_', ' ').toUpperCase()}</h3>
                                <div class="metric">${value}</div>
                            `;
                            grid.appendChild(card);
                        });
                    });
            }
            
            loadMetrics();
            setInterval(loadMetrics, 30000);
        </script>
    </body>
    </html>
    """)

@app.route('/api/metrics')
def get_metrics():
    return jsonify({
        "cpu_percent": f"{psutil.cpu_percent(interval=1):.1f}%",
        "memory_percent": f"{psutil.virtual_memory().percent:.1f}%",
        "disk_percent": f"{psutil.disk_usage('/').percent:.1f}%",
        "load_average": f"{os.getloadavg()[0]:.2f}",
        "total_processes": len(list(psutil.process_iter())),
        "python_processes": len([p for p in psutil.process_iter(['name']) if 'python' in p.info['name'].lower()]),
        "uptime_hours": f"{(time.time() - psutil.boot_time()) / 3600:.1f}h",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    import os
    import time
    app.run(host='0.0.0.0', port=9000, debug=False)
