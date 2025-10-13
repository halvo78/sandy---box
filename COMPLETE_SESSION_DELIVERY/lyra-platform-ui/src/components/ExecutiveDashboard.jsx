import { KPISummary } from './charts/KPISummary'
import { PerformanceChart } from './charts/PerformanceChart'

export function ExecutiveDashboard() {
  return (
    <div className="dashboard-grid executive-grid">
      <div className="grid-item kpi-summary">
        <KPISummary />
      </div>
      <div className="grid-item performance">
        <PerformanceChart />
      </div>
    </div>
  )
}
