
import psutil
import time
import json
import threading
from datetime import datetime, timedelta
from typing import Dict, Any, List

class ComprehensiveSystemMonitor:
    """
    Comprehensive system monitoring for production readiness
    """
    
    def __init__(self):
        self.monitoring_active = False
        self.metrics_history = []
        self.alerts = []
        self.thresholds = {
            "cpu_usage": 80.0,
            "memory_usage": 85.0,
            "disk_usage": 90.0,
            "response_time": 2.0
        }
        self.lock = threading.Lock()
        
    def collect_system_metrics(self) -> Dict[str, Any]:
        """Collect comprehensive system metrics"""
        
        # CPU metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        
        # Memory metrics
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        # Disk metrics
        disk = psutil.disk_usage('/')
        disk_io = psutil.disk_io_counters()
        
        # Network metrics
        network = psutil.net_io_counters()
        
        # Process metrics
        process_count = len(psutil.pids())
        
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "cpu": {
                "usage_percent": cpu_percent,
                "count": cpu_count,
                "frequency_mhz": cpu_freq.current if cpu_freq else 0
            },
            "memory": {
                "total_gb": memory.total / (1024**3),
                "available_gb": memory.available / (1024**3),
                "used_gb": memory.used / (1024**3),
                "usage_percent": memory.percent
            },
            "swap": {
                "total_gb": swap.total / (1024**3),
                "used_gb": swap.used / (1024**3),
                "usage_percent": swap.percent
            },
            "disk": {
                "total_gb": disk.total / (1024**3),
                "used_gb": disk.used / (1024**3),
                "free_gb": disk.free / (1024**3),
                "usage_percent": (disk.used / disk.total) * 100
            },
            "disk_io": {
                "read_bytes": disk_io.read_bytes if disk_io else 0,
                "write_bytes": disk_io.write_bytes if disk_io else 0,
                "read_count": disk_io.read_count if disk_io else 0,
                "write_count": disk_io.write_count if disk_io else 0
            },
            "network": {
                "bytes_sent": network.bytes_sent,
                "bytes_recv": network.bytes_recv,
                "packets_sent": network.packets_sent,
                "packets_recv": network.packets_recv
            },
            "processes": {
                "count": process_count
            }
        }
        
        return metrics
        
    def check_thresholds(self, metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check metrics against thresholds and generate alerts"""
        alerts = []
        
        # Check CPU usage
        if metrics["cpu"]["usage_percent"] > self.thresholds["cpu_usage"]:
            alerts.append({
                "type": "CPU_HIGH",
                "severity": "WARNING",
                "message": f"CPU usage {metrics['cpu']['usage_percent']:.1f}% exceeds threshold {self.thresholds['cpu_usage']}%",
                "timestamp": datetime.now().isoformat()
            })
            
        # Check memory usage
        if metrics["memory"]["usage_percent"] > self.thresholds["memory_usage"]:
            alerts.append({
                "type": "MEMORY_HIGH",
                "severity": "WARNING",
                "message": f"Memory usage {metrics['memory']['usage_percent']:.1f}% exceeds threshold {self.thresholds['memory_usage']}%",
                "timestamp": datetime.now().isoformat()
            })
            
        # Check disk usage
        if metrics["disk"]["usage_percent"] > self.thresholds["disk_usage"]:
            alerts.append({
                "type": "DISK_HIGH",
                "severity": "CRITICAL",
                "message": f"Disk usage {metrics['disk']['usage_percent']:.1f}% exceeds threshold {self.thresholds['disk_usage']}%",
                "timestamp": datetime.now().isoformat()
            })
            
        return alerts
        
    def start_monitoring(self, interval: int = 60):
        """Start continuous monitoring"""
        self.monitoring_active = True
        
        def monitor_loop():
            while self.monitoring_active:
                try:
                    metrics = self.collect_system_metrics()
                    alerts = self.check_thresholds(metrics)
                    
                    with self.lock:
                        self.metrics_history.append(metrics)
                        # Keep only last 1440 entries (24 hours at 1-minute intervals)
                        if len(self.metrics_history) > 1440:
                            self.metrics_history = self.metrics_history[-1440:]
                            
                        self.alerts.extend(alerts)
                        # Keep only last 1000 alerts
                        if len(self.alerts) > 1000:
                            self.alerts = self.alerts[-1000:]
                            
                    time.sleep(interval)
                    
                except Exception as e:
                    print(f"Monitoring error: {e}")
                    time.sleep(interval)
                    
        monitoring_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitoring_thread.start()
        
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring_active = False
        
    def get_current_status(self) -> Dict[str, Any]:
        """Get current system status"""
        with self.lock:
            latest_metrics = self.metrics_history[-1] if self.metrics_history else self.collect_system_metrics()
            recent_alerts = [alert for alert in self.alerts if 
                           datetime.fromisoformat(alert["timestamp"]) > datetime.now() - timedelta(hours=1)]
            
            return {
                "timestamp": datetime.now().isoformat(),
                "monitoring_active": self.monitoring_active,
                "latest_metrics": latest_metrics,
                "recent_alerts": recent_alerts,
                "alert_count_last_hour": len(recent_alerts),
                "metrics_history_count": len(self.metrics_history)
            }

# Global instance
system_monitor = ComprehensiveSystemMonitor()
