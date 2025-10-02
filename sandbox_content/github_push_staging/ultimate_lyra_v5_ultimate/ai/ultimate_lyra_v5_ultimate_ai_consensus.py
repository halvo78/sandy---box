"""
Ultimate Lyra Trading System - Final Commissioning: Ultimate AI Consensus
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY==================================
Synthesizes all commissioning reports and queries the most powerful paid AI models
for a definitive go/no-go recommendation on live trading.
"""

import os
import json
import asyncio
import httpx
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
FINAL_REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/ULTIMATE_COMMISSIONING_REPORT.md"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

# The most powerful paid models available
ULTIMATE_AI_PANEL = [
    "anthropic/claude-3.5-sonnet",
    "openai/gpt-4o",
    "google/gemini-1.5-pro",
    "mistralai/mistral-large",
    "anthropic/claude-3-opus",
    "xai/grok-1.5-flash", # Using a known valid Grok model
]

# All commissioning reports to be synthesized
COMMISSIONING_REPORTS = {
    "Phase 1: System Inspection": "/home/ubuntu/ultimate_lyra_v5/commissioning_phase1_report.md",
    "Phase 2: API Connectivity": "/home/ubuntu/ultimate_lyra_v5/commissioning_phase2_report.md",
    "Phase 3: AI Model Functionality": "/home/ubuntu/ultimate_lyra_v5/commissioning_phase3_definitive_report.md",
    "Phase 4: Financial Controls": "/home/ubuntu/ultimate_lyra_v5/commissioning_phase4_report.md",
    "Phase 5: Security & Compliance": "/home/ubuntu/ultimate_lyra_v5/commissioning_phase5_report.md",
    "Phase 6: Performance & Scalability": "/home/ubuntu/ultimate_lyra_v5/commissioning_phase6_report.md",
}

def read_report(file_path):
    """Read the content of a single report file."""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: Report file not found at {file_path}"

def synthesize_all_reports():
    """Combine all commissioning reports into a single comprehensive summary."""
    full_summary = """
# Comprehensive Commissioning Audit Summary for the Ultimate Lyra Trading System

This document contains the synthesized results of a 6-phase commissioning audit.
I need you to act as a panel of world-class system auditors and financial risk analysts.
Based *only* on the data provided below, provide a definitive one-word recommendation:
**GO** or **NO-GO** for activating this system for live trading with real capital.

Provide a single, concise paragraph justifying your decision, highlighting the most critical factor.
"""
    for phase_name, path in COMMISSIONING_REPORTS.items():
        full_summary += f"\n\n---\n\n## {phase_name}\n\n{read_report(path)}"
    return full_summary

async def query_ultimate_panel(client, model_name, api_key, prompt):
    """Query a single AI model from the ultimate panel."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = await client.post(f"{OPENROUTER_API_BASE}/chat/completions", headers=headers, json=data, timeout=120.0)
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            return model_name, "success", content
        else:
            return model_name, "error", f"API Error (Status: {response.status_code}): {response.text}"
    except Exception as e:
        return model_name, "error", f"An unexpected error occurred: {str(e)}"

async def generate_final_report():
    """Generate the ultimate commissioning report with the AI panel's verdict."""
    load_dotenv(dotenv_path=ENV_FILE)
    api_key = os.getenv("OPENROUTER_API_KEY_ALL_MODELS")

    if not api_key:
        final_report = "# ULTIMATE COMMISSIONING REPORT\n\n- ❌ **CRITICAL FAILURE:** The universal OpenRouter API key was not found."
        with open(FINAL_REPORT_FILE, "w") as f:
            f.write(final_report)
        print(f"📋 Ultimate commissioning failed. Report saved to: {FINAL_REPORT_FILE}")
        return

    # 1. Synthesize all data
    synthesized_prompt = synthesize_all_reports()

    # 2. Query the ultimate AI panel
    print("Querying the Ultimate AI Panel for a final verdict...")
    async with httpx.AsyncClient() as client:
        tasks = [query_ultimate_panel(client, model, api_key, synthesized_prompt) for model in ULTIMATE_AI_PANEL]
        responses = await asyncio.gather(*tasks)

    # 3. Collate and write the final report
    final_report = "# ULTIMATE COMMISSIONING REPORT: GO/NO-GO\n\n"
    final_report += f"**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    final_report += "**Verdict:** Pending\n\n"
    final_report += "## The Ultimate AI Consensus\n\nThis report represents the final judgment from a panel of the world's most advanced AI models on the production readiness of the Ultimate Lyra Trading System.\n\n"

    votes = {"GO": 0, "NO-GO": 0}
    for model, status, content in responses:
        final_report += f"### Verdict from: {model}\n"
        if status == "success":
            final_report += f"> {content}\n\n"
            if "NO-GO" in content.upper():
                votes["NO-GO"] += 1
            elif "GO" in content.upper():
                votes["GO"] += 1
        else:
            final_report += f"- **Status:** ❌ FAILED TO RESPOND\n"
            final_report += f"- **Details:** {content}\n\n"

    # Final Verdict
    final_verdict = "INCONCLUSIVE"
    if votes["GO"] > votes["NO-GO"]:
        final_verdict = "**GO** FOR LIVE DEPLOYMENT"
    elif votes["NO-GO"] > votes["GO"]:
        final_verdict = "**NO-GO** - CRITICAL ISSUES IDENTIFIED"
    elif votes["GO"] > 0 and votes["GO"] == votes["NO-GO"]:
        final_verdict = "**HUNG JURY** - SIGNIFICANT DISAGREEMENT"

    final_report += f"---\n\n## FINAL VERDICT: {final_verdict}\n\n"
    final_report += f"- **Vote Tally:** GO: {votes['GO']} | NO-GO: {votes['NO-GO']}\n"

    with open(FINAL_REPORT_FILE, "w") as f:
        f.write(final_report)

    print(f"📋 Ultimate Commissioning Report saved to: {FINAL_REPORT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_final_report())

