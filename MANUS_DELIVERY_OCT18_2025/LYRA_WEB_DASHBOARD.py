#!/usr/bin/env python3
"""
🎛️ LYRA WEB DASHBOARD
Complete control dashboard with real-time data visualization

Features:
- Real-time market data display
- AI consensus visualization
- Position management
- Trade history
- Performance metrics
- System status
- Control panel
"""

from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime
import logging

app = Flask(__name__)
logger = logging.getLogger('LyraDashboard')


class DashboardData:
    """Manages dashboard data"""
    
    def __init__(self):
        self.system_status = {
            "running": True,
            "capital": 1000000,
            "positions": 0,
            "trades_today": 0,
            "win_rate": 0.0,
            "total_profit": 0.0
        }
        
        self.market_data = {}
        self.ai_consensus = {}
        self.positions = []
        self.trade_history = []
    
    def update_system_status(self, data: dict):
        """Update system status"""
        self.system_status.update(data)
    
    def update_market_data(self, symbol: str, data: dict):
        """Update market data for a symbol"""
        self.market_data[symbol] = data
    
    def update_ai_consensus(self, symbol: str, consensus: dict):
        """Update AI consensus for a symbol"""
        self.ai_consensus[symbol] = consensus
    
    def add_position(self, position: dict):
        """Add a new position"""
        self.positions.append(position)
    
    def remove_position(self, symbol: str):
        """Remove a position"""
        self.positions = [p for p in self.positions if p['symbol'] != symbol]
    
    def add_trade(self, trade: dict):
        """Add a trade to history"""
        self.trade_history.insert(0, trade)  # Most recent first
        if len(self.trade_history) > 100:
            self.trade_history = self.trade_history[:100]


# Global dashboard data
dashboard_data = DashboardData()


@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')


@app.route('/api/status')
def get_status():
    """Get system status"""
    return jsonify(dashboard_data.system_status)


@app.route('/api/market_data')
def get_market_data():
    """Get all market data"""
    return jsonify(dashboard_data.market_data)


@app.route('/api/ai_consensus')
def get_ai_consensus():
    """Get AI consensus data"""
    return jsonify(dashboard_data.ai_consensus)


@app.route('/api/positions')
def get_positions():
    """Get current positions"""
    return jsonify(dashboard_data.positions)


@app.route('/api/trades')
def get_trades():
    """Get trade history"""
    limit = request.args.get('limit', 50, type=int)
    return jsonify(dashboard_data.trade_history[:limit])


@app.route('/api/control/start', methods=['POST'])
def start_system():
    """Start the trading system"""
    dashboard_data.system_status['running'] = True
    return jsonify({"success": True, "message": "System started"})


@app.route('/api/control/stop', methods=['POST'])
def stop_system():
    """Stop the trading system"""
    dashboard_data.system_status['running'] = False
    return jsonify({"success": True, "message": "System stopped"})


@app.route('/api/control/emergency_stop', methods=['POST'])
def emergency_stop():
    """Emergency stop - close all positions"""
    dashboard_data.system_status['running'] = False
    dashboard_data.positions = []
    return jsonify({"success": True, "message": "Emergency stop executed"})


def create_dashboard_html():
    """Create the dashboard HTML template"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Lyra Trading System - Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .card h2 {
            font-size: 1.5em;
            margin-bottom: 15px;
            border-bottom: 2px solid rgba(255, 255, 255, 0.3);
            padding-bottom: 10px;
        }
        
        .stat {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 10px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
        }
        
        .stat-label {
            font-weight: 600;
        }
        
        .stat-value {
            font-size: 1.2em;
        }
        
        .positive {
            color: #4ade80;
        }
        
        .negative {
            color: #f87171;
        }
        
        .neutral {
            color: #fbbf24;
        }
        
        .controls {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        
        button {
            flex: 1;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-start {
            background: #4ade80;
            color: #1f2937;
        }
        
        .btn-stop {
            background: #fbbf24;
            color: #1f2937;
        }
        
        .btn-emergency {
            background: #f87171;
            color: #fff;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }
        
        .status-running {
            background: #4ade80;
            box-shadow: 0 0 10px #4ade80;
        }
        
        .status-stopped {
            background: #f87171;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        th {
            background: rgba(255, 255, 255, 0.1);
            font-weight: 600;
        }
        
        tr:hover {
            background: rgba(255, 255, 255, 0.05);
        }
        
        .ai-vote {
            display: flex;
            gap: 10px;
            margin: 10px 0;
        }
        
        .vote-bar {
            flex: 1;
            height: 30px;
            border-radius: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 0.9em;
        }
        
        .vote-buy {
            background: #4ade80;
            color: #1f2937;
        }
        
        .vote-sell {
            background: #f87171;
            color: #fff;
        }
        
        .vote-hold {
            background: #fbbf24;
            color: #1f2937;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .loading {
            animation: pulse 2s infinite;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 Ultimate Lyra Trading System</h1>
            <p class="subtitle">AI-Powered Crypto Trading Dashboard</p>
        </header>
        
        <div class="grid">
            <!-- System Status -->
            <div class="card">
                <h2>System Status</h2>
                <div class="stat">
                    <span class="stat-label">Status:</span>
                    <span class="stat-value">
                        <span class="status-indicator status-running" id="status-indicator"></span>
                        <span id="status-text">Running</span>
                    </span>
                </div>
                <div class="stat">
                    <span class="stat-label">Capital:</span>
                    <span class="stat-value" id="capital">$1,000,000.00</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Positions:</span>
                    <span class="stat-value" id="positions">0 / 25</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Trades Today:</span>
                    <span class="stat-value" id="trades-today">0</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Win Rate:</span>
                    <span class="stat-value positive" id="win-rate">0.0%</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Total Profit:</span>
                    <span class="stat-value positive" id="total-profit">$0.00</span>
                </div>
                
                <div class="controls">
                    <button class="btn-start" onclick="startSystem()">▶️ Start</button>
                    <button class="btn-stop" onclick="stopSystem()">⏸️ Stop</button>
                    <button class="btn-emergency" onclick="emergencyStop()">🛑 Emergency</button>
                </div>
            </div>
            
            <!-- Market Overview -->
            <div class="card">
                <h2>Market Overview</h2>
                <div id="market-overview">
                    <p class="loading">Loading market data...</p>
                </div>
            </div>
            
            <!-- AI Consensus -->
            <div class="card">
                <h2>AI Hive Mind Consensus</h2>
                <div id="ai-consensus">
                    <p class="loading">Loading AI consensus...</p>
                </div>
            </div>
        </div>
        
        <!-- Positions Table -->
        <div class="card">
            <h2>Open Positions</h2>
            <table id="positions-table">
                <thead>
                    <tr>
                        <th>Symbol</th>
                        <th>Entry Price</th>
                        <th>Current Price</th>
                        <th>Amount</th>
                        <th>PnL</th>
                        <th>PnL %</th>
                    </tr>
                </thead>
                <tbody id="positions-body">
                    <tr>
                        <td colspan="6" style="text-align: center;">No open positions</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <!-- Trade History -->
        <div class="card">
            <h2>Recent Trades</h2>
            <table id="trades-table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Symbol</th>
                        <th>Side</th>
                        <th>Price</th>
                        <th>Amount</th>
                        <th>Profit</th>
                    </tr>
                </thead>
                <tbody id="trades-body">
                    <tr>
                        <td colspan="6" style="text-align: center;">No trades yet</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <script>
        // Update dashboard every 2 seconds
        setInterval(updateDashboard, 2000);
        updateDashboard();
        
        async function updateDashboard() {
            try {
                // Update system status
                const status = await fetch('/api/status').then(r => r.json());
                document.getElementById('capital').textContent = '$' + status.capital.toLocaleString('en-US', {minimumFractionDigits: 2});
                document.getElementById('positions').textContent = status.positions + ' / 25';
                document.getElementById('trades-today').textContent = status.trades_today;
                document.getElementById('win-rate').textContent = status.win_rate.toFixed(1) + '%';
                document.getElementById('total-profit').textContent = '$' + status.total_profit.toLocaleString('en-US', {minimumFractionDigits: 2});
                
                const statusIndicator = document.getElementById('status-indicator');
                const statusText = document.getElementById('status-text');
                if (status.running) {
                    statusIndicator.className = 'status-indicator status-running';
                    statusText.textContent = 'Running';
                } else {
                    statusIndicator.className = 'status-indicator status-stopped';
                    statusText.textContent = 'Stopped';
                }
                
                // Update market data
                const marketData = await fetch('/api/market_data').then(r => r.json());
                const marketOverview = document.getElementById('market-overview');
                marketOverview.innerHTML = '';
                for (const [symbol, data] of Object.entries(marketData)) {
                    const changeClass = data.change_24h >= 0 ? 'positive' : 'negative';
                    marketOverview.innerHTML += `
                        <div class="stat">
                            <span class="stat-label">${symbol}:</span>
                            <span class="stat-value ${changeClass}">
                                $${data.price.toLocaleString('en-US', {minimumFractionDigits: 2})}
                                (${data.change_24h >= 0 ? '+' : ''}${data.change_24h.toFixed(2)}%)
                            </span>
                        </div>
                    `;
                }
                
                // Update AI consensus
                const aiConsensus = await fetch('/api/ai_consensus').then(r => r.json());
                const aiConsensusDiv = document.getElementById('ai-consensus');
                aiConsensusDiv.innerHTML = '';
                for (const [symbol, consensus] of Object.entries(aiConsensus)) {
                    const buyPct = (consensus.breakdown.BUY * 100).toFixed(0);
                    const sellPct = (consensus.breakdown.SELL * 100).toFixed(0);
                    const holdPct = (consensus.breakdown.HOLD * 100).toFixed(0);
                    
                    aiConsensusDiv.innerHTML += `
                        <div style="margin-bottom: 15px;">
                            <strong>${symbol}</strong>: ${consensus.decision} (${(consensus.confidence * 100).toFixed(0)}%)
                            <div class="ai-vote">
                                <div class="vote-bar vote-buy" style="flex: ${buyPct}">BUY ${buyPct}%</div>
                                <div class="vote-bar vote-sell" style="flex: ${sellPct}">SELL ${sellPct}%</div>
                                <div class="vote-bar vote-hold" style="flex: ${holdPct}">HOLD ${holdPct}%</div>
                            </div>
                        </div>
                    `;
                }
                
            } catch (error) {
                console.error('Error updating dashboard:', error);
            }
        }
        
        async function startSystem() {
            await fetch('/api/control/start', {method: 'POST'});
            updateDashboard();
        }
        
        async function stopSystem() {
            await fetch('/api/control/stop', {method: 'POST'});
            updateDashboard();
        }
        
        async function emergencyStop() {
            if (confirm('Are you sure you want to execute an emergency stop? This will close all positions.')) {
                await fetch('/api/control/emergency_stop', {method: 'POST'});
                updateDashboard();
            }
        }
    </script>
</body>
</html>
    """
    
    # Save template
    import os
    os.makedirs('templates', exist_ok=True)
    with open('templates/dashboard.html', 'w') as f:
        f.write(html)


if __name__ == "__main__":
    create_dashboard_html()
    print("🎛️ Starting Lyra Web Dashboard...")
    print("📊 Dashboard URL: http://localhost:5000")
    print("🔗 Access from anywhere: http://YOUR_IP:5000")
    print("\nPress Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)

