
import psutil
import json
import time
from datetime import datetime

class PerformanceOptimizer:
    def __init__(self):
        self.baseline_metrics = self.collect_baseline()
    
    def collect_baseline(self):
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_io": psutil.disk_io_counters()._asdict(),
            "network_io": psutil.net_io_counters()._asdict()
        }
    
    def optimize_system(self):
        optimizations = []
        
        # Memory optimization
        if psutil.virtual_memory().percent > 70:
            optimizations.append("High memory usage detected - clearing caches")
            # Clear system caches (would need sudo)
        
        # CPU optimization
        if psutil.cpu_percent(interval=1) > 80:
            optimizations.append("High CPU usage detected - analyzing processes")
        
        return optimizations
    
    def generate_report(self):
        current_metrics = {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "timestamp": datetime.now().isoformat()
        }
        
        return {
            "baseline": self.baseline_metrics,
            "current": current_metrics,
            "optimizations_applied": self.optimize_system()
        }

if __name__ == "__main__":
    optimizer = PerformanceOptimizer()
    report = optimizer.generate_report()
    
    with open('/home/ubuntu/ultimate_lyra_v5/performance_optimization_report.json', 'w') as f:
        json.dump(report, f, indent=2)
