"""
Ultimate Lyra Trading System - Commissioning Audit Phase 3: Definitive AI Verification
=====================================================================================
Uses the new universal key to verify all 7 core AI models.
"""

import os
import json
import asyncio
import httpx
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/commissioning_phase3_definitive_report.md"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

# The 7 core AI models for the system
AI_MODELS = [
    "openai/gpt-4o",
    "anthropic/claude-3-opus",
    "google/gemini-pro", # Corrected model ID
    "meta-llama/llama-3-70b-instruct",
    "mistralai/mistral-large",
    "gryphe/mythomax-l2-13b",
    "xai/grok-1" # Corrected model ID
]

TEST_PROMPT = "Analyze the current BTC/USDT chart and provide a one-word trading signal (BUY, SELL, or HOLD) and a single sentence justification."

async def query_ai_model(client, model_name, api_key):
    """Query a single AI model with the universal key."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": TEST_PROMPT}]
    }
    try:
        response = await client.post(f"{OPENROUTER_API_BASE}/chat/completions", headers=headers, json=data, timeout=60.0)
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return model_name, "success", content
        else:
            return model_name, "error", f"API Error (Status: {response.status_code}): {response.text}"
    except Exception as e:
        return model_name, "error", f"An unexpected error occurred: {str(e)}"

def calculate_consensus(responses):
    """Calculate a simple consensus from the model responses."""
    votes = {"buy": 0, "sell": 0, "hold": 0}
    for _, status, content in responses:
        if status == "success":
            lower_content = content.lower()
            if "buy" in lower_content:
                votes["buy"] += 1
            elif "sell" in lower_content:
                votes["sell"] += 1
            elif "hold" in lower_content:
                votes["hold"] += 1
    
    if not any(votes.values()):
        return "Inconclusive (No valid votes)", votes

    max_votes = max(votes.values())
    winning_decisions = [decision for decision, count in votes.items() if count == max_votes]

    if len(winning_decisions) == 1:
        consensus = winning_decisions[0].upper()
    else:
        consensus = "Hung (No clear majority)"
        
    return consensus, votes

async def generate_report():
    """Generate the definitive verification report."""
    load_dotenv(dotenv_path=ENV_FILE)
    api_key = os.getenv("OPENROUTER_API_KEY_ALL_MODELS")

    if not api_key:
        report = "# Definitive AI Verification Report\n\n- ❌ **CRITICAL ERROR:** OPENROUTER_API_KEY_ALL_MODELS not found."
        with open(REPORT_FILE, "w") as f:
            f.write(report)
        print(f"📋 Definitive verification failed. Report saved to: {REPORT_FILE}")
        return

    report = "# Definitive AI Verification Report\n\n"
    report += f"**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    report += "**Status:** In Progress\n\n"
    report += "## Core AI Model Responses (Universal Key)\n\n"

    async with httpx.AsyncClient() as client:
        tasks = [query_ai_model(client, model, api_key) for model in AI_MODELS]
        responses = await asyncio.gather(*tasks)

    success_count = 0
    for model, status, content in responses:
        report += f"### {model}\n"
        if status == "success":
            report += f"- **Status:** ✅ Success\n"
            report += f"- **Response:** {content}\n\n"
            success_count += 1
        else:
            report += f"- **Status:** ❌ Error\n"
            report += f"- **Details:** {content}\n\n"
    
    consensus, votes = calculate_consensus(responses)
    report += "## AI Consensus Verification\n\n"
    report += f"- **Final Consensus:** **{consensus}**\n"
    report += f"- **Vote Tally:** Buy: {votes['buy']}, Sell: {votes['sell']}, Hold: {votes['hold']}\n"
    report += f"- **Success Rate:** {success_count}/{len(AI_MODELS)} ({success_count/len(AI_MODELS):.0%})\n"

    with open(REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Definitive AI verification report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_report())

