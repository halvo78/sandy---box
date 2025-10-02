"""
Ultimate Lyra Trading System - Commissioning Audit Phase 3: AI Model Functionality
=================================================================================
Verifies the functionality of individual AI models and the consensus mechanism.
"""

import os
import json
import asyncio
import httpx
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/commissioning_phase3_report.md"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

# The 7 AI models integrated into the system
AI_MODELS = [
    "openai/gpt-4o",
    "anthropic/claude-3-opus",
    "google/gemini-pro",
    "meta-llama/llama-3-70b-instruct",
    "mistralai/mistral-large",
    "gryphe/mythomax-l2-13b",
    "xai/grok-1"
]

TEST_PROMPT = "Given the current market conditions for BTC/USDT, should I buy, sell, or hold? Provide a one-word answer and a brief justification."

async def query_ai_model(client, model_name, api_key):
    """Query a single AI model with the test prompt."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": TEST_PROMPT}]
    }
    try:
        response = await client.post(f"{OPENROUTER_API_BASE}/chat/completions", headers=headers, json=data, timeout=45.0)
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return model_name, "success", content
        else:
            return model_name, "error", f"API Error (Status: {response.status_code}): {response.text}"
    except httpx.RequestError as e:
        return model_name, "error", f"Connection Error ({e.__class__.__name__})"
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
    
    # Determine consensus
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
    """Generate the final verification report for Phase 3."""
    load_dotenv(dotenv_path=ENV_FILE)
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("API Key not found!")
        report = "# Commissioning Audit Phase 3: AI Model Functionality Report\n\n- ❌ **CRITICAL ERROR:** OPENAI_API_KEY not found in .env.production."
        with open(REPORT_FILE, "w") as f:
            f.write(report)
        print(f"📋 Phase 3 verification failed. Report saved to: {REPORT_FILE}")
        return
    else:
        print(f"API Key found: {api_key[:5]}...{api_key[-4:]}")

    report = "# Commissioning Audit Phase 3: AI Model Functionality Report\n\n"
    report += f"**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    report += "**Status:** In Progress\n\n"
    report += "## Individual AI Model Responses\n\n"

    async with httpx.AsyncClient() as client:
        tasks = [query_ai_model(client, model, api_key) for model in AI_MODELS]
        responses = await asyncio.gather(*tasks)

    for model, status, content in responses:
        report += f"### {model}\n"
        if status == "success":
            report += f"- **Status:** ✅ Success\n"
            report += f"- **Response:** {content}\n\n"
        else:
            report += f"- **Status:** ❌ Error\n"
            report += f"- **Details:** {content}\n\n"
    
    # Calculate and report consensus
    consensus, votes = calculate_consensus(responses)
    report += "## AI Consensus Mechanism Verification\n\n"
    report += f"- **Final Consensus:** **{consensus}**\n"
    report += f"- **Vote Tally:**\n"
    report += f"    - Buy: {votes['buy']}\n"
    report += f"    - Sell: {votes['sell']}\n"
    report += f"    - Hold: {votes['hold']}\n"

    with open(REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Phase 3 verification report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_report())

