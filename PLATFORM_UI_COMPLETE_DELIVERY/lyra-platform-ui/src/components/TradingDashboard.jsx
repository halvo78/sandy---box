import { PriceChart } from './charts/PriceChart'
import { OrderBook } from './charts/OrderBook'
import { PositionManager } from './charts/PositionManager'
import { NewsFeed } from './charts/NewsFeed'

export function TradingDashboard() {
  return (
    <div className="dashboard-grid trading-grid">
      <div className="grid-item chart-main">
        <PriceChart />
      </div>
      <div className="grid-item orderbook">
        <OrderBook />
      </div>
      <div className="grid-item positions">
        <PositionManager />
      </div>
      <div className="grid-item news">
        <NewsFeed />
      </div>
    </div>
  )
}
