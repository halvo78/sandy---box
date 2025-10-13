#!/usr/bin/env python3
"""
Generate HFT Strategy Visualizations and Exchange Fee Management Panel
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.colors as mcolors

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
    'text_primary': '#FFFFFF',
    'text_secondary': '#8B93B0',
    'border': '#2F3659',
}

def create_hft_dashboard():
    """Create comprehensive HFT strategy dashboard"""
    fig = plt.figure(figsize=(24, 14), facecolor=COLORS['bg_primary'])
    
    gs = GridSpec(4, 4, figure=fig, hspace=0.35, wspace=0.35,
                  left=0.05, right=0.98, top=0.96, bottom=0.04)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'LYRA HFT Strategy Dashboard', 
                   fontsize=26, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.5, 0.5, 'Latency: 0.8ms | Orders/sec: 1,247', 
                   fontsize=14, color=COLORS['text_primary'], va='center')
    ax_header.text(0.95, 0.5, 'Status: ACTIVE', 
                   fontsize=16, color=COLORS['color_profit'], 
                   va='center', ha='right', fontweight='bold')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # 1. Order Flow Heatmap
    ax_flow = fig.add_subplot(gs[1:3, :2])
    ax_flow.set_facecolor(COLORS['bg_secondary'])
    
    # Generate order flow data
    np.random.seed(42)
    time_bins = 60
    price_bins = 30
    
    # Create bid/ask flow
    bid_flow = np.random.exponential(2, (price_bins//2, time_bins))
    ask_flow = np.random.exponential(2, (price_bins//2, time_bins))
    
    # Combine with neutral zone
    flow_data = np.vstack([ask_flow[::-1], bid_flow])
    
    # Create custom colormap (red for asks, green for bids)
    colors_list = ['#FF3366', '#FF6688', '#8B93B0', '#00FF88', '#00D9FF']
    n_bins = 100
    cmap = mcolors.LinearSegmentedColormap.from_list('custom', colors_list, N=n_bins)
    
    im = ax_flow.imshow(flow_data, aspect='auto', cmap=cmap, 
                        interpolation='bilinear', alpha=0.9)
    
    ax_flow.set_title('Order Flow Heatmap (Real-Time)', fontsize=18, 
                     color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_flow.set_xlabel('Time (seconds)', fontsize=12, color=COLORS['text_secondary'])
    ax_flow.set_ylabel('Price Levels', fontsize=12, color=COLORS['text_secondary'])
    ax_flow.tick_params(colors=COLORS['text_secondary'])
    
    # Add spread indicator
    ax_flow.axhline(price_bins//2, color=COLORS['text_primary'], 
                   linewidth=2, linestyle='--', alpha=0.7, label='Spread')
    ax_flow.legend(loc='upper right', framealpha=0.3)
    
    # 2. Latency Metrics
    ax_latency = fig.add_subplot(gs[1, 2:])
    ax_latency.set_facecolor(COLORS['bg_secondary'])
    
    # Generate latency data
    time_points = np.arange(100)
    latency_data = 0.5 + np.random.exponential(0.3, 100)
    latency_data = np.clip(latency_data, 0.1, 5)  # Clip outliers
    
    # Plot latency
    ax_latency.plot(time_points, latency_data, color=COLORS['color_buy'], 
                   linewidth=2, alpha=0.8)
    ax_latency.fill_between(time_points, latency_data, 
                           color=COLORS['color_buy'], alpha=0.2)
    
    # Add threshold lines
    ax_latency.axhline(1.0, color=COLORS['color_profit'], linewidth=2, 
                      linestyle='--', alpha=0.6, label='Target (1ms)')
    ax_latency.axhline(2.0, color=COLORS['color_warning'], linewidth=2, 
                      linestyle='--', alpha=0.6, label='Warning (2ms)')
    ax_latency.axhline(5.0, color=COLORS['color_sell'], linewidth=2, 
                      linestyle='--', alpha=0.6, label='Critical (5ms)')
    
    ax_latency.set_title('Execution Latency (ms)', fontsize=16, 
                        color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_latency.set_xlabel('Time', fontsize=11, color=COLORS['text_secondary'])
    ax_latency.set_ylabel('Latency (ms)', fontsize=11, color=COLORS['text_secondary'])
    ax_latency.set_ylim(0, 6)
    ax_latency.grid(True, alpha=0.1, color=COLORS['border'])
    ax_latency.legend(loc='upper right', framealpha=0.3, fontsize=9)
    ax_latency.tick_params(colors=COLORS['text_secondary'])
    
    # 3. Market Microstructure
    ax_micro = fig.add_subplot(gs[2, 2:])
    ax_micro.set_facecolor(COLORS['bg_secondary'])
    
    # Generate tick data
    ticks = np.arange(200)
    bid_prices = 50000 + np.cumsum(np.random.randn(200) * 0.5)
    ask_prices = bid_prices + np.random.uniform(5, 15, 200)
    mid_prices = (bid_prices + ask_prices) / 2
    
    # Plot bid/ask/mid
    ax_micro.plot(ticks, bid_prices, color=COLORS['color_profit'], 
                 linewidth=1.5, alpha=0.7, label='Bid')
    ax_micro.plot(ticks, ask_prices, color=COLORS['color_sell'], 
                 linewidth=1.5, alpha=0.7, label='Ask')
    ax_micro.plot(ticks, mid_prices, color=COLORS['color_buy'], 
                 linewidth=2, alpha=0.9, label='Mid Price')
    
    # Fill spread
    ax_micro.fill_between(ticks, bid_prices, ask_prices, 
                         color=COLORS['text_secondary'], alpha=0.1)
    
    ax_micro.set_title('Market Microstructure (Tick-by-Tick)', fontsize=16, 
                      color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_micro.set_xlabel('Ticks', fontsize=11, color=COLORS['text_secondary'])
    ax_micro.set_ylabel('Price (USD)', fontsize=11, color=COLORS['text_secondary'])
    ax_micro.grid(True, alpha=0.1, color=COLORS['border'])
    ax_micro.legend(loc='upper left', framealpha=0.3, fontsize=9)
    ax_micro.tick_params(colors=COLORS['text_secondary'])
    
    # 4. Execution Quality Metrics
    ax_quality = fig.add_subplot(gs[3, :2])
    ax_quality.set_facecolor(COLORS['bg_secondary'])
    
    metrics = ['Fill Rate', 'Slippage', 'Maker %', 'Adverse\nSelection', 'Spread\nCapture']
    values = [98.7, 0.02, 67.3, 0.15, 45.2]
    targets = [99.0, 0.01, 70.0, 0.10, 50.0]
    
    x_pos = np.arange(len(metrics))
    width = 0.35
    
    bars1 = ax_quality.bar(x_pos - width/2, values, width, 
                          color=COLORS['color_buy'], alpha=0.8, label='Current')
    bars2 = ax_quality.bar(x_pos + width/2, targets, width, 
                          color=COLORS['color_profit'], alpha=0.5, label='Target')
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax_quality.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.2f}',
                       ha='center', va='bottom', fontsize=10,
                       color=COLORS['text_primary'], fontweight='bold')
    
    ax_quality.set_title('Execution Quality Metrics', fontsize=16, 
                        color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_quality.set_ylabel('Value', fontsize=11, color=COLORS['text_secondary'])
    ax_quality.set_xticks(x_pos)
    ax_quality.set_xticklabels(metrics, fontsize=10, color=COLORS['text_primary'])
    ax_quality.legend(loc='upper right', framealpha=0.3)
    ax_quality.grid(True, alpha=0.1, color=COLORS['border'], axis='y')
    ax_quality.tick_params(colors=COLORS['text_secondary'])
    
    # 5. Order Book Imbalance
    ax_imbalance = fig.add_subplot(gs[3, 2:])
    ax_imbalance.set_facecolor(COLORS['bg_secondary'])
    
    # Generate imbalance data
    time_imb = np.arange(100)
    imbalance = np.cumsum(np.random.randn(100) * 0.1)
    imbalance = np.clip(imbalance, -1, 1)
    
    # Color based on imbalance
    colors_imb = [COLORS['color_profit'] if x > 0 else COLORS['color_sell'] 
                  for x in imbalance]
    
    ax_imbalance.bar(time_imb, imbalance, color=colors_imb, alpha=0.7, width=1)
    ax_imbalance.axhline(0, color=COLORS['text_secondary'], linewidth=1, 
                        linestyle='-', alpha=0.5)
    
    ax_imbalance.set_title('Order Book Imbalance', fontsize=16, 
                          color=COLORS['text_primary'], pad=15, fontweight='bold')
    ax_imbalance.set_xlabel('Time', fontsize=11, color=COLORS['text_secondary'])
    ax_imbalance.set_ylabel('Imbalance', fontsize=11, color=COLORS['text_secondary'])
    ax_imbalance.set_ylim(-1.2, 1.2)
    ax_imbalance.grid(True, alpha=0.1, color=COLORS['border'], axis='y')
    ax_imbalance.tick_params(colors=COLORS['text_secondary'])
    
    # Add legend
    bid_patch = patches.Patch(color=COLORS['color_profit'], label='Bid Heavy')
    ask_patch = patches.Patch(color=COLORS['color_sell'], label='Ask Heavy')
    ax_imbalance.legend(handles=[bid_patch, ask_patch], loc='upper right', 
                       framealpha=0.3, fontsize=9)
    
    plt.savefig('/home/ubuntu/hft_dashboard_mockup.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ HFT Dashboard mockup saved")
    plt.close()

def create_fee_management_panel():
    """Create Exchange Fee Management Panel"""
    fig = plt.figure(figsize=(20, 14), facecolor=COLORS['bg_primary'])
    
    gs = GridSpec(5, 3, figure=fig, hspace=0.4, wspace=0.35,
                  left=0.06, right=0.97, top=0.95, bottom=0.05)
    
    # Header
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(COLORS['bg_secondary'])
    ax_header.text(0.02, 0.5, 'Exchange Fee Management & Lock-In', 
                   fontsize=26, fontweight='bold', color=COLORS['color_buy'],
                   va='center')
    ax_header.text(0.95, 0.5, 'Last Updated: 2025-10-12 14:23:45 UTC', 
                   fontsize=12, color=COLORS['text_secondary'], 
                   va='center', ha='right')
    ax_header.set_xlim(0, 1)
    ax_header.set_ylim(0, 1)
    ax_header.axis('off')
    
    # Exchange fee data
    exchanges = [
        ('OKX', 0.08, 0.10, '2025-10-12', True),
        ('Binance', 0.10, 0.10, '2025-10-12', True),
        ('Coinbase', 0.40, 0.60, '2025-10-10', True),
        ('Kraken', 0.16, 0.26, '2025-10-11', True),
        ('Gate.io', 0.15, 0.20, '2025-10-12', True),
        ('Bitfinex', 0.10, 0.20, '2025-10-09', False),
        ('Bitstamp', 0.30, 0.50, '2025-10-08', False),
        ('Gemini', 0.25, 0.35, '2025-10-12', True),
    ]
    
    # 1. Fee Input Panel (Top Left)
    ax_input = fig.add_subplot(gs[1:3, 0])
    ax_input.set_facecolor(COLORS['bg_secondary'])
    ax_input.set_title('Fee Input & Lock-In', fontsize=16, 
                      color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    y_pos = 0.95
    ax_input.text(0.5, y_pos, 'Enter Current Exchange Fees', 
                 fontsize=13, color=COLORS['text_primary'], 
                 ha='center', fontweight='bold')
    y_pos -= 0.08
    
    # Example input fields
    for i, (exchange, maker, taker, _, locked) in enumerate(exchanges[:4]):
        # Exchange name
        ax_input.text(0.05, y_pos, exchange, fontsize=11, 
                     color=COLORS['text_primary'], fontweight='bold')
        
        # Maker fee input box
        rect_maker = patches.FancyBboxPatch((0.35, y_pos - 0.03), 0.25, 0.05,
                                           boxstyle="round,pad=0.01",
                                           facecolor=COLORS['bg_tertiary'],
                                           edgecolor=COLORS['border'], linewidth=1)
        ax_input.add_patch(rect_maker)
        ax_input.text(0.475, y_pos, f'{maker:.2f}%', fontsize=10, 
                     color=COLORS['text_primary'], ha='center', va='center',
                     family='monospace')
        ax_input.text(0.32, y_pos, 'M:', fontsize=9, 
                     color=COLORS['text_secondary'], ha='right', va='center')
        
        # Taker fee input box
        rect_taker = patches.FancyBboxPatch((0.65, y_pos - 0.03), 0.25, 0.05,
                                           boxstyle="round,pad=0.01",
                                           facecolor=COLORS['bg_tertiary'],
                                           edgecolor=COLORS['border'], linewidth=1)
        ax_input.add_patch(rect_taker)
        ax_input.text(0.775, y_pos, f'{taker:.2f}%', fontsize=10, 
                     color=COLORS['text_primary'], ha='center', va='center',
                     family='monospace')
        ax_input.text(0.62, y_pos, 'T:', fontsize=9, 
                     color=COLORS['text_secondary'], ha='right', va='center')
        
        y_pos -= 0.12
    
    # Lock button
    lock_btn = patches.FancyBboxPatch((0.25, y_pos - 0.02), 0.5, 0.08,
                                     boxstyle="round,pad=0.01",
                                     facecolor=COLORS['color_buy'],
                                     edgecolor='none')
    ax_input.add_patch(lock_btn)
    ax_input.text(0.5, y_pos + 0.02, '🔒 LOCK IN FEES', fontsize=12, 
                 color='#0A0E27', ha='center', va='center', fontweight='bold')
    
    ax_input.set_xlim(0, 1)
    ax_input.set_ylim(0, 1)
    ax_input.axis('off')
    
    # 2. Fee Comparison Table (Top Right)
    ax_table = fig.add_subplot(gs[1:3, 1:])
    ax_table.set_facecolor(COLORS['bg_secondary'])
    ax_table.set_title('Exchange Fee Comparison', fontsize=16, 
                      color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    # Table header
    y_table = 0.95
    headers = ['Exchange', 'Maker', 'Taker', 'Locked Date', 'Status']
    x_positions = [0.05, 0.30, 0.47, 0.64, 0.85]
    
    for x, header in zip(x_positions, headers):
        ax_table.text(x, y_table, header, fontsize=11, 
                     color=COLORS['text_secondary'], fontweight='bold')
    
    # Separator line
    ax_table.plot([0.02, 0.98], [y_table - 0.03, y_table - 0.03], 
                 color=COLORS['border'], linewidth=2)
    
    y_table -= 0.08
    
    # Table rows
    for exchange, maker, taker, date, locked in exchanges:
        # Highlight row
        if locked:
            rect = patches.Rectangle((0.02, y_table - 0.035), 0.96, 0.06,
                                    facecolor=COLORS['bg_tertiary'], alpha=0.5)
            ax_table.add_patch(rect)
        
        ax_table.text(x_positions[0], y_table, exchange, fontsize=10, 
                     color=COLORS['text_primary'], fontweight='bold')
        ax_table.text(x_positions[1], y_table, f'{maker:.2f}%', fontsize=10, 
                     color=COLORS['color_profit'], family='monospace')
        ax_table.text(x_positions[2], y_table, f'{taker:.2f}%', fontsize=10, 
                     color=COLORS['color_sell'], family='monospace')
        ax_table.text(x_positions[3], y_table, date, fontsize=9, 
                     color=COLORS['text_secondary'], family='monospace')
        
        status_color = COLORS['color_profit'] if locked else COLORS['text_secondary']
        status_text = '🔒 Locked' if locked else '⚠️ Update'
        ax_table.text(x_positions[4], y_table, status_text, fontsize=9, 
                     color=status_color, fontweight='bold')
        
        y_table -= 0.1
    
    ax_table.set_xlim(0, 1)
    ax_table.set_ylim(0, 1)
    ax_table.axis('off')
    
    # 3. Fee Impact Calculator (Bottom Left)
    ax_calc = fig.add_subplot(gs[3:, 0])
    ax_calc.set_facecolor(COLORS['bg_secondary'])
    ax_calc.set_title('Fee Impact Calculator', fontsize=16, 
                     color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    y_calc = 0.9
    
    # Input fields
    calc_inputs = [
        ('Trade Size:', '$1,000'),
        ('Entry Fee:', '0.10%'),
        ('Exit Fee:', '0.10%'),
        ('Target Profit:', '2.40%'),
    ]
    
    for label, value in calc_inputs:
        ax_calc.text(0.05, y_calc, label, fontsize=11, 
                    color=COLORS['text_secondary'])
        
        rect = patches.FancyBboxPatch((0.45, y_calc - 0.03), 0.50, 0.06,
                                     boxstyle="round,pad=0.01",
                                     facecolor=COLORS['bg_tertiary'],
                                     edgecolor=COLORS['border'], linewidth=1)
        ax_calc.add_patch(rect)
        ax_calc.text(0.70, y_calc, value, fontsize=11, 
                    color=COLORS['text_primary'], ha='center', va='center',
                    family='monospace', fontweight='bold')
        
        y_calc -= 0.15
    
    # Separator
    ax_calc.plot([0.05, 0.95], [y_calc + 0.05, y_calc + 0.05], 
                color=COLORS['border'], linewidth=2)
    y_calc -= 0.05
    
    # Results
    results = [
        ('Total Fees:', '$2.00', COLORS['color_sell']),
        ('Net Profit:', '$22.00', COLORS['color_profit']),
        ('ROI:', '2.20%', COLORS['color_profit']),
    ]
    
    for label, value, color in results:
        ax_calc.text(0.05, y_calc, label, fontsize=12, 
                    color=COLORS['text_secondary'], fontweight='bold')
        ax_calc.text(0.95, y_calc, value, fontsize=13, 
                    color=color, ha='right', fontweight='bold',
                    family='monospace')
        y_calc -= 0.12
    
    ax_calc.set_xlim(0, 1)
    ax_calc.set_ylim(0, 1)
    ax_calc.axis('off')
    
    # 4. Fee Visualization (Bottom Right)
    ax_viz = fig.add_subplot(gs[3:, 1:])
    ax_viz.set_facecolor(COLORS['bg_secondary'])
    ax_viz.set_title('Fee Comparison Across Exchanges', fontsize=16, 
                    color=COLORS['text_primary'], pad=15, fontweight='bold')
    
    # Extract data for visualization
    exch_names = [e[0] for e in exchanges]
    maker_fees = [e[1] for e in exchanges]
    taker_fees = [e[2] for e in exchanges]
    
    x_viz = np.arange(len(exch_names))
    width_viz = 0.35
    
    bars_maker = ax_viz.bar(x_viz - width_viz/2, maker_fees, width_viz,
                           color=COLORS['color_profit'], alpha=0.8, label='Maker Fee')
    bars_taker = ax_viz.bar(x_viz + width_viz/2, taker_fees, width_viz,
                           color=COLORS['color_sell'], alpha=0.8, label='Taker Fee')
    
    # Add value labels
    for bar in bars_maker:
        height = bar.get_height()
        ax_viz.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}%',
                   ha='center', va='bottom', fontsize=9,
                   color=COLORS['text_primary'])
    
    for bar in bars_taker:
        height = bar.get_height()
        ax_viz.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}%',
                   ha='center', va='bottom', fontsize=9,
                   color=COLORS['text_primary'])
    
    ax_viz.set_ylabel('Fee (%)', fontsize=12, color=COLORS['text_secondary'])
    ax_viz.set_xticks(x_viz)
    ax_viz.set_xticklabels(exch_names, fontsize=10, 
                          color=COLORS['text_primary'], rotation=45, ha='right')
    ax_viz.legend(loc='upper right', framealpha=0.3, fontsize=11)
    ax_viz.grid(True, alpha=0.1, color=COLORS['border'], axis='y')
    ax_viz.tick_params(colors=COLORS['text_secondary'])
    ax_viz.set_ylim(0, max(taker_fees) * 1.2)
    
    plt.savefig('/home/ubuntu/fee_management_mockup.png', 
                dpi=150, facecolor=COLORS['bg_primary'], 
                edgecolor='none', bbox_inches='tight')
    print("✅ Fee Management Panel mockup saved")
    plt.close()

if __name__ == '__main__':
    print("=" * 70)
    print("GENERATING HFT & FEE MANAGEMENT MOCKUPS")
    print("=" * 70)
    
    create_hft_dashboard()
    create_fee_management_panel()
    
    print("")
    print("=" * 70)
    print("✅ ALL HFT MOCKUPS GENERATED SUCCESSFULLY!")
    print("=" * 70)
    print("")
    print("📸 Generated mockups:")
    print("   1. hft_dashboard_mockup.png")
    print("   2. fee_management_mockup.png")
    print("")

