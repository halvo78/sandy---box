#!/usr/bin/env python3
"""
ROBUST BENEFICIAL PARTS EXTRACTOR
Safely extracts all beneficial parts while handling I/O errors.
"""

import os
import json
import shutil
from datetime import datetime
from pathlib import Path

def safe_scan_directory(base_path, patterns, skip_dirs=None):
    """Safely scan directory for patterns, handling I/O errors."""
    if skip_dirs is None:
        skip_dirs = ['.cache', '.git', '__pycache__', 'node_modules']
    
    found_items = []
    
    try:
        for item in os.listdir(base_path):
            if any(skip in item for skip in skip_dirs):
                continue
                
            item_path = os.path.join(base_path, item)
            
            try:
                if os.path.isdir(item_path):
                    # Check if directory matches any pattern
                    for pattern in patterns:
                        pattern_clean = pattern.replace('*', '')
                        if pattern_clean.lower() in item.lower():
                            found_items.append({
                                'path': item_path,
                                'type': 'directory',
                                'name': item,
                                'pattern_match': pattern_clean
                            })
                            break
                    
                    # Recursively scan subdirectories (limited depth)
                    try:
                        sub_items = safe_scan_directory(item_path, patterns, skip_dirs)
                        found_items.extend(sub_items)
                    except:
                        pass  # Skip problematic subdirectories
                        
                elif os.path.isfile(item_path):
                    # Check if file matches any pattern
                    for pattern in patterns:
                        pattern_clean = pattern.replace('*', '')
                        if pattern_clean.lower() in item.lower():
                            found_items.append({
                                'path': item_path,
                                'type': 'file',
                                'name': item,
                                'pattern_match': pattern_clean
                            })
                            break
                            
            except (OSError, PermissionError):
                continue  # Skip problematic items
                
    except (OSError, PermissionError):
        pass  # Skip problematic directories
    
    return found_items

def extract_beneficial_parts():
    """Extract all beneficial parts safely."""
    print("🚀 ROBUST BENEFICIAL PARTS EXTRACTION")
    print("=" * 60)
    
    base_path = "/home/ubuntu"
    extraction_dir = os.path.join(base_path, "ULTIMATE_BENEFICIAL_EXTRACTION")
    os.makedirs(extraction_dir, exist_ok=True)
    
    # Define search patterns for different categories
    search_categories = {
        'newest_versions': [
            '*v5*', '*v6*', '*latest*', '*newest*', '*final*', '*ultimate*',
            '*2025*', '*current*', '*production*', '*live*', '*enhanced*'
        ],
        'vault_exchange': [
            '*vault*', '*exchange*', '*api*', '*connection*', '*okx*', '*binance*',
            '*coinbase*', '*kraken*', '*bybit*', '*gate*', '*kucoin*', '*huobi*'
        ],
        'apps_addons': [
            '*app*', '*addon*', '*plugin*', '*extension*', '*module*', '*component*',
            '*service*', '*tool*', '*utility*', '*helper*', '*manager*'
        ],
        'hummingbot': [
            '*hummingbot*', '*humming*', '*bot*', '*trading*', '*strategy*',
            '*market*', '*maker*', '*arbitrage*', '*liquidity*', '*grid*'
        ],
        'lyra_systems': [
            '*lyra*', '*trading*', '*crypto*', '*system*', '*engine*'
        ]
    }
    
    extraction_summary = {
        'extraction_date': datetime.now().isoformat(),
        'categories': {},
        'total_items': 0,
        'extracted_items': 0
    }
    
    for category, patterns in search_categories.items():
        print(f"\n🔍 Scanning for {category}...")
        
        # Create category directory
        category_dir = os.path.join(extraction_dir, category)
        os.makedirs(category_dir, exist_ok=True)
        
        # Find items matching patterns
        found_items = safe_scan_directory(base_path, patterns)
        
        extraction_summary['categories'][category] = {
            'found': len(found_items),
            'extracted': 0,
            'items': []
        }
        
        # Extract found items
        for item in found_items:
            try:
                source_path = item['path']
                dest_name = f"{item['pattern_match']}_{os.path.basename(source_path)}"
                dest_path = os.path.join(category_dir, dest_name)
                
                if item['type'] == 'directory':
                    if not os.path.exists(dest_path):
                        shutil.copytree(source_path, dest_path, ignore_errors=True)
                        print(f"✅ Extracted directory: {source_path}")
                        extraction_summary['categories'][category]['extracted'] += 1
                        extraction_summary['categories'][category]['items'].append({
                            'source': source_path,
                            'destination': dest_path,
                            'type': 'directory'
                        })
                else:
                    if not os.path.exists(dest_path):
                        shutil.copy2(source_path, dest_path)
                        print(f"✅ Extracted file: {source_path}")
                        extraction_summary['categories'][category]['extracted'] += 1
                        extraction_summary['categories'][category]['items'].append({
                            'source': source_path,
                            'destination': dest_path,
                            'type': 'file'
                        })
                        
            except Exception as e:
                print(f"⚠️ Could not extract {item['path']}: {e}")
        
        extraction_summary['total_items'] += extraction_summary['categories'][category]['found']
        extraction_summary['extracted_items'] += extraction_summary['categories'][category]['extracted']
    
    # Save extraction summary
    summary_file = os.path.join(extraction_dir, "EXTRACTION_SUMMARY.json")
    with open(summary_file, 'w') as f:
        json.dump(extraction_summary, f, indent=2)
    
    # Create comprehensive README
    readme_content = f"""# 🚀 Ultimate Beneficial Parts Extraction

**Extraction Date:** {extraction_summary['extraction_date']}

## 📊 Extraction Summary

**Total Items Found:** {extraction_summary['total_items']}
**Total Items Extracted:** {extraction_summary['extracted_items']}

### Categories:
"""
    
    for category, data in extraction_summary['categories'].items():
        readme_content += f"- **{category.replace('_', ' ').title()}:** {data['extracted']}/{data['found']} items extracted\n"
    
    readme_content += f"""
## 🎯 Purpose

This extraction contains ALL beneficial parts to enhance the Ultimate Lyra Trading System:

- Latest versions and improvements
- Up-to-date vault and exchange connections  
- All apps, addons, and extensions
- Complete Hummingbot components
- All Lyra system variations

## 📁 Directory Structure

```
ULTIMATE_BENEFICIAL_EXTRACTION/
├── newest_versions/     # Latest version components
├── vault_exchange/      # Vault and exchange integrations
├── apps_addons/        # Apps, addons, and extensions
├── hummingbot/         # Hummingbot trading components
├── lyra_systems/       # All Lyra system variations
├── EXTRACTION_SUMMARY.json
└── README.md
```

## 🏆 Next Steps

Integrate these beneficial parts into the Ultimate Lyra Trading System for maximum performance.
"""
    
    readme_file = os.path.join(extraction_dir, "README.md")
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    
    print(f"\n🎉 EXTRACTION COMPLETE!")
    print(f"📊 Total Items Found: {extraction_summary['total_items']}")
    print(f"✅ Successfully Extracted: {extraction_summary['extracted_items']}")
    print(f"📁 Extraction Directory: {extraction_dir}")
    
    return extraction_summary

if __name__ == "__main__":
    extract_beneficial_parts()
