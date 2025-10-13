export function OrderBook() {
  const bids = [
    { price: 50000, amount: 1.5, total: 75000 },
    { price: 49950, amount: 2.3, total: 114885 },
    { price: 49900, amount: 0.8, total: 39920 },
  ]
  
  const asks = [
    { price: 50050, amount: 1.2, total: 60060 },
    { price: 50100, amount: 1.8, total: 90180 },
    { price: 50150, amount: 2.1, total: 105315 },
  ]
  
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-title">Order Book</h3>
      </div>
      <div className="orderbook-container">
        <div className="orderbook-header">
          <span>Price</span>
          <span>Amount</span>
          <span>Total</span>
        </div>
        
        <div className="orderbook-asks">
          {asks.reverse().map((ask, i) => (
            <div key={i} className="orderbook-row ask">
              <span className="price">{ask.price.toLocaleString()}</span>
              <span>{ask.amount.toFixed(4)}</span>
              <span>{ask.total.toLocaleString()}</span>
            </div>
          ))}
        </div>
        
        <div className="orderbook-spread">
          <span className="spread-label">Spread</span>
          <span className="spread-value">50.00 (0.10%)</span>
        </div>
        
        <div className="orderbook-bids">
          {bids.map((bid, i) => (
            <div key={i} className="orderbook-row bid">
              <span className="price">{bid.price.toLocaleString()}</span>
              <span>{bid.amount.toFixed(4)}</span>
              <span>{bid.total.toLocaleString()}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
