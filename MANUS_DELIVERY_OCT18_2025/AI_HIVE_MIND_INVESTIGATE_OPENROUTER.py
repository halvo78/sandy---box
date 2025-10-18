#!/usr/bin/env python3
"""
AI HIVE MIND INVESTIGATION - OPENROUTER API ISSUE
Using ALL available AI models to find the solution
"""

import os
import json
import requests
from typing import Dict, List, Any

# All available API keys from environment
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
XAI_API_KEY = os.getenv('XAI_API_KEY')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
PERPLEXITY_API_KEY = os.getenv('SONAR_API_KEY')

# The problematic OpenRouter API keys
OPENROUTER_KEYS = [
    "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",
    "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",
    "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",
    "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"
]

def query_claude(prompt: str) -> str:
    """Query Anthropic Claude for insights"""
    if not ANTHROPIC_API_KEY:
        return "Claude API key not available"
    
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )
        if response.status_code == 200:
            return response.json()['content'][0]['text']
        return f"Claude error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Claude exception: {str(e)}"

def query_grok(prompt: str) -> str:
    """Query xAI Grok for insights"""
    if not XAI_API_KEY:
        return "Grok API key not available"
    
    try:
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "grok-beta",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return f"Grok error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Grok exception: {str(e)}"

def query_perplexity(prompt: str) -> str:
    """Query Perplexity for real-time insights"""
    if not PERPLEXITY_API_KEY:
        return "Perplexity API key not available"
    
    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "sonar-pro",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return f"Perplexity error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Perplexity exception: {str(e)}"

def test_openrouter_variations() -> Dict[str, Any]:
    """Test different variations of OpenRouter API calls"""
    results = {}
    
    test_key = OPENROUTER_KEYS[0]
    
    # Test 1: Basic request
    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {test_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": "test"}]
            },
            timeout=10
        )
        results['basic'] = {"status": r.status_code, "response": r.text[:200]}
    except Exception as e:
        results['basic'] = {"error": str(e)}
    
    # Test 2: With HTTP-Referer header
    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {test_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://ultimate-lyra-trading.com",
                "X-Title": "Ultimate Trading System"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": "test"}]
            },
            timeout=10
        )
        results['with_referer'] = {"status": r.status_code, "response": r.text[:200]}
    except Exception as e:
        results['with_referer'] = {"error": str(e)}
    
    # Test 3: Free model
    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {test_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.2-3b-instruct:free",
                "messages": [{"role": "user", "content": "test"}]
            },
            timeout=10
        )
        results['free_model'] = {"status": r.status_code, "response": r.text[:200]}
    except Exception as e:
        results['free_model'] = {"error": str(e)}
    
    # Test 4: Different endpoint
    try:
        r = requests.get(
            "https://openrouter.ai/api/v1/generation",
            headers={"Authorization": f"Bearer {test_key}"},
            timeout=10
        )
        results['generation_endpoint'] = {"status": r.status_code, "response": r.text[:200]}
    except Exception as e:
        results['generation_endpoint'] = {"error": str(e)}
    
    # Test 5: Check credits
    try:
        r = requests.get(
            "https://openrouter.ai/api/v1/auth/key",
            headers={"Authorization": f"Bearer {test_key}"},
            timeout=10
        )
        results['auth_check'] = {"status": r.status_code, "response": r.text[:200]}
    except Exception as e:
        results['auth_check'] = {"error": str(e)}
    
    return results

def main():
    print("=" * 80)
    print("🤖 AI HIVE MIND INVESTIGATION - OPENROUTER API ISSUE")
    print("=" * 80)
    print()
    
    # Step 1: Test all variations
    print("📊 Testing OpenRouter API variations...")
    test_results = test_openrouter_variations()
    print(json.dumps(test_results, indent=2))
    print()
    
    # Step 2: Ask Claude for analysis
    print("🤖 Consulting Claude...")
    claude_prompt = f"""
    I have OpenRouter API keys that show "User not found" error (401) when trying to use chat completions,
    but they successfully return the models list. The account has $39.03 in credits and the keys are enabled
    in the dashboard. The keys worked in the past.
    
    Test results: {json.dumps(test_results, indent=2)}
    
    What could cause this specific error pattern and how can I fix it?
    Be specific and actionable.
    """
    claude_response = query_claude(claude_prompt)
    print(claude_response)
    print()
    
    # Step 3: Ask Grok for insights
    print("🤖 Consulting Grok...")
    grok_prompt = """
    OpenRouter API keys return "User not found" (401) for /chat/completions and /auth/key endpoints,
    but successfully list models. Account has credits. Keys worked before. What's wrong and how to fix?
    """
    grok_response = query_grok(grok_prompt)
    print(grok_response)
    print()
    
    # Step 4: Ask Perplexity for real-time info
    print("🤖 Consulting Perplexity...")
    perplexity_prompt = """
    Search for recent OpenRouter API issues, especially "User not found" errors with valid API keys.
    What are the common causes and solutions?
    """
    perplexity_response = query_perplexity(perplexity_prompt)
    print(perplexity_response)
    print()
    
    print("=" * 80)
    print("✅ AI HIVE MIND INVESTIGATION COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()

