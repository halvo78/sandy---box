#!/usr/bin/env python3
"""
AI Consensus System Analysis for Ultimate Lyra Trading System
This script will analyze the current system state and get AI consensus on what to preserve.
"""

import os
import json
import requests
from datetime import datetime

class AIConsensusAnalyzer:
    def __init__(self):
        self.openrouter_keys = [
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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"
        ]
        self.models = [
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4o",
            "google/gemini-pro-1.5",
            "meta-llama/llama-3.1-70b-instruct",
            "mistralai/mistral-large",
            "qwen/qwen-2.5-72b-instruct",
            "deepseek/deepseek-chat",
            "x-ai/grok-beta"
        ]
        
    def scan_system_files(self):
        """Scan the system for all files and categorize them."""
        file_inventory = {}
        base_dirs = ['/home/ubuntu/ultimate_lyra_systems', '/home/ubuntu/ultimate_lyra_v5', 
                    '/home/ubuntu/ULTIMATE_LYRA_DEFINITIVE_SYSTEM', '/home/ubuntu/ultimate_lyra_v5_ultimate']
        
        for base_dir in base_dirs:
            if os.path.exists(base_dir):
                try:
                    for root, dirs, files in os.walk(base_dir):
                        for file in files:
                            file_path = os.path.join(root, file)
                            try:
                                stat = os.stat(file_path)
                                file_inventory[file_path] = {
                                    'size': stat.st_size,
                                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                                    'accessible': True
                                }
                            except (OSError, IOError):
                                file_inventory[file_path] = {
                                    'size': 0,
                                    'modified': 'unknown',
                                    'accessible': False
                                }
                except Exception as e:
                    print(f"Error scanning {base_dir}: {e}")
                    
        return file_inventory
    
    def get_ai_consensus(self, prompt, file_list):
        """Get consensus from multiple AI models about file importance."""
        consensus_results = {}
        
        for i, (api_key, model) in enumerate(zip(self.openrouter_keys[:4], self.models[:4])):
            try:
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are an expert system analyst evaluating cryptocurrency trading system files. Rate each file as CRITICAL, USEFUL, or USELESS for a production trading system."
                        },
                        {
                            "role": "user",
                            "content": f"{prompt}\n\nFiles to evaluate:\n{json.dumps(file_list, indent=2)}"
                        }
                    ],
                    "max_tokens": 2000
                }
                
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    consensus_results[f"ai_{i+1}_{model.split('/')[-1]}"] = result['choices'][0]['message']['content']
                    print(f"✅ Got response from {model}")
                else:
                    print(f"❌ Error from {model}: {response.status_code}")
                    
            except Exception as e:
                print(f"❌ Exception with {model}: {e}")
                
        return consensus_results
    
    def analyze_system(self):
        """Perform comprehensive system analysis with AI consensus."""
        print("🔍 Starting AI Consensus System Analysis...")
        
        # Scan all files
        print("📁 Scanning system files...")
        file_inventory = self.scan_system_files()
        
        print(f"📊 Found {len(file_inventory)} files")
        
        # Group files by type for analysis
        python_files = {k: v for k, v in file_inventory.items() if k.endswith('.py')}
        config_files = {k: v for k, v in file_inventory.items() if k.endswith(('.json', '.yml', '.yaml', '.env'))}
        doc_files = {k: v for k, v in file_inventory.items() if k.endswith(('.md', '.txt', '.rst'))}
        db_files = {k: v for k, v in file_inventory.items() if k.endswith('.db')}
        
        analysis_results = {}
        
        # Analyze each category with AI consensus
        categories = {
            'python_files': python_files,
            'config_files': config_files,
            'documentation': doc_files,
            'databases': db_files
        }
        
        for category, files in categories.items():
            if files:
                print(f"🤖 Getting AI consensus on {category}...")
                prompt = f"Analyze these {category} from a cryptocurrency trading system. Determine which are CRITICAL (essential for production), USEFUL (beneficial but not essential), or USELESS (can be discarded) for the Ultimate Lyra Trading System."
                
                consensus = self.get_ai_consensus(prompt, list(files.keys())[:20])  # Limit to first 20 files per category
                analysis_results[category] = {
                    'files': files,
                    'ai_consensus': consensus
                }
        
        # Save results
        results_file = '/home/ubuntu/fresh_start/ai_consensus_analysis.json'
        with open(results_file, 'w') as f:
            json.dump(analysis_results, f, indent=2, default=str)
            
        print(f"💾 Analysis saved to {results_file}")
        return analysis_results

if __name__ == "__main__":
    analyzer = AIConsensusAnalyzer()
    results = analyzer.analyze_system()
    print("🎉 AI Consensus Analysis Complete!")
