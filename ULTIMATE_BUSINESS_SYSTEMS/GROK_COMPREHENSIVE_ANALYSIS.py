#!/usr/bin/env python3
"""
GROK COMPREHENSIVE ANALYSIS
Uses Grok through OpenRouter to analyze ALL GitHub repositories and sandbox content
to identify beneficial components that will increase system performance.
"""

import os
import logging
import json
import requests
from datetime import datetime
from pathlib import Path

def get_grok_analysis(content, analysis_type):
    """Get Grok analysis through OpenRouter API."""
    
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        logging.info("⚠️ OpenRouter API key not found")
        return None
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Craft specific prompt for Grok analysis
    if analysis_type == "github_analysis":
        prompt = f"""As Grok, analyze this GitHub repository content and identify ALL beneficial components that could enhance a cryptocurrency trading system. Look for:

1. Trading strategies and algorithms
2. Exchange integrations and APIs
3. Risk management systems
4. Performance optimization tools
5. Security enhancements
6. Monitoring and analytics
7. AI/ML components
8. Infrastructure improvements
9. Testing frameworks
10. Documentation and guides

Content to analyze:
{content}

Provide a detailed analysis with specific recommendations for integration and expected performance improvements. Be thorough and identify everything that could benefit the system."""

    elif analysis_type == "sandbox_analysis":
        prompt = f"""As Grok, analyze this sandbox content and identify ALL beneficial components for a cryptocurrency trading system. Focus on:

1. Latest versions and improvements
2. Configuration files and settings
3. Database schemas and data
4. Scripts and utilities
5. Integration components
6. Performance optimizations
7. Security configurations
8. Monitoring tools
9. Backup and recovery systems
10. Any hidden gems or valuable assets

Content to analyze:
{content}

Identify everything that could increase system performance percentage and provide specific integration recommendations."""

    else:
        prompt = f"""As Grok, analyze this content for cryptocurrency trading system enhancement:

{content}

Identify all beneficial components and provide recommendations."""
    
    data = {
        "model": "x-ai/grok-beta",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 4000,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            logging.info(f"⚠️ Unexpected response format: {result}")
            return None
            
    except requests.exceptions.RequestException as e:
        logging.info(f"⚠️ API request failed: {e}")
        return None
    except Exception as e:
        logging.info(f"⚠️ Error: {e}")
        return None

def analyze_github_repositories():
    """Analyze all GitHub repositories with Grok."""
    logging.info("🔍 GROK GITHUB REPOSITORY ANALYSIS")
    logging.info("=" * 50)
    
    github_repos = [
        "/home/ubuntu/ultimate-lyra-ecosystem",
        "/home/ubuntu/files-for-build", 
        "/home/ubuntu/lyra-files"
    ]
    
    github_analysis = {}
    
    for repo_path in github_repos:
        if os.path.exists(repo_path):
            logging.info(f"\n📂 Analyzing repository: {repo_path}")
            
            # Get repository structure and key files
            repo_content = get_repository_summary(repo_path)
            
            # Get Grok analysis
            analysis = get_grok_analysis(repo_content, "github_analysis")
            
            if analysis:
                github_analysis[repo_path] = {
                    'content_summary': repo_content,
                    'grok_analysis': analysis,
                    'analysis_date': datetime.now().isoformat()
                }
                logging.info(f"✅ Grok analysis completed for {repo_path}")
            else:
                logging.info(f"⚠️ Grok analysis failed for {repo_path}")
    
    return github_analysis

def analyze_sandbox_content():
    """Analyze sandbox content with Grok."""
    logging.info("\n🔍 GROK SANDBOX CONTENT ANALYSIS")
    logging.info("=" * 50)
    
    # Key sandbox directories to analyze
    sandbox_areas = [
        "/home/ubuntu/ULTIMATE_PRODUCTION_SYSTEM",
        "/home/ubuntu/CRYPTO_INTELLIGENCE_ARCHIVE",
        "/home/ubuntu/CONTAINERIZATION_ARCHIVE",
        "/home/ubuntu/ULTIMATE_SYSTEM_CAPABILITIES_ARCHIVE",
        "/home/ubuntu/ultimate_lyra_v5",
        "/home/ubuntu/ultimate_lyra_systems"
    ]
    
    sandbox_analysis = {}
    
    for area_path in sandbox_areas:
        if os.path.exists(area_path):
            logging.info(f"\n📁 Analyzing sandbox area: {area_path}")
            
            # Get area summary
            area_content = get_directory_summary(area_path)
            
            # Get Grok analysis
            analysis = get_grok_analysis(area_content, "sandbox_analysis")
            
            if analysis:
                sandbox_analysis[area_path] = {
                    'content_summary': area_content,
                    'grok_analysis': analysis,
                    'analysis_date': datetime.now().isoformat()
                }
                logging.info(f"✅ Grok analysis completed for {area_path}")
            else:
                logging.info(f"⚠️ Grok analysis failed for {area_path}")
    
    return sandbox_analysis

def get_repository_summary(repo_path):
    """Get a summary of repository content."""
    summary = f"Repository: {repo_path}\n\n"
    
    try:
        # Get directory structure
        summary += "Directory Structure:\n"
        for root, dirs, files in os.walk(repo_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            level = root.replace(repo_path, '').count(os.sep)
            indent = ' ' * 2 * level
            summary += f"{indent}{os.path.basename(root)}/\n"
            
            # Limit depth to avoid too much content
            if level < 3:
                subindent = ' ' * 2 * (level + 1)
                for file in files[:10]:  # Limit files shown
                    summary += f"{subindent}{file}\n"
                if len(files) > 10:
                    summary += f"{subindent}... and {len(files) - 10} more files\n"
        
        # Get key file contents
        key_files = ['README.md', 'package.json', 'requirements.txt', 'docker-compose.yml', 'Dockerfile']
        
        for key_file in key_files:
            file_path = os.path.join(repo_path, key_file)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()[:2000]  # Limit content
                        summary += f"\n{key_file} content:\n{content}\n"
                except:
                    summary += f"\n{key_file}: (could not read)\n"
    
    except Exception as e:
        summary += f"Error reading repository: {e}\n"
    
    return summary

def get_directory_summary(dir_path):
    """Get a summary of directory content."""
    summary = f"Directory: {dir_path}\n\n"
    
    try:
        # Get file count and types
        file_types = {}
        total_files = 0
        
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                total_files += 1
                ext = os.path.splitext(file)[1].lower()
                file_types[ext] = file_types.get(ext, 0) + 1
        
        summary += f"Total files: {total_files}\n"
        summary += "File types:\n"
        for ext, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True)[:10]:
            summary += f"  {ext or 'no extension'}: {count} files\n"
        
        # Get key files
        key_patterns = ['*.py', '*.json', '*.yaml', '*.yml', '*.md', '*.txt', '*.sql']
        summary += "\nKey files found:\n"
        
        for pattern in key_patterns:
            files = list(Path(dir_path).rglob(pattern))[:5]  # Limit to 5 files per type
            if files:
                summary += f"  {pattern}: {[f.name for f in files]}\n"
    
    except Exception as e:
        summary += f"Error reading directory: {e}\n"
    
    return summary

def generate_comprehensive_report(github_analysis, sandbox_analysis):
    """Generate comprehensive Grok analysis report."""
    
    report = f"""# 🤖 GROK COMPREHENSIVE ANALYSIS REPORT

**Generated:** {datetime.now().isoformat()}
**Analyzer:** Grok (x-ai/grok-beta) via OpenRouter
**Mission:** Identify ALL beneficial components to increase system performance

## 🎯 Executive Summary

Grok has conducted a comprehensive analysis of ALL GitHub repositories and sandbox content to identify beneficial components that will enhance the Ultimate Lyra Trading System performance.

## 📊 GitHub Repository Analysis

"""
    
    for repo_path, analysis in github_analysis.items():
        report += f"""### Repository: {os.path.basename(repo_path)}

**Path:** `{repo_path}`
**Analysis Date:** {analysis['analysis_date']}

#### Grok's Analysis:
{analysis['grok_analysis']}

---

"""
    
    report += """## 🔍 Sandbox Content Analysis

"""
    
    for area_path, analysis in sandbox_analysis.items():
        report += f"""### Sandbox Area: {os.path.basename(area_path)}

**Path:** `{area_path}`
**Analysis Date:** {analysis['analysis_date']}

#### Grok's Analysis:
{analysis['grok_analysis']}

---

"""
    
    report += """## 🚀 Integration Recommendations

Based on Grok's comprehensive analysis, the following components should be integrated to maximize system performance:

### Immediate Integrations (High Impact)
- Components identified by Grok as having immediate performance benefits

### Strategic Integrations (Medium-Long Term)
- Components that provide strategic advantages and future-proofing

### Performance Optimizations
- Specific optimizations identified by Grok to increase system efficiency

## 📈 Expected Performance Increase

Grok's analysis indicates potential performance improvements across multiple dimensions:
- Trading efficiency
- Risk management
- System reliability
- Scalability
- Security

## 🏆 Conclusion

This comprehensive analysis by Grok provides a roadmap for maximizing the Ultimate Lyra Trading System's performance through strategic integration of identified beneficial components.

---

*Analysis conducted by Grok AI through OpenRouter API*
"""
    
    return report

def main():
    """Main execution function."""
    logging.info("🤖 GROK COMPREHENSIVE ANALYSIS - STARTING")
    logging.info("=" * 60)
    
    # Check API key
    if not os.getenv('OPENROUTER_API_KEY'):
        logging.info("⚠️ OPENROUTER_API_KEY environment variable not set")
        return
    
    # Analyze GitHub repositories
    github_analysis = analyze_github_repositories()
    
    # Analyze sandbox content
    sandbox_analysis = analyze_sandbox_content()
    
    # Generate comprehensive report
    report = generate_comprehensive_report(github_analysis, sandbox_analysis)
    
    # Save report
    report_path = "/home/ubuntu/GROK_COMPREHENSIVE_ANALYSIS_REPORT.md"
    with open(report_path, 'w') as f:
        f.write(report)
    
    # Save raw analysis data
    analysis_data = {
        'github_analysis': github_analysis,
        'sandbox_analysis': sandbox_analysis,
        'generation_date': datetime.now().isoformat()
    }
    
    data_path = "/home/ubuntu/GROK_ANALYSIS_DATA.json"
    with open(data_path, 'w') as f:
        json.dump(analysis_data, f, indent=2)
    
    logging.info(f"\n🎉 GROK ANALYSIS COMPLETE!")
    logging.info(f"📄 Report saved: {report_path}")
    logging.info(f"📊 Data saved: {data_path}")
    logging.info(f"🔍 GitHub repos analyzed: {len(github_analysis)}")
    logging.info(f"📁 Sandbox areas analyzed: {len(sandbox_analysis)}")

if __name__ == "__main__":
    main()
