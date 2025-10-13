export function PositionManager() {
  const positions = [
    { pair: 'BTC/USDT', size: 0.5, entry: 49500, current: 50000, pnl: 250, pnlPercent: 1.01 },
    { pair: 'ETH/USDT', size: 10, entry: 2800, current: 2850, pnl: 500, pnlPercent: 1.79 },
  ]
  
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-title">Open Positions</h3>
        <button className="btn-primary btn-sm">New Trade</button>
      </div>
      <div className="positions-container">
        {positions.map((pos, i) => (
          <div key={i} className="position-card">
            <div className="position-header">
              <span className="position-pair">{pos.pair}</span>
              <span className={`position-pnl ${pos.pnl > 0 ? 'profit' : 'loss'}`}>
                +${pos.pnl.toFixed(2)} ({pos.pnlPercent.toFixed(2)}%)
              </span>
            </div>
            <div className="position-details">
              <div className="position-detail">
                <span className="label">Size:</span>
                <span className="value">{pos.size}</span>
              </div>
              <div className="position-detail">
                <span className="label">Entry:</span>
                <span className="value">${pos.entry.toLocaleString()}</span>
              </div>
              <div className="position-detail">
                <span className="label">Current:</span>
                <span className="value">${pos.current.toLocaleString()}</span>
              </div>
            </div>
            <button className="btn-danger btn-sm btn-full">Close Position</button>
          </div>
        ))}
      </div>
    </div>
  )
}
