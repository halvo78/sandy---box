import { RiskOverview } from './charts/RiskOverview'
import { ExposureChart } from './charts/ExposureChart'
import { CorrelationMatrix } from './charts/CorrelationMatrix'
import { AlertsPanel } from './charts/AlertsPanel'

export function RiskDashboard() {
  return (
    <div className="dashboard-grid risk-grid">
      <div className="grid-item risk-overview">
        <RiskOverview />
      </div>
      <div className="grid-item exposure">
        <ExposureChart />
      </div>
      <div className="grid-item correlation">
        <CorrelationMatrix />
      </div>
      <div className="grid-item alerts">
        <AlertsPanel />
      </div>
    </div>
  )
}
