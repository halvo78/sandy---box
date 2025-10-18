#!/usr/bin/env python3
"""
Consult ALL OpenRouter AI models to find the best integration strategy
for the 60+ additional projects discovered
"""

import os
import json
import requests
from typing import List, Dict, Any

# OpenRouter API configuration
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Top models to consult (diverse capabilities)
TOP_MODELS = [
    # Tier 1: Advanced Reasoning
    "deepseek/deepseek-r1:free",
    "anthropic/claude-3.5-sonnet",
    "openai/gpt-4o",
    "google/gemini-2.5-flash-preview",
    "x-ai/grok-2-vision-1212",
    
    # Tier 2: Code & Analysis
    "qwen/qwen-3-coder-plus",
    "deepseek/deepseek-coder",
    "meta-llama/llama-3.3-70b-instruct",
    
    # Tier 3: Fast Reasoning
    "anthropic/claude-haiku-4.5",
    "openai/gpt-4o-mini",
]

def consult_model(model: str, prompt: str) -> Dict[str, Any]:
    """Consult a single AI model"""
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 2000,
            "temperature": 0.7,
        }
        
        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=headers,
            json=data,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return {
                "model": model,
                "success": True,
                "response": result['choices'][0]['message']['content'],
                "tokens": result.get('usage', {})
            }
        else:
            return {
                "model": model,
                "success": False,
                "error": f"HTTP {response.status_code}: {response.text}"
            }
            
    except Exception as e:
        return {
            "model": model,
            "success": False,
            "error": str(e)
        }

def main():
    """Main consultation function"""
    
    prompt = """You are a world-class algorithmic trading expert. We have discovered 60+ additional open source trading projects worth $95M+ beyond our current 20 projects.

Our current system (15.0/10) includes:
- Freqtrade, Qlib, FinRL, VectorBT (Top 20)
- 30 AI models with hive mind
- MIT/PhD research
- 100X amplification plan

NEW DISCOVERIES (Top 10):
1. Nautilus Trader - Institutional-grade, Rust/Cython, sub-microsecond latency
2. QuantLib - Industry standard (Goldman Sachs, JP Morgan), 20+ years
3. Riskfolio-Lib - Advanced portfolio optimization
4. Zipline - Quantopian's backtesting (18K stars)
5. PyBroker - Modern ML-focused framework
6. Backtrader - 14K stars, 100+ indicators
7. CCXT - 39K stars, 100+ exchanges
8. Lean (QuantConnect) - 12K stars, 275K users
9. QuantStats - Portfolio analytics
10. pandas-ta - 130+ indicators

QUESTION: Which 3 projects should we integrate FIRST for maximum impact, and what specific features should we extract from each?

Provide a concise, actionable answer with:
1. Top 3 projects to integrate first
2. Specific features to extract from each
3. Expected impact on system rating (15.0/10 → ?)
4. Integration priority order

Keep response under 500 words."""

    print("=" * 80)
    print("CONSULTING ALL OPENROUTER AI MODELS")
    print("=" * 80)
    print(f"\nTotal models to consult: {len(TOP_MODELS)}")
    print(f"Prompt length: {len(prompt)} characters\n")
    
    results = []
    
    for i, model in enumerate(TOP_MODELS, 1):
        print(f"\n[{i}/{len(TOP_MODELS)}] Consulting: {model}")
        print("-" * 80)
        
        result = consult_model(model, prompt)
        results.append(result)
        
        if result['success']:
            print(f"✓ SUCCESS")
            print(f"Response length: {len(result['response'])} characters")
            print(f"Tokens used: {result.get('tokens', {})}")
            print(f"\nResponse preview:")
            print(result['response'][:300] + "..." if len(result['response']) > 300 else result['response'])
        else:
            print(f"✗ FAILED: {result['error']}")
    
    # Save results
    output_file = "/home/ubuntu/ALL_AI_MODELS_CONSULTATION_RESULTS.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "=" * 80)
    print("CONSULTATION COMPLETE")
    print("=" * 80)
    
    # Summary
    successful = sum(1 for r in results if r['success'])
    failed = len(results) - successful
    
    print(f"\nSuccessful consultations: {successful}/{len(results)}")
    print(f"Failed consultations: {failed}/{len(results)}")
    print(f"\nResults saved to: {output_file}")
    
    # Analyze consensus
    if successful > 0:
        print("\n" + "=" * 80)
        print("ANALYZING CONSENSUS")
        print("=" * 80)
        
        # Count project mentions
        project_mentions = {}
        for result in results:
            if result['success']:
                response = result['response'].lower()
                for project in ['nautilus', 'quantlib', 'riskfolio', 'zipline', 'pybroker', 
                               'backtrader', 'ccxt', 'lean', 'quantstats', 'pandas-ta']:
                    if project in response:
                        project_mentions[project] = project_mentions.get(project, 0) + 1
        
        print("\nProject mentions across all models:")
        for project, count in sorted(project_mentions.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / successful) * 100
            print(f"  {project.capitalize():15} - {count:2}/{successful} models ({percentage:.0f}%)")
        
        # Determine top 3 by consensus
        top_3 = sorted(project_mentions.items(), key=lambda x: x[1], reverse=True)[:3]
        print(f"\nTOP 3 BY AI CONSENSUS:")
        for i, (project, count) in enumerate(top_3, 1):
            percentage = (count / successful) * 100
            print(f"  {i}. {project.capitalize()} - {percentage:.0f}% consensus")

if __name__ == "__main__":
    main()
