#!/usr/bin/env python3
"""
🎯 ULTIMATE AI TRADING DASHBOARD
=================================

Best-in-world dashboard for watching AI trade in real-time
- Live AI decision tracking
- Real-time consensus visualization
- Progressive rollout status
- Hive mind learning metrics
- Individual coin performance
- AI confidence levels
- Trade execution timeline
"""

from flask import Flask, render_template_string, jsonify
import json
import os
from datetime import datetime
from typing import Dict, List, Any

app = Flask(__name__)

# HTML Template for the dashboard
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Ultimate AI Trading Dashboard</title>
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
            max-width: 1800px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            animation: fadeIn 1s;
        }
        
        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.3s, box-shadow 0.3s;
            animation: slideIn 0.5s;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 48px rgba(0,0,0,0.2);
        }
        
        .stat-card .label {
            font-size: 0.9em;
            opacity: 0.8;
            margin-bottom: 10px;
        }
        
        .stat-card .value {
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .stat-card .change {
            font-size: 0.9em;
            opacity: 0.9;
        }
        
        .stat-card.positive .value {
            color: #4ade80;
        }
        
        .stat-card.negative .value {
            color: #f87171;
        }
        
        .section {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: fadeIn 0.8s;
        }
        
        .section h2 {
            font-size: 1.8em;
            margin-bottom: 20px;
            border-bottom: 2px solid rgba(255, 255, 255, 0.3);
            padding-bottom: 10px;
        }
        
        .rollout-stages {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .stage-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            border: 2px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s;
        }
        
        .stage-card.active {
            border-color: #4ade80;
            background: rgba(74, 222, 128, 0.1);
        }
        
        .stage-card.completed {
            border-color: #60a5fa;
            background: rgba(96, 165, 250, 0.1);
        }
        
        .stage-card.pending {
            opacity: 0.6;
        }
        
        .stage-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .stage-title {
            font-size: 1.3em;
            font-weight: bold;
        }
        
        .stage-status {
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }
        
        .stage-status.active {
            background: #4ade80;
            color: #000;
        }
        
        .stage-status.completed {
            background: #60a5fa;
            color: #000;
        }
        
        .stage-status.pending {
            background: rgba(255, 255, 255, 0.2);
        }
        
        .coin-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        
        .coin-badge {
            background: rgba(255, 255, 255, 0.2);
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        
        .ai-team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .ai-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .ai-name {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .ai-model {
            font-size: 0.85em;
            opacity: 0.7;
            margin-bottom: 10px;
        }
        
        .ai-confidence {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .confidence-bar {
            flex: 1;
            height: 8px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 4px;
            overflow: hidden;
        }
        
        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #4ade80, #22c55e);
            transition: width 0.3s;
        }
        
        .positions-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        .positions-table th,
        .positions-table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .positions-table th {
            background: rgba(255, 255, 255, 0.1);
            font-weight: bold;
        }
        
        .positions-table tr:hover {
            background: rgba(255, 255, 255, 0.05);
        }
        
        .trade-timeline {
            max-height: 400px;
            overflow-y: auto;
        }
        
        .trade-item {
            background: rgba(255, 255, 255, 0.05);
            border-left: 4px solid #4ade80;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        
        .trade-item.sell {
            border-left-color: #60a5fa;
        }
        
        .trade-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }
        
        .trade-symbol {
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .trade-time {
            opacity: 0.7;
            font-size: 0.9em;
        }
        
        .trade-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            font-size: 0.9em;
        }
        
        .hive-mind-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        
        .hive-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .hive-symbol {
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 15px;
        }
        
        .hive-stats {
            display: grid;
            gap: 10px;
        }
        
        .hive-stat {
            display: flex;
            justify-content: space-between;
        }
        
        .hive-stat-label {
            opacity: 0.8;
        }
        
        .hive-stat-value {
            font-weight: bold;
        }
        
        .refresh-indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(74, 222, 128, 0.9);
            color: #000;
            padding: 10px 20px;
            border-radius: 20px;
            font-weight: bold;
            animation: pulse 2s infinite;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes slideIn {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        
        .status-indicator.active {
            background: #4ade80;
        }
        
        .status-indicator.trading {
            background: #fbbf24;
        }
    </style>
</head>
<body>
    <div class="refresh-indicator">🔄 Live Updates</div>
    
    <div class="container">
        <div class="header">
            <h1>🚀 ULTIMATE AI TRADING DASHBOARD</h1>
            <div class="subtitle">
                <span class="status-indicator active"></span>
                Full AI Autonomous Control • Progressive Rollout • Hive Mind Optimization
            </div>
        </div>
        
        <!-- Performance Stats -->
        <div class="stats-grid">
            <div class="stat-card positive">
                <div class="label">💰 Portfolio Value</div>
                <div class="value" id="portfolio-value">$10,000.00</div>
                <div class="change" id="portfolio-change">+0.00%</div>
            </div>
            
            <div class="stat-card positive">
                <div class="label">📈 Total P&L</div>
                <div class="value" id="total-pnl">$0.00</div>
                <div class="change" id="pnl-percent">0.00%</div>
            </div>
            
            <div class="stat-card">
                <div class="label">🎯 Win Rate</div>
                <div class="value" id="win-rate">0%</div>
                <div class="change" id="win-loss">0 / 0</div>
            </div>
            
            <div class="stat-card">
                <div class="label">🔄 Total Trades</div>
                <div class="value" id="total-trades">0</div>
                <div class="change" id="trades-today">0 today</div>
            </div>
            
            <div class="stat-card">
                <div class="label">🤖 AI Confidence</div>
                <div class="value" id="ai-confidence">0%</div>
                <div class="change">Average</div>
            </div>
            
            <div class="stat-card">
                <div class="label">🎮 Active Positions</div>
                <div class="value" id="active-positions">0</div>
                <div class="change" id="max-positions">Max: 25</div>
            </div>
        </div>
        
        <!-- Progressive Rollout Status -->
        <div class="section">
            <h2>📊 Progressive Rollout Status</h2>
            <div class="rollout-stages" id="rollout-stages">
                <!-- Stages will be populated by JavaScript -->
            </div>
        </div>
        
        <!-- AI Team Status -->
        <div class="section">
            <h2>🤖 AI Team Status (14 AIs)</h2>
            <div class="ai-team-grid" id="ai-team">
                <!-- AI team will be populated by JavaScript -->
            </div>
        </div>
        
        <!-- Hive Mind Learning -->
        <div class="section">
            <h2>🧠 Hive Mind Learning (Per Coin)</h2>
            <div class="hive-mind-grid" id="hive-mind">
                <!-- Hive mind data will be populated by JavaScript -->
            </div>
        </div>
        
        <!-- Active Positions -->
        <div class="section">
            <h2>💼 Active Positions</h2>
            <table class="positions-table">
                <thead>
                    <tr>
                        <th>Symbol</th>
                        <th>Entry Price</th>
                        <th>Current Price</th>
                        <th>Quantity</th>
                        <th>Value</th>
                        <th>P&L</th>
                        <th>P&L %</th>
                        <th>AI Confidence</th>
                        <th>Time Held</th>
                    </tr>
                </thead>
                <tbody id="positions-body">
                    <tr>
                        <td colspan="9" style="text-align: center; opacity: 0.5;">No active positions</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <!-- Trade Timeline -->
        <div class="section">
            <h2>⏱️ Recent Trades</h2>
            <div class="trade-timeline" id="trade-timeline">
                <div style="text-align: center; opacity: 0.5; padding: 40px;">
                    No trades yet. AI is analyzing markets...
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Refresh data every 5 seconds
        setInterval(refreshData, 5000);
        
        // Initial load
        refreshData();
        
        function refreshData() {
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {
                    updateStats(data);
                    updateRolloutStages(data.rollout_stages);
                    updateAITeam(data.ai_team);
                    updateHiveMind(data.coin_strategies);
                    updatePositions(data.positions);
                    updateTradeTimeline(data.trade_history);
                })
                .catch(error => console.error('Error fetching data:', error));
        }
        
        function updateStats(data) {
            const portfolio = data.portfolio;
            const performance = data.performance;
            
            document.getElementById('portfolio-value').textContent = 
                '$' + portfolio.total_value.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            
            document.getElementById('portfolio-change').textContent = 
                (portfolio.change_percent >= 0 ? '+' : '') + portfolio.change_percent.toFixed(2) + '%';
            
            document.getElementById('total-pnl').textContent = 
                '$' + performance.total_pnl.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            
            document.getElementById('pnl-percent').textContent = 
                (performance.pnl_percent >= 0 ? '+' : '') + performance.pnl_percent.toFixed(2) + '%';
            
            document.getElementById('win-rate').textContent = 
                (performance.win_rate * 100).toFixed(0) + '%';
            
            document.getElementById('win-loss').textContent = 
                performance.winning_trades + ' / ' + performance.losing_trades;
            
            document.getElementById('total-trades').textContent = 
                performance.total_trades;
            
            document.getElementById('ai-confidence').textContent = 
                (data.avg_confidence * 100).toFixed(0) + '%';
            
            document.getElementById('active-positions').textContent = 
                Object.keys(data.positions).length;
        }
        
        function updateRolloutStages(stages) {
            const container = document.getElementById('rollout-stages');
            container.innerHTML = stages.map(stage => `
                <div class="stage-card ${stage.status}">
                    <div class="stage-header">
                        <div class="stage-title">Stage ${stage.stage}</div>
                        <div class="stage-status ${stage.status}">${stage.status.toUpperCase()}</div>
                    </div>
                    <div>
                        <strong>Requirements:</strong><br>
                        ${stage.min_trades} trades • ${(stage.min_win_rate * 100).toFixed(0)}% win rate
                    </div>
                    <div class="coin-list">
                        ${stage.coins.map(coin => `<div class="coin-badge">${coin}</div>`).join('')}
                    </div>
                </div>
            `).join('');
        }
        
        function updateAITeam(aiTeam) {
            const container = document.getElementById('ai-team');
            container.innerHTML = Object.entries(aiTeam).map(([role, data]) => `
                <div class="ai-card">
                    <div class="ai-name">🤖 ${role.replace(/_/g, ' ').toUpperCase()}</div>
                    <div class="ai-model">${data.model}</div>
                    <div class="ai-confidence">
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: ${data.confidence * 100}%"></div>
                        </div>
                        <span>${(data.confidence * 100).toFixed(0)}%</span>
                    </div>
                </div>
            `).join('');
        }
        
        function updateHiveMind(strategies) {
            const container = document.getElementById('hive-mind');
            container.innerHTML = Object.entries(strategies).map(([symbol, strategy]) => `
                <div class="hive-card">
                    <div class="hive-symbol">${symbol}</div>
                    <div class="hive-stats">
                        <div class="hive-stat">
                            <span class="hive-stat-label">Trades:</span>
                            <span class="hive-stat-value">${strategy.trades}</span>
                        </div>
                        <div class="hive-stat">
                            <span class="hive-stat-label">Win Rate:</span>
                            <span class="hive-stat-value">${(strategy.win_rate * 100).toFixed(1)}%</span>
                        </div>
                        <div class="hive-stat">
                            <span class="hive-stat-label">Avg P&L:</span>
                            <span class="hive-stat-value">${strategy.avg_pnl.toFixed(2)}%</span>
                        </div>
                        <div class="hive-stat">
                            <span class="hive-stat-label">Total P&L:</span>
                            <span class="hive-stat-value">${strategy.total_pnl.toFixed(2)}%</span>
                        </div>
                    </div>
                </div>
            `).join('');
        }
        
        function updatePositions(positions) {
            const tbody = document.getElementById('positions-body');
            
            if (Object.keys(positions).length === 0) {
                tbody.innerHTML = '<tr><td colspan="9" style="text-align: center; opacity: 0.5;">No active positions</td></tr>';
                return;
            }
            
            tbody.innerHTML = Object.entries(positions).map(([symbol, pos]) => {
                const pnl = ((pos.current_price - pos.entry_price) / pos.entry_price) * 100;
                const pnlClass = pnl >= 0 ? 'positive' : 'negative';
                
                return `
                    <tr>
                        <td><strong>${symbol}</strong></td>
                        <td>$${pos.entry_price.toFixed(2)}</td>
                        <td>$${pos.current_price.toFixed(2)}</td>
                        <td>${pos.quantity.toFixed(4)}</td>
                        <td>$${pos.value.toFixed(2)}</td>
                        <td class="${pnlClass}">$${pos.pnl.toFixed(2)}</td>
                        <td class="${pnlClass}">${pnl.toFixed(2)}%</td>
                        <td>${(pos.confidence * 100).toFixed(0)}%</td>
                        <td>${pos.time_held}</td>
                    </tr>
                `;
            }).join('');
        }
        
        function updateTradeTimeline(trades) {
            const container = document.getElementById('trade-timeline');
            
            if (trades.length === 0) {
                container.innerHTML = '<div style="text-align: center; opacity: 0.5; padding: 40px;">No trades yet. AI is analyzing markets...</div>';
                return;
            }
            
            container.innerHTML = trades.slice(-20).reverse().map(trade => `
                <div class="trade-item ${trade.type.toLowerCase()}">
                    <div class="trade-header">
                        <div class="trade-symbol">${trade.type} ${trade.symbol}</div>
                        <div class="trade-time">${new Date(trade.timestamp).toLocaleString()}</div>
                    </div>
                    <div class="trade-details">
                        <div><strong>Price:</strong> $${trade.price.toFixed(2)}</div>
                        <div><strong>Quantity:</strong> ${trade.quantity.toFixed(4)}</div>
                        <div><strong>Size:</strong> $${trade.size.toFixed(2)}</div>
                        <div><strong>Confidence:</strong> ${(trade.confidence * 100).toFixed(0)}%</div>
                        ${trade.pnl !== undefined ? `
                            <div><strong>P&L:</strong> $${trade.pnl.toFixed(2)}</div>
                            <div><strong>P&L %:</strong> ${trade.pnl_percent.toFixed(2)}%</div>
                        ` : ''}
                    </div>
                </div>
            `).join('');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    """Main dashboard page"""
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/status')
def get_status():
    """Get current trading status"""
    try:
        # Load portfolio status from file
        if os.path.exists('data/ai_trading/portfolio_status.json'):
            with open('data/ai_trading/portfolio_status.json', 'r') as f:
                data = json.load(f)
            
            portfolio = data['portfolio']
            
            # Calculate additional metrics
            total_value = portfolio['cash'] + sum(
                pos['size'] for pos in portfolio['positions'].values()
            )
            
            change_percent = ((total_value - 10000) / 10000) * 100
            
            pnl_percent = (portfolio['performance']['total_pnl'] / 10000) * 100 if portfolio['performance']['total_pnl'] != 0 else 0
            
            # Calculate average confidence
            avg_confidence = 0.0
            if portfolio['trade_history']:
                confidences = [t.get('confidence', 0.0) for t in portfolio['trade_history']]
                avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
            
            # Mock AI team data (in production, this would come from the AI team)
            ai_team = {
                'market_analyst': {'model': 'google/gemini-pro-1.5', 'confidence': 0.92},
                'technical_analyst': {'model': 'anthropic/claude-3.5-sonnet', 'confidence': 0.88},
                'risk_manager': {'model': 'openai/gpt-4-turbo', 'confidence': 0.95},
                'entry_specialist': {'model': 'x-ai/grok-beta', 'confidence': 0.90},
                'exit_specialist': {'model': 'deepseek/deepseek-chat', 'confidence': 0.87},
                'sentiment_analyst': {'model': 'perplexity/sonar-large', 'confidence': 0.91},
                'volume_analyst': {'model': 'llama-3.1-405b', 'confidence': 0.89},
                'momentum_trader': {'model': 'gemini-flash-1.5', 'confidence': 0.93},
                'pattern_recognition': {'model': 'claude-3-opus', 'confidence': 0.94},
                'arbitrage_hunter': {'model': 'gpt-4o', 'confidence': 0.86},
                'liquidity_analyst': {'model': 'mistral-large', 'confidence': 0.88},
                'news_analyzer': {'model': 'sonar-huge', 'confidence': 0.92},
                'macro_strategist': {'model': 'claude-3.5-sonnet', 'confidence': 0.90},
                'execution_optimizer': {'model': 'grok-2', 'confidence': 0.91},
            }
            
            return jsonify({
                'portfolio': {
                    'cash': portfolio['cash'],
                    'total_value': total_value,
                    'change_percent': change_percent
                },
                'performance': {
                    'total_trades': portfolio['performance']['total_trades'],
                    'winning_trades': portfolio['performance']['winning_trades'],
                    'losing_trades': portfolio['performance']['losing_trades'],
                    'total_pnl': portfolio['performance']['total_pnl'],
                    'pnl_percent': pnl_percent,
                    'win_rate': portfolio['performance']['win_rate']
                },
                'positions': portfolio['positions'],
                'trade_history': portfolio['trade_history'],
                'current_stage': data['current_stage'],
                'active_coins': data['active_coins'],
                'rollout_stages': data['rollout_stages'],
                'coin_strategies': data['coin_strategies'],
                'ai_team': ai_team,
                'avg_confidence': avg_confidence,
                'timestamp': datetime.now().isoformat()
            })
        else:
            # Return default data if file doesn't exist
            return jsonify({
                'portfolio': {
                    'cash': 10000.0,
                    'total_value': 10000.0,
                    'change_percent': 0.0
                },
                'performance': {
                    'total_trades': 0,
                    'winning_trades': 0,
                    'losing_trades': 0,
                    'total_pnl': 0.0,
                    'pnl_percent': 0.0,
                    'win_rate': 0.0
                },
                'positions': {},
                'trade_history': [],
                'current_stage': 1,
                'active_coins': ['BTC/USDT'],
                'rollout_stages': [
                    {'stage': 1, 'coins': ['BTC/USDT'], 'min_trades': 10, 'min_win_rate': 0.70, 'status': 'active'}
                ],
                'coin_strategies': {},
                'ai_team': {},
                'avg_confidence': 0.0,
                'timestamp': datetime.now().isoformat()
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Ultimate AI Trading Dashboard',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Create data directory
    os.makedirs('data/ai_trading', exist_ok=True)
    
    # Run dashboard
    print("🚀 Starting Ultimate AI Trading Dashboard")
    print("📊 Dashboard: http://localhost:5000")
    print("🔗 API: http://localhost:5000/api/status")
    print("❤️ Health: http://localhost:5000/api/health")
    
    app.run(host='0.0.0.0', port=5000, debug=False)

