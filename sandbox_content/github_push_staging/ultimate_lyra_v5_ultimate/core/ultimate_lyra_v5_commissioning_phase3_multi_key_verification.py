"""
Ultimate Lyra Trading System - Commissioning Audit Phase 3: Multi-Key AI Verification
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYwJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY=====
Verifies the functionality of all 8 AI models using their specific API keys.
"""

import os
import json
import asyncio
import httpx
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/commissioning_phase3_multi_key_report.md"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

# Map keys to their primary intended models
AI_KEY_MAPPING = {
    "OPENROUTER_API_KEY_XAI": "xai/grok-1",
    "OPENROUTER_API_KEY_GROK": "xai/grok-1", # Grok 4 is not a valid model ID
    "OPENROUTER_API_KEY_CODEX": "codex/codex-cushman-001", # Example, may need adjustment
    "OPENROUTER_API_KEY_DEEPSEEK1": "deepseek/deepseek-coder",
    "OPENROUTER_API_KEY_DEEPSEEK2": "deepseek/deepseek-llm",
    "OPENROUTER_API_KEY_PREMIUM": "openai/gpt-4o", # Premium key can test a premium model
    "OPENROUTER_API_KEY_MICROSOFT": "microsoft/phi-3-medium-128k-instruct",
    "OPENROUTER_API_KEY_UNIVERSAL": "google/gemini-flash-1.5", # Universal key tests another model
}

TEST_PROMPT = "What is the primary use case for this AI model? Respond in one sentence."

async def query_ai_model(client, key_name, model_name, api_key):
    """Query a single AI model with its specific key."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": TEST_PROMPT}]
    }
    try:
        response = await client.post(f"{OPENROUTER_API_BASE}/chat/completions", headers=headers, json=data, timeout=30.0)
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return key_name, model_name, "success", content
        else:
            return key_name, model_name, "error", f"API Error (Status: {response.status_code}): {response.text}"
    except Exception as e:
        return key_name, model_name, "error", f"An unexpected error occurred: {str(e)}"

async def generate_report():
    """Generate the final verification report for the multi-key test."""
    load_dotenv(dotenv_path=ENV_FILE)
    
    report = "# Commissioning Audit Phase 3: Multi-Key AI Verification Report\n\n"
    report += f"**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    report += "**Status:** In Progress\n\n"
    report += "## Individual AI Key & Model Responses\n\n"

    async with httpx.AsyncClient() as client:
        tasks = []
        for key_name, model_name in AI_KEY_MAPPING.items():
            api_key = os.getenv(key_name)
            if api_key:
                tasks.append(query_ai_model(client, key_name, model_name, api_key))
            else:
                report += f"### {key_name} ({model_name})\n- **Status:** ❌ SKIPPED (API Key not found in .env)\n\n"
        
        responses = await asyncio.gather(*tasks)

    success_count = 0
    for key_name, model_name, status, content in responses:
        report += f"### {key_name} ({model_name})\n"
        if status == "success":
            report += f"- **Status:** ✅ Success\n"
            report += f"- **Response:** {content}\n\n"
            success_count += 1
        else:
            report += f"- **Status:** ❌ Error\n"
            report += f"- **Details:** {content}\n\n"
    
    report += "## Summary\n\n"
    report += f"- **Total Keys Tested:** {len(responses)}\n"
    report += f"- **Successful Connections:** {success_count}\n"
    report += f"- **Failed Connections:** {len(responses) - success_count}\n"

    with open(REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Phase 3 Multi-Key verification report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_report())

