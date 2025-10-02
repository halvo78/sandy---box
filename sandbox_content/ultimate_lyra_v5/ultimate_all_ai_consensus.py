"""
Ultimate Lyra Trading System - COMPLETE AI CONSENSUS
===================================================
Uses ALL available top-tier AI models from OpenRouter for definitive consensus.
"""

import os
import json
import asyncio
import httpx
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
MODELS_FILE = "/home/ubuntu/ultimate_lyra_v5/openrouter_models.json"
FINAL_REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/COMPLETE_AI_CONSENSUS_REPORT.md"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

def get_all_top_models():
    """Extract all top-tier AI models from the OpenRouter models list."""
    with open(MODELS_FILE, "r") as f:
        models_data = json.load(f)
    
    top_models = []
    for model in models_data["data"]:
        model_id = model["id"]
        model_name = model["name"]
        
        # Include all major AI providers and their latest models
        if any(keyword in model_id.lower() for keyword in [
            "gpt-5", "gpt-4o", "claude-4", "claude-3.5", "claude-3-opus", 
            "gemini-2.5", "gemini-pro", "grok", "mistral-large", "mistral-medium",
            "llama-3", "deepseek-v3"
        ]):
            # Skip free models for this comprehensive test
            if ":free" not in model_id:
                top_models.append((model_id, model_name))
    
    return top_models

async def query_model(client, model_id, model_name, api_key, prompt):
    """Query a single AI model."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }
    try:
        response = await client.post(f"{OPENROUTER_API_BASE}/chat/completions", headers=headers, json=data, timeout=90.0)
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return model_id, model_name, "success", content
        else:
            return model_id, model_name, "error", f"Status {response.status_code}: {response.text[:200]}"
    except Exception as e:
        return model_id, model_name, "error", f"Exception: {str(e)[:200]}"

async def run_complete_consensus():
    """Run the complete AI consensus with all available top models."""
    load_dotenv(dotenv_path=ENV_FILE)
    api_key = os.getenv("OPENROUTER_API_KEY_ALL_MODELS")

    if not api_key:
        print("❌ CRITICAL ERROR: Universal OpenRouter API key not found.")
        return

    # Get all top models
    top_models = get_all_top_models()
    print(f"🤖 Found {len(top_models)} top-tier AI models for consensus")

    # Create the comprehensive prompt
    prompt = """
You are a world-class financial systems auditor. Based on the Ultimate Lyra Trading System commissioning data:

SYSTEM STATUS:
- 3 trading systems operational (ports 8751, 9996, 8400)
- Performance: 100% success rate, <150ms latency, 700+ RPS throughput
- Security: Military-grade encryption, ISO 27001 compliant
- Financial controls: Never-sell-at-loss rule, $13,947.76 capital ready
- AI consensus: 5/7 models operational (71% success rate)
- Exchange connectivity: OKX healthy, Binance/Coinbase showing redirects

CRITICAL QUESTION: Should this system be activated for live trading with real capital?

Respond with exactly one word: **GO** or **NO-GO**

Then provide ONE sentence explaining the most critical factor in your decision.
"""

    # Query all models
    print("🚀 Querying ALL top-tier AI models...")
    async with httpx.AsyncClient() as client:
        # Use semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(10)
        
        async def worker(model_id, model_name):
            async with semaphore:
                return await query_model(client, model_id, model_name, api_key, prompt)
        
        tasks = [worker(model_id, model_name) for model_id, model_name in top_models]
        responses = await asyncio.gather(*tasks)

    # Process results
    go_votes = 0
    no_go_votes = 0
    successful_responses = 0
    
    report = "# COMPLETE AI CONSENSUS REPORT\n\n"
    report += f"**Total Models Queried:** {len(top_models)}\n"
    report += f"**Consensus Date:** $(date +'%Y-%m-%d %H:%M:%S')\n\n"
    report += "## Individual AI Verdicts\n\n"

    for model_id, model_name, status, content in responses:
        if status == "success":
            successful_responses += 1
            report += f"### {model_name} ({model_id})\n"
            report += f"**Response:** {content}\n\n"
            
            # Count votes
            if "NO-GO" in content.upper():
                no_go_votes += 1
            elif "GO" in content.upper():
                go_votes += 1
        else:
            report += f"### {model_name} ({model_id})\n"
            report += f"**Status:** ❌ FAILED - {content}\n\n"

    # Final verdict
    report += "---\n\n## FINAL CONSENSUS\n\n"
    report += f"**Successful Responses:** {successful_responses}/{len(top_models)} ({successful_responses/len(top_models)*100:.1f}%)\n"
    report += f"**GO Votes:** {go_votes}\n"
    report += f"**NO-GO Votes:** {no_go_votes}\n\n"

    if go_votes > no_go_votes:
        final_verdict = "**GO FOR LIVE DEPLOYMENT** ✅"
    elif no_go_votes > go_votes:
        final_verdict = "**NO-GO - CRITICAL ISSUES** ❌"
    else:
        final_verdict = "**INCONCLUSIVE - SPLIT DECISION** ⚠️"

    report += f"**FINAL VERDICT:** {final_verdict}\n"

    with open(FINAL_REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Complete AI Consensus Report saved to: {FINAL_REPORT_FILE}")
    print(f"🗳️ Final Verdict: {final_verdict}")

if __name__ == "__main__":
    asyncio.run(run_complete_consensus())
