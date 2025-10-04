#!/usr/bin/env python3
"""
Manual System Analysis for Ultimate Lyra Trading System
Since AI consensus failed, we'll do manual analysis based on file patterns and content.
"""

import os
import json
from datetime import datetime

def analyze_file_importance(file_path, file_info):
    """Manually analyze file importance based on patterns and content."""
    filename = os.path.basename(file_path)
    
    # Critical files (essential for production)
    critical_patterns = [
        'COMPLETE_ULTIMATE_DASHBOARD.py',
        'COMPLETE_STREAMLIT_PORTFOLIO.py', 
        'COMPLETE_TELEGRAM_INTEGRATION.py',
        'ULTIMATE_REAL_EXCHANGE_PORTFOLIO.py',
        'EXCHANGE_API_CREDENTIAL_VALIDATOR.py',
        'PRODUCTION_EXCHANGE_CONFIGURATION.py',
        'ULTIMATE_AI_CONSENSUS_COMMISSIONING.py',
        'ULTIMATE_MULTI_SOURCE_API_SYSTEM.py',
        'ULTIMATE_COMPREHENSIVE_DISCOVERY_SYSTEM.py',
        'ai_portfolio.db',
        'ultimate_portfolio.db'
    ]
    
    # Useful files (beneficial but not essential)
    useful_patterns = [
        'NGROK_COMPLETE_SETUP.py',
        'ULTIMATE_DASHBOARD_CONTROL_SYSTEM.py',
        'system_status_check.py',
        'complete_dashboard.db',
        'telegram_system.db',
        'commissioning_audit.db',
        'exchange_validation.db',
        'production_exchanges.db',
        'COMPLETION REPORT.md',
        'SUCCESS REPORT.md',
        'DELIVERY REPORT.md'
    ]
    
    # Check if file is accessible
    if not file_info['accessible']:
        return 'CORRUPTED'
    
    # Check file size (empty files are likely corrupted)
    if file_info['size'] == 0:
        return 'EMPTY/CORRUPTED'
    
    # Check against critical patterns
    for pattern in critical_patterns:
        if pattern in filename:
            return 'CRITICAL'
    
    # Check against useful patterns
    for pattern in useful_patterns:
        if pattern in filename:
            return 'USEFUL'
    
    # Default to useless if no patterns match
    return 'USELESS'

def create_recovery_plan():
    """Create a recovery plan based on file analysis."""
    
    # Load the analysis results
    with open('/home/ubuntu/fresh_start/ai_consensus_analysis.json', 'r') as f:
        analysis = json.load(f)
    
    recovery_plan = {
        'critical_files': [],
        'useful_files': [],
        'corrupted_files': [],
        'useless_files': [],
        'recovery_actions': []
    }
    
    # Analyze all files
    all_files = {}
    for category in analysis.values():
        all_files.update(category['files'])
    
    for file_path, file_info in all_files.items():
        importance = analyze_file_importance(file_path, file_info)
        
        if importance == 'CRITICAL':
            recovery_plan['critical_files'].append({
                'path': file_path,
                'size': file_info['size'],
                'accessible': file_info['accessible']
            })
        elif importance == 'USEFUL':
            recovery_plan['useful_files'].append({
                'path': file_path,
                'size': file_info['size'],
                'accessible': file_info['accessible']
            })
        elif importance in ['CORRUPTED', 'EMPTY/CORRUPTED']:
            recovery_plan['corrupted_files'].append({
                'path': file_path,
                'reason': importance
            })
        else:
            recovery_plan['useless_files'].append(file_path)
    
    # Create recovery actions
    recovery_plan['recovery_actions'] = [
        "1. Copy all CRITICAL files to fresh_start/critical/",
        "2. Copy all USEFUL files to fresh_start/useful/", 
        "3. Create GitHub repository structure",
        "4. Push critical files to halvo78/ultimate-lyra-ecosystem",
        "5. Push useful files to halvo78/files-for-build",
        "6. Set up production environment from clean files"
    ]
    
    # Save recovery plan
    with open('/home/ubuntu/fresh_start/recovery_plan.json', 'w') as f:
        json.dump(recovery_plan, f, indent=2)
    
    return recovery_plan

def execute_file_recovery(recovery_plan):
    """Execute the file recovery based on the plan."""
    
    # Create directories
    os.makedirs('/home/ubuntu/fresh_start/critical', exist_ok=True)
    os.makedirs('/home/ubuntu/fresh_start/useful', exist_ok=True)
    os.makedirs('/home/ubuntu/fresh_start/github_ready', exist_ok=True)
    
    recovered_count = 0
    failed_count = 0
    
    # Copy critical files
    print("🔥 Recovering CRITICAL files...")
    for file_info in recovery_plan['critical_files']:
        if file_info['accessible'] and file_info['size'] > 0:
            try:
                source = file_info['path']
                filename = os.path.basename(source)
                dest = f"/home/ubuntu/fresh_start/critical/{filename}"
                
                with open(source, 'rb') as src, open(dest, 'wb') as dst:
                    dst.write(src.read())
                
                print(f"✅ Recovered: {filename}")
                recovered_count += 1
            except Exception as e:
                print(f"❌ Failed to recover {filename}: {e}")
                failed_count += 1
    
    # Copy useful files
    print("📁 Recovering USEFUL files...")
    for file_info in recovery_plan['useful_files']:
        if file_info['accessible'] and file_info['size'] > 0:
            try:
                source = file_info['path']
                filename = os.path.basename(source)
                dest = f"/home/ubuntu/fresh_start/useful/{filename}"
                
                with open(source, 'rb') as src, open(dest, 'wb') as dst:
                    dst.write(src.read())
                
                print(f"✅ Recovered: {filename}")
                recovered_count += 1
            except Exception as e:
                print(f"❌ Failed to recover {filename}: {e}")
                failed_count += 1
    
    print(f"\n📊 Recovery Summary:")
    print(f"✅ Successfully recovered: {recovered_count} files")
    print(f"❌ Failed to recover: {failed_count} files")
    
    return recovered_count, failed_count

if __name__ == "__main__":
    print("🔍 Starting Manual System Analysis...")
    
    # Create recovery plan
    recovery_plan = create_recovery_plan()
    
    print(f"📊 Analysis Results:")
    print(f"🔥 Critical files: {len(recovery_plan['critical_files'])}")
    print(f"📁 Useful files: {len(recovery_plan['useful_files'])}")
    print(f"💀 Corrupted files: {len(recovery_plan['corrupted_files'])}")
    print(f"🗑️ Useless files: {len(recovery_plan['useless_files'])}")
    
    # Execute recovery
    print("\n🚀 Starting File Recovery...")
    recovered, failed = execute_file_recovery(recovery_plan)
    
    print("\n🎉 Manual Analysis and Recovery Complete!")
