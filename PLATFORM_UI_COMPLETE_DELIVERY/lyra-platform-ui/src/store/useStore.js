import { create } from 'zustand'

export const useStore = create((set) => ({
  currentDashboard: 'trading',
  theme: 'dark',
  selectedExchange: 'OKX',
  selectedPair: 'BTC/USDT',
  timeframe: '1h',
  
  setDashboard: (dashboard) => set({ currentDashboard: dashboard }),
  setTheme: (theme) => set({ theme }),
  setExchange: (exchange) => set({ selectedExchange: exchange }),
  setPair: (pair) => set({ selectedPair: pair }),
  setTimeframe: (timeframe) => set({ timeframe }),
}))
