"""
Query OpenRouter for a list of all available models and save it to a file.
"""

import os
import json
import asyncio
import httpx
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
OUTPUT_FILE = "/home/ubuntu/ultimate_lyra_v5/openrouter_models.json"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

async def get_models(api_key):
    """Fetch the list of models from OpenRouter."""
    headers = {"Authorization": f"Bearer {api_key}"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{OPENROUTER_API_BASE}/models", headers=headers, timeout=30.0)
            if response.status_code == 200:
                models = response.json()
                with open(OUTPUT_FILE, "w") as f:
                    json.dump(models, f, indent=4)
                print(f"✅ Successfully fetched and saved {len(models['data'])} models to {OUTPUT_FILE}")
            else:
                print(f"❌ Error fetching models: Status {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    load_dotenv(dotenv_path=ENV_FILE)
    api_key = os.getenv("OPENROUTER_API_KEY_ALL_MODELS")
    if not api_key:
        print("❌ CRITICAL ERROR: OPENROUTER_API_KEY_ALL_MODELS not found.")
    else:
        asyncio.run(get_models(api_key))

