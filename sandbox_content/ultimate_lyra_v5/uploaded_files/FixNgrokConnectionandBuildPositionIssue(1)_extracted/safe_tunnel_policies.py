#!/usr/bin/env python3
"""
Safe Tunnel Policies for Spot-Only Operations
Ensures no trading exposure through ngrok tunnels
"""

import re
from typing import Dict, List

class SpotTunnelFilter:
    """Filters and controls tunnel access for spot-only operations"""
    
    def __init__(self):
        # Blocked endpoints for safety
        self.blocked_patterns = [
            r'/api/v\d+/.*/(margin|futures|perpetual|perp)',
            r'/trade/(margin|futures|perpetual|perp)',
            r'/order/(margin|futures|perpetual|perp)',
            r'/withdraw',
            r'/transfer',
            r'/lending'
        ]
        
        # Allowed spot-only patterns
        self.allowed_patterns = [
            r'/health',
            r'/status',
            r'/api/v\d+/.*/spot',
            r'/market-data',
            r'/account/balance',
            r'/ingest/event',
            r'/metrics',
            r'/logs'
        ]
    
    def is_spot_request(self, request_path: str) -> bool:
        """Check if request is spot-only safe"""
        # Block dangerous patterns
        for pattern in self.blocked_patterns:
            if re.search(pattern, request_path, re.IGNORECASE):
                return False
        
        # Allow safe patterns
        for pattern in self.allowed_patterns:
            if re.search(pattern, request_path, re.IGNORECASE):
                return True
        
        # Default deny for unknown patterns
        return False
    
    def is_perp_locked(self, tunnel_name: str) -> bool:
        """Check if tunnel should be locked for perpetual trading"""
        perp_tunnels = ['futures', 'margin', 'perpetual', 'perp']
        return any(perp in tunnel_name.lower() for perp in perp_tunnels)
    
    def filter_command(self, command: str) -> bool:
        """Filter commands for safety"""
        dangerous_commands = [
            'rm -rf',
            'sudo',
            'chmod 777',
            'wget',
            'curl.*withdraw',
            'curl.*transfer'
        ]
        
        for dangerous in dangerous_commands:
            if re.search(dangerous, command, re.IGNORECASE):
                return False
        
        return True
