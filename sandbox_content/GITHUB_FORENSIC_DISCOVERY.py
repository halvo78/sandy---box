"""
GITHUB FORENSIC DISCOVERY - COMPLETE LYRA ECOSYSTEM EXTRACTION
==============================================================
Discovers and catalogs EVERYTHING from the GitHub repositories
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path

class GitHubForensicDiscovery:
    def __init__(self):
        self.github_data = {
            "discovery_timestamp": datetime.now().isoformat(),
            "repositories": {},
            "python_files": {},
            "trading_systems": {},
            "ai_systems": {},
            "security_systems": {},
            "deployment_files": {},
            "configuration_files": {},
            "documentation": {},
            "proof_files": {},
            "demo_files": {},
            "total_files": 0,
            "total_python_files": 0
        }
        
        self.repo_paths = [
            "/home/ubuntu/ultimate-lyra-ecosystem",
            "/home/ubuntu/files-for-build"
        ]
    
    def discover_repository_structure(self):
        """Discover the complete structure of all repositories"""
        print("🔍 Discovering GitHub repository structure...")
        
        for repo_path in self.repo_paths:
            if os.path.exists(repo_path):
                repo_name = os.path.basename(repo_path)
                print(f"📁 Analyzing repository: {repo_name}")
                
                repo_data = {
                    "path": repo_path,
                    "files": {},
                    "directories": [],
                    "python_files": [],
                    "total_files": 0
                }
                
                # Walk through all files
                for root, dirs, files in os.walk(repo_path):
                    # Skip .git directory for file listing
                    if '.git' in root:
                        continue
                    
                    for directory in dirs:
                        if not directory.startswith('.'):
                            repo_data["directories"].append(os.path.join(root, directory))
                    
                    for file in files:
                        if not file.startswith('.'):
                            file_path = os.path.join(root, file)
                            relative_path = os.path.relpath(file_path, repo_path)
                            
                            try:
                                stat = os.stat(file_path)
                                file_info = {
                                    "size": stat.st_size,
                                    "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                                    "type": self.get_file_type(file),
                                    "relative_path": relative_path
                                }
                                
                                repo_data["files"][relative_path] = file_info
                                repo_data["total_files"] += 1
                                self.github_data["total_files"] += 1
                                
                                if file.endswith('.py'):
                                    repo_data["python_files"].append(relative_path)
                                    self.github_data["total_python_files"] += 1
                                    self.analyze_python_file(file_path, relative_path)
                                
                            except Exception as e:
                                print(f"❌ Error analyzing {file_path}: {e}")
                
                self.github_data["repositories"][repo_name] = repo_data
                print(f"✅ {repo_name}: {repo_data['total_files']} files, {len(repo_data['python_files'])} Python files")
    
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
            'env': 'environment',
            'dockerfile': 'docker',
            'requirements': 'dependencies'
        }
        
        return type_map.get(ext, ext)
    
    def analyze_python_file(self, file_path, relative_path):
        """Analyze Python files for functions, classes, and purpose"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            analysis = {
                "path": relative_path,
                "size": len(content),
                "lines": len(content.split('\n')),
                "functions": self.extract_functions(content),
                "classes": self.extract_classes(content),
                "imports": self.extract_imports(content),
                "purpose": self.determine_purpose(relative_path, content),
                "keywords": self.extract_keywords(content)
            }
            
            self.github_data["python_files"][relative_path] = analysis
            
            # Categorize by purpose
            purpose = analysis["purpose"]
            if "trading" in purpose:
                self.github_data["trading_systems"][relative_path] = analysis
            elif "ai" in purpose:
                self.github_data["ai_systems"][relative_path] = analysis
            elif "security" in purpose:
                self.github_data["security_systems"][relative_path] = analysis
            elif "deploy" in purpose:
                self.github_data["deployment_files"][relative_path] = analysis
            elif "proof" in purpose or "demo" in purpose:
                self.github_data["proof_files"][relative_path] = analysis
            
        except Exception as e:
            print(f"❌ Error analyzing Python file {file_path}: {e}")
    
    def extract_functions(self, content):
        """Extract function definitions"""
        functions = []
        lines = content.split('\n')
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('def ') or stripped.startswith('async def '):
                func_name = stripped.split('(')[0].replace('def ', '').replace('async ', '').strip()
                functions.append(func_name)
        return functions
    
    def extract_classes(self, content):
        """Extract class definitions"""
        classes = []
        lines = content.split('\n')
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('class '):
                class_name = stripped.split('(')[0].replace('class ', '').strip(':')
                classes.append(class_name)
        return classes
    
    def extract_imports(self, content):
        """Extract import statements"""
        imports = []
        lines = content.split('\n')
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('import ') or stripped.startswith('from '):
                imports.append(stripped)
        return imports[:10]  # Limit to first 10 imports
    
    def determine_purpose(self, filename, content):
        """Determine the purpose of the file"""
        filename_lower = filename.lower()
        content_lower = content.lower()
        
        purposes = []
        
        # Check filename
        if any(word in filename_lower for word in ['trading', 'trade']):
            purposes.append('trading')
        if any(word in filename_lower for word in ['ai', 'artificial', 'intelligence']):
            purposes.append('ai')
        if any(word in filename_lower for word in ['security', 'secure', 'vault']):
            purposes.append('security')
        if any(word in filename_lower for word in ['deploy', 'install', 'setup']):
            purposes.append('deployment')
        if any(word in filename_lower for word in ['proof', 'demo', 'test']):
            purposes.append('proof')
        if any(word in filename_lower for word in ['config', 'env', 'settings']):
            purposes.append('configuration')
        
        # Check content
        if any(word in content_lower for word in ['buy', 'sell', 'order', 'exchange', 'portfolio']):
            purposes.append('trading')
        if any(word in content_lower for word in ['openai', 'gpt', 'claude', 'ai_model']):
            purposes.append('ai')
        if any(word in content_lower for word in ['encrypt', 'decrypt', 'password', 'secret']):
            purposes.append('security')
        
        return '_'.join(purposes) if purposes else 'utility'
    
    def extract_keywords(self, content):
        """Extract important keywords from content"""
        important_keywords = [
            'trading', 'ai', 'security', 'vault', 'exchange', 'portfolio',
            'buy', 'sell', 'order', 'profit', 'loss', 'risk', 'compliance',
            'openai', 'gpt', 'claude', 'model', 'consensus', 'analysis',
            'encrypt', 'decrypt', 'secure', 'auth', 'token', 'key',
            'deploy', 'docker', 'kubernetes', 'production', 'live',
            'proof', 'demo', 'test', 'verification', 'validation'
        ]
        
        content_lower = content.lower()
        found_keywords = []
        
        for keyword in important_keywords:
            if keyword in content_lower:
                found_keywords.append(keyword)
        
        return found_keywords[:15]  # Limit to top 15 keywords
    
    def discover_configuration_files(self):
        """Discover all configuration files"""
        print("🔍 Discovering configuration files...")
        
        config_extensions = ['.env', '.yml', '.yaml', '.json', '.conf', '.cfg', '.ini']
        
        for repo_path in self.repo_paths:
            if os.path.exists(repo_path):
                for root, dirs, files in os.walk(repo_path):
                    if '.git' in root:
                        continue
                    
                    for file in files:
                        if any(file.endswith(ext) for ext in config_extensions) or 'config' in file.lower():
                            file_path = os.path.join(root, file)
                            relative_path = os.path.relpath(file_path, repo_path)
                            
                            try:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                                
                                self.github_data["configuration_files"][relative_path] = {
                                    "size": len(content),
                                    "type": self.get_file_type(file),
                                    "repo": os.path.basename(repo_path),
                                    "has_secrets": any(word in content.lower() for word in ['password', 'secret', 'key', 'token']),
                                    "lines": len(content.split('\n'))
                                }
                            except:
                                pass
    
    def discover_documentation(self):
        """Discover all documentation files"""
        print("🔍 Discovering documentation...")
        
        doc_extensions = ['.md', '.txt', '.rst', '.doc']
        
        for repo_path in self.repo_paths:
            if os.path.exists(repo_path):
                for root, dirs, files in os.walk(repo_path):
                    if '.git' in root:
                        continue
                    
                    for file in files:
                        if any(file.endswith(ext) for ext in doc_extensions):
                            file_path = os.path.join(root, file)
                            relative_path = os.path.relpath(file_path, repo_path)
                            
                            try:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                                
                                self.github_data["documentation"][relative_path] = {
                                    "size": len(content),
                                    "lines": len(content.split('\n')),
                                    "repo": os.path.basename(repo_path),
                                    "type": self.get_file_type(file),
                                    "keywords": self.extract_keywords(content)
                                }
                            except:
                                pass
    
    def generate_summary_report(self):
        """Generate a comprehensive summary report"""
        summary = f"""# GITHUB FORENSIC DISCOVERY REPORT

**Discovery Date:** {self.github_data['discovery_timestamp']}

## 📊 DISCOVERY SUMMARY

**Total Files:** {self.github_data['total_files']}
**Python Files:** {self.github_data['total_python_files']}
**Trading Systems:** {len(self.github_data['trading_systems'])}
**AI Systems:** {len(self.github_data['ai_systems'])}
**Security Systems:** {len(self.github_data['security_systems'])}
**Deployment Files:** {len(self.github_data['deployment_files'])}
**Configuration Files:** {len(self.github_data['configuration_files'])}
**Documentation Files:** {len(self.github_data['documentation'])}
**Proof/Demo Files:** {len(self.github_data['proof_files'])}

## 🏗️ REPOSITORY STRUCTURE

"""
        
        for repo_name, repo_data in self.github_data['repositories'].items():
            summary += f"### {repo_name}\n"
            summary += f"- **Total Files:** {repo_data['total_files']}\n"
            summary += f"- **Python Files:** {len(repo_data['python_files'])}\n"
            summary += f"- **Directories:** {len(repo_data['directories'])}\n\n"
        
        summary += "## 🎯 KEY TRADING SYSTEMS\n\n"
        for file_path, analysis in list(self.github_data['trading_systems'].items())[:10]:
            summary += f"### {os.path.basename(file_path)}\n"
            summary += f"- **Functions:** {len(analysis['functions'])}\n"
            summary += f"- **Classes:** {len(analysis['classes'])}\n"
            summary += f"- **Keywords:** {', '.join(analysis['keywords'][:5])}\n\n"
        
        summary += "## 🤖 KEY AI SYSTEMS\n\n"
        for file_path, analysis in list(self.github_data['ai_systems'].items())[:10]:
            summary += f"### {os.path.basename(file_path)}\n"
            summary += f"- **Functions:** {len(analysis['functions'])}\n"
            summary += f"- **Classes:** {len(analysis['classes'])}\n"
            summary += f"- **Keywords:** {', '.join(analysis['keywords'][:5])}\n\n"
        
        summary += "## 🔐 KEY SECURITY SYSTEMS\n\n"
        for file_path, analysis in list(self.github_data['security_systems'].items())[:10]:
            summary += f"### {os.path.basename(file_path)}\n"
            summary += f"- **Functions:** {len(analysis['functions'])}\n"
            summary += f"- **Classes:** {len(analysis['classes'])}\n"
            summary += f"- **Keywords:** {', '.join(analysis['keywords'][:5])}\n\n"
        
        return summary
    
    def run_complete_discovery(self):
        """Run complete GitHub forensic discovery"""
        print("🚀 STARTING GITHUB FORENSIC DISCOVERY")
        print("=" * 60)
        
        self.discover_repository_structure()
        self.discover_configuration_files()
        self.discover_documentation()
        
        # Save complete data
        output_file = "/home/ubuntu/GITHUB_FORENSIC_DISCOVERY.json"
        with open(output_file, 'w') as f:
            json.dump(self.github_data, f, indent=2)
        
        # Generate summary
        summary = self.generate_summary_report()
        summary_file = "/home/ubuntu/GITHUB_FORENSIC_SUMMARY.md"
        with open(summary_file, 'w') as f:
            f.write(summary)
        
        print("\n✅ GITHUB FORENSIC DISCOVERY COMPLETE!")
        print(f"📊 Complete data: {output_file}")
        print(f"📋 Summary report: {summary_file}")
        
        return self.github_data

def main():
    discovery = GitHubForensicDiscovery()
    return discovery.run_complete_discovery()

if __name__ == "__main__":
    main()
