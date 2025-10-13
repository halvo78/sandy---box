export function NewsFeed() {
  const news = [
    { title: 'Bitcoin reaches new all-time high', source: 'CoinDesk', time: '5m ago', sentiment: 'bullish' },
    { title: 'Ethereum upgrade scheduled for Q2', source: 'CryptoPanic', time: '15m ago', sentiment: 'bullish' },
    { title: 'SEC announces new crypto regulations', source: 'Bloomberg', time: '1h ago', sentiment: 'neutral' },
  ]
  
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-title">News Feed</h3>
      </div>
      <div className="news-container">
        {news.map((item, i) => (
          <div key={i} className="news-item">
            <div className="news-header">
              <span className={`news-sentiment ${item.sentiment}`}></span>
              <span className="news-time">{item.time}</span>
            </div>
            <h4 className="news-title">{item.title}</h4>
            <span className="news-source">{item.source}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
