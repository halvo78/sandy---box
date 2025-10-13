import { useStore } from '../store/useStore'
import { Moon, Sun, Bell } from 'lucide-react'

export function Header() {
  const { theme, setTheme, selectedExchange, selectedPair } = useStore()
  
  return (
    <header className="header">
      <div className="header-left">
        <h2 className="header-title">{selectedExchange}</h2>
        <span className="header-subtitle">{selectedPair}</span>
      </div>
      
      <div className="header-right">
        <button className="header-btn">
          <Bell size={20} />
        </button>
        <button 
          className="header-btn"
          onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
        >
          {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
        </button>
      </div>
    </header>
  )
}
