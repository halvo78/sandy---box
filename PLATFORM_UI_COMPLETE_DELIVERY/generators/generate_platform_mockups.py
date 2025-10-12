#!/usr/bin/env python3
"""
Generate visual mockups of the LYRA Trading Platform
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.font_manager as fm

# Set style
plt.style.use('dark_background')

# Color scheme
COLORS = {
    'bg_primary': '#0A0E27',
    'bg_secondary': '#1A1F3A',
    'bg_tertiary': '#252B4D',
    'bg_elevated': '#2F3659',
    'color_buy': '#00D9FF',
    'color_sell': '#FF3366',
    'color_profit': '#00FF88',
    'text_primary': '#FFFFFF',
    'text_secondary': '#8B93B0',
    'border': '#2F3659',
}

def create_trading_dashboard():
    """Create Trading Dashboard mockup"""
    fig = plt.figure(figsize=(20, 12), facecolor=COLORS['bg_primary'])
    
    # Create main grid
    gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3,
                  left=0.08, right=0.98, top=0.95, bottom=0.05)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'LYRA Trading Platform', 
                   fontsize=24, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.3, 0.5, 'OKX | BTC/USDT', 
                   fontsize=16, color=COLORS['text_primary'], va='center')
    ax_header.text(0.95, 0.5, '$50,234.56 ▲ +2.34%', 
                   fontsize=16, color=COLORS['color_profit'], 
                   va='center', ha='right', fontweight='bold')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # Price Chart (large, left)
    ax_chart = fig.add_subplot(gs[1:, :2])
    ax_chart.set_facecolor(COLORS['bg_secondary'])
    
    # Generate candlestick-like data
    np.random.seed(42)
    x = np.arange(100)
    price = 50000 + np.cumsum(np.random.randn(100) * 200)
    
    # Plot price line
    ax_chart.plot(x, price, color=COLORS['color_buy'], linewidth=2, alpha=0.8)
    ax_chart.fill_between(x, price.min(), price, color=COLORS['color_buy'], alpha=0.1)
    
    # Add moving average
    ma = np.convolve(price, np.ones(20)/20, mode='valid')
    ax_chart.plot(x[19:], ma, color=COLORS['color_profit'], linewidth=1.5, 
                  alpha=0.6, linestyle='--', label='MA(20)')
    
    ax_chart.set_title('BTC/USDT - Real-Time Price Chart', 
                       fontsize=18, color=COLORS['text_primary'], 
                       pad=20, fontweight='bold')
    ax_chart.set_xlabel('Time', fontsize=12, color=COLORS['text_secondary'])
    ax_chart.set_ylabel('Price (USD)', fontsize=12, color=COLORS['text_secondary'])
    ax_chart.grid(True, alpha=0.1, color=COLORS['border'])
    ax_chart.legend(loc='upper left', framealpha=0.3)
    ax_chart.tick_params(colors=COLORS['text_secondary'])
    
    # Order Book (top right)
    ax_orderbook = fig.add_subplot(gs[1, 2])
    ax_orderbook.set_facecolor(COLORS['bg_secondary'])
    ax_orderbook.set_title('Order Book', fontsize=16, color=COLORS['text_primary'],
                           pad=15, fontweight='bold')
    
    # Asks (red)
    asks_prices = [50250, 50240, 50230, 50220, 50210]
    asks_amounts = [1.2, 2.1, 0.8, 1.5, 2.3]
    y_asks = np.arange(len(asks_prices))
    
    for i, (price, amount) in enumerate(zip(asks_prices, asks_amounts)):
        ax_orderbook.barh(y_asks[i], amount, height=0.7, 
                         color=COLORS['color_sell'], alpha=0.3)
        ax_orderbook.text(-0.1, y_asks[i], f'${price:,}', 
                         fontsize=10, color=COLORS['color_sell'],
                         ha='right', va='center', fontweight='bold')
        ax_orderbook.text(amount + 0.1, y_asks[i], f'{amount:.2f}', 
                         fontsize=9, color=COLORS['text_secondary'],
                         ha='left', va='center')
    
    # Spread line
    spread_y = len(asks_prices)
    ax_orderbook.axhline(spread_y - 0.5, color=COLORS['text_secondary'], 
                        linewidth=2, linestyle='--', alpha=0.5)
    ax_orderbook.text(1.5, spread_y - 0.5, 'SPREAD: $50', 
                     fontsize=10, color=COLORS['text_secondary'],
                     ha='center', va='bottom', bbox=dict(boxstyle='round',
                     facecolor=COLORS['bg_tertiary'], alpha=0.8))
    
    # Bids (green)
    bids_prices = [50200, 50190, 50180, 50170, 50160]
    bids_amounts = [1.8, 1.3, 2.5, 0.9, 1.7]
    y_bids = np.arange(len(bids_prices)) + spread_y
    
    for i, (price, amount) in enumerate(zip(bids_prices, bids_amounts)):
        ax_orderbook.barh(y_bids[i], amount, height=0.7, 
                         color=COLORS['color_profit'], alpha=0.3)
        ax_orderbook.text(-0.1, y_bids[i], f'${price:,}', 
                         fontsize=10, color=COLORS['color_profit'],
                         ha='right', va='center', fontweight='bold')
        ax_orderbook.text(amount + 0.1, y_bids[i], f'{amount:.2f}', 
                         fontsize=9, color=COLORS['text_secondary'],
                         ha='left', va='center')
    
    ax_orderbook.set_xlim(-0.5, 3)
    ax_orderbook.set_ylim(-0.5, len(asks_prices) + len(bids_prices))
    ax_orderbook.axis('off')
    
    # Position Manager (bottom right)
    ax_positions = fig.add_subplot(gs[2, 2])
    ax_positions.set_facecolor(COLORS['bg_secondary'])
    ax_positions.set_title('Open Positions', fontsize=16, 
                          color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    positions = [
        ('BTC/USDT', 0.5, 49500, 50234, 367),
        ('ETH/USDT', 10, 2800, 2850, 500),
        ('SOL/USDT', 50, 95, 98, 150),
    ]
    
    y_pos = 0
    for pair, size, entry, current, pnl in positions:
        # Position card background
        rect = patches.Rectangle((0.05, y_pos), 0.9, 0.28, 
                                 facecolor=COLORS['bg_tertiary'],
                                 edgecolor=COLORS['border'], linewidth=1)
        ax_positions.add_patch(rect)
        
        # Pair name
        ax_positions.text(0.08, y_pos + 0.22, pair, fontsize=12, 
                         color=COLORS['text_primary'], fontweight='bold')
        
        # P&L
        pnl_color = COLORS['color_profit'] if pnl > 0 else COLORS['color_sell']
        pnl_text = f'+${pnl:.2f}' if pnl > 0 else f'-${abs(pnl):.2f}'
        ax_positions.text(0.92, y_pos + 0.22, pnl_text, fontsize=12, 
                         color=pnl_color, fontweight='bold', ha='right')
        
        # Details
        ax_positions.text(0.08, y_pos + 0.12, f'Size: {size}', 
                         fontsize=9, color=COLORS['text_secondary'])
        ax_positions.text(0.4, y_pos + 0.12, f'Entry: ${entry:,}', 
                         fontsize=9, color=COLORS['text_secondary'])
        ax_positions.text(0.08, y_pos + 0.04, f'Current: ${current:,}', 
                         fontsize=9, color=COLORS['text_secondary'])
        
        y_pos += 0.32
    
    ax_positions.set_xlim(0, 1)
    ax_positions.set_ylim(0, 1)
    ax_positions.axis('off')
    
    plt.savefig('/home/ubuntu/trading_dashboard_mockup.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ Trading Dashboard mockup saved")
    plt.close()

def create_risk_dashboard():
    """Create Risk Dashboard mockup"""
    fig = plt.figure(figsize=(20, 12), facecolor=COLORS['bg_primary'])
    
    gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3,
                  left=0.08, right=0.98, top=0.95, bottom=0.05)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'LYRA Risk Management', 
                   fontsize=24, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.95, 0.5, 'Portfolio Health: EXCELLENT', 
                   fontsize=16, color=COLORS['color_profit'], 
                   va='center', ha='right', fontweight='bold')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # Risk Metrics (top row)
    ax_metrics = fig.add_subplot(gs[1, :])
    ax_metrics.set_facecolor(COLORS['bg_secondary'])
    ax_metrics.set_title('Key Risk Metrics', fontsize=18, 
                        color=COLORS['text_primary'], pad=20, fontweight='bold')
    
    metrics = [
        ('Total Exposure', '$13,947', COLORS['color_buy']),
        ('VaR (95%)', '$698', COLORS['text_primary']),
        ('Sharpe Ratio', '2.34', COLORS['color_profit']),
        ('Max Drawdown', '8.5%', COLORS['color_profit']),
        ('Win Rate', '78.9%', COLORS['color_profit']),
    ]
    
    x_pos = 0.1
    for label, value, color in metrics:
        ax_metrics.text(x_pos, 0.7, label, fontsize=12, 
                       color=COLORS['text_secondary'], ha='center')
        ax_metrics.text(x_pos, 0.3, value, fontsize=20, 
                       color=color, ha='center', fontweight='bold')
        x_pos += 0.18
    
    ax_metrics.set_xlim(0, 1)
    ax_metrics.set_ylim(0, 1)
    ax_metrics.axis('off')
    
    # Portfolio Exposure (pie chart)
    ax_exposure = fig.add_subplot(gs[2, 0])
    ax_exposure.set_facecolor(COLORS['bg_secondary'])
    
    assets = ['BTC', 'ETH', 'SOL', 'ADA', 'USDT']
    sizes = [35, 25, 15, 10, 15]
    colors_pie = [COLORS['color_buy'], COLORS['color_profit'], 
                  '#FFB800', '#7B61FF', COLORS['text_secondary']]
    
    wedges, texts, autotexts = ax_exposure.pie(sizes, labels=assets, 
                                                colors=colors_pie,
                                                autopct='%1.1f%%',
                                                startangle=90,
                                                textprops={'color': COLORS['text_primary'],
                                                          'fontsize': 12})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax_exposure.set_title('Portfolio Allocation', fontsize=16, 
                         color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    # Correlation Matrix
    ax_corr = fig.add_subplot(gs[2, 1])
    ax_corr.set_facecolor(COLORS['bg_secondary'])
    
    assets_corr = ['BTC', 'ETH', 'SOL', 'ADA']
    corr_matrix = np.array([
        [1.0, 0.85, 0.72, 0.68],
        [0.85, 1.0, 0.78, 0.71],
        [0.72, 0.78, 1.0, 0.65],
        [0.68, 0.71, 0.65, 1.0]
    ])
    
    im = ax_corr.imshow(corr_matrix, cmap='RdYlGn', vmin=0, vmax=1, aspect='auto')
    
    ax_corr.set_xticks(np.arange(len(assets_corr)))
    ax_corr.set_yticks(np.arange(len(assets_corr)))
    ax_corr.set_xticklabels(assets_corr, color=COLORS['text_primary'])
    ax_corr.set_yticklabels(assets_corr, color=COLORS['text_primary'])
    
    # Add correlation values
    for i in range(len(assets_corr)):
        for j in range(len(assets_corr)):
            text = ax_corr.text(j, i, f'{corr_matrix[i, j]:.2f}',
                               ha="center", va="center", 
                               color="white", fontweight='bold', fontsize=11)
    
    ax_corr.set_title('Correlation Matrix', fontsize=16, 
                     color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    # Alerts Panel
    ax_alerts = fig.add_subplot(gs[2, 2])
    ax_alerts.set_facecolor(COLORS['bg_secondary'])
    ax_alerts.set_title('Active Alerts', fontsize=16, 
                       color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    alerts = [
        ('✅', 'All systems operational', COLORS['color_profit']),
        ('⚠️', 'BTC correlation high (0.85)', COLORS['text_secondary']),
        ('✅', 'Risk limits: OK', COLORS['color_profit']),
        ('✅', 'Exposure within limits', COLORS['color_profit']),
    ]
    
    y_alert = 0.85
    for icon, text, color in alerts:
        ax_alerts.text(0.05, y_alert, icon, fontsize=16, va='center')
        ax_alerts.text(0.15, y_alert, text, fontsize=11, 
                      color=color, va='center')
        y_alert -= 0.2
    
    ax_alerts.set_xlim(0, 1)
    ax_alerts.set_ylim(0, 1)
    ax_alerts.axis('off')
    
    plt.savefig('/home/ubuntu/risk_dashboard_mockup.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ Risk Dashboard mockup saved")
    plt.close()

def create_executive_dashboard():
    """Create Executive Dashboard mockup"""
    fig = plt.figure(figsize=(20, 12), facecolor=COLORS['bg_primary'])
    
    gs = GridSpec(3, 4, figure=fig, hspace=0.3, wspace=0.3,
                  left=0.08, right=0.98, top=0.95, bottom=0.05)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'LYRA Executive Dashboard', 
                   fontsize=24, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.95, 0.5, 'Q4 2025', 
                   fontsize=16, color=COLORS['text_primary'], 
                   va='center', ha='right')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # KPI Cards
    kpis = [
        ('Total P&L', '+$2,847', '+24.5%', COLORS['color_profit']),
        ('Win Rate', '78.9%', '+5.2%', COLORS['color_profit']),
        ('Total Trades', '2,718', '+342', COLORS['color_buy']),
        ('Avg Trade', '$149', '+$12', COLORS['color_profit']),
    ]
    
    for idx, (label, value, change, color) in enumerate(kpis):
        ax_kpi = fig.add_subplot(gs[1, idx])
        ax_kpi.set_facecolor(COLORS['bg_secondary'])
        
        # Border
        rect = patches.Rectangle((0, 0), 1, 1, 
                                facecolor='none',
                                edgecolor=COLORS['border'], linewidth=2)
        ax_kpi.add_patch(rect)
        
        ax_kpi.text(0.5, 0.75, label, fontsize=14, 
                   color=COLORS['text_secondary'], ha='center')
        ax_kpi.text(0.5, 0.45, value, fontsize=24, 
                   color=color, ha='center', fontweight='bold')
        ax_kpi.text(0.5, 0.2, change, fontsize=12, 
                   color=color, ha='center')
        
        ax_kpi.set_xlim(0, 1)
        ax_kpi.set_ylim(0, 1)
        ax_kpi.axis('off')
    
    # Performance Chart
    ax_perf = fig.add_subplot(gs[2, :])
    ax_perf.set_facecolor(COLORS['bg_secondary'])
    
    np.random.seed(42)
    days = np.arange(30)
    cumulative_pnl = np.cumsum(np.random.randn(30) * 50 + 30)
    
    ax_perf.plot(days, cumulative_pnl, color=COLORS['color_profit'], 
                linewidth=3, marker='o', markersize=4)
    ax_perf.fill_between(days, 0, cumulative_pnl, 
                         color=COLORS['color_profit'], alpha=0.2)
    
    ax_perf.set_title('Cumulative P&L (Last 30 Days)', fontsize=18, 
                     color=COLORS['text_primary'], pad=20, fontweight='bold')
    ax_perf.set_xlabel('Days', fontsize=12, color=COLORS['text_secondary'])
    ax_perf.set_ylabel('P&L (USD)', fontsize=12, color=COLORS['text_secondary'])
    ax_perf.grid(True, alpha=0.1, color=COLORS['border'])
    ax_perf.tick_params(colors=COLORS['text_secondary'])
    ax_perf.axhline(0, color=COLORS['text_secondary'], linewidth=1, 
                   linestyle='--', alpha=0.5)
    
    plt.savefig('/home/ubuntu/executive_dashboard_mockup.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ Executive Dashboard mockup saved")
    plt.close()

if __name__ == '__main__':
    print("=" * 70)
    print("GENERATING LYRA PLATFORM MOCKUPS")
    print("=" * 70)
    
    create_trading_dashboard()
    create_risk_dashboard()
    create_executive_dashboard()
    
    print("")
    print("=" * 70)
    print("✅ ALL MOCKUPS GENERATED SUCCESSFULLY!")
    print("=" * 70)
    print("")
    print("📸 Generated mockups:")
    print("   1. trading_dashboard_mockup.png")
    print("   2. risk_dashboard_mockup.png")
    print("   3. executive_dashboard_mockup.png")
    print("")

