"""
ULTIMATE FORENSIC DISCOVERY - COMPLETE SYSTEM EXTRACTION
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY================
Finds EVERYTHING in both sandbox and ngrok Ubuntu systems.
No assumptions, no building - just complete discovery and cataloging.
"""

import os
import json
import subprocess
import sqlite3
import hashlib
from datetime import datetime
from pathlib import Path
import requests
import socket

# --- Configuration ---
DISCOVERY_OUTPUT_DIR = "/home/ubuntu/COMPLETE_FORENSIC_DISCOVERY/"
DISCOVERY_REPORT = "/home/ubuntu/COMPLETE_FORENSIC_DISCOVERY/ULTIMATE_DISCOVERY_REPORT.json"

class UltimateForensicDiscovery:
    def __init__(self):
        self.discovery_data = {
            "discovery_timestamp": datetime.now().isoformat(),
            "sandbox_systems": {},
            "ngrok_systems": {},
            "processes": {},
            "ports": {},
            "files": {},
            "databases": {},
            "configurations": {},
            "ai_integrations": {},
            "trading_systems": {},
            "vault_systems": {},
            "docker_containers": {},
            "services": {},
            "logs": {},
            "scripts": {},
            "documentation": {},
            "success_indicators": {},
            "api_endpoints": {},
            "network_connections": {},
            "environment_variables": {},
            "installed_packages": {},
            "git_repositories": {},
            "cron_jobs": {},
            "systemd_services": {}
        }
        
        # Create output directory
        os.makedirs(DISCOVERY_OUTPUT_DIR, exist_ok=True)
    
    def discover_all_processes(self):
        """Discover ALL running processes"""
        print("🔍 Discovering all running processes...")
        
        try:
            # Get detailed process information
            result = subprocess.run(['ps', 'auxww'], capture_output=True, text=True)
            processes = {}
            
            for line in result.stdout.split('\n')[1:]:  # Skip header
                if line.strip():
                    parts = line.split(None, 10)
                    if len(parts) >= 11:
                        pid = parts[1]
                        processes[pid] = {
                            "user": parts[0],
                            "pid": parts[1],
                            "cpu": parts[2],
                            "mem": parts[3],
                            "vsz": parts[4],
                            "rss": parts[5],
                            "tty": parts[6],
                            "stat": parts[7],
                            "start": parts[8],
                            "time": parts[9],
                            "command": parts[10] if len(parts) > 10 else ""
                        }
            
            self.discovery_data["processes"] = processes
            print(f"✅ Found {len(processes)} processes")
            
        except Exception as e:
            print(f"❌ Error discovering processes: {e}")
    
    def discover_all_ports(self):
        """Discover ALL open ports and listening services"""
        print("🔍 Discovering all open ports...")
        
        try:
            # Get all listening ports
            result = subprocess.run(['netstat', '-tulpn'], capture_output=True, text=True)
            ports = {}
            
            for line in result.stdout.split('\n'):
                if 'LISTEN' in line or 'udp' in line:
                    parts = line.split()
                    if len(parts) >= 4:
                        address = parts[3]
                        if ':' in address:
                            port = address.split(':')[-1]
                            if port.isdigit():
                                ports[port] = {
                                    "protocol": parts[0],
                                    "address": address,
                                    "state": parts[5] if len(parts) > 5 else "LISTENING",
                                    "process": parts[6] if len(parts) > 6 else "unknown"
                                }
            
            self.discovery_data["ports"] = ports
            print(f"✅ Found {len(ports)} open ports")
            
        except Exception as e:
            print(f"❌ Error discovering ports: {e}")
    
    def discover_all_files(self):
        """Discover ALL relevant files in the system"""
        print("🔍 Discovering all files...")
        
        search_paths = [
            "/home/ubuntu",
            "/opt",
            "/var/log",
            "/etc",
            "/usr/local/bin"
        ]
        
        files = {}
        file_count = 0
        
        for search_path in search_paths:
            if os.path.exists(search_path):
                for root, dirs, filenames in os.walk(search_path):
                    # Skip certain directories to avoid overwhelming output
                    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
                    
                    for filename in filenames:
                        file_path = os.path.join(root, filename)
                        try:
                            stat = os.stat(file_path)
                            files[file_path] = {
                                "size": stat.st_size,
                                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                                "permissions": oct(stat.st_mode)[-3:],
                                "type": self.get_file_type(filename),
                                "is_executable": os.access(file_path, os.X_OK)
                            }
                            file_count += 1
                            
                            # Limit to prevent overwhelming output
                            if file_count > 10000:
                                break
                        except:
                            continue
                    
                    if file_count > 10000:
                        break
        
        self.discovery_data["files"] = files
        print(f"✅ Found {len(files)} files")
    
    def get_file_type(self, filename):
        """Determine file type from extension"""
        ext = filename.split('.')[-1].lower() if '.' in filename else 'unknown'
        
        type_map = {
            'py': 'python',
            'js': 'javascript',
            'sh': 'shell',
            'yml': 'yaml',
            'yaml': 'yaml',
            'json': 'json',
            'md': 'markdown',
            'txt': 'text',
            'log': 'log',
            'conf': 'config',
            'cfg': 'config',
            'ini': 'config',
            'env': 'environment',
            'sql': 'database',
            'db': 'database',
            'sqlite': 'database'
        }
        
        return type_map.get(ext, ext)
    
    def discover_docker_containers(self):
        """Discover all Docker containers"""
        print("🔍 Discovering Docker containers...")
        
        try:
            # Check if Docker is available
            result = subprocess.run(['docker', 'ps', '-a', '--format', 'json'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                containers = {}
                for line in result.stdout.strip().split('\n'):
                    if line:
                        try:
                            container = json.loads(line)
                            containers[container.get('ID', 'unknown')] = container
                        except:
                            continue
                
                self.discovery_data["docker_containers"] = containers
                print(f"✅ Found {len(containers)} Docker containers")
            else:
                print("ℹ️ Docker not available or no containers found")
                
        except Exception as e:
            print(f"❌ Error discovering Docker containers: {e}")
    
    def discover_databases(self):
        """Discover all database files and connections"""
        print("🔍 Discovering databases...")
        
        databases = {}
        
        # Find SQLite databases
        for root, dirs, files in os.walk("/home/ubuntu"):
            for file in files:
                if file.endswith(('.db', '.sqlite', '.sqlite3')):
                    db_path = os.path.join(root, file)
                    try:
                        conn = sqlite3.connect(db_path)
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        tables = [row[0] for row in cursor.fetchall()]
                        conn.close()
                        
                        databases[db_path] = {
                            "type": "sqlite",
                            "tables": tables,
                            "size": os.path.getsize(db_path)
                        }
                    except:
                        databases[db_path] = {
                            "type": "sqlite",
                            "error": "Could not read database",
                            "size": os.path.getsize(db_path)
                        }
        
        self.discovery_data["databases"] = databases
        print(f"✅ Found {len(databases)} databases")
    
    def discover_api_endpoints(self):
        """Discover all API endpoints by testing common ports"""
        print("🔍 Discovering API endpoints...")
        
        endpoints = {}
        common_ports = [3000, 5000, 8000, 8080, 8081, 8082, 8090, 8091, 8100, 8101, 8102, 8400, 8751, 9996]
        
        for port in common_ports:
            try:
                # Test HTTP
                response = requests.get(f"http://localhost:{port}", timeout=2)
                endpoints[f"http://localhost:{port}"] = {
                    "status_code": response.status_code,
                    "content_type": response.headers.get('content-type', ''),
                    "server": response.headers.get('server', ''),
                    "content_length": len(response.content)
                }
            except:
                pass
            
            try:
                # Test HTTPS
                response = requests.get(f"https://localhost:{port}", timeout=2, verify=False)
                endpoints[f"https://localhost:{port}"] = {
                    "status_code": response.status_code,
                    "content_type": response.headers.get('content-type', ''),
                    "server": response.headers.get('server', ''),
                    "content_length": len(response.content)
                }
            except:
                pass
        
        self.discovery_data["api_endpoints"] = endpoints
        print(f"✅ Found {len(endpoints)} API endpoints")
    
    def discover_environment_variables(self):
        """Discover environment variables"""
        print("🔍 Discovering environment variables...")
        
        env_vars = dict(os.environ)
        # Filter out sensitive information
        filtered_env = {}
        
        for key, value in env_vars.items():
            if any(sensitive in key.lower() for sensitive in ['password', 'secret', 'key', 'token']):
                filtered_env[key] = "[REDACTED]"
            else:
                filtered_env[key] = value
        
        self.discovery_data["environment_variables"] = filtered_env
        print(f"✅ Found {len(filtered_env)} environment variables")
    
    def discover_installed_packages(self):
        """Discover installed Python packages"""
        print("🔍 Discovering installed packages...")
        
        try:
            result = subprocess.run(['pip3', 'list', '--format=json'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                packages = json.loads(result.stdout)
                package_dict = {pkg['name']: pkg['version'] for pkg in packages}
                self.discovery_data["installed_packages"] = package_dict
                print(f"✅ Found {len(package_dict)} installed packages")
            
        except Exception as e:
            print(f"❌ Error discovering packages: {e}")
    
    def discover_git_repositories(self):
        """Discover Git repositories"""
        print("🔍 Discovering Git repositories...")
        
        repos = {}
        
        for root, dirs, files in os.walk("/home/ubuntu"):
            if '.git' in dirs:
                try:
                    # Get git status
                    result = subprocess.run(['git', 'status', '--porcelain'], 
                                          cwd=root, capture_output=True, text=True)
                    
                    # Get remote URL
                    remote_result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                                 cwd=root, capture_output=True, text=True)
                    
                    repos[root] = {
                        "status": result.stdout.strip(),
                        "remote": remote_result.stdout.strip() if remote_result.returncode == 0 else "none",
                        "has_changes": bool(result.stdout.strip())
                    }
                except:
                    repos[root] = {"error": "Could not read git info"}
        
        self.discovery_data["git_repositories"] = repos
        print(f"✅ Found {len(repos)} Git repositories")
    
    def discover_systemd_services(self):
        """Discover systemd services"""
        print("🔍 Discovering systemd services...")
        
        try:
            result = subprocess.run(['systemctl', 'list-units', '--type=service', '--no-pager'], 
                                  capture_output=True, text=True)
            
            services = {}
            for line in result.stdout.split('\n'):
                if '.service' in line:
                    parts = line.split()
                    if len(parts) >= 4:
                        service_name = parts[0]
                        services[service_name] = {
                            "loaded": parts[1],
                            "active": parts[2],
                            "sub": parts[3],
                            "description": ' '.join(parts[4:]) if len(parts) > 4 else ""
                        }
            
            self.discovery_data["systemd_services"] = services
            print(f"✅ Found {len(services)} systemd services")
            
        except Exception as e:
            print(f"❌ Error discovering systemd services: {e}")
    
    def discover_success_indicators(self):
        """Find all success indicators in files and logs"""
        print("🔍 Discovering success indicators...")
        
        success_keywords = [
            "success", "complete", "operational", "ready", "deployed", 
            "active", "running", "healthy", "100%", "production",
            "commissioned", "validated", "approved", "go live"
        ]
        
        success_files = {}
        
        # Search in specific directories
        search_dirs = ["/home/ubuntu/ultimate_lyra_v5", "/home/ubuntu/upload"]
        
        for search_dir in search_dirs:
            if os.path.exists(search_dir):
                for root, dirs, files in os.walk(search_dir):
                    for file in files:
                        if file.endswith(('.md', '.txt', '.json', '.log', '.py')):
                            file_path = os.path.join(root, file)
                            try:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read().lower()
                                    
                                    matches = []
                                    for keyword in success_keywords:
                                        if keyword in content:
                                            matches.append(keyword)
                                    
                                    if matches:
                                        success_files[file_path] = {
                                            "matches": matches,
                                            "match_count": len(matches),
                                            "file_size": os.path.getsize(file_path)
                                        }
                            except:
                                continue
        
        self.discovery_data["success_indicators"] = success_files
        print(f"✅ Found success indicators in {len(success_files)} files")
    
    def discover_ngrok_systems(self):
        """Discover ngrok tunnels and systems"""
        print("🔍 Discovering ngrok systems...")
        
        ngrok_data = {}
        
        try:
            # Check ngrok API
            response = requests.get("http://localhost:4040/api/tunnels", timeout=5)
            if response.status_code == 200:
                tunnels = response.json()
                ngrok_data["tunnels"] = tunnels
                print(f"✅ Found {len(tunnels.get('tunnels', []))} ngrok tunnels")
            
        except Exception as e:
            print(f"ℹ️ Ngrok API not accessible: {e}")
        
        # Check for ngrok processes
        try:
            result = subprocess.run(['pgrep', '-f', 'ngrok'], capture_output=True, text=True)
            if result.stdout.strip():
                ngrok_data["processes"] = result.stdout.strip().split('\n')
        except:
            pass
        
        self.discovery_data["ngrok_systems"] = ngrok_data
    
    def run_complete_discovery(self):
        """Run complete forensic discovery"""
        print("🚀 STARTING ULTIMATE FORENSIC DISCOVERY")
        print("=" * 60)
        
        # Run all discovery methods
        self.discover_all_processes()
        self.discover_all_ports()
        self.discover_all_files()
        self.discover_docker_containers()
        self.discover_databases()
        self.discover_api_endpoints()
        self.discover_environment_variables()
        self.discover_installed_packages()
        self.discover_git_repositories()
        self.discover_systemd_services()
        self.discover_success_indicators()
        self.discover_ngrok_systems()
        
        # Save discovery data
        with open(DISCOVERY_REPORT, 'w') as f:
            json.dump(self.discovery_data, f, indent=2)
        
        # Generate summary report
        self.generate_summary_report()
        
        print("\n✅ ULTIMATE FORENSIC DISCOVERY COMPLETE!")
        print(f"📊 Discovery report saved to: {DISCOVERY_REPORT}")
        
        return self.discovery_data
    
    def generate_summary_report(self):
        """Generate a human-readable summary report"""
        summary = f"""# ULTIMATE FORENSIC DISCOVERY REPORT

**Discovery Date:** {self.discovery_data['discovery_timestamp']}

## 📊 DISCOVERY SUMMARY

**Processes Found:** {len(self.discovery_data['processes'])}
**Open Ports:** {len(self.discovery_data['ports'])}
**Files Cataloged:** {len(self.discovery_data['files'])}
**Docker Containers:** {len(self.discovery_data['docker_containers'])}
**Databases:** {len(self.discovery_data['databases'])}
**API Endpoints:** {len(self.discovery_data['api_endpoints'])}
**Environment Variables:** {len(self.discovery_data['environment_variables'])}
**Installed Packages:** {len(self.discovery_data['installed_packages'])}
**Git Repositories:** {len(self.discovery_data['git_repositories'])}
**Systemd Services:** {len(self.discovery_data['systemd_services'])}
**Success Indicators:** {len(self.discovery_data['success_indicators'])}

## 🔍 KEY FINDINGS

### Active Ports
"""
        
        for port, info in list(self.discovery_data['ports'].items())[:10]:
            summary += f"- **Port {port}**: {info['protocol']} - {info.get('process', 'unknown')}\n"
        
        summary += "\n### API Endpoints\n"
        for endpoint, info in list(self.discovery_data['api_endpoints'].items())[:10]:
            summary += f"- **{endpoint}**: Status {info['status_code']}\n"
        
        summary += "\n### Success Indicators (Top Files)\n"
        sorted_success = sorted(self.discovery_data['success_indicators'].items(), 
                              key=lambda x: x[1]['match_count'], reverse=True)
        
        for file_path, info in sorted_success[:10]:
            summary += f"- **{os.path.basename(file_path)}**: {info['match_count']} success indicators\n"
        
        summary += f"\n## 📁 COMPLETE DATA\n\nFull discovery data available in: `{DISCOVERY_REPORT}`\n"
        
        summary_path = os.path.join(DISCOVERY_OUTPUT_DIR, "DISCOVERY_SUMMARY.md")
        with open(summary_path, 'w') as f:
            f.write(summary)
        
        print(f"📋 Summary report saved to: {summary_path}")

def main():
    """Main discovery function"""
    discovery = UltimateForensicDiscovery()
    return discovery.run_complete_discovery()

if __name__ == "__main__":
    main()
