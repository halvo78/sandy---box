"""
ULTIMATE AI VALIDATION - COMPLETE SYSTEM ALIGNMENT
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY===========
Uses OpenRouter's best paid AIs and Grok to validate the complete,
unified Ultimate Lyra Trading System for 100% alignment and readiness.
"""

import os
import json
import httpx
from datetime import datetime

# --- Configuration ---
API_URL = "https://openrouter.ai/api/v1/chat/completions"
VALIDATION_REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/ULTIMATE_AI_VALIDATION_REPORT.md"
UNIFIED_CONFIG_FILE = "/home/ubuntu/ultimate_lyra_v5/UNIFIED_SYSTEM_CONFIG.json"
INTEGRATION_REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/COMPLETE_INTEGRATION_REPORT.md"
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"

# --- AI Models for Consensus ---
AI_PANEL = [
    {"name": "Claude 3.5 Sonnet", "id": "anthropic/claude-3.5-sonnet"},
    {"name": "GPT-4o", "id": "openai/gpt-4o"},
    {"name": "Gemini 1.5 Flash", "id": "google/gemini-flash-1.5"},
    {"name": "Grok-1", "id": "xai/grok-1"},
    {"name": "Mistral Large", "id": "mistralai/mistral-large"},
    {"name": "Claude 3 Opus", "id": "anthropic/claude-3-opus"},
    {"name": "Qwen 2 72B", "id": "qwen/qwen-2-72b-instruct"}
]

def get_api_key():
    """Read the API key from the .env.production file"""
    try:
        with open(ENV_FILE, 'r') as f:
            for line in f:
                if line.startswith("OPENROUTER_API_KEY="):
                    return line.strip().split('=')[1]
    except FileNotFoundError:
        print(f"❌ WARNING: {ENV_FILE} not found. Using default key.")
    return "sk-or-v1-YOUR_OPENROUTER_API_KEY_HERE"

def run_ultimate_validation():
    """Main validation function"""
    print("🤖 STARTING ULTIMATE AI VALIDATION...")
    
    api_key = get_api_key()
    if not api_key:
        print("❌ CRITICAL ERROR: OpenRouter API key not found.")
        return

    # 1. Load all system data
    try:
        with open(UNIFIED_CONFIG_FILE, 'r') as f:
            unified_config = json.load(f)
        with open(INTEGRATION_REPORT_FILE, 'r') as f:
            integration_report = f.read()
    except FileNotFoundError as e:
        print(f"❌ CRITICAL ERROR: Missing data file - {e.filename}")
        return

    # 2. Create the master prompt
    master_prompt = create_master_prompt(unified_config, integration_report)
    
    # 3. Query the AI Panel
    ai_responses = []
    for model in AI_PANEL:
        print(f"🧠 Querying {model['name']}...")
        try:
            response = query_ai_model(model['id'], master_prompt, api_key)
            ai_responses.append({"model": model['name'], "response": response})
            print(f"   ✅ Response received.")
        except Exception as e:
            error_message = f"Failed to get response: {e}"
            ai_responses.append({"model": model['name'], "response": error_message})
            print(f"   ❌ {error_message}")

    # 4. Generate the final validation report
    generate_validation_report(ai_responses)
    
    print("✅ ULTIMATE AI VALIDATION FINISHED!")

def create_master_prompt(config, report):
    """Create the master prompt for the AI panel"""
    prompt = f"""
    **SYSTEM ANALYSIS & VALIDATION REQUEST**

    **CONTEXT:**
    You are a world-class AI systems architect and auditor. I have just completed a massive integration of a complex, AI-powered cryptocurrency trading ecosystem called the "Ultimate Lyra Trading System". This involved a deep forensic discovery of a user's Ubuntu system, identifying 10 active trading systems, and integrating 7 previously missing components into a single, unified sandbox environment. All documentation (82 files) has also been processed.

    **YOUR TASK:**
    Perform a final, definitive validation of the entire integrated system. Based on ALL the information provided below, I need your expert judgment on whether this system is **100% complete, aligned, and ready for production deployment with real capital**. Your final verdict must be a clear **"GO"** or **"NO-GO"**.

    **CRITERIA FOR "GO" VERDICT:**
    1.  **Completeness:** Are all 10 systems properly integrated? Is all documentation accounted for?
    2.  **Alignment:** Does the unified system accurately reflect the discovered components and user's intent?
    3.  **Functionality:** Based on the configuration, does the system appear fully functional and operational?
    4.  **Risk Assessment:** Are there any obvious red flags, security concerns, or operational risks?

    --- 

    **SYSTEM DATA FOR ANALYSIS:**

    **1. UNIFIED SYSTEM CONFIGURATION:**
    ```json
    {json.dumps(config, indent=2)}
    ```

    **2. COMPLETE INTEGRATION REPORT:**
    ```markdown
    {report}
    ```

    --- 

    **FINAL INSTRUCTIONS:**
    1.  Thoroughly analyze all the provided data.
    2.  Provide a concise summary of your findings, highlighting key strengths and critical weaknesses.
    3.  Conclude with your final, one-word verdict: **GO** or **NO-GO**.
    """
    return prompt

def query_ai_model(model_id, prompt, api_key):
    """Query a single AI model from OpenRouter"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    with httpx.Client(timeout=180.0) as client:
        response = client.post(API_URL, headers=headers, json=data)
        response.raise_for_status() # Raise an exception for bad status codes
        return response.json()["choices"][0]["message"]["content"]

def generate_validation_report(responses):
    """Generate the final validation report"""
    report = "# ULTIMATE AI VALIDATION REPORT\n\n"
    report += f"**Validation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += "This report contains the final validation and verdict from a panel of the world's best paid AI models on the completeness, alignment, and production readiness of the fully integrated Ultimate Lyra Trading System.\n\n"
    
    go_votes = 0
    no_go_votes = 0
    
    # --- AI Panel Verdicts ---
    report += "## 🤖 AI Panel Verdicts\n\n"
    for res in responses:
        report += f"### 🧠 {res['model']}\n\n"
        report += f"> {res['response'].strip()}\n\n"
        if "GO" in res['response'].upper() and "NO-GO" not in res['response'].upper():
            go_votes += 1
        elif "NO-GO" in res['response'].upper():
            no_go_votes += 1

    # --- Final Consensus ---
    report += "## 🎯 Final Consensus Verdict\n\n"
    report += f"**Total Votes:** {len(responses)}\n"
    report += f"- **GO Votes:** {go_votes}\n"
    report += f"- **NO-GO Votes:** {no_go_votes}\n\n"
    
    final_verdict = "INCONCLUSIVE"
    if go_votes > no_go_votes:
        final_verdict = "✅ GO FOR DEPLOYMENT"
    elif no_go_votes > go_votes:
        final_verdict = "❌ NO-GO - CRITICAL ISSUES IDENTIFIED"
    
    report += f"**FINAL VERDICT:** **{final_verdict}**\n\n"
    
    with open(VALIDATION_REPORT_FILE, 'w') as f:
        f.write(report)
    
    print(f"📋 Ultimate AI Validation Report saved to: {VALIDATION_REPORT_FILE}")

if __name__ == "__main__":
    run_ultimate_validation()

