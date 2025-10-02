"""
Parse the list of OpenRouter models to find the correct IDs for Gemini and Grok.
"""

import json

MODELS_FILE = "/home/ubuntu/ultimate_lyra_v5/openrouter_models.json"

def find_ids():
    """Find and print the correct model IDs."""
    with open(MODELS_FILE, "r") as f:
        models = json.load(f)

    gemini_id = None
    grok_id = None

    for model in models["data"]:
        model_id = model["id"]
        if "google" in model_id and "gemini" in model_id and "pro" in model_id:
            gemini_id = model_id
        if "xai" in model_id and "grok" in model_id:
            grok_id = model_id

    print("--- Found Model IDs ---")
    if gemini_id:
        print(f"Gemini Pro ID: {gemini_id}")
    else:
        print("Gemini Pro ID not found.")

    if grok_id:
        print(f"Grok ID: {grok_id}")
    else:
        print("Grok ID not found.")

if __name__ == "__main__":
    find_ids()

