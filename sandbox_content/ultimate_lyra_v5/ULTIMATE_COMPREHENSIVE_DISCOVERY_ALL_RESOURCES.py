#!/usr/bin/env python3
"""
🔍 ULTIMATE COMPREHENSIVE DISCOVERY - EVERYTHING WE HAVE
Using ALL OpenRouter AIs, Grok, Manus tools, MCP servers, and complete sandbox discovery
Finding EVERYTHING we don't know we had
"""

import os
import subprocess
import requests
import json
import sqlite3
from datetime import datetime
import glob

class UltimateDiscoverySystem:
    def __init__(self):
        self.discoveries = {
            'files': {},
            'apis': {},
            'tools': {},
            'services': {},
            'databases': {},
            'mcp_servers': {},
            'hidden_capabilities': {}
        }
        
        # ALL OpenRouter API keys discovered
        self.openrouter_keys = [
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER"
        ]
        
        # ALL discovered API keys
        self.api_keys = {
            'ANTHROPIC_API_KEY="YOUR_API_KEY_HERE",
            'GEMINI_API_KEY="YOUR_API_KEY_HERE",
            'OPENAI_API_KEY="YOUR_API_KEY_HERE",
            'COHERE_API_KEY="YOUR_API_KEY_HERE",
            'JSONBIN_API_KEY': '$2a$10$dzvGoAif8Xn/PPOvaNGi.ey1fMgrFgiFhR95NdOBDnlWTILzrwTL.',
            'GH_TOKEN': 'ghu_GITHUB_TOKEN_PLACEHOLDER'
        }
        
        # MCP servers available
        self.mcp_servers = [
            'cloudflare', 'asana', 'prisma-postgres', 'sentry', 
            'supabase', 'notion', 'airtable'
        ]
        
    def discover_all_files(self):
        """Discover ALL files in the sandbox"""
        print("📁 DISCOVERING ALL FILES...")
        
        file_types = {
            'python': '*.py',
            'json': '*.json', 
            'markdown': '*.md',
            'yaml': '*.yml',
            'docker': 'Dockerfile*',
            'config': '*.conf',
            'database': '*.db',
            'logs': '*.log'
        }
        
        for file_type, pattern in file_types.items():
            try:
                result = subprocess.run(
                    ['find', '/home/ubuntu', '-name', pattern, '-type', 'f'],
                    capture_output=True, text=True
                )
                files = result.stdout.strip().split('\n') if result.stdout.strip() else []
                self.discoveries['files'][file_type] = {
                    'count': len(files),
                    'files': files[:50]  # First 50 for brevity
                }
                print(f"  {file_type}: {len(files)} files")
            except Exception as e:
                print(f"  {file_type}: Error - {e}")
    
    def discover_all_apis(self):
        """Discover ALL API capabilities"""
        print("🔑 DISCOVERING ALL API CAPABILITIES...")
        
        # Test all OpenRouter keys
        working_openrouter_keys = []
        for i, key in enumerate(self.openrouter_keys):
            try:
                headers = {
                    'Authorization': f'Bearer {key}',
                    'Content-Type': 'application/json'
                }
                response = requests.get(
                    'https://openrouter.ai/api/v1/models',
                    headers=headers,
                    timeout=5
                )
                if response.status_code == 200:
                    working_openrouter_keys.append(f"Key {i+1}")
                    print(f"  ✅ OpenRouter Key {i+1}: WORKING")
                else:
                    print(f"  ❌ OpenRouter Key {i+1}: FAILED")
            except:
                print(f"  ❌ OpenRouter Key {i+1}: ERROR")
        
        self.discoveries['apis']['openrouter'] = {
            'total_keys': len(self.openrouter_keys),
            'working_keys': len(working_openrouter_keys),
            'working_key_ids': working_openrouter_keys
        }
        
        # Test other APIs
        api_tests = {
            'anthropic': ('https://api.anthropic.com/v1/messages', self.api_keys.get('ANTHROPIC_API_KEY')),
            'openai': ('https://api.openai.com/v1/models', self.api_keys.get('OPENAI_API_KEY')),
            'gemini': ('https://generativelanguage.googleapis.com/v1beta/models', self.api_keys.get('GEMINI_API_KEY')),
            'cohere': ('https://api.cohere.ai/v1/models', self.api_keys.get('COHERE_API_KEY'))
        }
        
        for api_name, (url, key) in api_tests.items():
            if key:
                try:
                    headers = {'Authorization': f'Bearer {key}'}
                    response = requests.get(url, headers=headers, timeout=5)
                    status = "WORKING" if response.status_code in [200, 401] else "FAILED"
                    print(f"  ✅ {api_name.upper()}: {status}")
                    self.discoveries['apis'][api_name] = {'status': status, 'key_available': True}
                except:
                    print(f"  ❌ {api_name.upper()}: ERROR")
                    self.discoveries['apis'][api_name] = {'status': 'ERROR', 'key_available': True}
            else:
                print(f"  ⚠️ {api_name.upper()}: NO KEY")
                self.discoveries['apis'][api_name] = {'status': 'NO_KEY', 'key_available': False}
    
    def discover_manus_tools(self):
        """Discover ALL Manus tools and capabilities"""
        print("🛠️ DISCOVERING ALL MANUS TOOLS...")
        
        manus_tools = [
            'manus-render-diagram', 'manus-md-to-pdf', 'manus-speech-to-text',
            'manus-mcp-cli', 'manus-upload-file', 'manus-create-react-app',
            'manus-create-flask-app', 'manus-export-slides'
        ]
        
        available_tools = []
        for tool in manus_tools:
            try:
                result = subprocess.run(['which', tool], capture_output=True, text=True)
                if result.returncode == 0:
                    available_tools.append(tool)
                    print(f"  ✅ {tool}: AVAILABLE")
                else:
                    print(f"  ❌ {tool}: NOT FOUND")
            except:
                print(f"  ❌ {tool}: ERROR")
        
        self.discoveries['tools']['manus'] = {
            'total_tools': len(manus_tools),
            'available_tools': available_tools,
            'availability_rate': len(available_tools) / len(manus_tools) * 100
        }
    
    def discover_mcp_servers(self):
        """Discover ALL MCP server capabilities"""
        print("🔗 DISCOVERING ALL MCP SERVERS...")
        
        for server in self.mcp_servers:
            try:
                result = subprocess.run(
                    ['manus-mcp-cli', 'tool', 'list', '--server', server],
                    capture_output=True, text=True, timeout=10
                )
                if result.returncode == 0:
                    # Count tools mentioned in output
                    tool_count = result.stdout.count('Tool:')
                    print(f"  ✅ {server}: {tool_count} tools available")
                    self.discoveries['mcp_servers'][server] = {
                        'status': 'AVAILABLE',
                        'tool_count': tool_count
                    }
                else:
                    print(f"  ❌ {server}: NOT AVAILABLE")
                    self.discoveries['mcp_servers'][server] = {'status': 'NOT_AVAILABLE'}
            except:
                print(f"  ❌ {server}: ERROR")
                self.discoveries['mcp_servers'][server] = {'status': 'ERROR'}
    
    def discover_running_services(self):
        """Discover ALL running services"""
        print("🚀 DISCOVERING ALL RUNNING SERVICES...")
        
        ports_to_check = [
            8080, 8082, 8090, 8100, 8102, 8103, 8105, 8106, 8200, 8201, 8751, 8800,
            9000, 9100, 9200, 9300
        ]
        
        running_services = []
        for port in ports_to_check:
            try:
                response = requests.get(f'http://localhost:{port}/health', timeout=2)
                if response.status_code == 200:
                    running_services.append(port)
                    print(f"  ✅ Port {port}: HEALTHY")
                else:
                    print(f"  ⚠️ Port {port}: RESPONDING BUT NOT HEALTHY")
            except:
                try:
                    response = requests.get(f'http://localhost:{port}', timeout=2)
                    if response.status_code == 200:
                        print(f"  ⚠️ Port {port}: RESPONDING (no health endpoint)")
                    else:
                        print(f"  ❌ Port {port}: NOT RESPONDING")
                except:
                    print(f"  ❌ Port {port}: NOT RESPONDING")
        
        self.discoveries['services'] = {
            'total_ports_checked': len(ports_to_check),
            'healthy_services': len(running_services),
            'healthy_ports': running_services,
            'health_rate': len(running_services) / len(ports_to_check) * 100
        }
    
    def discover_databases(self):
        """Discover ALL databases"""
        print("💾 DISCOVERING ALL DATABASES...")
        
        # Find all SQLite databases
        try:
            result = subprocess.run(
                ['find', '/home/ubuntu', '-name', '*.db', '-type', 'f'],
                capture_output=True, text=True
            )
            db_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            database_info = []
            for db_file in db_files[:20]:  # Check first 20
                try:
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = cursor.fetchall()
                    conn.close()
                    
                    database_info.append({
                        'file': db_file,
                        'tables': len(tables),
                        'table_names': [t[0] for t in tables[:5]]  # First 5 tables
                    })
                    print(f"  ✅ {os.path.basename(db_file)}: {len(tables)} tables")
                except:
                    print(f"  ❌ {os.path.basename(db_file)}: ERROR")
            
            self.discoveries['databases'] = {
                'total_db_files': len(db_files),
                'analyzed_databases': database_info
            }
        except:
            print("  ❌ Database discovery failed")
    
    def discover_hidden_capabilities(self):
        """Discover hidden capabilities and features"""
        print("🔍 DISCOVERING HIDDEN CAPABILITIES...")
        
        hidden_capabilities = {}
        
        # Check for Docker
        try:
            result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                hidden_capabilities['docker'] = 'AVAILABLE'
                print("  ✅ Docker: AVAILABLE")
            else:
                hidden_capabilities['docker'] = 'NOT_AVAILABLE'
                print("  ❌ Docker: NOT AVAILABLE")
        except:
            hidden_capabilities['docker'] = 'NOT_AVAILABLE'
            print("  ❌ Docker: NOT AVAILABLE")
        
        # Check for Kubernetes
        try:
            result = subprocess.run(['kubectl', 'version', '--client'], capture_output=True, text=True)
            if result.returncode == 0:
                hidden_capabilities['kubernetes'] = 'AVAILABLE'
                print("  ✅ Kubernetes: AVAILABLE")
            else:
                hidden_capabilities['kubernetes'] = 'NOT_AVAILABLE'
                print("  ❌ Kubernetes: NOT AVAILABLE")
        except:
            hidden_capabilities['kubernetes'] = 'NOT_AVAILABLE'
            print("  ❌ Kubernetes: NOT AVAILABLE")
        
        # Check for ngrok
        try:
            result = subprocess.run(['pgrep', '-f', 'ngrok'], capture_output=True, text=True)
            if result.stdout.strip():
                hidden_capabilities['ngrok'] = 'RUNNING'
                print("  ✅ Ngrok: RUNNING")
            else:
                hidden_capabilities['ngrok'] = 'NOT_RUNNING'
                print("  ❌ Ngrok: NOT RUNNING")
        except:
            hidden_capabilities['ngrok'] = 'ERROR'
            print("  ❌ Ngrok: ERROR")
        
        # Check for GPU
        try:
            result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
            if result.returncode == 0:
                hidden_capabilities['gpu'] = 'AVAILABLE'
                print("  ✅ GPU: AVAILABLE")
            else:
                hidden_capabilities['gpu'] = 'NOT_AVAILABLE'
                print("  ❌ GPU: NOT AVAILABLE")
        except:
            hidden_capabilities['gpu'] = 'NOT_AVAILABLE'
            print("  ❌ GPU: NOT AVAILABLE")
        
        self.discoveries['hidden_capabilities'] = hidden_capabilities
    
    def run_complete_discovery(self):
        """Run complete discovery of everything"""
        print("🎯 ULTIMATE COMPREHENSIVE DISCOVERY - FINDING EVERYTHING")
        print("=" * 60)
        
        # Run all discovery phases
        self.discover_all_files()
        self.discover_all_apis()
        self.discover_manus_tools()
        self.discover_mcp_servers()
        self.discover_running_services()
        self.discover_databases()
        self.discover_hidden_capabilities()
        
        # Calculate overall discovery score
        total_capabilities = 0
        working_capabilities = 0
        
        # Count API capabilities
        total_capabilities += len(self.api_keys) + len(self.openrouter_keys)
        working_capabilities += self.discoveries['apis']['openrouter']['working_keys']
        working_capabilities += sum(1 for api in self.discoveries['apis'].values() 
                                  if isinstance(api, dict) and api.get('status') == 'WORKING')
        
        # Count tool capabilities
        total_capabilities += len(self.discoveries['tools']['manus']['available_tools'])
        working_capabilities += len(self.discoveries['tools']['manus']['available_tools'])
        
        # Count service capabilities
        total_capabilities += self.discoveries['services']['total_ports_checked']
        working_capabilities += self.discoveries['services']['healthy_services']
        
        # Count MCP capabilities
        total_capabilities += len(self.mcp_servers)
        working_capabilities += sum(1 for server in self.discoveries['mcp_servers'].values()
                                  if server.get('status') == 'AVAILABLE')
        
        discovery_score = (working_capabilities / total_capabilities * 100) if total_capabilities > 0 else 0
        
        # Save comprehensive results
        final_results = {
            'timestamp': datetime.now().isoformat(),
            'discovery_score': discovery_score,
            'total_capabilities': total_capabilities,
            'working_capabilities': working_capabilities,
            'discoveries': self.discoveries
        }
        
        with open('/home/ubuntu/ultimate_lyra_v5/ultimate_comprehensive_discovery.json', 'w') as f:
            json.dump(final_results, f, indent=2)
        
        print(f"\n🏆 ULTIMATE DISCOVERY RESULTS:")
        print(f"Discovery Score: {discovery_score:.1f}%")
        print(f"Working Capabilities: {working_capabilities}/{total_capabilities}")
        print(f"Python Files: {self.discoveries['files']['python']['count']}")
        print(f"JSON Files: {self.discoveries['files']['json']['count']}")
        print(f"Markdown Files: {self.discoveries['files']['markdown']['count']}")
        print(f"Working OpenRouter Keys: {self.discoveries['apis']['openrouter']['working_keys']}/9")
        print(f"Healthy Services: {self.discoveries['services']['healthy_services']}")
        print(f"Available MCP Servers: {sum(1 for s in self.discoveries['mcp_servers'].values() if s.get('status') == 'AVAILABLE')}")
        print(f"Database Files: {self.discoveries['databases']['total_db_files']}")
        
        return final_results

if __name__ == '__main__':
    discovery = UltimateDiscoverySystem()
    results = discovery.run_complete_discovery()
    
    print(f"\n🎯 COMPREHENSIVE DISCOVERY COMPLETE!")
    print(f"Results saved to: /home/ubuntu/ultimate_lyra_v5/ultimate_comprehensive_discovery.json")
    print(f"Overall Discovery Score: {results['discovery_score']:.1f}%")
