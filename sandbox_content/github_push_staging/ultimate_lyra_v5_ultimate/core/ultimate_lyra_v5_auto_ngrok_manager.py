#!/usr/bin/env python3
"""
Automated Ngrok & Ingest Gateway Manager
Monitors and auto-restarts ngrok tunnel and ingest gateway to prevent connection drops
"""

import os
import time
import subprocess
import requests
import psutil
import logging
import signal
import sys
from datetime import datetime
from typing import Dict, List, Optional

class AutoNgrokManager:
    def __init__(self):
        self.setup_logging()
        self.ngrok_url = "https://3ce37fa57d09.ngrok.app"
        self.local_port = 8081
        self.check_interval = 30  # seconds
        self.restart_count = 0
        self.max_restarts = 10
        self.running = True
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def setup_logging(self):
        """Setup comprehensive logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('/tmp/auto_ngrok_manager.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        self.logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.running = False
        sys.exit(0)
    
    def check_process_running(self, process_name: str) -> List[Dict]:
        """Check if a process is running and return process info"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'status']):
            try:
                if process_name.lower() in ' '.join(proc.info['cmdline']).lower():
                    processes.append({
                        'pid': proc.info['pid'],
                        'status': proc.info['status'],
                        'cmdline': ' '.join(proc.info['cmdline'])
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes
    
    def kill_process_by_name(self, process_name: str):
        """Kill all processes matching the name"""
        processes = self.check_process_running(process_name)
        for proc in processes:
            try:
                self.logger.info(f"Killing process {proc['pid']}: {proc['cmdline']}")
                os.kill(proc['pid'], signal.SIGKILL)
                time.sleep(2)
            except ProcessLookupError:
                pass  # Process already dead
            except Exception as e:
                self.logger.error(f"Error killing process {proc['pid']}: {e}")
    
    def check_port_available(self, port: int) -> bool:
        """Check if a port is available"""
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
                return True
            except OSError:
                return False
    
    def free_port(self, port: int):
        """Free up a port by killing processes using it"""
        try:
            result = subprocess.run(
                f"sudo lsof -ti:{port}",
                shell=True,
                capture_output=True,
                text=True
            )
            if result.stdout.strip():
                pids = result.stdout.strip().split('\n')
                for pid in pids:
                    try:
                        self.logger.info(f"Killing process {pid} using port {port}")
                        os.kill(int(pid), signal.SIGKILL)
                    except:
                        pass
                time.sleep(3)
        except Exception as e:
            self.logger.error(f"Error freeing port {port}: {e}")
    
    def start_ingest_gateway(self) -> bool:
        """Start the ingest gateway"""
        try:
            # Change to the correct directory
            os.chdir('/home/halvolyra/ultimate_lyra_systems')
            
            # Activate virtual environment and start gateway
            cmd = """
            cd /home/halvolyra/ultimate_lyra_systems && 
            source venv/bin/activate && 
            python3 ingest_gateway.py > /tmp/ingest_gateway.log 2>&1 &
            """
            
            subprocess.run(cmd, shell=True, check=True)
            time.sleep(5)  # Give it time to start
            
            # Verify it's running
            if self.check_local_gateway():
                self.logger.info("✅ Ingest gateway started successfully")
                return True
            else:
                self.logger.error("❌ Ingest gateway failed to start")
                return False
                
        except Exception as e:
            self.logger.error(f"Error starting ingest gateway: {e}")
            return False
    
    def check_local_gateway(self) -> bool:
        """Check if local ingest gateway is responding"""
        try:
            response = requests.get(f"http://localhost:{self.local_port}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def check_ngrok_tunnel(self) -> bool:
        """Check if ngrok tunnel is responding"""
        try:
            response = requests.get(f"{self.ngrok_url}/health", timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def restart_ingest_gateway(self) -> bool:
        """Restart the ingest gateway"""
        self.logger.info("🔄 Restarting ingest gateway...")
        
        # Kill existing processes
        self.kill_process_by_name("ingest_gateway")
        
        # Free up the port
        self.free_port(self.local_port)
        
        # Wait a bit
        time.sleep(5)
        
        # Start new instance
        return self.start_ingest_gateway()
    
    def get_system_status(self) -> Dict:
        """Get comprehensive system status"""
        return {
            "timestamp": datetime.now().isoformat(),
            "local_gateway": self.check_local_gateway(),
            "ngrok_tunnel": self.check_ngrok_tunnel(),
            "ingest_processes": self.check_process_running("ingest_gateway"),
            "port_available": self.check_port_available(self.local_port),
            "restart_count": self.restart_count
        }
    
    def monitor_and_restart(self):
        """Main monitoring loop"""
        self.logger.info("🚀 Starting Auto Ngrok Manager...")
        
        while self.running and self.restart_count < self.max_restarts:
            try:
                status = self.get_system_status()
                self.logger.info(f"Status check: Local={status['local_gateway']}, Ngrok={status['ngrok_tunnel']}")
                
                # Check if we need to restart
                needs_restart = False
                
                if not status['local_gateway']:
                    self.logger.warning("❌ Local gateway not responding")
                    needs_restart = True
                
                if not status['ngrok_tunnel']:
                    self.logger.warning("❌ Ngrok tunnel not responding")
                    needs_restart = True
                
                # Check for zombie processes
                ingest_procs = status['ingest_processes']
                for proc in ingest_procs:
                    if proc['status'] in ['stopped', 'zombie']:
                        self.logger.warning(f"❌ Found zombie process: {proc}")
                        needs_restart = True
                
                if needs_restart:
                    self.restart_count += 1
                    self.logger.info(f"🔄 Restart attempt {self.restart_count}/{self.max_restarts}")
                    
                    if self.restart_ingest_gateway():
                        self.logger.info("✅ Restart successful")
                        # Reset restart count on successful restart
                        if self.restart_count > 0:
                            self.restart_count = max(0, self.restart_count - 1)
                    else:
                        self.logger.error("❌ Restart failed")
                
                # Wait before next check
                time.sleep(self.check_interval)
                
            except KeyboardInterrupt:
                self.logger.info("Received interrupt signal, shutting down...")
                break
            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {e}")
                time.sleep(self.check_interval)
        
        if self.restart_count >= self.max_restarts:
            self.logger.critical(f"❌ Max restarts ({self.max_restarts}) reached, giving up")
        
        self.logger.info("🛑 Auto Ngrok Manager stopped")

def main():
    """Main entry point"""
    manager = AutoNgrokManager()
    
    # Initial status check
    status = manager.get_system_status()
    print("📊 Initial System Status:")
    print(f"  Local Gateway: {'✅' if status['local_gateway'] else '❌'}")
    print(f"  Ngrok Tunnel: {'✅' if status['ngrok_tunnel'] else '❌'}")
    print(f"  Ingest Processes: {len(status['ingest_processes'])}")
    print(f"  Port {manager.local_port} Available: {'✅' if status['port_available'] else '❌'}")
    
    # Start monitoring
    manager.monitor_and_restart()

if __name__ == "__main__":
    main()
