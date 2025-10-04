#!/usr/bin/env python3
"""
Ultimate Best Parts Extractor
Extracts all the best, most valuable components from the entire sandbox
"""

import os
import shutil
import json
import tarfile
import zipfile
from datetime import datetime, timedelta
import subprocess

def run_command(cmd):
    """Run shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except:
        return ""

def get_file_age_days(filepath):
    """Get file age in days"""
    try:
        mtime = os.path.getmtime(filepath)
        age = (datetime.now() - datetime.fromtimestamp(mtime)).days
        return age
    except:
        return 999

def is_valuable_file(filepath, filename):
    """Determine if a file is valuable based on various criteria"""
    
    # Always include these patterns
    valuable_patterns = [
        'ULTIMATE', 'FINAL', 'COMPLETE', 'COMPREHENSIVE', 'ENHANCED',
        'PRODUCTION', 'DEPLOYMENT', 'SYSTEM', 'TRADING', 'LYRA',
        'API', 'AI', 'CONSENSUS', 'VALIDATION', 'REPORT',
        'README', 'DOCUMENTATION', 'GUIDE', 'INSTRUCTIONS'
    ]
    
    # Valuable file extensions
    valuable_extensions = [
        '.py', '.md', '.json', '.yml', '.yaml', '.env', '.sh',
        '.tar.gz', '.zip', '.txt', '.log', '.html', '.js', '.css'
    ]
    
    # Skip these patterns
    skip_patterns = [
        '__pycache__', '.pyc', '.git/', 'node_modules/',
        '.cache/', 'temp/', 'tmp/', '.DS_Store'
    ]
    
    # Check skip patterns
    for pattern in skip_patterns:
        if pattern in filepath:
            return False
    
    # Check if filename contains valuable patterns
    filename_upper = filename.upper()
    for pattern in valuable_patterns:
        if pattern in filename_upper:
            return True
    
    # Check file extension
    for ext in valuable_extensions:
        if filename.endswith(ext):
            return True
    
    # Check if file is recent (last 14 days) and not too small
    if get_file_age_days(filepath) <= 14:
        try:
            size = os.path.getsize(filepath)
            if size > 100:  # At least 100 bytes
                return True
        except:
            pass
    
    return False

def extract_best_parts():
    """Extract all the best parts from the sandbox"""
    
    base_dir = "/home/ubuntu"
    output_dir = "/home/ubuntu/ULTIMATE_BEST_PARTS_ARCHIVE"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Categories for organization
    categories = {
        'CORE_SYSTEMS': [],
        'AI_INTEGRATION': [],
        'TRADING_ENGINE': [],
        'DOCUMENTATION': [],
        'DEPLOYMENT': [],
        'TESTING_VALIDATION': [],
        'CONFIGURATION': [],
        'ARCHIVES': [],
        'UTILITIES': []
    }
    
    total_files = 0
    total_size = 0
    
    print("🔍 Scanning for valuable files...")
    
    # Walk through all directories
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        skip_dirs = ['.git', '__pycache__', 'node_modules', '.cache', '.nvm']
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            filepath = os.path.join(root, file)
            
            if is_valuable_file(filepath, file):
                try:
                    size = os.path.getsize(filepath)
                    rel_path = os.path.relpath(filepath, base_dir)
                    
                    # Categorize the file
                    category = 'UTILITIES'  # default
                    file_upper = file.upper()
                    
                    if any(x in file_upper for x in ['LYRA', 'TRADING', 'SYSTEM']):
                        category = 'CORE_SYSTEMS'
                    elif any(x in file_upper for x in ['AI', 'CONSENSUS', 'OPENROUTER']):
                        category = 'AI_INTEGRATION'
                    elif any(x in file_upper for x in ['ENGINE', 'STRATEGY', 'PORTFOLIO']):
                        category = 'TRADING_ENGINE'
                    elif any(x in file_upper for x in ['README', 'DOC', 'GUIDE', 'REPORT']):
                        category = 'DOCUMENTATION'
                    elif any(x in file_upper for x in ['DEPLOY', 'DOCKER', 'KUBERNETES']):
                        category = 'DEPLOYMENT'
                    elif any(x in file_upper for x in ['TEST', 'VALID', 'CHECK']):
                        category = 'TESTING_VALIDATION'
                    elif any(x in file_upper for x in ['CONFIG', '.ENV', 'SETUP']):
                        category = 'CONFIGURATION'
                    elif any(x in file_upper for x in ['.TAR.GZ', '.ZIP']):
                        category = 'ARCHIVES'
                    
                    categories[category].append({
                        'file': file,
                        'path': rel_path,
                        'full_path': filepath,
                        'size': size,
                        'age_days': get_file_age_days(filepath)
                    })
                    
                    total_files += 1
                    total_size += size
                    
                    if total_files % 100 == 0:
                        print(f"Found {total_files} valuable files...")
                        
                except Exception as e:
                    continue
    
    print(f"\n📊 EXTRACTION SUMMARY")
    print(f"Total valuable files found: {total_files}")
    print(f"Total size: {total_size / (1024*1024):.1f} MB")
    
    # Create organized directory structure
    for category, files in categories.items():
        if files:
            category_dir = os.path.join(output_dir, category)
            os.makedirs(category_dir, exist_ok=True)
            
            print(f"\n📁 {category}: {len(files)} files")
            
            for file_info in files[:10]:  # Show first 10 files
                print(f"  - {file_info['file']} ({file_info['size']} bytes)")
            
            if len(files) > 10:
                print(f"  ... and {len(files) - 10} more files")
    
    # Copy files to organized structure
    print(f"\n📦 Copying files to archive...")
    
    for category, files in categories.items():
        if files:
            category_dir = os.path.join(output_dir, category)
            
            for file_info in files:
                try:
                    # Create subdirectory structure to avoid name conflicts
                    rel_dir = os.path.dirname(file_info['path'])
                    if rel_dir:
                        target_dir = os.path.join(category_dir, rel_dir)
                        os.makedirs(target_dir, exist_ok=True)
                        target_path = os.path.join(target_dir, file_info['file'])
                    else:
                        target_path = os.path.join(category_dir, file_info['file'])
                    
                    # Copy file
                    shutil.copy2(file_info['full_path'], target_path)
                    
                except Exception as e:
                    print(f"Error copying {file_info['file']}: {e}")
                    continue
    
    # Create summary report
    summary = {
        'extraction_date': datetime.now().isoformat(),
        'total_files': total_files,
        'total_size_mb': round(total_size / (1024*1024), 2),
        'categories': {}
    }
    
    for category, files in categories.items():
        if files:
            summary['categories'][category] = {
                'file_count': len(files),
                'total_size_mb': round(sum(f['size'] for f in files) / (1024*1024), 2),
                'files': [f['file'] for f in files[:20]]  # First 20 files
            }
    
    # Save summary
    with open(os.path.join(output_dir, 'EXTRACTION_SUMMARY.json'), 'w') as f:
        json.dump(summary, f, indent=2)
    
    # Create README
    readme_content = f"""# Ultimate Best Parts Archive

This archive contains all the most valuable components extracted from the sandbox environment.

## Extraction Summary
- **Total Files**: {total_files}
- **Total Size**: {total_size / (1024*1024):.1f} MB
- **Extraction Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Categories

"""
    
    for category, files in categories.items():
        if files:
            readme_content += f"### {category.replace('_', ' ').title()}\n"
            readme_content += f"- **Files**: {len(files)}\n"
            readme_content += f"- **Size**: {sum(f['size'] for f in files) / (1024*1024):.1f} MB\n\n"
    
    readme_content += """
## Usage

Each category contains the most valuable files from that domain:
- **CORE_SYSTEMS**: Main Lyra trading system components
- **AI_INTEGRATION**: OpenRouter and AI consensus systems
- **TRADING_ENGINE**: Trading strategies and portfolio management
- **DOCUMENTATION**: All guides, reports, and documentation
- **DEPLOYMENT**: Docker, Kubernetes, and deployment configs
- **TESTING_VALIDATION**: All testing and validation systems
- **CONFIGURATION**: Environment files and configurations
- **ARCHIVES**: Important tar.gz and zip files
- **UTILITIES**: Helper scripts and tools

All files have been organized to preserve their original directory structure where possible.
"""
    
    with open(os.path.join(output_dir, 'README.md'), 'w') as f:
        f.write(readme_content)
    
    print(f"\n✅ EXTRACTION COMPLETE!")
    print(f"Archive location: {output_dir}")
    print(f"Files extracted: {total_files}")
    print(f"Total size: {total_size / (1024*1024):.1f} MB")
    
    return output_dir

if __name__ == "__main__":
    extract_best_parts()
