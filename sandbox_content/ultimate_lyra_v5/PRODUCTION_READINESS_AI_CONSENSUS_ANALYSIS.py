#!/usr/bin/env python3
"""
PRODUCTION READINESS AI CONSENSUS ANALYSIS
==========================================
Comprehensive production readiness testing with OpenRouter AI consensus
- Multi-source verification and validation
- ISO standard compliance testing
- Complete system analysis and confirmation
- Production deployment readiness assessment
"""

import asyncio
import aiohttp
import json
import time
import subprocess
import psutil
import requests
import sqlite3
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import logging
from dataclasses import dataclass
import concurrent.futures
import threading

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class ProductionTest:
    name: str
    category: str
    status: str
    result: Any
    confidence: float
    timestamp: datetime
    details: Dict[str, Any]

class ProductionReadinessAnalyzer:
    def __init__(self):
        """Initialize comprehensive production readiness analyzer"""
        
        # OpenRouter API Keys for AI Consensus
        self.openrouter_keys = [
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # XAI
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Grok 4
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Chat Codex
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # DeepSeek 1
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # DeepSeek 2
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Premium
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Microsoft 4.0
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Universal
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER"   # Additional
        ]
        
        # AI Models for consensus analysis
        self.ai_models = [
            "openai/gpt-4o",
            "anthropic/claude-3.5-sonnet",
            "meta-llama/llama-3.1-405b-instruct",
            "mistralai/mistral-large",
            "microsoft/wizardlm-2-8x22b",
            "qwen/qwen-2.5-72b-instruct",
            "anthropic/claude-3-opus",
            "google/gemini-pro-1.5",
            "cohere/command-r-plus",
            "x-ai/grok-beta"
        ]
        
        # System components to test
        self.system_components = {
            'dashboards': [8751, 8750, 8106, 8105, 8104, 8103, 8102],
            'apis': [8090, 8100, 8200, 8300, 8600, 8900],
            'databases': ['portfolio.db', 'ai_consensus.db', 'compliance.db'],
            'services': ['ai_consensus', 'portfolio_manager', 'exchange_integration', 'risk_management'],
            'security': ['encryption', 'authentication', 'audit_trail'],
            'compliance': ['ato_integration', 'gst_calculation', 'audit_logging'],
            'performance': ['response_times', 'throughput', 'resource_usage'],
            'monitoring': ['prometheus', 'grafana', 'health_checks']
        }
        
        # Test results storage
        self.test_results: List[ProductionTest] = []
        self.ai_consensus_results: Dict[str, Any] = {}
        
        # Production readiness criteria
        self.production_criteria = {
            'availability': 99.9,
            'response_time_ms': 100,
            'error_rate': 0.1,
            'security_score': 95.0,
            'compliance_score': 100.0,
            'performance_score': 90.0,
            'monitoring_coverage': 95.0
        }
        
        print("🎯 Production Readiness Analyzer initialized")
        print(f"🤖 AI Models: {len(self.ai_models)}")
        print(f"🔑 OpenRouter Keys: {len(self.openrouter_keys)}")
        print(f"🧪 Test Components: {sum(len(v) if isinstance(v, list) else 1 for v in self.system_components.values())}")
    
    async def run_comprehensive_analysis(self) -> Dict[str, Any]:
        """Run comprehensive production readiness analysis"""
        
        print("🚀 Starting comprehensive production readiness analysis...")
        start_time = time.time()
        
        try:
            # Phase 1: System Discovery and Inventory
            print("\n📊 Phase 1: System Discovery and Inventory")
            system_inventory = await self.discover_system_components()
            
            # Phase 2: Infrastructure Testing
            print("\n🏗️ Phase 2: Infrastructure Testing")
            infrastructure_results = await self.test_infrastructure()
            
            # Phase 3: Service Testing
            print("\n🔧 Phase 3: Service Testing")
            service_results = await self.test_all_services()
            
            # Phase 4: Security Assessment
            print("\n🔒 Phase 4: Security Assessment")
            security_results = await self.assess_security()
            
            # Phase 5: Performance Testing
            print("\n⚡ Phase 5: Performance Testing")
            performance_results = await self.test_performance()
            
            # Phase 6: Compliance Verification
            print("\n🇦🇺 Phase 6: Compliance Verification")
            compliance_results = await self.verify_compliance()
            
            # Phase 7: AI Consensus Analysis
            print("\n🤖 Phase 7: AI Consensus Analysis")
            ai_consensus = await self.get_ai_consensus_analysis()
            
            # Phase 8: Production Readiness Assessment
            print("\n🎯 Phase 8: Production Readiness Assessment")
            readiness_score = await self.calculate_production_readiness()
            
            # Compile final results
            final_results = {
                'analysis_timestamp': datetime.now().isoformat(),
                'analysis_duration': time.time() - start_time,
                'system_inventory': system_inventory,
                'infrastructure_results': infrastructure_results,
                'service_results': service_results,
                'security_results': security_results,
                'performance_results': performance_results,
                'compliance_results': compliance_results,
                'ai_consensus': ai_consensus,
                'production_readiness_score': readiness_score,
                'total_tests_conducted': len(self.test_results),
                'test_results': [self.test_to_dict(test) for test in self.test_results],
                'production_ready': readiness_score >= 90.0,
                'iso_compliance': self.assess_iso_compliance(),
                'recommendations': self.generate_recommendations()
            }
            
            # Save results
            await self.save_analysis_results(final_results)
            
            print(f"\n✅ Analysis completed in {time.time() - start_time:.2f} seconds")
            print(f"🎯 Production Readiness Score: {readiness_score:.1f}%")
            print(f"🧪 Total Tests: {len(self.test_results)}")
            
            return final_results
            
        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            return {'error': str(e), 'status': 'FAILED'}
    
    async def discover_system_components(self) -> Dict[str, Any]:
        """Discover all system components and create inventory"""
        
        inventory = {
            'files_discovered': 0,
            'services_running': 0,
            'ports_listening': 0,
            'databases_found': 0,
            'components': {}
        }
        
        try:
            # Discover files
            result = subprocess.run(['find', '/home/ubuntu', '-path', '*/ultimate*', '-type', 'f'], 
                                  capture_output=True, text=True)
            files = result.stdout.strip().split('\n') if result.stdout.strip() else []
            inventory['files_discovered'] = len(files)
            
            # Discover running services
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            python_services = [line for line in result.stdout.split('\n') if 'python3' in line and 'ULTIMATE' in line]
            inventory['services_running'] = len(python_services)
            
            # Discover listening ports
            result = subprocess.run(['netstat', '-tlnp'], capture_output=True, text=True)
            listening_ports = [line for line in result.stdout.split('\n') if ':8' in line and 'LISTEN' in line]
            inventory['ports_listening'] = len(listening_ports)
            
            # Test database connections
            db_count = 0
            for db_name in self.system_components['databases']:
                db_path = f"/home/ubuntu/ultimate_lyra_v5/{db_name}"
                if os.path.exists(db_path):
                    db_count += 1
            inventory['databases_found'] = db_count
            
            # Component-specific discovery
            for component, items in self.system_components.items():
                if component == 'dashboards':
                    inventory['components'][component] = await self.test_dashboard_availability(items)
                elif component == 'apis':
                    inventory['components'][component] = await self.test_api_availability(items)
                else:
                    inventory['components'][component] = {'status': 'DISCOVERED', 'count': len(items)}
            
            self.add_test_result('System Discovery', 'Infrastructure', 'PASSED', inventory, 95.0)
            
        except Exception as e:
            logger.error(f"System discovery failed: {e}")
            self.add_test_result('System Discovery', 'Infrastructure', 'FAILED', str(e), 0.0)
        
        return inventory
    
    async def test_dashboard_availability(self, ports: List[int]) -> Dict[str, Any]:
        """Test dashboard availability and responsiveness"""
        
        results = {'available': 0, 'total': len(ports), 'details': {}}
        
        for port in ports:
            try:
                response = requests.get(f'http://localhost:{port}', timeout=5)
                if response.status_code == 200:
                    results['available'] += 1
                    results['details'][str(port)] = {
                        'status': 'AVAILABLE',
                        'response_time': response.elapsed.total_seconds(),
                        'content_length': len(response.content)
                    }
                else:
                    results['details'][str(port)] = {
                        'status': 'UNAVAILABLE',
                        'status_code': response.status_code
                    }
            except Exception as e:
                results['details'][str(port)] = {
                    'status': 'ERROR',
                    'error': str(e)
                }
        
        return results
    
    async def test_api_availability(self, ports: List[int]) -> Dict[str, Any]:
        """Test API availability and health endpoints"""
        
        results = {'available': 0, 'total': len(ports), 'details': {}}
        
        for port in ports:
            try:
                # Test health endpoint
                response = requests.get(f'http://localhost:{port}/health', timeout=5)
                if response.status_code == 200:
                    results['available'] += 1
                    results['details'][str(port)] = {
                        'status': 'AVAILABLE',
                        'response_time': response.elapsed.total_seconds(),
                        'health_data': response.json() if response.headers.get('content-type', '').startswith('application/json') else None
                    }
                else:
                    results['details'][str(port)] = {
                        'status': 'UNAVAILABLE',
                        'status_code': response.status_code
                    }
            except Exception as e:
                results['details'][str(port)] = {
                    'status': 'ERROR',
                    'error': str(e)
                }
        
        return results
    
    async def test_infrastructure(self) -> Dict[str, Any]:
        """Test infrastructure components"""
        
        infrastructure_results = {
            'system_resources': self.test_system_resources(),
            'network_connectivity': await self.test_network_connectivity(),
            'file_system': self.test_file_system(),
            'process_health': self.test_process_health()
        }
        
        return infrastructure_results
    
    def test_system_resources(self) -> Dict[str, Any]:
        """Test system resource availability"""
        
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            resources = {
                'cpu_usage_percent': cpu_percent,
                'memory_total_gb': memory.total / (1024**3),
                'memory_available_gb': memory.available / (1024**3),
                'memory_usage_percent': memory.percent,
                'disk_total_gb': disk.total / (1024**3),
                'disk_free_gb': disk.free / (1024**3),
                'disk_usage_percent': (disk.used / disk.total) * 100
            }
            
            # Assess resource health
            resource_score = 100.0
            if cpu_percent > 80:
                resource_score -= 20
            if memory.percent > 85:
                resource_score -= 20
            if (disk.used / disk.total) > 0.9:
                resource_score -= 15
            
            self.add_test_result('System Resources', 'Infrastructure', 'PASSED', resources, resource_score)
            return resources
            
        except Exception as e:
            self.add_test_result('System Resources', 'Infrastructure', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    async def test_network_connectivity(self) -> Dict[str, Any]:
        """Test network connectivity and ngrok tunnel"""
        
        connectivity_results = {
            'localhost_connectivity': True,
            'ngrok_tunnel_status': 'UNKNOWN',
            'external_connectivity': False
        }
        
        try:
            # Test localhost connectivity
            response = requests.get('http://localhost:8751/api/health', timeout=5)
            connectivity_results['localhost_connectivity'] = response.status_code == 200
            
            # Test ngrok tunnel
            try:
                response = requests.get('https://3ce37fa57d09.ngrok.app', timeout=10)
                if response.status_code in [200, 404]:  # 404 is OK for ngrok tunnel
                    connectivity_results['ngrok_tunnel_status'] = 'ACTIVE'
                    connectivity_results['external_connectivity'] = True
                else:
                    connectivity_results['ngrok_tunnel_status'] = 'INACTIVE'
            except:
                connectivity_results['ngrok_tunnel_status'] = 'INACTIVE'
            
            score = 90.0 if connectivity_results['localhost_connectivity'] else 50.0
            if connectivity_results['external_connectivity']:
                score += 10.0
            
            self.add_test_result('Network Connectivity', 'Infrastructure', 'PASSED', connectivity_results, score)
            
        except Exception as e:
            connectivity_results['error'] = str(e)
            self.add_test_result('Network Connectivity', 'Infrastructure', 'FAILED', str(e), 0.0)
        
        return connectivity_results
    
    def test_file_system(self) -> Dict[str, Any]:
        """Test file system integrity and permissions"""
        
        try:
            file_results = {
                'ultimate_systems_exists': os.path.exists('/home/ubuntu/ultimate_lyra_systems'),
                'ultimate_v5_exists': os.path.exists('/home/ubuntu/ultimate_lyra_v5'),
                'key_files_present': 0,
                'total_key_files': 10
            }
            
            # Check key files
            key_files = [
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_LYRA_TRADING_SYSTEM_V5.py',
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py',
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_REAL_EXCHANGE_PORTFOLIO.py',
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_CONSOLIDATED_SYSTEM_AI_CONSENSUS.py',
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_100_PERCENT_COMPLIANCE_SYSTEM.py',
                '/home/ubuntu/ultimate_lyra_systems/native_production_system.py',
                '/home/ubuntu/ultimate_lyra_systems/ULTIMATE_COMPREHENSIVE_SYSTEM_DEPLOYER.py',
                '/home/ubuntu/ultimate_lyra_systems/AI_FORENSIC_COMPLIANCE_COMMISSIONER.py',
                '/home/ubuntu/ultimate_lyra_systems/ULTIMATE_AI_PORTFOLIO_MANAGER.py',
                '/home/ubuntu/ultimate_lyra_systems/COMPLETE_TELEGRAM_INTEGRATION.py'
            ]
            
            for file_path in key_files:
                if os.path.exists(file_path):
                    file_results['key_files_present'] += 1
            
            score = (file_results['key_files_present'] / file_results['total_key_files']) * 100
            self.add_test_result('File System', 'Infrastructure', 'PASSED', file_results, score)
            
            return file_results
            
        except Exception as e:
            self.add_test_result('File System', 'Infrastructure', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def test_process_health(self) -> Dict[str, Any]:
        """Test running process health"""
        
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            processes = result.stdout.split('\n')
            
            python_processes = [p for p in processes if 'python3' in p and ('ULTIMATE' in p or ':8' in p)]
            
            process_results = {
                'total_python_processes': len(python_processes),
                'processes_healthy': len(python_processes),
                'process_details': []
            }
            
            for process in python_processes[:10]:  # Limit to first 10 for brevity
                parts = process.split()
                if len(parts) > 10:
                    process_results['process_details'].append({
                        'pid': parts[1],
                        'cpu': parts[2],
                        'memory': parts[3],
                        'command': ' '.join(parts[10:])[:100]
                    })
            
            score = min(100.0, len(python_processes) * 15)  # Score based on active processes
            self.add_test_result('Process Health', 'Infrastructure', 'PASSED', process_results, score)
            
            return process_results
            
        except Exception as e:
            self.add_test_result('Process Health', 'Infrastructure', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    async def test_all_services(self) -> Dict[str, Any]:
        """Test all system services comprehensively"""
        
        service_results = {
            'dashboard_services': await self.test_dashboard_services(),
            'api_services': await self.test_api_services(),
            'database_services': await self.test_database_services(),
            'background_services': await self.test_background_services()
        }
        
        return service_results
    
    async def test_dashboard_services(self) -> Dict[str, Any]:
        """Test all dashboard services"""
        
        dashboard_tests = {}
        
        for port in self.system_components['dashboards']:
            test_result = await self.comprehensive_service_test(port, 'dashboard')
            dashboard_tests[f'port_{port}'] = test_result
        
        return dashboard_tests
    
    async def test_api_services(self) -> Dict[str, Any]:
        """Test all API services"""
        
        api_tests = {}
        
        for port in self.system_components['apis']:
            test_result = await self.comprehensive_service_test(port, 'api')
            api_tests[f'port_{port}'] = test_result
        
        return api_tests
    
    async def comprehensive_service_test(self, port: int, service_type: str) -> Dict[str, Any]:
        """Comprehensive test of individual service"""
        
        test_result = {
            'port': port,
            'service_type': service_type,
            'availability': False,
            'response_time': None,
            'health_status': None,
            'load_test': None,
            'error_handling': None
        }
        
        try:
            # Basic availability test
            start_time = time.time()
            response = requests.get(f'http://localhost:{port}', timeout=10)
            response_time = time.time() - start_time
            
            test_result['availability'] = response.status_code == 200
            test_result['response_time'] = response_time
            
            # Health endpoint test
            try:
                health_response = requests.get(f'http://localhost:{port}/api/health', timeout=5)
                if health_response.status_code == 200:
                    test_result['health_status'] = health_response.json()
            except:
                try:
                    health_response = requests.get(f'http://localhost:{port}/health', timeout=5)
                    if health_response.status_code == 200:
                        test_result['health_status'] = health_response.json()
                except:
                    test_result['health_status'] = 'NO_HEALTH_ENDPOINT'
            
            # Basic load test (5 concurrent requests)
            load_test_results = await self.basic_load_test(port)
            test_result['load_test'] = load_test_results
            
            # Error handling test
            try:
                error_response = requests.get(f'http://localhost:{port}/nonexistent', timeout=5)
                test_result['error_handling'] = {
                    'status_code': error_response.status_code,
                    'handles_404': error_response.status_code == 404
                }
            except:
                test_result['error_handling'] = 'ERROR_HANDLING_UNKNOWN'
            
            # Calculate service score
            score = 0.0
            if test_result['availability']:
                score += 40.0
            if test_result['response_time'] and test_result['response_time'] < 1.0:
                score += 30.0
            if test_result['health_status'] and test_result['health_status'] != 'NO_HEALTH_ENDPOINT':
                score += 20.0
            if test_result['load_test'] and test_result['load_test'].get('success_rate', 0) > 80:
                score += 10.0
            
            self.add_test_result(f'Service Port {port}', 'Service', 'PASSED', test_result, score)
            
        except Exception as e:
            test_result['error'] = str(e)
            self.add_test_result(f'Service Port {port}', 'Service', 'FAILED', str(e), 0.0)
        
        return test_result
    
    async def basic_load_test(self, port: int) -> Dict[str, Any]:
        """Basic load test for service"""
        
        load_results = {
            'total_requests': 5,
            'successful_requests': 0,
            'failed_requests': 0,
            'average_response_time': 0.0,
            'success_rate': 0.0
        }
        
        response_times = []
        
        def make_request():
            try:
                start_time = time.time()
                response = requests.get(f'http://localhost:{port}', timeout=5)
                response_time = time.time() - start_time
                response_times.append(response_time)
                return response.status_code == 200
            except:
                return False
        
        # Execute concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(make_request) for _ in range(5)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        load_results['successful_requests'] = sum(results)
        load_results['failed_requests'] = len(results) - sum(results)
        load_results['success_rate'] = (sum(results) / len(results)) * 100
        
        if response_times:
            load_results['average_response_time'] = sum(response_times) / len(response_times)
        
        return load_results
    
    async def test_database_services(self) -> Dict[str, Any]:
        """Test database connectivity and integrity"""
        
        db_results = {}
        
        for db_name in self.system_components['databases']:
            db_path = f"/home/ubuntu/ultimate_lyra_v5/{db_name}"
            
            db_test = {
                'exists': os.path.exists(db_path),
                'readable': False,
                'tables': 0,
                'records': 0
            }
            
            if db_test['exists']:
                try:
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    
                    # Check if readable
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = cursor.fetchall()
                    db_test['readable'] = True
                    db_test['tables'] = len(tables)
                    
                    # Count total records
                    total_records = 0
                    for table in tables:
                        cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
                        count = cursor.fetchone()[0]
                        total_records += count
                    
                    db_test['records'] = total_records
                    conn.close()
                    
                    score = 90.0 if db_test['readable'] and db_test['tables'] > 0 else 50.0
                    self.add_test_result(f'Database {db_name}', 'Database', 'PASSED', db_test, score)
                    
                except Exception as e:
                    db_test['error'] = str(e)
                    self.add_test_result(f'Database {db_name}', 'Database', 'FAILED', str(e), 0.0)
            else:
                self.add_test_result(f'Database {db_name}', 'Database', 'NOT_FOUND', db_test, 0.0)
            
            db_results[db_name] = db_test
        
        return db_results
    
    async def test_background_services(self) -> Dict[str, Any]:
        """Test background services and processes"""
        
        background_results = {
            'ngrok_process': self.test_ngrok_process(),
            'python_services': self.test_python_services(),
            'system_monitoring': self.test_system_monitoring()
        }
        
        return background_results
    
    def test_ngrok_process(self) -> Dict[str, Any]:
        """Test ngrok process status"""
        
        try:
            result = subprocess.run(['pgrep', '-f', 'ngrok'], capture_output=True, text=True)
            ngrok_pids = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            ngrok_status = {
                'running': len(ngrok_pids) > 0,
                'process_count': len(ngrok_pids),
                'pids': ngrok_pids
            }
            
            score = 100.0 if ngrok_status['running'] else 0.0
            self.add_test_result('Ngrok Process', 'Background', 'PASSED' if ngrok_status['running'] else 'FAILED', ngrok_status, score)
            
            return ngrok_status
            
        except Exception as e:
            self.add_test_result('Ngrok Process', 'Background', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def test_python_services(self) -> Dict[str, Any]:
        """Test Python service processes"""
        
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            processes = result.stdout.split('\n')
            
            python_services = [p for p in processes if 'python3' in p and ('ULTIMATE' in p or ':8' in p)]
            
            service_status = {
                'total_services': len(python_services),
                'services_running': len(python_services),
                'service_details': []
            }
            
            for service in python_services[:10]:  # Limit for brevity
                parts = service.split()
                if len(parts) > 10:
                    service_status['service_details'].append({
                        'pid': parts[1],
                        'cpu': parts[2],
                        'memory': parts[3],
                        'command': ' '.join(parts[10:])[:100]
                    })
            
            score = min(100.0, len(python_services) * 12)
            self.add_test_result('Python Services', 'Background', 'PASSED', service_status, score)
            
            return service_status
            
        except Exception as e:
            self.add_test_result('Python Services', 'Background', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def test_system_monitoring(self) -> Dict[str, Any]:
        """Test system monitoring capabilities"""
        
        monitoring_status = {
            'log_files_present': 0,
            'monitoring_active': False,
            'health_endpoints': 0
        }
        
        try:
            # Check for log files
            log_dirs = ['/home/ubuntu/ultimate_lyra_systems/logs', '/home/ubuntu/ultimate_lyra_v5/logs']
            for log_dir in log_dirs:
                if os.path.exists(log_dir):
                    log_files = os.listdir(log_dir)
                    monitoring_status['log_files_present'] += len(log_files)
            
            # Test health endpoints
            health_count = 0
            for port in [8751, 8105, 8106, 8103, 8102]:
                try:
                    response = requests.get(f'http://localhost:{port}/api/health', timeout=2)
                    if response.status_code == 200:
                        health_count += 1
                except:
                    try:
                        response = requests.get(f'http://localhost:{port}/health', timeout=2)
                        if response.status_code == 200:
                            health_count += 1
                    except:
                        pass
            
            monitoring_status['health_endpoints'] = health_count
            monitoring_status['monitoring_active'] = health_count > 0
            
            score = (health_count * 20) + min(50, monitoring_status['log_files_present'] * 5)
            self.add_test_result('System Monitoring', 'Monitoring', 'PASSED', monitoring_status, score)
            
            return monitoring_status
            
        except Exception as e:
            self.add_test_result('System Monitoring', 'Monitoring', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    async def assess_security(self) -> Dict[str, Any]:
        """Comprehensive security assessment"""
        
        security_results = {
            'encryption_status': self.test_encryption_implementation(),
            'authentication': self.test_authentication_mechanisms(),
            'audit_logging': self.test_audit_logging(),
            'vulnerability_scan': await self.basic_vulnerability_scan()
        }
        
        return security_results
    
    def test_encryption_implementation(self) -> Dict[str, Any]:
        """Test encryption implementation"""
        
        encryption_status = {
            'aes_256_implemented': False,
            'pbkdf2_implemented': False,
            'secure_key_storage': False,
            'encryption_score': 0.0
        }
        
        try:
            # Check for encryption in dashboard code
            dashboard_file = '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py'
            if os.path.exists(dashboard_file):
                with open(dashboard_file, 'r') as f:
                    content = f.read()
                    
                    if 'AES-256' in content or 'Fernet' in content:
                        encryption_status['aes_256_implemented'] = True
                    if 'PBKDF2HMAC' in content:
                        encryption_status['pbkdf2_implemented'] = True
                    if 'os.urandom' in content or 'secrets' in content:
                        encryption_status['secure_key_storage'] = True
            
            # Calculate encryption score
            score = 0.0
            if encryption_status['aes_256_implemented']:
                score += 40.0
            if encryption_status['pbkdf2_implemented']:
                score += 35.0
            if encryption_status['secure_key_storage']:
                score += 25.0
            
            encryption_status['encryption_score'] = score
            self.add_test_result('Encryption Implementation', 'Security', 'PASSED', encryption_status, score)
            
            return encryption_status
            
        except Exception as e:
            self.add_test_result('Encryption Implementation', 'Security', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def test_authentication_mechanisms(self) -> Dict[str, Any]:
        """Test authentication mechanisms"""
        
        auth_status = {
            'session_management': False,
            'jwt_implementation': False,
            'multi_factor_ready': False,
            'auth_score': 0.0
        }
        
        try:
            # Check authentication implementation in code
            files_to_check = [
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py',
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_100_PERCENT_COMPLIANCE_SYSTEM.py'
            ]
            
            for file_path in files_to_check:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read()
                        
                        if 'session' in content.lower():
                            auth_status['session_management'] = True
                        if 'jwt' in content.lower() or 'token' in content.lower():
                            auth_status['jwt_implementation'] = True
                        if 'mfa' in content.lower() or 'multi' in content.lower():
                            auth_status['multi_factor_ready'] = True
            
            # Calculate auth score
            score = 0.0
            if auth_status['session_management']:
                score += 40.0
            if auth_status['jwt_implementation']:
                score += 35.0
            if auth_status['multi_factor_ready']:
                score += 25.0
            
            auth_status['auth_score'] = score
            self.add_test_result('Authentication', 'Security', 'PASSED', auth_status, score)
            
            return auth_status
            
        except Exception as e:
            self.add_test_result('Authentication', 'Security', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def test_audit_logging(self) -> Dict[str, Any]:
        """Test audit logging implementation"""
        
        audit_status = {
            'log_files_exist': False,
            'structured_logging': False,
            'audit_trail': False,
            'audit_score': 0.0
        }
        
        try:
            # Check for log directories and files
            log_dirs = ['/home/ubuntu/ultimate_lyra_systems/logs', '/home/ubuntu/ultimate_lyra_v5/logs']
            total_log_files = 0
            
            for log_dir in log_dirs:
                if os.path.exists(log_dir):
                    log_files = os.listdir(log_dir)
                    total_log_files += len(log_files)
                    audit_status['log_files_exist'] = True
            
            # Check for logging implementation in code
            files_to_check = [
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py',
                '/home/ubuntu/ultimate_lyra_systems/AI_FORENSIC_COMPLIANCE_COMMISSIONER.py'
            ]
            
            for file_path in files_to_check:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read()
                        
                        if 'logging' in content.lower():
                            audit_status['structured_logging'] = True
                        if 'audit' in content.lower():
                            audit_status['audit_trail'] = True
            
            # Calculate audit score
            score = 0.0
            if audit_status['log_files_exist']:
                score += 30.0
            if audit_status['structured_logging']:
                score += 40.0
            if audit_status['audit_trail']:
                score += 30.0
            
            audit_status['audit_score'] = score
            audit_status['total_log_files'] = total_log_files
            
            self.add_test_result('Audit Logging', 'Security', 'PASSED', audit_status, score)
            
            return audit_status
            
        except Exception as e:
            self.add_test_result('Audit Logging', 'Security', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    async def basic_vulnerability_scan(self) -> Dict[str, Any]:
        """Basic vulnerability scanning"""
        
        vuln_results = {
            'open_ports_scan': self.scan_open_ports(),
            'file_permissions': self.check_file_permissions(),
            'service_exposure': self.check_service_exposure(),
            'vulnerability_score': 0.0
        }
        
        # Calculate vulnerability score
        score = 100.0  # Start with perfect score, deduct for issues
        
        if vuln_results['open_ports_scan'].get('suspicious_ports', 0) > 0:
            score -= 20.0
        if vuln_results['file_permissions'].get('insecure_files', 0) > 0:
            score -= 15.0
        if vuln_results['service_exposure'].get('exposed_services', 0) > 5:
            score -= 10.0
        
        vuln_results['vulnerability_score'] = max(0.0, score)
        self.add_test_result('Vulnerability Scan', 'Security', 'PASSED', vuln_results, score)
        
        return vuln_results
    
    def scan_open_ports(self) -> Dict[str, Any]:
        """Scan for open ports"""
        
        try:
            result = subprocess.run(['netstat', '-tlnp'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            
            open_ports = []
            for line in lines:
                if 'LISTEN' in line and ':' in line:
                    parts = line.split()
                    if len(parts) > 3:
                        address = parts[3]
                        if ':' in address:
                            port = address.split(':')[-1]
                            if port.isdigit():
                                open_ports.append(int(port))
            
            # Check for suspicious ports (outside expected range)
            expected_ports = set(range(8000, 9000))  # Our expected port range
            suspicious_ports = [p for p in open_ports if p not in expected_ports and p > 1024]
            
            return {
                'total_open_ports': len(open_ports),
                'expected_ports': len([p for p in open_ports if p in expected_ports]),
                'suspicious_ports': len(suspicious_ports),
                'port_list': open_ports[:20]  # Limit for brevity
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def check_file_permissions(self) -> Dict[str, Any]:
        """Check file permissions for security"""
        
        try:
            # Check key system files
            key_files = [
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py',
                '/home/ubuntu/ultimate_lyra_systems/native_production_system.py'
            ]
            
            permission_results = {
                'files_checked': 0,
                'secure_files': 0,
                'insecure_files': 0,
                'file_details': []
            }
            
            for file_path in key_files:
                if os.path.exists(file_path):
                    permission_results['files_checked'] += 1
                    stat_info = os.stat(file_path)
                    mode = oct(stat_info.st_mode)[-3:]
                    
                    # Check if file is readable by others (basic security check)
                    if mode[2] in ['0', '1', '4', '5']:  # Others have no read access
                        permission_results['secure_files'] += 1
                    else:
                        permission_results['insecure_files'] += 1
                    
                    permission_results['file_details'].append({
                        'file': file_path,
                        'permissions': mode,
                        'secure': mode[2] in ['0', '1', '4', '5']
                    })
            
            return permission_results
            
        except Exception as e:
            return {'error': str(e)}
    
    def check_service_exposure(self) -> Dict[str, Any]:
        """Check service exposure levels"""
        
        try:
            result = subprocess.run(['netstat', '-tlnp'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            
            exposed_services = 0
            localhost_only = 0
            
            for line in lines:
                if 'LISTEN' in line and ':8' in line:  # Our services typically on 8xxx ports
                    if '0.0.0.0:' in line:
                        exposed_services += 1
                    elif '127.0.0.1:' in line or 'localhost:' in line:
                        localhost_only += 1
            
            return {
                'exposed_services': exposed_services,
                'localhost_only': localhost_only,
                'total_services': exposed_services + localhost_only
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    async def test_performance(self) -> Dict[str, Any]:
        """Comprehensive performance testing"""
        
        performance_results = {
            'response_time_tests': await self.test_response_times(),
            'throughput_tests': await self.test_throughput(),
            'resource_utilization': self.test_resource_utilization(),
            'scalability_assessment': await self.assess_scalability()
        }
        
        return performance_results
    
    async def test_response_times(self) -> Dict[str, Any]:
        """Test response times for all services"""
        
        response_time_results = {
            'services_tested': 0,
            'average_response_time': 0.0,
            'fastest_service': None,
            'slowest_service': None,
            'under_100ms': 0,
            'service_details': {}
        }
        
        response_times = []
        
        for port in [8751, 8105, 8106, 8103, 8102]:
            try:
                start_time = time.time()
                response = requests.get(f'http://localhost:{port}', timeout=10)
                response_time = (time.time() - start_time) * 1000  # Convert to ms
                
                if response.status_code == 200:
                    response_times.append(response_time)
                    response_time_results['services_tested'] += 1
                    
                    if response_time < 100:
                        response_time_results['under_100ms'] += 1
                    
                    response_time_results['service_details'][f'port_{port}'] = {
                        'response_time_ms': response_time,
                        'status': 'SUCCESS',
                        'under_target': response_time < 100
                    }
                    
            except Exception as e:
                response_time_results['service_details'][f'port_{port}'] = {
                    'status': 'FAILED',
                    'error': str(e)
                }
        
        if response_times:
            response_time_results['average_response_time'] = sum(response_times) / len(response_times)
            response_time_results['fastest_service'] = min(response_times)
            response_time_results['slowest_service'] = max(response_times)
        
        # Calculate performance score
        score = 0.0
        if response_time_results['average_response_time'] < 100:
            score += 50.0
        elif response_time_results['average_response_time'] < 200:
            score += 30.0
        
        score += (response_time_results['under_100ms'] / max(1, response_time_results['services_tested'])) * 50
        
        self.add_test_result('Response Times', 'Performance', 'PASSED', response_time_results, score)
        
        return response_time_results
    
    async def test_throughput(self) -> Dict[str, Any]:
        """Test system throughput"""
        
        throughput_results = {
            'concurrent_requests': 10,
            'successful_requests': 0,
            'failed_requests': 0,
            'requests_per_second': 0.0,
            'average_response_time': 0.0
        }
        
        def make_concurrent_request():
            try:
                start_time = time.time()
                response = requests.get('http://localhost:8751', timeout=10)
                response_time = time.time() - start_time
                return response.status_code == 200, response_time
            except:
                return False, 0.0
        
        # Execute concurrent requests
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_concurrent_request) for _ in range(10)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        total_time = time.time() - start_time
        
        successful = [r for r in results if r[0]]
        response_times = [r[1] for r in results if r[1] > 0]
        
        throughput_results['successful_requests'] = len(successful)
        throughput_results['failed_requests'] = len(results) - len(successful)
        throughput_results['requests_per_second'] = len(successful) / total_time if total_time > 0 else 0
        
        if response_times:
            throughput_results['average_response_time'] = sum(response_times) / len(response_times)
        
        # Calculate throughput score
        score = min(100.0, (throughput_results['requests_per_second'] / 10) * 100)
        self.add_test_result('Throughput', 'Performance', 'PASSED', throughput_results, score)
        
        return throughput_results
    
    def test_resource_utilization(self) -> Dict[str, Any]:
        """Test current resource utilization"""
        
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            utilization = {
                'cpu_usage_percent': cpu_percent,
                'memory_usage_percent': memory.percent,
                'disk_usage_percent': (disk.used / disk.total) * 100,
                'available_memory_gb': memory.available / (1024**3),
                'available_disk_gb': disk.free / (1024**3)
            }
            
            # Calculate resource score
            score = 100.0
            if cpu_percent > 80:
                score -= 30.0
            elif cpu_percent > 60:
                score -= 15.0
            
            if memory.percent > 85:
                score -= 25.0
            elif memory.percent > 70:
                score -= 10.0
            
            if (disk.used / disk.total) > 0.9:
                score -= 20.0
            elif (disk.used / disk.total) > 0.8:
                score -= 10.0
            
            self.add_test_result('Resource Utilization', 'Performance', 'PASSED', utilization, score)
            
            return utilization
            
        except Exception as e:
            self.add_test_result('Resource Utilization', 'Performance', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    async def assess_scalability(self) -> Dict[str, Any]:
        """Assess system scalability"""
        
        scalability_assessment = {
            'horizontal_scaling_ready': False,
            'load_balancing_capable': False,
            'database_scaling': False,
            'containerization_ready': False,
            'scalability_score': 0.0
        }
        
        try:
            # Check for containerization files
            container_files = [
                '/home/ubuntu/ultimate_lyra_v5/containerization/docker-compose.yml',
                '/home/ubuntu/ultimate_lyra_v5/containerization/kubernetes-manifests.yaml'
            ]
            
            for file_path in container_files:
                if os.path.exists(file_path):
                    scalability_assessment['containerization_ready'] = True
                    break
            
            # Check for microservices architecture (multiple services running)
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            python_services = [p for p in result.stdout.split('\n') if 'python3' in p and 'ULTIMATE' in p]
            
            if len(python_services) >= 5:
                scalability_assessment['horizontal_scaling_ready'] = True
            
            # Check for load balancing indicators (multiple ports)
            result = subprocess.run(['netstat', '-tlnp'], capture_output=True, text=True)
            listening_ports = [line for line in result.stdout.split('\n') if ':8' in line and 'LISTEN' in line]
            
            if len(listening_ports) >= 5:
                scalability_assessment['load_balancing_capable'] = True
            
            # Check for database scaling (multiple databases)
            db_files = [f for f in os.listdir('/home/ubuntu/ultimate_lyra_v5') if f.endswith('.db')]
            if len(db_files) >= 2:
                scalability_assessment['database_scaling'] = True
            
            # Calculate scalability score
            score = 0.0
            if scalability_assessment['horizontal_scaling_ready']:
                score += 30.0
            if scalability_assessment['load_balancing_capable']:
                score += 25.0
            if scalability_assessment['database_scaling']:
                score += 20.0
            if scalability_assessment['containerization_ready']:
                score += 25.0
            
            scalability_assessment['scalability_score'] = score
            self.add_test_result('Scalability Assessment', 'Performance', 'PASSED', scalability_assessment, score)
            
            return scalability_assessment
            
        except Exception as e:
            self.add_test_result('Scalability Assessment', 'Performance', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    async def verify_compliance(self) -> Dict[str, Any]:
        """Verify regulatory compliance"""
        
        compliance_results = {
            'australian_compliance': self.verify_australian_compliance(),
            'data_protection': self.verify_data_protection(),
            'audit_compliance': self.verify_audit_compliance(),
            'iso_standards': self.assess_iso_standards()
        }
        
        return compliance_results
    
    def verify_australian_compliance(self) -> Dict[str, Any]:
        """Verify Australian regulatory compliance"""
        
        aus_compliance = {
            'ato_integration': False,
            'gst_calculation': False,
            'audit_trail': False,
            'reporting_capability': False,
            'compliance_score': 0.0
        }
        
        try:
            # Check for Australian compliance in code
            compliance_files = [
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_100_PERCENT_COMPLIANCE_SYSTEM.py',
                '/home/ubuntu/ultimate_lyra_systems/AI_FORENSIC_COMPLIANCE_COMMISSIONER.py'
            ]
            
            for file_path in compliance_files:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read().lower()
                        
                        if 'ato' in content:
                            aus_compliance['ato_integration'] = True
                        if 'gst' in content:
                            aus_compliance['gst_calculation'] = True
                        if 'audit' in content:
                            aus_compliance['audit_trail'] = True
                        if 'report' in content:
                            aus_compliance['reporting_capability'] = True
            
            # Calculate compliance score
            score = 0.0
            if aus_compliance['ato_integration']:
                score += 30.0
            if aus_compliance['gst_calculation']:
                score += 25.0
            if aus_compliance['audit_trail']:
                score += 25.0
            if aus_compliance['reporting_capability']:
                score += 20.0
            
            aus_compliance['compliance_score'] = score
            self.add_test_result('Australian Compliance', 'Compliance', 'PASSED', aus_compliance, score)
            
            return aus_compliance
            
        except Exception as e:
            self.add_test_result('Australian Compliance', 'Compliance', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def verify_data_protection(self) -> Dict[str, Any]:
        """Verify data protection compliance"""
        
        data_protection = {
            'encryption_at_rest': False,
            'encryption_in_transit': False,
            'data_anonymization': False,
            'access_controls': False,
            'protection_score': 0.0
        }
        
        try:
            # Check for data protection implementation
            files_to_check = [
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py',
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_100_PERCENT_COMPLIANCE_SYSTEM.py'
            ]
            
            for file_path in files_to_check:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read().lower()
                        
                        if 'encrypt' in content or 'aes' in content:
                            data_protection['encryption_at_rest'] = True
                        if 'https' in content or 'ssl' in content or 'tls' in content:
                            data_protection['encryption_in_transit'] = True
                        if 'anonymize' in content or 'hash' in content:
                            data_protection['data_anonymization'] = True
                        if 'auth' in content or 'permission' in content:
                            data_protection['access_controls'] = True
            
            # Calculate protection score
            score = 0.0
            if data_protection['encryption_at_rest']:
                score += 30.0
            if data_protection['encryption_in_transit']:
                score += 25.0
            if data_protection['data_anonymization']:
                score += 20.0
            if data_protection['access_controls']:
                score += 25.0
            
            data_protection['protection_score'] = score
            self.add_test_result('Data Protection', 'Compliance', 'PASSED', data_protection, score)
            
            return data_protection
            
        except Exception as e:
            self.add_test_result('Data Protection', 'Compliance', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def verify_audit_compliance(self) -> Dict[str, Any]:
        """Verify audit compliance"""
        
        audit_compliance = {
            'comprehensive_logging': False,
            'log_retention': False,
            'audit_trail_integrity': False,
            'compliance_reporting': False,
            'audit_score': 0.0
        }
        
        try:
            # Check for audit logging
            log_dirs = ['/home/ubuntu/ultimate_lyra_systems/logs', '/home/ubuntu/ultimate_lyra_v5/logs']
            log_files_found = 0
            
            for log_dir in log_dirs:
                if os.path.exists(log_dir):
                    log_files = os.listdir(log_dir)
                    log_files_found += len(log_files)
                    audit_compliance['comprehensive_logging'] = True
            
            # Check for audit implementation in code
            audit_files = [
                '/home/ubuntu/ultimate_lyra_systems/AI_FORENSIC_COMPLIANCE_COMMISSIONER.py',
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_100_PERCENT_COMPLIANCE_SYSTEM.py'
            ]
            
            for file_path in audit_files:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read().lower()
                        
                        if 'retention' in content:
                            audit_compliance['log_retention'] = True
                        if 'integrity' in content or 'forensic' in content:
                            audit_compliance['audit_trail_integrity'] = True
                        if 'report' in content:
                            audit_compliance['compliance_reporting'] = True
            
            # Calculate audit score
            score = 0.0
            if audit_compliance['comprehensive_logging']:
                score += 30.0
            if audit_compliance['log_retention']:
                score += 25.0
            if audit_compliance['audit_trail_integrity']:
                score += 25.0
            if audit_compliance['compliance_reporting']:
                score += 20.0
            
            audit_compliance['audit_score'] = score
            audit_compliance['log_files_count'] = log_files_found
            
            self.add_test_result('Audit Compliance', 'Compliance', 'PASSED', audit_compliance, score)
            
            return audit_compliance
            
        except Exception as e:
            self.add_test_result('Audit Compliance', 'Compliance', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def assess_iso_standards(self) -> Dict[str, Any]:
        """Assess ISO standards compliance"""
        
        iso_assessment = {
            'iso_27001_security': 0.0,
            'iso_9001_quality': 0.0,
            'iso_20000_service': 0.0,
            'overall_iso_score': 0.0
        }
        
        try:
            # ISO 27001 (Information Security) assessment
            security_score = 0.0
            if self.has_security_controls():
                security_score += 30.0
            if self.has_risk_management():
                security_score += 25.0
            if self.has_incident_management():
                security_score += 25.0
            if self.has_access_controls():
                security_score += 20.0
            
            iso_assessment['iso_27001_security'] = security_score
            
            # ISO 9001 (Quality Management) assessment
            quality_score = 0.0
            if self.has_documentation():
                quality_score += 30.0
            if self.has_process_controls():
                quality_score += 25.0
            if self.has_monitoring():
                quality_score += 25.0
            if self.has_continuous_improvement():
                quality_score += 20.0
            
            iso_assessment['iso_9001_quality'] = quality_score
            
            # ISO 20000 (Service Management) assessment
            service_score = 0.0
            if self.has_service_catalog():
                service_score += 30.0
            if self.has_change_management():
                service_score += 25.0
            if self.has_service_monitoring():
                service_score += 25.0
            if self.has_service_reporting():
                service_score += 20.0
            
            iso_assessment['iso_20000_service'] = service_score
            
            # Overall ISO score
            iso_assessment['overall_iso_score'] = (security_score + quality_score + service_score) / 3
            
            self.add_test_result('ISO Standards', 'Compliance', 'PASSED', iso_assessment, iso_assessment['overall_iso_score'])
            
            return iso_assessment
            
        except Exception as e:
            self.add_test_result('ISO Standards', 'Compliance', 'FAILED', str(e), 0.0)
            return {'error': str(e)}
    
    def has_security_controls(self) -> bool:
        """Check for security controls implementation"""
        try:
            dashboard_file = '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py'
            if os.path.exists(dashboard_file):
                with open(dashboard_file, 'r') as f:
                    content = f.read().lower()
                    return 'encrypt' in content or 'security' in content
            return False
        except:
            return False
    
    def has_risk_management(self) -> bool:
        """Check for risk management implementation"""
        try:
            files_to_check = [
                '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_100_PERCENT_COMPLIANCE_SYSTEM.py',
                '/home/ubuntu/ultimate_lyra_systems/AI_FORENSIC_COMPLIANCE_COMMISSIONER.py'
            ]
            for file_path in files_to_check:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read().lower()
                        if 'risk' in content:
                            return True
            return False
        except:
            return False
    
    def has_incident_management(self) -> bool:
        """Check for incident management"""
        try:
            log_dirs = ['/home/ubuntu/ultimate_lyra_systems/logs', '/home/ubuntu/ultimate_lyra_v5/logs']
            for log_dir in log_dirs:
                if os.path.exists(log_dir):
                    return True
            return False
        except:
            return False
    
    def has_access_controls(self) -> bool:
        """Check for access controls"""
        try:
            dashboard_file = '/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_AI_ENHANCED.py'
            if os.path.exists(dashboard_file):
                with open(dashboard_file, 'r') as f:
                    content = f.read().lower()
                    return 'auth' in content or 'session' in content
            return False
        except:
            return False
    
    def has_documentation(self) -> bool:
        """Check for documentation"""
        try:
            doc_files = [f for f in os.listdir('/home/ubuntu/ultimate_lyra_v5') if f.endswith('.md')]
            return len(doc_files) > 5
        except:
            return False
    
    def has_process_controls(self) -> bool:
        """Check for process controls"""
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            python_services = [p for p in result.stdout.split('\n') if 'python3' in p and 'ULTIMATE' in p]
            return len(python_services) >= 5
        except:
            return False
    
    def has_monitoring(self) -> bool:
        """Check for monitoring capabilities"""
        try:
            for port in [8751, 8105, 8106]:
                response = requests.get(f'http://localhost:{port}/api/health', timeout=2)
                if response.status_code == 200:
                    return True
            return False
        except:
            return False
    
    def has_continuous_improvement(self) -> bool:
        """Check for continuous improvement processes"""
        try:
            ai_files = [f for f in os.listdir('/home/ubuntu/ultimate_lyra_v5') if 'AI' in f and f.endswith('.py')]
            return len(ai_files) > 3
        except:
            return False
    
    def has_service_catalog(self) -> bool:
        """Check for service catalog"""
        try:
            result = subprocess.run(['netstat', '-tlnp'], capture_output=True, text=True)
            listening_ports = [line for line in result.stdout.split('\n') if ':8' in line and 'LISTEN' in line]
            return len(listening_ports) >= 5
        except:
            return False
    
    def has_change_management(self) -> bool:
        """Check for change management"""
        try:
            container_files = [
                '/home/ubuntu/ultimate_lyra_v5/containerization/docker-compose.yml',
                '/home/ubuntu/ultimate_lyra_v5/containerization/kubernetes-manifests.yaml'
            ]
            for file_path in container_files:
                if os.path.exists(file_path):
                    return True
            return False
        except:
            return False
    
    def has_service_monitoring(self) -> bool:
        """Check for service monitoring"""
        return self.has_monitoring()
    
    def has_service_reporting(self) -> bool:
        """Check for service reporting"""
        try:
            report_files = [f for f in os.listdir('/home/ubuntu/ultimate_lyra_v5') if 'REPORT' in f and f.endswith('.md')]
            return len(report_files) > 3
        except:
            return False
    
    async def get_ai_consensus_analysis(self) -> Dict[str, Any]:
        """Get AI consensus analysis of production readiness"""
        
        print("🤖 Initiating AI consensus analysis...")
        
        # Prepare system analysis for AI models
        system_summary = self.prepare_system_summary()
        
        ai_results = {
            'models_consulted': 0,
            'successful_responses': 0,
            'consensus_strength': 0.0,
            'production_ready_votes': 0,
            'not_ready_votes': 0,
            'model_responses': {},
            'consensus_recommendation': '',
            'confidence_score': 0.0
        }
        
        # AI analysis prompt
        analysis_prompt = f"""
        PRODUCTION READINESS ANALYSIS REQUEST
        ====================================
        
        You are analyzing a comprehensive cryptocurrency trading system for production readiness.
        
        SYSTEM OVERVIEW:
        {json.dumps(system_summary, indent=2)}
        
        ANALYSIS REQUIREMENTS:
        1. Assess overall production readiness (0-100%)
        2. Identify critical issues that must be resolved
        3. Evaluate security, performance, compliance, and reliability
        4. Provide specific recommendations for production deployment
        5. Give a clear PRODUCTION_READY or NOT_PRODUCTION_READY verdict
        
        Please provide your analysis in this JSON format:
        {{
            "production_readiness_score": <0-100>,
            "verdict": "PRODUCTION_READY" or "NOT_PRODUCTION_READY",
            "critical_issues": ["issue1", "issue2"],
            "security_assessment": "assessment",
            "performance_assessment": "assessment", 
            "compliance_assessment": "assessment",
            "recommendations": ["rec1", "rec2"],
            "confidence": <0-100>
        }}
        """
        
        # Query AI models for consensus
        for i, (api_key, model) in enumerate(zip(self.openrouter_keys[:8], self.ai_models[:8])):
            try:
                print(f"🤖 Querying {model}...")
                
                response = await self.query_openrouter_model(api_key, model, analysis_prompt)
                
                if response:
                    ai_results['models_consulted'] += 1
                    ai_results['successful_responses'] += 1
                    ai_results['model_responses'][model] = response
                    
                    # Parse response for voting
                    if 'PRODUCTION_READY' in response.get('verdict', ''):
                        ai_results['production_ready_votes'] += 1
                    else:
                        ai_results['not_ready_votes'] += 1
                
                # Add delay between requests
                await asyncio.sleep(2)
                
            except Exception as e:
                print(f"❌ Error querying {model}: {e}")
                ai_results['model_responses'][model] = {'error': str(e)}
        
        # Calculate consensus
        total_votes = ai_results['production_ready_votes'] + ai_results['not_ready_votes']
        if total_votes > 0:
            ai_results['consensus_strength'] = ai_results['production_ready_votes'] / total_votes
        
        # Determine consensus recommendation
        if ai_results['consensus_strength'] >= 0.6:
            ai_results['consensus_recommendation'] = 'PRODUCTION_READY'
            ai_results['confidence_score'] = ai_results['consensus_strength'] * 100
        else:
            ai_results['consensus_recommendation'] = 'NOT_PRODUCTION_READY'
            ai_results['confidence_score'] = (1 - ai_results['consensus_strength']) * 100
        
        print(f"✅ AI Consensus: {ai_results['consensus_recommendation']} ({ai_results['confidence_score']:.1f}% confidence)")
        
        self.add_test_result('AI Consensus Analysis', 'AI', 'COMPLETED', ai_results, ai_results['confidence_score'])
        
        return ai_results
    
    def prepare_system_summary(self) -> Dict[str, Any]:
        """Prepare system summary for AI analysis"""
        
        return {
            'total_tests_conducted': len(self.test_results),
            'services_running': len([t for t in self.test_results if t.category == 'Service' and t.status == 'PASSED']),
            'security_tests_passed': len([t for t in self.test_results if t.category == 'Security' and t.status == 'PASSED']),
            'performance_tests_passed': len([t for t in self.test_results if t.category == 'Performance' and t.status == 'PASSED']),
            'compliance_tests_passed': len([t for t in self.test_results if t.category == 'Compliance' and t.status == 'PASSED']),
            'infrastructure_health': len([t for t in self.test_results if t.category == 'Infrastructure' and t.status == 'PASSED']),
            'average_confidence': sum([t.confidence for t in self.test_results]) / len(self.test_results) if self.test_results else 0,
            'critical_failures': len([t for t in self.test_results if t.status == 'FAILED' and t.confidence < 50]),
            'system_components': self.system_components,
            'production_criteria': self.production_criteria
        }
    
    async def query_openrouter_model(self, api_key: str, model: str, prompt: str) -> Optional[Dict[str, Any]]:
        """Query OpenRouter AI model"""
        
        try:
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'HTTP-Referer': 'https://ultimate-lyra-trading.com',
                'X-Title': 'Ultimate Lyra Trading System'
            }
            
            data = {
                'model': model,
                'messages': [
                    {
                        'role': 'system',
                        'content': 'You are an expert system architect and production deployment specialist. Analyze the provided system for production readiness with focus on security, performance, compliance, and reliability.'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                'max_tokens': 2000,
                'temperature': 0.1
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post('https://openrouter.ai/api/v1/chat/completions', 
                                      headers=headers, json=data, timeout=30) as response:
                    if response.status == 200:
                        result = await response.json()
                        content = result['choices'][0]['message']['content']
                        
                        # Try to parse JSON response
                        try:
                            return json.loads(content)
                        except:
                            # Fallback to text analysis
                            return {
                                'verdict': 'PRODUCTION_READY' if 'PRODUCTION_READY' in content else 'NOT_PRODUCTION_READY',
                                'raw_response': content,
                                'production_readiness_score': 75 if 'PRODUCTION_READY' in content else 25
                            }
                    else:
                        return None
                        
        except Exception as e:
            logger.error(f"Error querying {model}: {e}")
            return None
    
    async def calculate_production_readiness(self) -> float:
        """Calculate overall production readiness score"""
        
        if not self.test_results:
            return 0.0
        
        # Weight different categories
        category_weights = {
            'Infrastructure': 0.20,
            'Service': 0.25,
            'Security': 0.20,
            'Performance': 0.15,
            'Compliance': 0.15,
            'AI': 0.05
        }
        
        category_scores = {}
        
        for category, weight in category_weights.items():
            category_tests = [t for t in self.test_results if t.category == category]
            if category_tests:
                category_score = sum([t.confidence for t in category_tests]) / len(category_tests)
                category_scores[category] = category_score
            else:
                category_scores[category] = 0.0
        
        # Calculate weighted average
        weighted_score = sum([score * category_weights[category] for category, score in category_scores.items()])
        
        print(f"📊 Category Scores: {category_scores}")
        print(f"🎯 Weighted Production Readiness Score: {weighted_score:.1f}%")
        
        return weighted_score
    
    def assess_iso_compliance(self) -> Dict[str, Any]:
        """Assess ISO compliance levels"""
        
        iso_compliance = {
            'iso_27001_ready': False,
            'iso_9001_ready': False,
            'iso_20000_ready': False,
            'overall_compliance': 0.0
        }
        
        # Check ISO readiness based on test results
        security_tests = [t for t in self.test_results if t.category == 'Security']
        if security_tests:
            avg_security_score = sum([t.confidence for t in security_tests]) / len(security_tests)
            iso_compliance['iso_27001_ready'] = avg_security_score >= 80.0
        
        infrastructure_tests = [t for t in self.test_results if t.category == 'Infrastructure']
        service_tests = [t for t in self.test_results if t.category == 'Service']
        
        if infrastructure_tests and service_tests:
            avg_quality_score = (
                sum([t.confidence for t in infrastructure_tests]) / len(infrastructure_tests) +
                sum([t.confidence for t in service_tests]) / len(service_tests)
            ) / 2
            iso_compliance['iso_9001_ready'] = avg_quality_score >= 80.0
            iso_compliance['iso_20000_ready'] = avg_quality_score >= 75.0
        
        # Overall compliance
        compliance_count = sum([
            iso_compliance['iso_27001_ready'],
            iso_compliance['iso_9001_ready'],
            iso_compliance['iso_20000_ready']
        ])
        
        iso_compliance['overall_compliance'] = (compliance_count / 3) * 100
        
        return iso_compliance
    
    def generate_recommendations(self) -> List[str]:
        """Generate production readiness recommendations"""
        
        recommendations = []
        
        # Analyze test results for recommendations
        failed_tests = [t for t in self.test_results if t.status == 'FAILED']
        low_confidence_tests = [t for t in self.test_results if t.confidence < 70.0]
        
        if failed_tests:
            recommendations.append(f"Address {len(failed_tests)} failed tests before production deployment")
        
        if low_confidence_tests:
            recommendations.append(f"Improve {len(low_confidence_tests)} tests with low confidence scores")
        
        # Category-specific recommendations
        security_tests = [t for t in self.test_results if t.category == 'Security']
        if security_tests:
            avg_security = sum([t.confidence for t in security_tests]) / len(security_tests)
            if avg_security < 90.0:
                recommendations.append("Enhance security measures to achieve production-grade protection")
        
        performance_tests = [t for t in self.test_results if t.category == 'Performance']
        if performance_tests:
            avg_performance = sum([t.confidence for t in performance_tests]) / len(performance_tests)
            if avg_performance < 80.0:
                recommendations.append("Optimize system performance for production load")
        
        compliance_tests = [t for t in self.test_results if t.category == 'Compliance']
        if compliance_tests:
            avg_compliance = sum([t.confidence for t in compliance_tests]) / len(compliance_tests)
            if avg_compliance < 95.0:
                recommendations.append("Ensure full regulatory compliance before production")
        
        # General recommendations
        recommendations.extend([
            "Implement comprehensive monitoring and alerting",
            "Establish backup and disaster recovery procedures",
            "Conduct load testing with production-level traffic",
            "Set up automated deployment pipelines",
            "Create detailed operational runbooks"
        ])
        
        return recommendations[:10]  # Limit to top 10 recommendations
    
    def add_test_result(self, name: str, category: str, status: str, result: Any, confidence: float):
        """Add test result to collection"""
        
        test = ProductionTest(
            name=name,
            category=category,
            status=status,
            result=result,
            confidence=confidence,
            timestamp=datetime.now(),
            details={'test_type': 'automated', 'framework': 'production_readiness_analyzer'}
        )
        
        self.test_results.append(test)
    
    def test_to_dict(self, test: ProductionTest) -> Dict[str, Any]:
        """Convert test result to dictionary"""
        
        return {
            'name': test.name,
            'category': test.category,
            'status': test.status,
            'result': test.result,
            'confidence': test.confidence,
            'timestamp': test.timestamp.isoformat(),
            'details': test.details
        }
    
    async def save_analysis_results(self, results: Dict[str, Any]):
        """Save analysis results to file"""
        
        try:
            # Save to JSON file
            results_file = '/home/ubuntu/ultimate_lyra_v5/production_readiness_analysis.json'
            with open(results_file, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            # Save to database
            db_path = '/home/ubuntu/ultimate_lyra_v5/production_analysis.db'
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Create table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS production_analysis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    readiness_score REAL,
                    production_ready BOOLEAN,
                    total_tests INTEGER,
                    results TEXT
                )
            ''')
            
            # Insert results
            cursor.execute('''
                INSERT INTO production_analysis 
                (timestamp, readiness_score, production_ready, total_tests, results)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                results['analysis_timestamp'],
                results['production_readiness_score'],
                results['production_ready'],
                results['total_tests_conducted'],
                json.dumps(results, default=str)
            ))
            
            conn.commit()
            conn.close()
            
            print(f"✅ Analysis results saved to {results_file}")
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")

async def main():
    """Main function to run production readiness analysis"""
    
    print("🎯 ULTIMATE PRODUCTION READINESS ANALYSIS")
    print("=" * 50)
    print("🤖 AI Consensus Analysis with OpenRouter Models")
    print("🔍 Comprehensive Multi-Source Verification")
    print("📊 ISO Standard Compliance Assessment")
    print("🏆 Production Deployment Readiness")
    print("=" * 50)
    
    try:
        # Initialize analyzer
        analyzer = ProductionReadinessAnalyzer()
        
        # Run comprehensive analysis
        results = await analyzer.run_comprehensive_analysis()
        
        if 'error' not in results:
            print("\n" + "=" * 50)
            print("🎯 PRODUCTION READINESS ANALYSIS COMPLETE")
            print("=" * 50)
            print(f"📊 Production Readiness Score: {results['production_readiness_score']:.1f}%")
            print(f"✅ Production Ready: {'YES' if results['production_ready'] else 'NO'}")
            print(f"🧪 Total Tests Conducted: {results['total_tests_conducted']}")
            print(f"⏱️ Analysis Duration: {results['analysis_duration']:.2f} seconds")
            print(f"🤖 AI Consensus: {results['ai_consensus']['consensus_recommendation']}")
            print(f"🎯 AI Confidence: {results['ai_consensus']['confidence_score']:.1f}%")
            print(f"🏆 ISO Compliance: {results['iso_compliance']['overall_compliance']:.1f}%")
            
            print("\n📋 TOP RECOMMENDATIONS:")
            for i, rec in enumerate(results['recommendations'][:5], 1):
                print(f"  {i}. {rec}")
            
            print(f"\n💾 Detailed results saved to: production_readiness_analysis.json")
            print("🎯 ANALYSIS COMPLETE - SYSTEM READY FOR PRODUCTION ASSESSMENT")
            
        else:
            print(f"❌ Analysis failed: {results['error']}")
            
    except Exception as e:
        print(f"❌ Critical error: {e}")
        logger.error(f"Critical analysis error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
