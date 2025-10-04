
import time
import json
import threading
from datetime import datetime
from typing import Dict, List, Callable

class AdvancedMonitor:
    """Advanced monitoring system with predictive alerts"""
    
    def __init__(self):
        self.metrics = {}
        self.thresholds = {}
        self.alerts = []
        self.callbacks = {}
        self.monitoring_active = False
        
    def register_metric(self, name: str, warning_threshold: float, critical_threshold: float):
        """Register a metric for monitoring"""
        self.thresholds[name] = {
            'warning': warning_threshold,
            'critical': critical_threshold
        }
        self.metrics[name] = []
        
    def record_metric(self, name: str, value: float):
        """Record a metric value"""
        timestamp = time.time()
        
        if name not in self.metrics:
            self.metrics[name] = []
            
        self.metrics[name].append({
            'timestamp': timestamp,
            'value': value
        })
        
        # Keep only last 1000 entries
        if len(self.metrics[name]) > 1000:
            self.metrics[name] = self.metrics[name][-1000:]
            
        # Check thresholds
        self.check_thresholds(name, value)
        
    def check_thresholds(self, name: str, value: float):
        """Check if value exceeds thresholds"""
        if name not in self.thresholds:
            return
            
        thresholds = self.thresholds[name]
        
        if value >= thresholds['critical']:
            self.trigger_alert(name, 'CRITICAL', value, thresholds['critical'])
        elif value >= thresholds['warning']:
            self.trigger_alert(name, 'WARNING', value, thresholds['warning'])
            
    def trigger_alert(self, metric_name: str, severity: str, value: float, threshold: float):
        """Trigger an alert"""
        alert = {
            'timestamp': datetime.now().isoformat(),
            'metric': metric_name,
            'severity': severity,
            'value': value,
            'threshold': threshold,
            'message': f"{metric_name} {severity}: {value} exceeds {threshold}"
        }
        
        self.alerts.append(alert)
        
        # Execute callback if registered
        if metric_name in self.callbacks:
            self.callbacks[metric_name](alert)
            
    def register_callback(self, metric_name: str, callback: Callable):
        """Register callback for metric alerts"""
        self.callbacks[metric_name] = callback
        
    def get_trend(self, metric_name: str, window: int = 10) -> str:
        """Get trend for a metric"""
        if metric_name not in self.metrics or len(self.metrics[metric_name]) < window:
            return "INSUFFICIENT_DATA"
            
        recent_values = [m['value'] for m in self.metrics[metric_name][-window:]]
        
        if len(recent_values) < 2:
            return "STABLE"
            
        # Simple trend calculation
        first_half = sum(recent_values[:len(recent_values)//2]) / (len(recent_values)//2)
        second_half = sum(recent_values[len(recent_values)//2:]) / (len(recent_values) - len(recent_values)//2)
        
        if second_half > first_half * 1.1:
            return "INCREASING"
        elif second_half < first_half * 0.9:
            return "DECREASING"
        else:
            return "STABLE"
