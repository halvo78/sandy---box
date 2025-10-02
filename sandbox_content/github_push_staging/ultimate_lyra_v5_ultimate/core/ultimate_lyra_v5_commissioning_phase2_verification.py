"""
Ultimate Lyra Trading System - Commissioning Audit Phase 2: API Connectivity
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY======================================
Verifies connectivity to all external APIs (Exchanges and AI Models).
"""

import os
import json
import asyncio
import httpx
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/commissioning_phase2_report.md"

EXCHANGES = {
    "OKX": "https://www.okx.com",
    "Binance": "https://api.binance.com",
    "Coinbase": "https://api.coinbase.com",
}

AI_SERVICES = {
    "OpenRouter": "https://openrouter.ai/api/v1",
}

async def check_api_connectivity(client, name, base_url, headers=None):
    """Check connectivity to a single API endpoint."""
    try:
        response = await client.get(base_url, headers=headers, timeout=10.0)
        # We are looking for a successful connection, not necessarily a 200 OK without auth
        if response.status_code < 500:
            return f"- ✅ **{name}:** Connected (Status: {response.status_code})\n"
        else:
            return f"- ❌ **{name}:** Connection Failed (Status: {response.status_code})\n"
    except httpx.RequestError as e:
        return f"- ❌ **{name}:** Connection Error ({e.__class__.__name__})\n"

def load_env():
    """Load environment variables from .env.production file."""
    load_dotenv(dotenv_path=ENV_FILE)

async def generate_report():
    """Generate the final verification report for Phase 2."""
    load_env()
    report = "# Commissioning Audit Phase 2: API Connectivity Report\n\n"
    report += f"**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    report += "**Status:** In Progress\n\n"

    async with httpx.AsyncClient() as client:
        # Verify Exchange APIs
        report += "### Exchange API Connectivity\n\n"
        exchange_tasks = []
        for name, url in EXCHANGES.items():
            # Specific endpoint checks would require authentication setup, 
            # for now, we check the base URL reachability.
            exchange_tasks.append(check_api_connectivity(client, name, url))
        results = await asyncio.gather(*exchange_tasks)
        for result in results:
            report += result

        # Verify AI Service APIs
        report += "\n### AI Service API Connectivity\n\n"
        ai_tasks = []
        for name, url in AI_SERVICES.items():
            api_key = os.getenv("OPENAI_API_KEY") # Assuming this key is for OpenRouter
            headers = {"Authorization": f"Bearer {api_key}"}
            # Checking a simple endpoint like models list
            ai_tasks.append(check_api_connectivity(client, name, f"{url}/models", headers=headers))
        results = await asyncio.gather(*ai_tasks)
        for result in results:
            report += result

    with open(REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Phase 2 verification report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_report())

