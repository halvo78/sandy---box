
import json
import time
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

class ComprehensiveRiskManager:
    """
    Comprehensive risk management system for trading operations
    """
    
    def __init__(self):
        self.risk_limits = {
            "max_daily_loss": 500.0,
            "max_drawdown": 0.15,
            "max_position_size": 2000.0,
            "max_concurrent_positions": 25,
            "max_correlation": 0.70,
            "min_profit_target": 0.024,
            "emergency_stop_loss": 0.05
        }
        
        self.current_positions = {}
        self.daily_pnl = 0.0
        self.peak_portfolio_value = 0.0
        self.current_portfolio_value = 0.0
        self.risk_events = []
        self.lock = threading.Lock()
        
    def check_position_risk(self, symbol: str, position_size: float, entry_price: float) -> Dict[str, Any]:
        """Check if a new position meets risk criteria"""
        with self.lock:
            # Check position size limit
            if position_size > self.risk_limits["max_position_size"]:
                return {
                    "approved": False,
                    "reason": f"Position size {position_size} exceeds limit {self.risk_limits['max_position_size']}"
                }
                
            # Check concurrent positions limit
            if len(self.current_positions) >= self.risk_limits["max_concurrent_positions"]:
                return {
                    "approved": False,
                    "reason": f"Maximum concurrent positions {self.risk_limits['max_concurrent_positions']} reached"
                }
                
            # Check daily loss limit
            if self.daily_pnl <= -self.risk_limits["max_daily_loss"]:
                return {
                    "approved": False,
                    "reason": f"Daily loss limit {self.risk_limits['max_daily_loss']} exceeded"
                }
                
            # Check drawdown limit
            if self.peak_portfolio_value > 0:
                current_drawdown = (self.peak_portfolio_value - self.current_portfolio_value) / self.peak_portfolio_value
                if current_drawdown > self.risk_limits["max_drawdown"]:
                    return {
                        "approved": False,
                        "reason": f"Drawdown {current_drawdown:.2%} exceeds limit {self.risk_limits['max_drawdown']:.2%}"
                    }
                    
            return {"approved": True, "reason": "All risk checks passed"}
            
    def add_position(self, symbol: str, position_size: float, entry_price: float) -> bool:
        """Add a new position to tracking"""
        with self.lock:
            position_id = f"{symbol}_{int(time.time())}"
            self.current_positions[position_id] = {
                "symbol": symbol,
                "size": position_size,
                "entry_price": entry_price,
                "entry_time": datetime.now().isoformat(),
                "unrealized_pnl": 0.0
            }
            return True
            
    def close_position(self, position_id: str, exit_price: float) -> Dict[str, Any]:
        """Close a position and calculate PnL"""
        with self.lock:
            if position_id not in self.current_positions:
                return {"success": False, "reason": "Position not found"}
                
            position = self.current_positions[position_id]
            pnl = (exit_price - position["entry_price"]) * position["size"]
            
            self.daily_pnl += pnl
            
            # Update peak portfolio value
            self.current_portfolio_value += pnl
            if self.current_portfolio_value > self.peak_portfolio_value:
                self.peak_portfolio_value = self.current_portfolio_value
                
            # Remove position
            del self.current_positions[position_id]
            
            return {
                "success": True,
                "pnl": pnl,
                "daily_pnl": self.daily_pnl,
                "position_closed": position
            }
            
    def emergency_stop(self) -> Dict[str, Any]:
        """Emergency stop all trading activities"""
        with self.lock:
            emergency_event = {
                "timestamp": datetime.now().isoformat(),
                "event_type": "EMERGENCY_STOP",
                "reason": "Emergency stop triggered",
                "open_positions": len(self.current_positions),
                "daily_pnl": self.daily_pnl
            }
            
            self.risk_events.append(emergency_event)
            
            # In a real system, this would close all positions
            # For now, we just log the event
            
            return emergency_event
            
    def get_risk_status(self) -> Dict[str, Any]:
        """Get current risk status"""
        with self.lock:
            current_drawdown = 0.0
            if self.peak_portfolio_value > 0:
                current_drawdown = (self.peak_portfolio_value - self.current_portfolio_value) / self.peak_portfolio_value
                
            return {
                "timestamp": datetime.now().isoformat(),
                "daily_pnl": self.daily_pnl,
                "current_positions": len(self.current_positions),
                "current_drawdown": current_drawdown,
                "risk_limits": self.risk_limits,
                "within_limits": {
                    "daily_loss": self.daily_pnl > -self.risk_limits["max_daily_loss"],
                    "max_drawdown": current_drawdown < self.risk_limits["max_drawdown"],
                    "position_count": len(self.current_positions) < self.risk_limits["max_concurrent_positions"]
                }
            }

# Global instance
risk_manager = ComprehensiveRiskManager()
