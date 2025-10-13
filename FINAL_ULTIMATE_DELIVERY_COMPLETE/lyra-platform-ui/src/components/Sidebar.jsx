import { useStore } from '../store/useStore'
import { BarChart3, Shield, TrendingUp, FileCheck, Settings } from 'lucide-react'

export function Sidebar() {
  const { currentDashboard, setDashboard } = useStore()
  
  const menuItems = [
    { id: 'trading', icon: TrendingUp, label: 'Trading' },
    { id: 'risk', icon: Shield, label: 'Risk' },
    { id: 'executive', icon: BarChart3, label: 'Executive' },
    { id: 'compliance', icon: FileCheck, label: 'Compliance' },
  ]
  
  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h1 className="sidebar-title">LYRA</h1>
        <p className="sidebar-subtitle">Trading Platform</p>
      </div>
      
      <nav className="sidebar-nav">
        {menuItems.map(item => (
          <button
            key={item.id}
            className={`sidebar-item ${currentDashboard === item.id ? 'active' : ''}`}
            onClick={() => setDashboard(item.id)}
          >
            <item.icon size={20} />
            <span>{item.label}</span>
          </button>
        ))}
      </nav>
      
      <div className="sidebar-footer">
        <button className="sidebar-item">
          <Settings size={20} />
          <span>Settings</span>
        </button>
      </div>
    </div>
  )
}
