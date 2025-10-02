"""
Test script to verify the OpenRouter API key.
"""

import os
from openai import AsyncOpenAI

async def main():
    """Main function to test the OpenRouter API key."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY environment variable not set.")
        return

    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    try:
        models_response = await client.models.list()
        print("Successfully connected to OpenRouter. Available models:")
        for model in models_response.data:
            print(f"- {model.id}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
