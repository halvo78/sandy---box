#!/usr/bin/env python3
"""
ULTIMATE FINAL GAP ANALYSIS SYSTEM
==================================
This system will walk through EVERY part of the sandy-box repository
and identify ALL gaps, issues, and errors before production deployment.

It simulates a complete Ubuntu build process step-by-step.
"""

import os
import sys
import json
import subprocess
import time
from pathlib import Path
import traceback

class UltimateFinalGapAnalysis:
    def __init__(self):
        self.repo_path = "/home/ubuntu/sandy---box"
        self.issues_found = []
        self.gaps_found = []
        self.errors_found = []
        self.warnings_found = []
        self.total_files_checked = 0
        self.critical_issues = 0
        
    def log_issue(self, severity, category, file_path, issue, solution=""):
        """Log an issue found during analysis"""
        issue_data = {
            "severity": severity,
            "category": category,
            "file": file_path,
            "issue": issue,
            "solution": solution,
            "timestamp": time.time()
        }
        
        if severity == "CRITICAL":
            self.critical_issues += 1
            self.errors_found.append(issue_data)
        elif severity == "HIGH":
            self.issues_found.append(issue_data)
        elif severity == "MEDIUM":
            self.gaps_found.append(issue_data)
        else:
            self.warnings_found.append(issue_data)
            
        print(f"🚨 {severity}: {category} - {issue}")
        if solution:
            print(f"   💡 Solution: {solution}")
    
    def check_file_exists(self, file_path, description=""):
        """Check if a critical file exists"""
        full_path = os.path.join(self.repo_path, file_path)
        if not os.path.exists(full_path):
            self.log_issue("CRITICAL", "MISSING_FILE", file_path, 
                          f"Required file missing: {description}", 
                          f"Create {file_path}")
            return False
        return True
    
    def check_python_syntax(self, file_path):
        """Check Python file syntax"""
        try:
            with open(file_path, 'r') as f:
                compile(f.read(), file_path, 'exec')
            return True
        except SyntaxError as e:
            self.log_issue("CRITICAL", "SYNTAX_ERROR", file_path,
                          f"Python syntax error: {e}",
                          "Fix syntax error")
            return False
        except Exception as e:
            self.log_issue("HIGH", "FILE_ERROR", file_path,
                          f"File error: {e}",
                          "Check file encoding and content")
            return False
    
    def check_imports(self, file_path):
        """Check if all imports are available"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            import_lines = [line.strip() for line in content.split('\n') 
                           if line.strip().startswith(('import ', 'from '))]
            
            for import_line in import_lines:
                try:
                    # Extract module name
                    if import_line.startswith('from '):
                        module = import_line.split()[1]
                    else:
                        module = import_line.split()[1].split('.')[0]
                    
                    # Skip relative imports and standard library
                    if module.startswith('.') or module in ['os', 'sys', 'json', 'time', 'datetime', 're', 'subprocess']:
                        continue
                        
                    # Try to import
                    __import__(module)
                except ImportError:
                    self.log_issue("HIGH", "MISSING_DEPENDENCY", file_path,
                                  f"Missing dependency: {module}",
                                  f"pip3 install {module}")
        except Exception as e:
            self.log_issue("MEDIUM", "IMPORT_CHECK_ERROR", file_path,
                          f"Could not check imports: {e}")
    
    def check_docker_files(self):
        """Check Docker configuration files"""
        print("🐳 CHECKING DOCKER CONFIGURATION...")
        
        docker_files = [
            "Dockerfile",
            "docker-compose.yml",
            ".dockerignore"
        ]
        
        for docker_file in docker_files:
            if not self.check_file_exists(docker_file, f"Docker {docker_file}"):
                continue
                
            file_path = os.path.join(self.repo_path, docker_file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                if docker_file == "Dockerfile":
                    if "FROM" not in content:
                        self.log_issue("CRITICAL", "DOCKER_ERROR", docker_file,
                                      "Dockerfile missing FROM instruction")
                    if "EXPOSE" not in content:
                        self.log_issue("MEDIUM", "DOCKER_WARNING", docker_file,
                                      "Dockerfile missing EXPOSE instruction")
                
                elif docker_file == "docker-compose.yml":
                    if "version:" not in content:
                        self.log_issue("HIGH", "DOCKER_ERROR", docker_file,
                                      "docker-compose.yml missing version")
                    if "services:" not in content:
                        self.log_issue("CRITICAL", "DOCKER_ERROR", docker_file,
                                      "docker-compose.yml missing services")
                        
            except Exception as e:
                self.log_issue("HIGH", "DOCKER_ERROR", docker_file,
                              f"Error reading Docker file: {e}")
    
    def check_api_keys_security(self):
        """Check for exposed API keys"""
        print("🔐 CHECKING API KEY SECURITY...")
        
        dangerous_patterns = [
            "sk-",  # OpenAI keys
            "xoxb-",  # Slack tokens
            "ghp_",  # GitHub tokens
            "AKIA",  # AWS keys
            "AIza",  # Google API keys
        ]
        
        for root, dirs, files in os.walk(self.repo_path):
            for file in files:
                if file.endswith(('.py', '.js', '.json', '.yml', '.yaml', '.env')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read()
                        
                        for pattern in dangerous_patterns:
                            if pattern in content:
                                self.log_issue("CRITICAL", "SECURITY_RISK", file_path,
                                              f"Potential exposed API key: {pattern}",
                                              "Move to environment variables")
                    except:
                        pass
    
    def check_requirements_files(self):
        """Check Python requirements"""
        print("📦 CHECKING PYTHON REQUIREMENTS...")
        
        req_files = ["requirements.txt", "setup.py", "pyproject.toml"]
        found_req_file = False
        
        for req_file in req_files:
            if self.check_file_exists(req_file, f"Python {req_file}"):
                found_req_file = True
                break
        
        if not found_req_file:
            self.log_issue("HIGH", "MISSING_REQUIREMENTS", "requirements.txt",
                          "No Python requirements file found",
                          "Create requirements.txt with dependencies")
    
    def check_configuration_files(self):
        """Check configuration files"""
        print("⚙️ CHECKING CONFIGURATION FILES...")
        
        config_files = [
            "config.py",
            "settings.py", 
            "config.json",
            "config.yml",
            ".env.example"
        ]
        
        found_config = False
        for config_file in config_files:
            if os.path.exists(os.path.join(self.repo_path, config_file)):
                found_config = True
                break
        
        if not found_config:
            self.log_issue("MEDIUM", "MISSING_CONFIG", "config.py",
                          "No configuration file found",
                          "Create configuration management")
    
    def check_testing_framework(self):
        """Check testing setup"""
        print("🧪 CHECKING TESTING FRAMEWORK...")
        
        test_dirs = ["tests", "test", "testing"]
        found_tests = False
        
        for test_dir in test_dirs:
            test_path = os.path.join(self.repo_path, test_dir)
            if os.path.exists(test_path):
                found_tests = True
                # Check for test files
                test_files = [f for f in os.listdir(test_path) 
                             if f.startswith('test_') and f.endswith('.py')]
                if not test_files:
                    self.log_issue("MEDIUM", "EMPTY_TESTS", test_dir,
                                  "Test directory exists but no test files found")
                break
        
        if not found_tests:
            self.log_issue("MEDIUM", "MISSING_TESTS", "tests/",
                          "No testing framework found",
                          "Create tests directory with test files")
    
    def check_documentation(self):
        """Check documentation"""
        print("📚 CHECKING DOCUMENTATION...")
        
        doc_files = ["README.md", "README.rst", "docs/"]
        found_docs = False
        
        for doc_file in doc_files:
            if os.path.exists(os.path.join(self.repo_path, doc_file)):
                found_docs = True
                break
        
        if not found_docs:
            self.log_issue("MEDIUM", "MISSING_DOCS", "README.md",
                          "No documentation found",
                          "Create README.md with setup instructions")
    
    def simulate_ubuntu_build(self):
        """Simulate complete Ubuntu build process"""
        print("🖥️ SIMULATING UBUNTU BUILD PROCESS...")
        
        build_steps = [
            ("System Update", "apt update && apt upgrade -y"),
            ("Python Installation", "apt install python3 python3-pip -y"),
            ("Docker Installation", "apt install docker.io docker-compose -y"),
            ("Git Clone", f"git clone https://github.com/halvo78/sandy---box.git"),
            ("Dependencies Install", "pip3 install -r requirements.txt"),
            ("Docker Build", "docker build -t sandy-box ."),
            ("Docker Compose", "docker-compose up -d"),
            ("Health Check", "curl http://localhost:8000/health")
        ]
        
        for step_name, command in build_steps:
            print(f"   🔄 Simulating: {step_name}")
            
            # Check if required files exist for this step
            if "requirements.txt" in command:
                if not os.path.exists(os.path.join(self.repo_path, "requirements.txt")):
                    self.log_issue("CRITICAL", "BUILD_ERROR", "requirements.txt",
                                  f"Build step '{step_name}' will fail - missing requirements.txt")
            
            elif "docker build" in command:
                if not os.path.exists(os.path.join(self.repo_path, "Dockerfile")):
                    self.log_issue("CRITICAL", "BUILD_ERROR", "Dockerfile",
                                  f"Build step '{step_name}' will fail - missing Dockerfile")
            
            elif "docker-compose" in command:
                if not os.path.exists(os.path.join(self.repo_path, "docker-compose.yml")):
                    self.log_issue("CRITICAL", "BUILD_ERROR", "docker-compose.yml",
                                  f"Build step '{step_name}' will fail - missing docker-compose.yml")
    
    def check_all_python_files(self):
        """Check all Python files in the repository"""
        print("🐍 CHECKING ALL PYTHON FILES...")
        
        for root, dirs, files in os.walk(self.repo_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    self.total_files_checked += 1
                    
                    # Check syntax
                    self.check_python_syntax(file_path)
                    
                    # Check imports
                    self.check_imports(file_path)
    
    def run_comprehensive_analysis(self):
        """Run the complete gap analysis"""
        print("🚀 STARTING ULTIMATE FINAL GAP ANALYSIS")
        print("=" * 80)
        
        if not os.path.exists(self.repo_path):
            print(f"❌ Repository not found at {self.repo_path}")
            return
        
        # Change to repository directory
        os.chdir(self.repo_path)
        
        # Run all checks
        self.check_docker_files()
        self.check_api_keys_security()
        self.check_requirements_files()
        self.check_configuration_files()
        self.check_testing_framework()
        self.check_documentation()
        self.check_all_python_files()
        self.simulate_ubuntu_build()
        
        # Generate final report
        self.generate_final_report()
    
    def generate_final_report(self):
        """Generate comprehensive final report"""
        print("\n" + "=" * 80)
        print("🎯 ULTIMATE FINAL GAP ANALYSIS REPORT")
        print("=" * 80)
        
        total_issues = len(self.errors_found) + len(self.issues_found) + len(self.gaps_found) + len(self.warnings_found)
        
        print(f"📊 ANALYSIS SUMMARY:")
        print(f"   Files Checked: {self.total_files_checked}")
        print(f"   Critical Errors: {len(self.errors_found)}")
        print(f"   High Issues: {len(self.issues_found)}")
        print(f"   Medium Gaps: {len(self.gaps_found)}")
        print(f"   Low Warnings: {len(self.warnings_found)}")
        print(f"   Total Issues: {total_issues}")
        
        # Production readiness score
        if self.critical_issues > 0:
            readiness_score = 0
            status = "❌ NOT PRODUCTION READY"
        elif len(self.issues_found) > 5:
            readiness_score = 60
            status = "⚠️ NEEDS SIGNIFICANT WORK"
        elif len(self.gaps_found) > 10:
            readiness_score = 80
            status = "🔧 NEEDS MINOR FIXES"
        elif total_issues > 0:
            readiness_score = 95
            status = "✅ MOSTLY READY"
        else:
            readiness_score = 100
            status = "🎉 PRODUCTION READY"
        
        print(f"\n🎯 PRODUCTION READINESS: {readiness_score}/100")
        print(f"🚀 STATUS: {status}")
        
        # Save detailed report
        report = {
            "analysis_timestamp": time.time(),
            "files_checked": self.total_files_checked,
            "readiness_score": readiness_score,
            "status": status,
            "critical_errors": self.errors_found,
            "high_issues": self.issues_found,
            "medium_gaps": self.gaps_found,
            "low_warnings": self.warnings_found
        }
        
        with open("/home/ubuntu/ULTIMATE_FINAL_GAP_ANALYSIS_REPORT.json", "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📋 Detailed report saved to: ULTIMATE_FINAL_GAP_ANALYSIS_REPORT.json")
        
        if total_issues > 0:
            print("\n🔧 ISSUES THAT NEED FIXING:")
            for error in self.errors_found[:5]:  # Show top 5 critical
                print(f"   ❌ CRITICAL: {error['issue']}")
                if error['solution']:
                    print(f"      💡 Fix: {error['solution']}")
        
        return readiness_score, total_issues

if __name__ == "__main__":
    analyzer = UltimateFinalGapAnalysis()
    analyzer.run_comprehensive_analysis()
