#!/usr/bin/env python3
"""
Generate Comprehensive Portfolio Management Dashboards
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.colors as mcolors
from datetime import datetime, timedelta

# Color scheme
COLORS = {
    'bg_primary': '#0A0E27',
    'bg_secondary': '#1A1F3A',
    'bg_tertiary': '#252B4D',
    'bg_elevated': '#2F3659',
    'color_buy': '#00D9FF',
    'color_sell': '#FF3366',
    'color_profit': '#00FF88',
    'color_warning': '#FFB800',
    'color_purple': '#7B61FF',
    'text_primary': '#FFFFFF',
    'text_secondary': '#8B93B0',
    'border': '#2F3659',
}

def create_portfolio_overview():
    """Create Portfolio Overview Dashboard"""
    fig = plt.figure(figsize=(24, 14), facecolor=COLORS['bg_primary'])
    
    gs = GridSpec(4, 4, figure=fig, hspace=0.4, wspace=0.4,
                  left=0.05, right=0.98, top=0.96, bottom=0.04)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'Portfolio Overview Dashboard', 
                   fontsize=26, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.5, 0.5, 'Total Value: $13,947.76 | 24h Change: +$342.18 (+2.51%)', 
                   fontsize=14, color=COLORS['text_primary'], va='center')
    ax_header.text(0.95, 0.5, 'Updated: Just Now', 
                   fontsize=12, color=COLORS['text_secondary'], 
                   va='center', ha='right')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # KPI Cards (Top Row)
    kpis = [
        ('Total Assets', '$13,947.76', '+2.51%', COLORS['color_profit']),
        ('Total Return', '+$2,847.12', '+25.7%', COLORS['color_profit']),
        ('Win Rate', '78.9%', '+5.2pp', COLORS['color_profit']),
        ('Sharpe Ratio', '2.34', '+0.12', COLORS['color_profit']),
    ]
    
    for idx, (label, value, change, color) in enumerate(kpis):
        ax_kpi = fig.add_subplot(gs[1, idx])
        ax_kpi.set_facecolor(COLORS['bg_secondary'])
        
        # Border
        rect = patches.Rectangle((0, 0), 1, 1, 
                                facecolor='none',
                                edgecolor=COLORS['border'], linewidth=2)
        ax_kpi.add_patch(rect)
        
        ax_kpi.text(0.5, 0.75, label, fontsize=12, 
                   color=COLORS['text_secondary'], ha='center', fontweight='bold')
        ax_kpi.text(0.5, 0.45, value, fontsize=22, 
                   color=COLORS['text_primary'], ha='center', fontweight='bold',
                   family='monospace')
        ax_kpi.text(0.5, 0.2, change, fontsize=11, 
                   color=color, ha='center', fontweight='bold')
        
        ax_kpi.set_xlim(0, 1)
        ax_kpi.set_ylim(0, 1)
        ax_kpi.axis('off')
    
    # Asset Allocation Pie Chart
    ax_pie = fig.add_subplot(gs[2:, 0])
    ax_pie.set_facecolor(COLORS['bg_secondary'])
    
    assets = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT', 'USDT']
    sizes = [30, 22, 15, 12, 8, 13]
    colors_pie = [COLORS['color_buy'], COLORS['color_profit'], 
                  COLORS['color_warning'], COLORS['color_purple'],
                  '#FF6B9D', COLORS['text_secondary']]
    
    wedges, texts, autotexts = ax_pie.pie(sizes, labels=assets, 
                                            colors=colors_pie,
                                            autopct='%1.1f%%',
                                            startangle=90,
                                            textprops={'color': COLORS['text_primary'],
                                                      'fontsize': 11,
                                                      'fontweight': 'bold'})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    ax_pie.set_title('Asset Allocation', fontsize=16, 
                     color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    # Portfolio Performance Chart
    ax_perf = fig.add_subplot(gs[2:, 1:3])
    ax_perf.set_facecolor(COLORS['bg_secondary'])
    
    # Generate performance data
    np.random.seed(42)
    days = 90
    dates = [datetime.now() - timedelta(days=days-i) for i in range(days)]
    portfolio_value = 11000 + np.cumsum(np.random.randn(days) * 50 + 30)
    benchmark = 11000 + np.cumsum(np.random.randn(days) * 40 + 25)
    
    ax_perf.plot(dates, portfolio_value, color=COLORS['color_profit'], 
                linewidth=2.5, label='Portfolio', marker='o', markersize=2)
    ax_perf.plot(dates, benchmark, color=COLORS['color_warning'], 
                linewidth=2, label='Benchmark (BTC)', linestyle='--', alpha=0.7)
    
    ax_perf.fill_between(dates, portfolio_value, benchmark, 
                         where=(portfolio_value >= benchmark),
                         color=COLORS['color_profit'], alpha=0.2,
                         label='Outperformance')
    ax_perf.fill_between(dates, portfolio_value, benchmark, 
                         where=(portfolio_value < benchmark),
                         color=COLORS['color_sell'], alpha=0.2,
                         label='Underperformance')
    
    ax_perf.set_title('Portfolio Performance (90 Days)', fontsize=16, 
                     color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_perf.set_xlabel('Date', fontsize=11, color=COLORS['text_secondary'])
    ax_perf.set_ylabel('Value (USD)', fontsize=11, color=COLORS['text_secondary'])
    ax_perf.grid(True, alpha=0.1, color=COLORS['border'])
    ax_perf.legend(loc='upper left', framealpha=0.3, fontsize=10)
    ax_perf.tick_params(colors=COLORS['text_secondary'])
    
    # Format x-axis dates
    import matplotlib.dates as mdates
    ax_perf.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax_perf.xaxis.set_major_locator(mdates.DayLocator(interval=15))
    plt.setp(ax_perf.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Holdings Table
    ax_table = fig.add_subplot(gs[2:, 3])
    ax_table.set_facecolor(COLORS['bg_secondary'])
    ax_table.set_title('Top Holdings', fontsize=16, 
                      color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    holdings = [
        ('BTC', 0.084, '$4,200', '+12.3%'),
        ('ETH', 1.23, '$3,075', '+8.7%'),
        ('SOL', 21.5, '$2,107', '+15.2%'),
        ('ADA', 4200, '$1,680', '+6.1%'),
        ('DOT', 180, '$1,116', '+4.3%'),
        ('USDT', 1813, '$1,813', '0.0%'),
    ]
    
    y_pos = 0.95
    # Header
    ax_table.text(0.05, y_pos, 'Asset', fontsize=10, 
                 color=COLORS['text_secondary'], fontweight='bold')
    ax_table.text(0.25, y_pos, 'Amount', fontsize=10, 
                 color=COLORS['text_secondary'], fontweight='bold')
    ax_table.text(0.50, y_pos, 'Value', fontsize=10, 
                 color=COLORS['text_secondary'], fontweight='bold')
    ax_table.text(0.75, y_pos, '24h', fontsize=10, 
                 color=COLORS['text_secondary'], fontweight='bold')
    
    y_pos -= 0.08
    ax_table.plot([0.02, 0.98], [y_pos + 0.02, y_pos + 0.02], 
                 color=COLORS['border'], linewidth=1.5)
    
    y_pos -= 0.05
    
    for asset, amount, value, change in holdings:
        # Highlight row
        rect = patches.Rectangle((0.02, y_pos - 0.035), 0.96, 0.07,
                                facecolor=COLORS['bg_tertiary'], alpha=0.3)
        ax_table.add_patch(rect)
        
        ax_table.text(0.05, y_pos, asset, fontsize=10, 
                     color=COLORS['text_primary'], fontweight='bold')
        ax_table.text(0.25, y_pos, f'{amount:,.2f}', fontsize=9, 
                     color=COLORS['text_secondary'], family='monospace')
        ax_table.text(0.50, y_pos, value, fontsize=10, 
                     color=COLORS['text_primary'], fontweight='bold',
                     family='monospace')
        
        change_color = COLORS['color_profit'] if '+' in change else COLORS['text_secondary']
        ax_table.text(0.75, y_pos, change, fontsize=9, 
                     color=change_color, fontweight='bold')
        
        y_pos -= 0.13
    
    ax_table.set_xlim(0, 1)
    ax_table.set_ylim(0, 1)
    ax_table.axis('off')
    
    plt.savefig('/home/ubuntu/portfolio_overview_dashboard.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ Portfolio Overview Dashboard saved")
    plt.close()

def create_risk_analytics_dashboard():
    """Create Advanced Risk Analytics Dashboard"""
    fig = plt.figure(figsize=(24, 14), facecolor=COLORS['bg_primary'])
    
    gs = GridSpec(4, 4, figure=fig, hspace=0.4, wspace=0.4,
                  left=0.05, right=0.98, top=0.96, bottom=0.04)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'Risk Analytics Dashboard', 
                   fontsize=26, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.95, 0.5, 'Risk Score: 6.2/10 (MODERATE)', 
                   fontsize=14, color=COLORS['color_warning'], 
                   va='center', ha='right', fontweight='bold')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # Risk Metrics Gauges
    risk_metrics = [
        ('Volatility', 18.5, 25, '%'),
        ('VaR (95%)', 5.2, 10, '%'),
        ('Beta', 0.85, 1.5, ''),
        ('Max Drawdown', 12.3, 20, '%'),
    ]
    
    for idx, (label, value, max_val, unit) in enumerate(risk_metrics):
        ax_gauge = fig.add_subplot(gs[1, idx])
        ax_gauge.set_facecolor(COLORS['bg_secondary'])
        
        # Create gauge
        theta = np.linspace(0, np.pi, 100)
        r = 0.8
        
        # Background arc
        ax_gauge.plot(r * np.cos(theta), r * np.sin(theta), 
                     color=COLORS['border'], linewidth=8, alpha=0.3)
        
        # Value arc
        value_theta = np.linspace(0, np.pi * (value / max_val), 100)
        
        # Color based on risk level
        if value / max_val < 0.5:
            arc_color = COLORS['color_profit']
        elif value / max_val < 0.75:
            arc_color = COLORS['color_warning']
        else:
            arc_color = COLORS['color_sell']
        
        ax_gauge.plot(r * np.cos(value_theta), r * np.sin(value_theta), 
                     color=arc_color, linewidth=8)
        
        # Center text
        ax_gauge.text(0, -0.2, f'{value}{unit}', fontsize=20, 
                     color=COLORS['text_primary'], ha='center', 
                     fontweight='bold', family='monospace')
        ax_gauge.text(0, -0.45, label, fontsize=11, 
                     color=COLORS['text_secondary'], ha='center')
        ax_gauge.text(0, -0.6, f'Max: {max_val}{unit}', fontsize=9, 
                     color=COLORS['text_secondary'], ha='center', alpha=0.7)
        
        ax_gauge.set_xlim(-1, 1)
        ax_gauge.set_ylim(-0.7, 1)
        ax_gauge.axis('off')
    
    # Drawdown Chart
    ax_dd = fig.add_subplot(gs[2, :2])
    ax_dd.set_facecolor(COLORS['bg_secondary'])
    
    np.random.seed(42)
    days = 90
    returns = np.random.randn(days) * 0.02
    cumulative = np.cumprod(1 + returns)
    running_max = np.maximum.accumulate(cumulative)
    drawdown = (cumulative - running_max) / running_max * 100
    
    ax_dd.fill_between(range(days), drawdown, 0, 
                       color=COLORS['color_sell'], alpha=0.4)
    ax_dd.plot(range(days), drawdown, color=COLORS['color_sell'], 
              linewidth=2)
    
    ax_dd.set_title('Drawdown Analysis', fontsize=16, 
                   color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_dd.set_xlabel('Days', fontsize=11, color=COLORS['text_secondary'])
    ax_dd.set_ylabel('Drawdown (%)', fontsize=11, color=COLORS['text_secondary'])
    ax_dd.grid(True, alpha=0.1, color=COLORS['border'])
    ax_dd.tick_params(colors=COLORS['text_secondary'])
    ax_dd.axhline(0, color=COLORS['text_secondary'], linewidth=1, linestyle='--')
    
    # Value at Risk Distribution
    ax_var = fig.add_subplot(gs[2, 2:])
    ax_var.set_facecolor(COLORS['bg_secondary'])
    
    returns_dist = np.random.normal(0.001, 0.02, 10000)
    var_95 = np.percentile(returns_dist, 5)
    var_99 = np.percentile(returns_dist, 1)
    
    n, bins, patches_hist = ax_var.hist(returns_dist * 100, bins=50, 
                                        color=COLORS['color_buy'], alpha=0.6,
                                        edgecolor='none')
    
    # Color the tail
    for i, patch in enumerate(patches_hist):
        if bins[i] < var_95 * 100:
            patch.set_facecolor(COLORS['color_sell'])
            patch.set_alpha(0.8)
    
    ax_var.axvline(var_95 * 100, color=COLORS['color_warning'], 
                  linewidth=2, linestyle='--', label=f'VaR 95%: {var_95*100:.2f}%')
    ax_var.axvline(var_99 * 100, color=COLORS['color_sell'], 
                  linewidth=2, linestyle='--', label=f'VaR 99%: {var_99*100:.2f}%')
    
    ax_var.set_title('Value at Risk Distribution', fontsize=16, 
                    color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_var.set_xlabel('Daily Returns (%)', fontsize=11, color=COLORS['text_secondary'])
    ax_var.set_ylabel('Frequency', fontsize=11, color=COLORS['text_secondary'])
    ax_var.legend(loc='upper left', framealpha=0.3, fontsize=10)
    ax_var.grid(True, alpha=0.1, color=COLORS['border'], axis='y')
    ax_var.tick_params(colors=COLORS['text_secondary'])
    
    # Risk Contribution by Asset
    ax_contrib = fig.add_subplot(gs[3, :2])
    ax_contrib.set_facecolor(COLORS['bg_secondary'])
    
    assets_risk = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT']
    risk_contrib = [35, 28, 18, 12, 7]
    
    bars = ax_contrib.barh(assets_risk, risk_contrib, 
                          color=[COLORS['color_buy'], COLORS['color_profit'],
                                COLORS['color_warning'], COLORS['color_purple'],
                                '#FF6B9D'])
    
    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax_contrib.text(width + 1, bar.get_y() + bar.get_height()/2,
                       f'{width}%',
                       ha='left', va='center', fontsize=11,
                       color=COLORS['text_primary'], fontweight='bold')
    
    ax_contrib.set_title('Risk Contribution by Asset', fontsize=16, 
                        color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_contrib.set_xlabel('Risk Contribution (%)', fontsize=11, 
                          color=COLORS['text_secondary'])
    ax_contrib.grid(True, alpha=0.1, color=COLORS['border'], axis='x')
    ax_contrib.tick_params(colors=COLORS['text_secondary'])
    ax_contrib.set_xlim(0, max(risk_contrib) * 1.2)
    
    # Correlation Heatmap
    ax_corr = fig.add_subplot(gs[3, 2:])
    ax_corr.set_facecolor(COLORS['bg_secondary'])
    
    assets_corr = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT']
    corr_matrix = np.array([
        [1.00, 0.85, 0.72, 0.68, 0.63],
        [0.85, 1.00, 0.78, 0.71, 0.67],
        [0.72, 0.78, 1.00, 0.65, 0.61],
        [0.68, 0.71, 0.65, 1.00, 0.58],
        [0.63, 0.67, 0.61, 0.58, 1.00]
    ])
    
    im = ax_corr.imshow(corr_matrix, cmap='RdYlGn', vmin=0, vmax=1, aspect='auto')
    
    ax_corr.set_xticks(np.arange(len(assets_corr)))
    ax_corr.set_yticks(np.arange(len(assets_corr)))
    ax_corr.set_xticklabels(assets_corr, color=COLORS['text_primary'], fontsize=11)
    ax_corr.set_yticklabels(assets_corr, color=COLORS['text_primary'], fontsize=11)
    
    # Add correlation values
    for i in range(len(assets_corr)):
        for j in range(len(assets_corr)):
            text = ax_corr.text(j, i, f'{corr_matrix[i, j]:.2f}',
                               ha="center", va="center", 
                               color="white", fontweight='bold', fontsize=10)
    
    ax_corr.set_title('Asset Correlation Matrix', fontsize=16, 
                     color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax_corr, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(colors=COLORS['text_secondary'])
    
    plt.savefig('/home/ubuntu/risk_analytics_dashboard.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ Risk Analytics Dashboard saved")
    plt.close()

def create_rebalancing_dashboard():
    """Create Portfolio Rebalancing Dashboard"""
    fig = plt.figure(figsize=(24, 14), facecolor=COLORS['bg_primary'])
    
    gs = GridSpec(4, 3, figure=fig, hspace=0.4, wspace=0.4,
                  left=0.05, right=0.98, top=0.96, bottom=0.04)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'Portfolio Rebalancing Dashboard', 
                   fontsize=26, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.95, 0.5, 'Rebalancing Needed: YES', 
                   fontsize=14, color=COLORS['color_warning'], 
                   va='center', ha='right', fontweight='bold')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # Target vs Actual Allocation
    ax_alloc = fig.add_subplot(gs[1:3, 0])
    ax_alloc.set_facecolor(COLORS['bg_secondary'])
    
    assets_alloc = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT', 'USDT']
    target_alloc = [25, 25, 15, 10, 10, 15]
    actual_alloc = [30, 22, 15, 12, 8, 13]
    
    x_pos = np.arange(len(assets_alloc))
    width = 0.35
    
    bars1 = ax_alloc.bar(x_pos - width/2, target_alloc, width,
                        color=COLORS['color_profit'], alpha=0.7, label='Target')
    bars2 = ax_alloc.bar(x_pos + width/2, actual_alloc, width,
                        color=COLORS['color_buy'], alpha=0.7, label='Actual')
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax_alloc.text(bar.get_x() + bar.get_width()/2., height,
                     f'{height}%',
                     ha='center', va='bottom', fontsize=10,
                     color=COLORS['text_primary'])
    
    for bar in bars2:
        height = bar.get_height()
        ax_alloc.text(bar.get_x() + bar.get_width()/2., height,
                     f'{height}%',
                     ha='center', va='bottom', fontsize=10,
                     color=COLORS['text_primary'])
    
    ax_alloc.set_title('Target vs Actual Allocation', fontsize=16, 
                      color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_alloc.set_ylabel('Allocation (%)', fontsize=11, color=COLORS['text_secondary'])
    ax_alloc.set_xticks(x_pos)
    ax_alloc.set_xticklabels(assets_alloc, fontsize=11, color=COLORS['text_primary'])
    ax_alloc.legend(loc='upper right', framealpha=0.3, fontsize=11)
    ax_alloc.grid(True, alpha=0.1, color=COLORS['border'], axis='y')
    ax_alloc.tick_params(colors=COLORS['text_secondary'])
    
    # Deviation from Target
    ax_dev = fig.add_subplot(gs[1:3, 1])
    ax_dev.set_facecolor(COLORS['bg_secondary'])
    
    deviation = [actual - target for actual, target in zip(actual_alloc, target_alloc)]
    colors_dev = [COLORS['color_profit'] if d < 0 else COLORS['color_sell'] for d in deviation]
    
    bars_dev = ax_dev.barh(assets_alloc, deviation, color=colors_dev, alpha=0.7)
    
    # Add value labels
    for bar in bars_dev:
        width = bar.get_width()
        label_x = width + 0.2 if width > 0 else width - 0.2
        ax_dev.text(label_x, bar.get_y() + bar.get_height()/2,
                   f'{width:+.1f}%',
                   ha='left' if width > 0 else 'right', va='center', 
                   fontsize=10, color=COLORS['text_primary'], fontweight='bold')
    
    ax_dev.axvline(0, color=COLORS['text_secondary'], linewidth=2, linestyle='-')
    ax_dev.set_title('Deviation from Target', fontsize=16, 
                    color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_dev.set_xlabel('Deviation (%)', fontsize=11, color=COLORS['text_secondary'])
    ax_dev.grid(True, alpha=0.1, color=COLORS['border'], axis='x')
    ax_dev.tick_params(colors=COLORS['text_secondary'])
    
    # Rebalancing Actions
    ax_actions = fig.add_subplot(gs[1:3, 2])
    ax_actions.set_facecolor(COLORS['bg_secondary'])
    ax_actions.set_title('Recommended Actions', fontsize=16, 
                        color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    actions = [
        ('SELL', 'BTC', 0.014, '$700', COLORS['color_sell']),
        ('BUY', 'ETH', 0.12, '$300', COLORS['color_profit']),
        ('HOLD', 'SOL', 0, '$0', COLORS['text_secondary']),
        ('BUY', 'ADA', 500, '$200', COLORS['color_profit']),
        ('BUY', 'DOT', 32, '$200', COLORS['color_profit']),
        ('BUY', 'USDT', 200, '$200', COLORS['color_profit']),
    ]
    
    y_pos = 0.95
    # Header
    ax_actions.text(0.05, y_pos, 'Action', fontsize=10, 
                   color=COLORS['text_secondary'], fontweight='bold')
    ax_actions.text(0.25, y_pos, 'Asset', fontsize=10, 
                   color=COLORS['text_secondary'], fontweight='bold')
    ax_actions.text(0.45, y_pos, 'Amount', fontsize=10, 
                   color=COLORS['text_secondary'], fontweight='bold')
    ax_actions.text(0.75, y_pos, 'Value', fontsize=10, 
                   color=COLORS['text_secondary'], fontweight='bold')
    
    y_pos -= 0.08
    ax_actions.plot([0.02, 0.98], [y_pos + 0.02, y_pos + 0.02], 
                   color=COLORS['border'], linewidth=1.5)
    
    y_pos -= 0.05
    
    for action, asset, amount, value, color in actions:
        # Action button
        btn_rect = patches.FancyBboxPatch((0.03, y_pos - 0.025), 0.15, 0.05,
                                         boxstyle="round,pad=0.005",
                                         facecolor=color, alpha=0.3,
                                         edgecolor=color, linewidth=1.5)
        ax_actions.add_patch(btn_rect)
        ax_actions.text(0.105, y_pos, action, fontsize=9, 
                       color=color, ha='center', va='center', fontweight='bold')
        
        ax_actions.text(0.25, y_pos, asset, fontsize=10, 
                       color=COLORS['text_primary'], fontweight='bold')
        
        if amount != 0:
            ax_actions.text(0.45, y_pos, f'{amount:,.3f}', fontsize=9, 
                           color=COLORS['text_secondary'], family='monospace')
        else:
            ax_actions.text(0.45, y_pos, '-', fontsize=9, 
                           color=COLORS['text_secondary'])
        
        ax_actions.text(0.75, y_pos, value, fontsize=10, 
                       color=COLORS['text_primary'], fontweight='bold',
                       family='monospace')
        
        y_pos -= 0.13
    
    ax_actions.set_xlim(0, 1)
    ax_actions.set_ylim(0, 1)
    ax_actions.axis('off')
    
    # Rebalancing Impact
    ax_impact = fig.add_subplot(gs[3, :])
    ax_impact.set_facecolor(COLORS['bg_secondary'])
    ax_impact.set_title('Rebalancing Impact Analysis', fontsize=16, 
                       color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    metrics_impact = [
        ('Expected Return', '12.5%', '13.2%', '+0.7%'),
        ('Portfolio Risk', '18.5%', '17.2%', '-1.3%'),
        ('Sharpe Ratio', '2.34', '2.51', '+0.17'),
        ('Diversification', '0.68', '0.75', '+0.07'),
        ('Transaction Costs', '-', '$35', '$35'),
    ]
    
    y_impact = 0.85
    # Header
    ax_impact.text(0.05, y_impact, 'Metric', fontsize=11, 
                  color=COLORS['text_secondary'], fontweight='bold')
    ax_impact.text(0.35, y_impact, 'Current', fontsize=11, 
                  color=COLORS['text_secondary'], fontweight='bold')
    ax_impact.text(0.55, y_impact, 'After Rebalancing', fontsize=11, 
                  color=COLORS['text_secondary'], fontweight='bold')
    ax_impact.text(0.85, y_impact, 'Change', fontsize=11, 
                  color=COLORS['text_secondary'], fontweight='bold')
    
    y_impact -= 0.12
    ax_impact.plot([0.02, 0.98], [y_impact + 0.04, y_impact + 0.04], 
                  color=COLORS['border'], linewidth=2)
    
    y_impact -= 0.08
    
    for metric, current, after, change in metrics_impact:
        ax_impact.text(0.05, y_impact, metric, fontsize=11, 
                      color=COLORS['text_primary'])
        ax_impact.text(0.35, y_impact, current, fontsize=11, 
                      color=COLORS['text_primary'], family='monospace',
                      fontweight='bold')
        ax_impact.text(0.55, y_impact, after, fontsize=11, 
                      color=COLORS['text_primary'], family='monospace',
                      fontweight='bold')
        
        if '+' in change:
            change_color = COLORS['color_profit']
        elif '-' in change and change != '-':
            change_color = COLORS['color_sell']
        else:
            change_color = COLORS['text_secondary']
        
        ax_impact.text(0.85, y_impact, change, fontsize=11, 
                      color=change_color, fontweight='bold')
        
        y_impact -= 0.15
    
    ax_impact.set_xlim(0, 1)
    ax_impact.set_ylim(0, 1)
    ax_impact.axis('off')
    
    plt.savefig('/home/ubuntu/rebalancing_dashboard.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ Rebalancing Dashboard saved")
    plt.close()

if __name__ == '__main__':
    print("=" * 70)
    print("GENERATING PORTFOLIO MANAGEMENT DASHBOARDS")
    print("=" * 70)
    
    create_portfolio_overview()
    create_risk_analytics_dashboard()
    create_rebalancing_dashboard()
    
    print("")
    print("=" * 70)
    print("✅ ALL PORTFOLIO DASHBOARDS GENERATED SUCCESSFULLY!")
    print("=" * 70)
    print("")
    print("📸 Generated dashboards:")
    print("   1. portfolio_overview_dashboard.png")
    print("   2. risk_analytics_dashboard.png")
    print("   3. rebalancing_dashboard.png")
    print("")

