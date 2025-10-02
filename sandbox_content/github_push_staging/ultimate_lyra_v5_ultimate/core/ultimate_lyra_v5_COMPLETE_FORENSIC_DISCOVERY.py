"""
COMPLETE FORENSIC DISCOVERY - FIND EVERYTHING
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY======
Comprehensive forensic discovery of ALL systems, files, processes, ports,
configurations, databases, logs, and components across the entire system.
This will find EVERYTHING so nothing is missed or left out.
"""

import os
import json
import subprocess
import sqlite3
import glob
import hashlib
import time
from datetime import datetime
from pathlib import Path
import psutil

class CompleteForensicDiscovery:
    def __init__(self):
        self.discovery_results = {
            "timestamp": datetime.now().isoformat(),
            "total_files": 0,
            "total_directories": 0,
            "active_processes": [],
            "listening_ports": [],
            "databases": [],
            "python_files": [],
            "trading_systems": [],
            "ai_systems": [],
            "configuration_files": [],
            "log_files": [],
            "vault_systems": [],
            "exchange_configs": [],
            "docker_configs": [],
            "environment_files": [],
            "jupyter_notebooks": [],
            "documentation": [],
            "test_files": [],
            "api_keys_found": [],
            "running_services": [],
            "system_metrics": {}
        }
        
    def discover_everything(self):
        """Perform complete forensic discovery of the entire system"""
        print("🔍 STARTING COMPLETE FORENSIC DISCOVERY")
        print("=" * 60)
        
        # 1. File System Discovery
        self.discover_file_system()
        
        # 2. Process Discovery
        self.discover_processes()
        
        # 3. Network Discovery
        self.discover_network()
        
        # 4. Database Discovery
        self.discover_databases()
        
        # 5. Trading System Discovery
        self.discover_trading_systems()
        
        # 6. AI System Discovery
        self.discover_ai_systems()
        
        # 7. Configuration Discovery
        self.discover_configurations()
        
        # 8. Security Discovery
        self.discover_security_components()
        
        # 9. Docker Discovery
        self.discover_docker_systems()
        
        # 10. System Metrics
        self.discover_system_metrics()
        
        # 11. Generate Report
        self.generate_discovery_report()
        
        print("✅ COMPLETE FORENSIC DISCOVERY FINISHED")
        return self.discovery_results
    
    def discover_file_system(self):
        """Discover all files and directories"""
        print("📁 Discovering file system...")
        
        # Count all files and directories
        total_files = 0
        total_dirs = 0
        
        for root, dirs, files in os.walk("/home/ubuntu"):
            total_dirs += len(dirs)
            total_files += len(files)
            
            # Look for specific file types
            for file in files:
                file_path = os.path.join(root, file)
                
                # Python files
                if file.endswith('.py'):
                    self.discovery_results["python_files"].append(file_path)
                
                # Configuration files
                if any(ext in file.lower() for ext in ['.env', '.conf', '.config', '.json', '.yaml', '.yml']):
                    self.discovery_results["configuration_files"].append(file_path)
                
                # Log files
                if any(ext in file.lower() for ext in ['.log', 'log']):
                    self.discovery_results["log_files"].append(file_path)
                
                # Documentation
                if any(ext in file.lower() for ext in ['.md', '.txt', '.rst', '.doc']):
                    self.discovery_results["documentation"].append(file_path)
                
                # Test files
                if 'test' in file.lower() or file.startswith('test_'):
                    self.discovery_results["test_files"].append(file_path)
                
                # Jupyter notebooks
                if file.endswith('.ipynb'):
                    self.discovery_results["jupyter_notebooks"].append(file_path)
        
        self.discovery_results["total_files"] = total_files
        self.discovery_results["total_directories"] = total_dirs
        
        print(f"   📊 Found {total_files} files and {total_dirs} directories")
        print(f"   🐍 Found {len(self.discovery_results['python_files'])} Python files")
        print(f"   ⚙️ Found {len(self.discovery_results['configuration_files'])} config files")
    
    def discover_processes(self):
        """Discover all running processes"""
        print("⚡ Discovering active processes...")
        
        for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'cpu_percent', 'memory_percent']):
            try:
                proc_info = proc.info
                if proc_info['cmdline'] and any('python' in cmd.lower() for cmd in proc_info['cmdline']):
                    self.discovery_results["active_processes"].append({
                        "pid": proc_info['pid'],
                        "name": proc_info['name'],
                        "cmdline": ' '.join(proc_info['cmdline']),
                        "cpu_percent": proc_info['cpu_percent'],
                        "memory_percent": proc_info['memory_percent']
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        print(f"   🔄 Found {len(self.discovery_results['active_processes'])} Python processes")
    
    def discover_network(self):
        """Discover network connections and listening ports"""
        print("🌐 Discovering network connections...")
        
        try:
            # Get listening ports
            result = subprocess.run(['netstat', '-tlnp'], capture_output=True, text=True)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'LISTEN' in line and 'python' in line.lower():
                        parts = line.split()
                        if len(parts) >= 4:
                            port_info = {
                                "address": parts[3],
                                "process": parts[-1] if len(parts) > 6 else "unknown"
                            }
                            self.discovery_results["listening_ports"].append(port_info)
        except Exception as e:
            print(f"   ⚠️ Error discovering network: {e}")
        
        print(f"   🔌 Found {len(self.discovery_results['listening_ports'])} listening ports")
    
    def discover_databases(self):
        """Discover all database files"""
        print("🗄️ Discovering databases...")
        
        # Find SQLite databases
        db_patterns = ['*.db', '*.sqlite', '*.sqlite3']
        for pattern in db_patterns:
            for db_file in glob.glob(f"/home/ubuntu/**/{pattern}", recursive=True):
                try:
                    # Try to connect and get table info
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = [row[0] for row in cursor.fetchall()]
                    conn.close()
                    
                    self.discovery_results["databases"].append({
                        "path": db_file,
                        "type": "sqlite",
                        "tables": tables,
                        "size": os.path.getsize(db_file)
                    })
                except Exception:
                    # Still record the file even if we can't read it
                    self.discovery_results["databases"].append({
                        "path": db_file,
                        "type": "sqlite",
                        "tables": [],
                        "size": os.path.getsize(db_file) if os.path.exists(db_file) else 0
                    })
        
        print(f"   💾 Found {len(self.discovery_results['databases'])} database files")
    
    def discover_trading_systems(self):
        """Discover all trading system components"""
        print("💰 Discovering trading systems...")
        
        trading_keywords = ['trading', 'lyra', 'amplification', 'hummingbot', 'exchange', 'portfolio']
        
        for py_file in self.discovery_results["python_files"]:
            if any(keyword in py_file.lower() for keyword in trading_keywords):
                try:
                    with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                    # Analyze the file
                    system_info = {
                        "path": py_file,
                        "size": len(content),
                        "lines": len(content.split('\n')),
                        "has_flask": 'flask' in content.lower(),
                        "has_trading": 'trading' in content.lower(),
                        "has_ai": any(ai in content.lower() for ai in ['openrouter', 'gpt', 'claude', 'ai']),
                        "has_exchange": any(ex in content.lower() for ex in ['okx', 'binance', 'kraken']),
                        "has_port": any(port in content for port in ['8751', '9996', '8400'])
                    }
                    
                    self.discovery_results["trading_systems"].append(system_info)
                except Exception as e:
                    print(f"   ⚠️ Error reading {py_file}: {e}")
        
        print(f"   📈 Found {len(self.discovery_results['trading_systems'])} trading system files")
    
    def discover_ai_systems(self):
        """Discover all AI system components"""
        print("🤖 Discovering AI systems...")
        
        ai_keywords = ['openrouter', 'gpt', 'claude', 'grok', 'ai', 'consensus', 'model']
        
        for py_file in self.discovery_results["python_files"]:
            if any(keyword in py_file.lower() for keyword in ai_keywords):
                try:
                    with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    ai_info = {
                        "path": py_file,
                        "has_openrouter": 'openrouter' in content.lower(),
                        "has_grok": 'grok' in content.lower(),
                        "has_consensus": 'consensus' in content.lower(),
                        "has_api_key": 'api_key' in content.lower() or 'sk-or-' in content
                    }
                    
                    self.discovery_results["ai_systems"].append(ai_info)
                except Exception:
                    continue
        
        print(f"   🧠 Found {len(self.discovery_results['ai_systems'])} AI system files")
    
    def discover_configurations(self):
        """Discover all configuration files and environment variables"""
        print("⚙️ Discovering configurations...")
        
        # Look for environment files
        env_patterns = ['.env*', '*.env', 'config.*']
        for pattern in env_patterns:
            for env_file in glob.glob(f"/home/ubuntu/**/{pattern}", recursive=True):
                self.discovery_results["environment_files"].append(env_file)
        
        print(f"   🔧 Found {len(self.discovery_results['environment_files'])} environment files")
    
    def discover_security_components(self):
        """Discover vault systems and security components"""
        print("🔐 Discovering security components...")
        
        # Look for vault directories and files
        vault_patterns = ['*vault*', '*secret*', '*key*', '*credential*']
        for pattern in vault_patterns:
            for item in glob.glob(f"/home/ubuntu/**/{pattern}", recursive=True):
                if os.path.isdir(item):
                    self.discovery_results["vault_systems"].append({
                        "path": item,
                        "type": "directory",
                        "contents": os.listdir(item) if os.path.exists(item) else []
                    })
                else:
                    self.discovery_results["vault_systems"].append({
                        "path": item,
                        "type": "file",
                        "size": os.path.getsize(item) if os.path.exists(item) else 0
                    })
        
        print(f"   🛡️ Found {len(self.discovery_results['vault_systems'])} security components")
    
    def discover_docker_systems(self):
        """Discover Docker configurations"""
        print("🐳 Discovering Docker systems...")
        
        docker_files = []
        for root, dirs, files in os.walk("/home/ubuntu"):
            for file in files:
                if 'docker' in file.lower() or file == 'Dockerfile':
                    docker_files.append(os.path.join(root, file))
        
        self.discovery_results["docker_configs"] = docker_files
        print(f"   📦 Found {len(docker_files)} Docker configuration files")
    
    def discover_system_metrics(self):
        """Get current system metrics"""
        print("📊 Gathering system metrics...")
        
        self.discovery_results["system_metrics"] = {
            "cpu_count": psutil.cpu_count(),
            "cpu_percent": psutil.cpu_percent(),
            "memory_total": psutil.virtual_memory().total,
            "memory_available": psutil.virtual_memory().available,
            "memory_percent": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('/').percent,
            "boot_time": psutil.boot_time(),
            "load_average": os.getloadavg() if hasattr(os, 'getloadavg') else None
        }
    
    def generate_discovery_report(self):
        """Generate comprehensive discovery report"""
        report_file = "/home/ubuntu/ultimate_lyra_v5/COMPLETE_FORENSIC_DISCOVERY_REPORT.json"
        
        with open(report_file, 'w') as f:
            json.dump(self.discovery_results, f, indent=2, default=str)
        
        # Generate summary report
        summary_file = "/home/ubuntu/ultimate_lyra_v5/FORENSIC_DISCOVERY_SUMMARY.md"
        with open(summary_file, 'w') as f:
            f.write("# COMPLETE FORENSIC DISCOVERY SUMMARY\n\n")
            f.write(f"**Discovery Date:** {self.discovery_results['timestamp']}\n\n")
            f.write("## System Overview\n\n")
            f.write(f"- **Total Files:** {self.discovery_results['total_files']:,}\n")
            f.write(f"- **Total Directories:** {self.discovery_results['total_directories']:,}\n")
            f.write(f"- **Python Files:** {len(self.discovery_results['python_files'])}\n")
            f.write(f"- **Active Processes:** {len(self.discovery_results['active_processes'])}\n")
            f.write(f"- **Listening Ports:** {len(self.discovery_results['listening_ports'])}\n")
            f.write(f"- **Databases:** {len(self.discovery_results['databases'])}\n")
            f.write(f"- **Trading Systems:** {len(self.discovery_results['trading_systems'])}\n")
            f.write(f"- **AI Systems:** {len(self.discovery_results['ai_systems'])}\n")
            f.write(f"- **Vault Components:** {len(self.discovery_results['vault_systems'])}\n")
            f.write(f"- **Docker Configs:** {len(self.discovery_results['docker_configs'])}\n")
            f.write(f"- **Environment Files:** {len(self.discovery_results['environment_files'])}\n")
        
        print(f"📋 Discovery report saved to: {report_file}")
        print(f"📋 Summary report saved to: {summary_file}")

if __name__ == "__main__":
    discoverer = CompleteForensicDiscovery()
    results = discoverer.discover_everything()
    
    print("\n🎯 DISCOVERY COMPLETE!")
    print(f"Total items discovered: {results['total_files'] + results['total_directories']:,}")
    print("Check the generated reports for full details.")
