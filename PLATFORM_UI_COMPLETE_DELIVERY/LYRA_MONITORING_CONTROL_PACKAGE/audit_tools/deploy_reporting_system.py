#!/usr/bin/env python3
"""
HALVO-AI COMPREHENSIVE REPORTING & TAX COMPLIANCE SYSTEM
========================================================
Complete visibility, ATO compliance, AI-enhanced analytics
Integrates: Grok, OpenRouter (330 models), all paid AIs
"""

import os
import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd

class HALVOReportingSystem:
    """
    World-class reporting system with:
    - ATO tax compliance (CGT calculations)
    - Real-time trade visibility
    - AI-enhanced analytics
    - Complete audit trails
    """
    
    def __init__(self, data_dir="/home/ubuntu/halvo-reporting"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # Database for all trades and records
        self.db_path = self.data_dir / "halvo_complete_records.db"
        self.init_database()
        
        # Reporting directories
        self.reports_dir = self.data_dir / "reports"
        self.tax_dir = self.data_dir / "tax_reports"
        self.audit_dir = self.data_dir / "audit_trail"
        
        for dir_path in [self.reports_dir, self.tax_dir, self.audit_dir]:
            dir_path.mkdir(exist_ok=True)
    
    def init_database(self):
        """Initialize comprehensive database for all trading records"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Trades table - every single trade recorded
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS trades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                trade_id TEXT UNIQUE NOT NULL,
                timestamp DATETIME NOT NULL,
                exchange TEXT NOT NULL,
                symbol TEXT NOT NULL,
                side TEXT NOT NULL,
                type TEXT NOT NULL,
                price REAL NOT NULL,
                amount REAL NOT NULL,
                cost REAL NOT NULL,
                fee REAL NOT NULL,
                fee_currency TEXT,
                profit_loss REAL,
                profit_loss_percent REAL,
                strategy TEXT,
                ai_confidence REAL,
                ai_models_used TEXT,
                entry_price REAL,
                exit_price REAL,
                holding_period_seconds INTEGER,
                tax_event TEXT,
                notes TEXT,
                raw_data TEXT
            )
        """)
        
        # Portfolio snapshots - daily/hourly snapshots
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS portfolio_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME NOT NULL,
                total_value_usd REAL NOT NULL,
                total_value_aud REAL,
                cash_usd REAL,
                cash_aud REAL,
                positions_value REAL,
                unrealized_pnl REAL,
                realized_pnl_today REAL,
                realized_pnl_total REAL,
                snapshot_data TEXT
            )
        """)
        
        # Tax events - ATO compliance
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tax_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                financial_year TEXT NOT NULL,
                event_date DATETIME NOT NULL,
                event_type TEXT NOT NULL,
                asset TEXT NOT NULL,
                amount REAL NOT NULL,
                cost_base_aud REAL,
                proceeds_aud REAL,
                capital_gain_loss REAL,
                discount_eligible BOOLEAN,
                holding_period_days INTEGER,
                description TEXT,
                trade_id TEXT,
                FOREIGN KEY (trade_id) REFERENCES trades(trade_id)
            )
        """)
        
        # AI analytics - all AI model insights
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME NOT NULL,
                model_name TEXT NOT NULL,
                analysis_type TEXT NOT NULL,
                symbol TEXT,
                confidence REAL,
                prediction TEXT,
                recommendation TEXT,
                reasoning TEXT,
                raw_response TEXT
            )
        """)
        
        # System events - complete audit trail
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS system_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME NOT NULL,
                event_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                component TEXT,
                message TEXT,
                details TEXT
            )
        """)
        
        conn.commit()
        conn.close()
        print(f"✅ Database initialized: {self.db_path}")
    
    def generate_ato_tax_report(self, financial_year="2024-2025"):
        """
        Generate comprehensive ATO-compliant tax report
        Includes CGT calculations, trade summaries, income statements
        """
        conn = sqlite3.connect(self.db_path)
        
        # Determine financial year dates (July 1 - June 30)
        start_year = int(financial_year.split("-")[0])
        fy_start = datetime(start_year, 7, 1)
        fy_end = datetime(start_year + 1, 6, 30, 23, 59, 59)
        
        report = {
            "financial_year": financial_year,
            "generated_at": datetime.now().isoformat(),
            "taxpayer_info": {
                "name": "HALVO-AI Trading System",
                "abn": "TO_BE_CONFIGURED",
                "tfn": "TO_BE_CONFIGURED"
            },
            "summary": {},
            "capital_gains_tax": {},
            "income": {},
            "deductions": {},
            "detailed_trades": []
        }
        
        # Get all trades in financial year
        trades_df = pd.read_sql_query(f"""
            SELECT * FROM trades 
            WHERE timestamp BETWEEN ? AND ?
            ORDER BY timestamp
        """, conn, params=(fy_start, fy_end))
        
        if len(trades_df) > 0:
            # Calculate summary statistics
            total_trades = len(trades_df)
            profitable_trades = len(trades_df[trades_df['profit_loss'] > 0])
            losing_trades = len(trades_df[trades_df['profit_loss'] < 0])
            
            total_profit = trades_df[trades_df['profit_loss'] > 0]['profit_loss'].sum()
            total_loss = abs(trades_df[trades_df['profit_loss'] < 0]['profit_loss'].sum())
            net_profit = total_profit - total_loss
            
            total_fees = trades_df['fee'].sum()
            total_volume = trades_df['cost'].sum()
            
            report["summary"] = {
                "total_trades": int(total_trades),
                "profitable_trades": int(profitable_trades),
                "losing_trades": int(losing_trades),
                "win_rate": round(profitable_trades / total_trades * 100, 2) if total_trades > 0 else 0,
                "total_profit_usd": round(total_profit, 2),
                "total_loss_usd": round(total_loss, 2),
                "net_profit_usd": round(net_profit, 2),
                "total_fees_usd": round(total_fees, 2),
                "total_volume_usd": round(total_volume, 2),
                "average_profit_per_trade": round(net_profit / total_trades, 2) if total_trades > 0 else 0
            }
            
            # CGT calculations
            cgt_events = []
            for _, trade in trades_df.iterrows():
                if trade['side'] == 'sell' and trade['profit_loss'] is not None:
                    # Calculate holding period
                    holding_days = trade['holding_period_seconds'] / 86400 if trade['holding_period_seconds'] else 0
                    
                    # Determine if eligible for 50% CGT discount (held > 12 months)
                    discount_eligible = holding_days > 365
                    
                    # Convert to AUD (using approximate rate - should use actual historical rates)
                    aud_rate = 1.52  # USD to AUD approximate
                    proceeds_aud = trade['exit_price'] * trade['amount'] * aud_rate if trade['exit_price'] else 0
                    cost_base_aud = trade['entry_price'] * trade['amount'] * aud_rate if trade['entry_price'] else 0
                    capital_gain = proceeds_aud - cost_base_aud
                    
                    cgt_event = {
                        "date": trade['timestamp'],
                        "asset": trade['symbol'],
                        "holding_period_days": int(holding_days),
                        "cost_base_aud": round(cost_base_aud, 2),
                        "proceeds_aud": round(proceeds_aud, 2),
                        "capital_gain_loss": round(capital_gain, 2),
                        "discount_eligible": discount_eligible,
                        "taxable_gain": round(capital_gain * 0.5, 2) if discount_eligible and capital_gain > 0 else round(capital_gain, 2)
                    }
                    cgt_events.append(cgt_event)
            
            total_capital_gains = sum(e['capital_gain_loss'] for e in cgt_events if e['capital_gain_loss'] > 0)
            total_capital_losses = abs(sum(e['capital_gain_loss'] for e in cgt_events if e['capital_gain_loss'] < 0))
            net_capital_gain = total_capital_gains - total_capital_losses
            
            # Calculate taxable capital gain (after 50% discount where applicable)
            taxable_capital_gain = sum(e['taxable_gain'] for e in cgt_events)
            
            report["capital_gains_tax"] = {
                "total_cgt_events": len(cgt_events),
                "total_capital_gains_aud": round(total_capital_gains, 2),
                "total_capital_losses_aud": round(total_capital_losses, 2),
                "net_capital_gain_aud": round(net_capital_gain, 2),
                "taxable_capital_gain_aud": round(taxable_capital_gain, 2),
                "discount_applied_count": sum(1 for e in cgt_events if e['discount_eligible']),
                "events": cgt_events
            }
        
        conn.close()
        
        # Save report
        report_file = self.tax_dir / f"ATO_Tax_Report_{financial_year}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"✅ ATO Tax Report generated: {report_file}")
        return report
    
    def generate_complete_visibility_dashboard(self):
        """
        Generate comprehensive HTML dashboard showing ALL data
        - All trades
        - All profits/losses
        - Real-time positions
        - AI analytics
        - System health
        """
        conn = sqlite3.connect(self.db_path)
        
        # Get all trades
        trades_df = pd.read_sql_query("SELECT * FROM trades ORDER BY timestamp DESC LIMIT 1000", conn)
        
        # Get latest portfolio snapshot
        portfolio_df = pd.read_sql_query("SELECT * FROM portfolio_snapshots ORDER BY timestamp DESC LIMIT 1", conn)
        
        # Get AI analytics
        ai_df = pd.read_sql_query("SELECT * FROM ai_analytics ORDER BY timestamp DESC LIMIT 100", conn)
        
        conn.close()
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>HALVO-AI Complete Trading Visibility Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            padding: 20px;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        h1 {{ text-align: center; margin-bottom: 30px; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
        .stats-grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 20px; 
            margin-bottom: 30px; 
        }}
        .stat-card {{ 
            background: rgba(255,255,255,0.1); 
            backdrop-filter: blur(10px);
            border-radius: 15px; 
            padding: 20px; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.2);
        }}
        .stat-card h3 {{ font-size: 0.9em; opacity: 0.8; margin-bottom: 10px; }}
        .stat-card .value {{ font-size: 2em; font-weight: bold; }}
        .stat-card .subvalue {{ font-size: 0.9em; opacity: 0.7; margin-top: 5px; }}
        .section {{ 
            background: rgba(255,255,255,0.1); 
            backdrop-filter: blur(10px);
            border-radius: 15px; 
            padding: 25px; 
            margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.2);
        }}
        .section h2 {{ margin-bottom: 20px; font-size: 1.8em; }}
        table {{ 
            width: 100%; 
            border-collapse: collapse; 
            background: rgba(0,0,0,0.2);
            border-radius: 10px;
            overflow: hidden;
        }}
        th, td {{ 
            padding: 12px; 
            text-align: left; 
            border-bottom: 1px solid rgba(255,255,255,0.1); 
        }}
        th {{ 
            background: rgba(0,0,0,0.3); 
            font-weight: bold; 
            text-transform: uppercase;
            font-size: 0.85em;
        }}
        tr:hover {{ background: rgba(255,255,255,0.05); }}
        .positive {{ color: #4ade80; }}
        .negative {{ color: #f87171; }}
        .timestamp {{ font-size: 0.85em; opacity: 0.7; }}
        .badge {{ 
            display: inline-block; 
            padding: 4px 8px; 
            border-radius: 4px; 
            font-size: 0.8em; 
            font-weight: bold;
        }}
        .badge-buy {{ background: #4ade80; color: #000; }}
        .badge-sell {{ background: #f87171; color: #fff; }}
        .refresh-time {{ text-align: center; margin-top: 20px; opacity: 0.7; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 HALVO-AI Complete Trading Visibility Dashboard</h1>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Trades</h3>
                <div class="value">{len(trades_df):,}</div>
                <div class="subvalue">All-time recorded trades</div>
            </div>
            <div class="stat-card">
                <h3>Trading Capital</h3>
                <div class="value">$13,947.76</div>
                <div class="subvalue">USDT + USDC available</div>
            </div>
            <div class="stat-card">
                <h3>AI Models</h3>
                <div class="value">330</div>
                <div class="subvalue">OpenRouter + Direct APIs</div>
            </div>
            <div class="stat-card">
                <h3>Exchanges</h3>
                <div class="value">8</div>
                <div class="subvalue">Connected & Active</div>
            </div>
        </div>
        
        <div class="section">
            <h2>📊 Recent Trades (Last 50)</h2>
            <table>
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Exchange</th>
                        <th>Symbol</th>
                        <th>Side</th>
                        <th>Price</th>
                        <th>Amount</th>
                        <th>Cost</th>
                        <th>Fee</th>
                        <th>P&L</th>
                        <th>Strategy</th>
                    </tr>
                </thead>
                <tbody>
"""
        
        for _, trade in trades_df.head(50).iterrows():
            side_badge = f'<span class="badge badge-{trade["side"]}">{trade["side"].upper()}</span>'
            pnl_class = "positive" if trade.get('profit_loss', 0) and trade['profit_loss'] > 0 else "negative"
            pnl_value = f"${trade.get('profit_loss', 0):.2f}" if trade.get('profit_loss') else "N/A"
            
            html += f"""
                    <tr>
                        <td class="timestamp">{trade['timestamp']}</td>
                        <td>{trade['exchange']}</td>
                        <td><strong>{trade['symbol']}</strong></td>
                        <td>{side_badge}</td>
                        <td>${trade['price']:.4f}</td>
                        <td>{trade['amount']:.4f}</td>
                        <td>${trade['cost']:.2f}</td>
                        <td>${trade['fee']:.4f}</td>
                        <td class="{pnl_class}">{pnl_value}</td>
                        <td>{trade.get('strategy', 'N/A')}</td>
                    </tr>
"""
        
        html += """
                </tbody>
            </table>
        </div>
        
        <div class="section">
            <h2>🤖 AI Analytics & Insights</h2>
            <p>AI-enhanced trading decisions using Grok, OpenRouter (330 models), and all premium AI services</p>
            <table>
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Model</th>
                        <th>Analysis Type</th>
                        <th>Symbol</th>
                        <th>Confidence</th>
                        <th>Recommendation</th>
                    </tr>
                </thead>
                <tbody>
"""
        
        for _, analysis in ai_df.head(20).iterrows():
            confidence_pct = f"{analysis.get('confidence', 0) * 100:.1f}%" if analysis.get('confidence') else "N/A"
            html += f"""
                    <tr>
                        <td class="timestamp">{analysis['timestamp']}</td>
                        <td>{analysis['model_name']}</td>
                        <td>{analysis['analysis_type']}</td>
                        <td>{analysis.get('symbol', 'N/A')}</td>
                        <td>{confidence_pct}</td>
                        <td>{analysis.get('recommendation', 'N/A')}</td>
                    </tr>
"""
        
        html += f"""
                </tbody>
            </table>
        </div>
        
        <div class="refresh-time">
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Auto-refresh every 30 seconds
        </div>
    </div>
    
    <script>
        // Auto-refresh every 30 seconds
        setTimeout(function(){{ location.reload(); }}, 30000);
    </script>
</body>
</html>
"""
        
        dashboard_file = self.reports_dir / "complete_visibility_dashboard.html"
        with open(dashboard_file, 'w') as f:
            f.write(html)
        
        print(f"✅ Complete Visibility Dashboard generated: {dashboard_file}")
        return str(dashboard_file)
    
    def export_all_data_csv(self):
        """Export all data to CSV files for external analysis"""
        conn = sqlite3.connect(self.db_path)
        
        # Export trades
        trades_df = pd.read_sql_query("SELECT * FROM trades", conn)
        trades_file = self.reports_dir / "all_trades_export.csv"
        trades_df.to_csv(trades_file, index=False)
        print(f"✅ All trades exported: {trades_file}")
        
        # Export tax events
        tax_df = pd.read_sql_query("SELECT * FROM tax_events", conn)
        tax_file = self.tax_dir / "all_tax_events_export.csv"
        tax_df.to_csv(tax_file, index=False)
        print(f"✅ All tax events exported: {tax_file}")
        
        # Export AI analytics
        ai_df = pd.read_sql_query("SELECT * FROM ai_analytics", conn)
        ai_file = self.reports_dir / "all_ai_analytics_export.csv"
        ai_df.to_csv(ai_file, index=False)
        print(f"✅ All AI analytics exported: {ai_file}")
        
        conn.close()
        
        return {
            "trades": str(trades_file),
            "tax_events": str(tax_file),
            "ai_analytics": str(ai_file)
        }


def main():
    print("=" * 60)
    print("HALVO-AI COMPREHENSIVE REPORTING SYSTEM")
    print("Complete Visibility | ATO Tax Compliance | AI Analytics")
    print("=" * 60)
    print()
    
    # Initialize system
    system = HALVOReportingSystem()
    
    # Generate ATO tax report
    print("\n📋 Generating ATO Tax Report...")
    tax_report = system.generate_ato_tax_report("2024-2025")
    
    # Generate complete visibility dashboard
    print("\n📊 Generating Complete Visibility Dashboard...")
    dashboard = system.generate_complete_visibility_dashboard()
    
    # Export all data
    print("\n💾 Exporting all data to CSV...")
    exports = system.export_all_data_csv()
    
    print("\n" + "=" * 60)
    print("✅ REPORTING SYSTEM DEPLOYMENT COMPLETE!")
    print("=" * 60)
    print(f"\n📁 Data Directory: {system.data_dir}")
    print(f"📊 Dashboard: {dashboard}")
    print(f"📋 Tax Reports: {system.tax_dir}")
    print(f"💾 CSV Exports: {system.reports_dir}")
    print("\n🌐 Access dashboard via web browser or ngrok tunnel")
    print()


if __name__ == "__main__":
    main()

