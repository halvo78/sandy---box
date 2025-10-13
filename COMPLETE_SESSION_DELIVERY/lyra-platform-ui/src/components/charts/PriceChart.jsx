import { useEffect, useRef } from 'react'
import { createChart } from 'lightweight-charts'

export function PriceChart() {
  const chartContainerRef = useRef()
  const chartRef = useRef()
  
  useEffect(() => {
    if (!chartContainerRef.current) return
    
    const chart = createChart(chartContainerRef.current, {
      width: chartContainerRef.current.clientWidth,
      height: 500,
      layout: {
        background: { color: '#1A1F3A' },
        textColor: '#8B93B0',
      },
      grid: {
        vertLines: { color: '#252B4D' },
        horzLines: { color: '#252B4D' },
      },
      timeScale: {
        borderColor: '#2F3659',
      },
    })
    
    const candlestickSeries = chart.addCandlestickSeries({
      upColor: '#00FF88',
      downColor: '#FF3366',
      borderVisible: false,
      wickUpColor: '#00FF88',
      wickDownColor: '#FF3366',
    })
    
    // Sample data
    const data = generateSampleData()
    candlestickSeries.setData(data)
    
    chartRef.current = chart
    
    // Handle resize
    const handleResize = () => {
      chart.applyOptions({
        width: chartContainerRef.current.clientWidth,
      })
    }
    
    window.addEventListener('resize', handleResize)
    
    return () => {
      window.removeEventListener('resize', handleResize)
      chart.remove()
    }
  }, [])
  
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-title">BTC/USDT</h3>
        <div className="timeframe-selector">
          {['1m', '5m', '15m', '1h', '4h', '1d'].map(tf => (
            <button key={tf} className="timeframe-btn">{tf}</button>
          ))}
        </div>
      </div>
      <div ref={chartContainerRef} className="chart-container" />
    </div>
  )
}

function generateSampleData() {
  const data = []
  let time = Math.floor(Date.now() / 1000) - 86400 * 30
  let price = 50000
  
  for (let i = 0; i < 100; i++) {
    const change = (Math.random() - 0.5) * 1000
    const open = price
    const close = price + change
    const high = Math.max(open, close) + Math.random() * 500
    const low = Math.min(open, close) - Math.random() * 500
    
    data.push({
      time,
      open,
      high,
      low,
      close,
    })
    
    price = close
    time += 3600
  }
  
  return data
}
