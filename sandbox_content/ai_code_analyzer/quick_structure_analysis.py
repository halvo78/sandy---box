#!/usr/bin/env python3
"""
Quick structural analysis of the Ultimate Lyra Trading System codebase.
"""

import os
from pathlib import Path
from collections import defaultdict, Counter
import json

def analyze_codebase_structure():
    """Analyze the structure of the codebase."""
    codebase_path = "/home/ubuntu/github_push_staging"
    
    # Initialize counters
    file_types = Counter()
    directory_structure = defaultdict(list)
    file_sizes = []
    total_files = 0
    total_size = 0
    
    # Categories for files
    categories = {
        'Core Trading Logic': [],
        'AI/ML Components': [],
        'Configuration': [],
        'Documentation': [],
        'Testing': [],
        'Security': [],
        'Monitoring': [],
        'Deployment': [],
        'Data Files': [],
        'Scripts': [],
        'Other': []
    }
    
    # Walk through the codebase
    for root, dirs, files in os.walk(codebase_path):
        # Skip .git directories
        if '.git' in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, codebase_path)
            
            try:
                file_size = os.path.getsize(file_path)
                file_sizes.append(file_size)
                total_size += file_size
                total_files += 1
                
                # Get file extension
                ext = Path(file).suffix.lower()
                file_types[ext] += 1
                
                # Categorize file
                category = categorize_file(file_path, file)
                categories[category].append(relative_path)
                
                # Track directory structure
                dir_name = os.path.basename(root)
                directory_structure[dir_name].append(file)
                
            except (OSError, IOError):
                continue
    
    # Generate analysis report
    report = {
        'summary': {
            'total_files': total_files,
            'total_size_mb': round(total_size / (1024 * 1024), 2),
            'average_file_size_kb': round((total_size / total_files) / 1024, 2) if total_files > 0 else 0,
            'largest_file_size_mb': round(max(file_sizes) / (1024 * 1024), 2) if file_sizes else 0
        },
        'file_types': dict(file_types.most_common(20)),
        'categories': {k: len(v) for k, v in categories.items()},
        'category_details': categories,
        'directory_structure': dict(directory_structure)
    }
    
    return report

def categorize_file(file_path, filename):
    """Categorize a file based on its path and name."""
    path_lower = file_path.lower()
    name_lower = filename.lower()
    ext = Path(filename).suffix.lower()
    
    # Core Trading Logic
    if any(keyword in path_lower for keyword in ['trading', 'strategy', 'order', 'position', 'execution', 'portfolio']):
        return 'Core Trading Logic'
    
    # AI/ML Components
    if any(keyword in path_lower for keyword in ['ai', 'ml', 'model', 'neural', 'learning', 'prediction']):
        return 'AI/ML Components'
    
    # Configuration
    if ext in ['.json', '.yaml', '.yml', '.ini', '.conf', '.config'] or 'config' in name_lower:
        return 'Configuration'
    
    # Documentation
    if ext in ['.md', '.txt', '.rst', '.doc', '.docx'] or 'readme' in name_lower:
        return 'Documentation'
    
    # Testing
    if any(keyword in path_lower for keyword in ['test', 'spec', 'unittest']):
        return 'Testing'
    
    # Security
    if any(keyword in path_lower for keyword in ['security', 'auth', 'crypto', 'ssl', 'cert']):
        return 'Security'
    
    # Monitoring
    if any(keyword in path_lower for keyword in ['monitor', 'log', 'metric', 'health', 'dashboard']):
        return 'Monitoring'
    
    # Deployment
    if any(keyword in path_lower for keyword in ['deploy', 'docker', 'k8s', 'kubernetes', 'helm']):
        return 'Deployment'
    
    # Data Files
    if ext in ['.db', '.sqlite', '.csv', '.parquet', '.h5']:
        return 'Data Files'
    
    # Scripts
    if ext in ['.py', '.sh', '.bash', '.ps1'] and 'script' in path_lower:
        return 'Scripts'
    
    return 'Other'

def main():
    print("🔍 Analyzing Ultimate Lyra Trading System structure...")
    
    report = analyze_codebase_structure()
    
    # Save report
    output_path = "/home/ubuntu/ai_analysis_results/structure_analysis.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print(f"📊 Structure Analysis Complete!")
    print(f"Total Files: {report['summary']['total_files']}")
    print(f"Total Size: {report['summary']['total_size_mb']} MB")
    print(f"Average File Size: {report['summary']['average_file_size_kb']} KB")
    
    print("\n📂 File Categories:")
    for category, count in report['categories'].items():
        print(f"  {category}: {count} files")
    
    print("\n📄 Top File Types:")
    for ext, count in list(report['file_types'].items())[:10]:
        print(f"  {ext or 'no extension'}: {count} files")
    
    print(f"\n💾 Report saved to: {output_path}")

if __name__ == "__main__":
    main()
