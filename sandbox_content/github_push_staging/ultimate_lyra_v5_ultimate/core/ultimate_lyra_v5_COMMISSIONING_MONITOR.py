
from flask import Flask, jsonify, render_template_string
import psutil
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def commissioning_dashboard():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ultimate Commissioning Monitor</title>
        <meta http-equiv="refresh" content="10">
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #0a0a0a; color: white; }
            .container { max-width: 1600px; margin: 0 auto; }
            .header { text-align: center; margin-bottom: 30px; background: linear-gradient(45deg, #ff6b35, #f7931e); padding: 20px; border-radius: 10px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px; }
            .card { background: #1a1a1a; border-radius: 10px; padding: 20px; border: 2px solid #333; }
            .metric { font-size: 28px; font-weight: bold; color: #00ff88; margin: 10px 0; }
            .status-pass { border-color: #00ff88; }
            .status-fail { border-color: #ff4444; }
            .status-pending { border-color: #ffaa00; }
            .progress-bar { width: 100%; height: 20px; background: #333; border-radius: 10px; overflow: hidden; }
            .progress-fill { height: 100%; background: linear-gradient(90deg, #00ff88, #00cc66); transition: width 0.3s; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎯 Ultimate Commissioning Monitor</h1>
                <p>Real-time Production Commissioning Status</p>
            </div>
            <div class="grid" id="commissioning-grid">
                <!-- Commissioning status will be loaded here -->
            </div>
        </div>
        <script>
            function loadCommissioningStatus() {
                fetch('/api/commissioning/status')
                    .then(response => response.json())
                    .then(data => {
                        const grid = document.getElementById('commissioning-grid');
                        grid.innerHTML = '';
                        
                        // Overall status card
                        const overallCard = document.createElement('div');
                        overallCard.className = `card status-${data.overall_status.toLowerCase()}`;
                        overallCard.innerHTML = `
                            <h3>🏆 OVERALL COMMISSIONING STATUS</h3>
                            <div class="metric">${data.overall_status}</div>
                            <div class="progress-bar">
                                <div class="progress-fill" style="width: ${data.completion_percentage}%"></div>
                            </div>
                            <p>${data.completion_percentage}% Complete</p>
                        `;
                        grid.appendChild(overallCard);
                        
                        // Individual test categories
                        Object.entries(data.test_categories).forEach(([category, status]) => {
                            const card = document.createElement('div');
                            card.className = `card status-${status.status.toLowerCase()}`;
                            card.innerHTML = `
                                <h3>${category.toUpperCase()}</h3>
                                <div class="metric">${status.passed}/${status.total}</div>
                                <div class="progress-bar">
                                    <div class="progress-fill" style="width: ${(status.passed/status.total)*100}%"></div>
                                </div>
                                <p>Status: ${status.status}</p>
                            `;
                            grid.appendChild(card);
                        });
                    });
            }
            
            loadCommissioningStatus();
            setInterval(loadCommissioningStatus, 10000);
        </script>
    </body>
    </html>
    """)

@app.route('/api/commissioning/status')
def commissioning_status():
    # Get commissioning status from database
    try:
        conn = sqlite3.connect('/home/ubuntu/ultimate_lyra_v5/ultimate_commissioning.db')
        cursor = conn.cursor()
        
        # Get test results by category
        cursor.execute("""
            SELECT category, status, COUNT(*) as count 
            FROM commissioning_tests 
            GROUP BY category, status
        """)
        results = cursor.fetchall()
        
        test_categories = {}
        total_tests = 0
        passed_tests = 0
        
        for category, status, count in results:
            if category not in test_categories:
                test_categories[category] = {"total": 0, "passed": 0, "status": "PENDING"}
            
            test_categories[category]["total"] += count
            total_tests += count
            
            if status == "PASSED":
                test_categories[category]["passed"] += count
                passed_tests += count
        
        # Calculate status for each category
        for category in test_categories:
            if test_categories[category]["passed"] == test_categories[category]["total"]:
                test_categories[category]["status"] = "PASS"
            elif test_categories[category]["passed"] > 0:
                test_categories[category]["status"] = "PARTIAL"
            else:
                test_categories[category]["status"] = "PENDING"
        
        completion_percentage = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        overall_status = "PASS" if completion_percentage == 100 else "PARTIAL" if completion_percentage > 0 else "PENDING"
        
        conn.close()
        
        return jsonify({
            "overall_status": overall_status,
            "completion_percentage": round(completion_percentage, 1),
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "test_categories": test_categories,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "overall_status": "ERROR",
            "completion_percentage": 0
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9300, debug=False)
