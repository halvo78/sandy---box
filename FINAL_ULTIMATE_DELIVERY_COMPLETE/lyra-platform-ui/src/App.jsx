import { useState, useEffect } from 'react'
import './App.css'
import { TradingDashboard } from './components/TradingDashboard'
import { RiskDashboard } from './components/RiskDashboard'
import { ExecutiveDashboard } from './components/ExecutiveDashboard'
import { ComplianceDashboard } from './components/ComplianceDashboard'
import { Sidebar } from './components/Sidebar'
import { Header } from './components/Header'
import { useStore } from './store/useStore'

function App() {
  const { currentDashboard, theme } = useStore()
  
  useEffect(() => {
    // Apply theme to document
    document.documentElement.classList.toggle('dark', theme === 'dark')
  }, [theme])
  
  const renderDashboard = () => {
    switch (currentDashboard) {
      case 'trading':
        return <TradingDashboard />
      case 'risk':
        return <RiskDashboard />
      case 'executive':
        return <ExecutiveDashboard />
      case 'compliance':
        return <ComplianceDashboard />
      default:
        return <TradingDashboard />
    }
  }
  
  return (
    <div className="app">
      <Sidebar />
      <div className="main-content">
        <Header />
        <div className="dashboard-container">
          {renderDashboard()}
        </div>
      </div>
    </div>
  )
}

export default App

