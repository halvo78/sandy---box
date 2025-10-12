import { TransactionTable } from './charts/TransactionTable'
import { ComplianceMetrics } from './charts/ComplianceMetrics'

export function ComplianceDashboard() {
  return (
    <div className="dashboard-grid compliance-grid">
      <div className="grid-item transactions">
        <TransactionTable />
      </div>
      <div className="grid-item metrics">
        <ComplianceMetrics />
      </div>
    </div>
  )
}
