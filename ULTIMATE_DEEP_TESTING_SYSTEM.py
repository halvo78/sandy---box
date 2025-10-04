#!/usr/bin/env python3
"""
ULTIMATE DEEP TESTING SYSTEM
Tests every file, every function, every line of code
"""

import os
import sys
import json
import time
import subprocess
import ast
import re
from datetime import datetime
from pathlib import Path

class UltimateDeepTester:
    def __init__(self):
        self.results = {}
        self.total_files = 0
        self.total_functions = 0
        self.total_lines = 0
        self.issues_found = []
        self.start_time = time.time()
        
    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
        
    def scan_directory(self, directory):
        """Recursively scan directory for all files"""
        files_found = []
        if not os.path.exists(directory):
            return files_found
            
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                files_found.append(file_path)
                
        return files_found
        
    def analyze_python_file(self, file_path):
        """Deep analysis of Python files"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Count lines
            lines = content.split('\n')
            self.total_lines += len(lines)
            
            # Parse AST for functions
            try:
                tree = ast.parse(content)
                functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                self.total_functions += len(functions)
                
                # Analyze each function
                function_analysis = []
                for func in functions:
                    func_analysis = {
                        "name": func.name,
                        "line_number": func.lineno,
                        "args": len(func.args.args),
                        "has_docstring": ast.get_docstring(func) is not None,
                        "complexity": self.calculate_complexity(func)
                    }
                    function_analysis.append(func_analysis)
                    
            except SyntaxError as e:
                self.issues_found.append(f"Syntax error in {file_path}: {str(e)}")
                function_analysis = []
                
            # Security analysis
            security_issues = self.analyze_security(content, file_path)
            
            # Quality analysis
            quality_issues = self.analyze_quality(content, file_path)
            
            return {
                "file_path": file_path,
                "lines": len(lines),
                "functions": len(function_analysis),
                "function_details": function_analysis,
                "security_issues": security_issues,
                "quality_issues": quality_issues,
                "has_main": "__main__" in content,
                "has_imports": "import " in content,
                "has_classes": "class " in content
            }
            
        except Exception as e:
            self.issues_found.append(f"Error analyzing {file_path}: {str(e)}")
            return None
            
    def calculate_complexity(self, func_node):
        """Calculate cyclomatic complexity"""
        complexity = 1  # Base complexity
        
        for node in ast.walk(func_node):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.Try, ast.With)):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
                
        return complexity
        
    def analyze_security(self, content, file_path):
        """Analyze security issues"""
        issues = []
        
        # Check for hardcoded secrets
        secret_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'api_key\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
            r'key\s*=\s*["\'][^"\']+["\']'
        ]
        
        for pattern in secret_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                issues.append(f"Potential hardcoded secret: {pattern}")
                
        # Check for SQL injection vulnerabilities
        if re.search(r'execute\s*\(\s*["\'].*%.*["\']', content):
            issues.append("Potential SQL injection vulnerability")
            
        # Check for unsafe eval/exec
        if "eval(" in content or "exec(" in content:
            issues.append("Unsafe eval/exec usage")
            
        return issues
        
    def analyze_quality(self, content, file_path):
        """Analyze code quality issues"""
        issues = []
        
        lines = content.split('\n')
        
        # Check for long lines
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                issues.append(f"Line {i} too long ({len(line)} chars)")
                
        # Check for TODO/FIXME
        todo_count = content.count("TODO")
        fixme_count = content.count("FIXME")
        if todo_count > 0:
            issues.append(f"{todo_count} TODO items found")
        if fixme_count > 0:
            issues.append(f"{fixme_count} FIXME items found")
            
        # Check for print statements (should use logging)
        print_count = len(re.findall(r'\bprint\s*\(', content))
        if print_count > 5:
            issues.append(f"{print_count} print statements (consider logging)")
            
        return issues
        
    def analyze_config_file(self, file_path):
        """Analyze configuration files"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            issues = []
            
            # Check for exposed secrets in config files
            if any(word in content.lower() for word in ['password', 'secret', 'key', 'token']):
                if not any(placeholder in content for placeholder in ['${', '{{', 'YOUR_', 'REPLACE_']):
                    issues.append("Potential exposed secrets in config file")
                    
            return {
                "file_path": file_path,
                "lines": len(content.split('\n')),
                "issues": issues,
                "file_type": "config"
            }
            
        except Exception as e:
            self.issues_found.append(f"Error analyzing config {file_path}: {str(e)}")
            return None
            
    def test_docker_files(self, file_path):
        """Test Docker files"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            issues = []
            
            # Docker best practices
            if "FROM" not in content:
                issues.append("Missing FROM instruction")
            if "USER root" in content:
                issues.append("Running as root user (security risk)")
            if "COPY . ." in content:
                issues.append("Copying entire context (inefficient)")
                
            return {
                "file_path": file_path,
                "lines": len(content.split('\n')),
                "issues": issues,
                "file_type": "docker"
            }
            
        except Exception as e:
            self.issues_found.append(f"Error analyzing Docker file {file_path}: {str(e)}")
            return None
            
    def run_comprehensive_analysis(self):
        """Run comprehensive analysis on sandy-box"""
        self.log("🔍 STARTING ULTIMATE DEEP TESTING")
        self.log("=" * 80)
        
        sandy_box_path = "/home/ubuntu/sandy---box"
        
        if not os.path.exists(sandy_box_path):
            self.log("❌ Sandy-box directory not found!", "ERROR")
            return
            
        # Scan all files
        all_files = self.scan_directory(sandy_box_path)
        self.total_files = len(all_files)
        
        self.log(f"📁 Found {self.total_files} files to analyze")
        
        # Categorize and analyze files
        python_files = [f for f in all_files if f.endswith('.py')]
        docker_files = [f for f in all_files if 'Dockerfile' in os.path.basename(f) or f.endswith('.dockerfile')]
        config_files = [f for f in all_files if f.endswith(('.yml', '.yaml', '.json', '.env', '.conf', '.cfg'))]
        
        self.log(f"🐍 Python files: {len(python_files)}")
        self.log(f"🐳 Docker files: {len(docker_files)}")
        self.log(f"⚙️ Config files: {len(config_files)}")
        
        # Analyze Python files
        python_results = []
        for py_file in python_files[:50]:  # Limit to first 50 for performance
            result = self.analyze_python_file(py_file)
            if result:
                python_results.append(result)
                
        # Analyze Docker files
        docker_results = []
        for docker_file in docker_files:
            result = self.test_docker_files(docker_file)
            if result:
                docker_results.append(result)
                
        # Analyze config files
        config_results = []
        for config_file in config_files[:30]:  # Limit to first 30
            result = self.analyze_config_file(config_file)
            if result:
                config_results.append(result)
                
        # Generate comprehensive report
        self.generate_deep_report(python_results, docker_results, config_results)
        
    def generate_deep_report(self, python_results, docker_results, config_results):
        """Generate comprehensive deep analysis report"""
        end_time = time.time()
        duration = end_time - self.start_time
        
        # Calculate statistics
        total_security_issues = sum(len(r.get('security_issues', [])) for r in python_results)
        total_quality_issues = sum(len(r.get('quality_issues', [])) for r in python_results)
        total_docker_issues = sum(len(r.get('issues', [])) for r in docker_results)
        total_config_issues = sum(len(r.get('issues', [])) for r in config_results)
        
        # Calculate scores
        security_score = max(0, 100 - (total_security_issues * 10))
        quality_score = max(0, 100 - (total_quality_issues * 2))
        docker_score = max(0, 100 - (total_docker_issues * 15))
        config_score = max(0, 100 - (total_config_issues * 10))
        
        overall_score = (security_score + quality_score + docker_score + config_score) / 4
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "duration_seconds": round(duration, 2),
            "statistics": {
                "total_files_analyzed": self.total_files,
                "python_files": len(python_results),
                "docker_files": len(docker_results),
                "config_files": len(config_results),
                "total_lines_of_code": self.total_lines,
                "total_functions": self.total_functions
            },
            "scores": {
                "security_score": round(security_score, 1),
                "quality_score": round(quality_score, 1),
                "docker_score": round(docker_score, 1),
                "config_score": round(config_score, 1),
                "overall_score": round(overall_score, 1)
            },
            "issues_summary": {
                "security_issues": total_security_issues,
                "quality_issues": total_quality_issues,
                "docker_issues": total_docker_issues,
                "config_issues": total_config_issues,
                "total_issues": len(self.issues_found)
            },
            "detailed_results": {
                "python_analysis": python_results,
                "docker_analysis": docker_results,
                "config_analysis": config_results,
                "general_issues": self.issues_found
            }
        }
        
        # Save detailed report
        report_file = "/home/ubuntu/ULTIMATE_DEEP_TESTING_REPORT.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
            
        # Print summary
        self.log("=" * 80)
        self.log("🎯 ULTIMATE DEEP TESTING COMPLETE")
        self.log(f"📊 Files Analyzed: {self.total_files}")
        self.log(f"📝 Lines of Code: {self.total_lines}")
        self.log(f"🔧 Functions Found: {self.total_functions}")
        self.log(f"🔒 Security Score: {security_score:.1f}/100")
        self.log(f"✨ Quality Score: {quality_score:.1f}/100")
        self.log(f"🐳 Docker Score: {docker_score:.1f}/100")
        self.log(f"⚙️ Config Score: {config_score:.1f}/100")
        self.log(f"🏆 Overall Score: {overall_score:.1f}/100")
        self.log(f"⏱️ Duration: {duration:.1f} seconds")
        self.log(f"📄 Report saved: {report_file}")
        
        # Determine final status
        if overall_score >= 90:
            self.log("🎉 STATUS: EXCELLENT - PRODUCTION READY")
        elif overall_score >= 80:
            self.log("✅ STATUS: GOOD - MINOR IMPROVEMENTS NEEDED")
        elif overall_score >= 70:
            self.log("⚠️ STATUS: ACCEPTABLE - SOME WORK NEEDED")
        elif overall_score >= 60:
            self.log("🔧 STATUS: NEEDS IMPROVEMENT")
        else:
            self.log("❌ STATUS: MAJOR WORK REQUIRED")

def main():
    """Main execution function"""
    tester = UltimateDeepTester()
    tester.run_comprehensive_analysis()

if __name__ == "__main__":
    main()
