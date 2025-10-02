#!/usr/bin/env python3
"""
Ultimate Lyra Trading System - Grok and OpenRouter AI Consensus Validation
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY==================================
Validates all fixes and system components using Grok and OpenRouter AI consensus.
"""

import os
import asyncio
import json
import datetime
import httpx
from typing import Dict, Any, List

# --- Configuration ---
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

# --- Models ---
GROK_MODEL = "huggingfaceh4/zephyr-7b-beta"
CONSENSUS_MODELS = [
    "google/gemini-pro",
    "mistralai/mistral-7b-instruct",
    "anthropic/claude-2",
]

# --- Files to Validate ---
FILES_TO_VALIDATE = [
    "/home/ubuntu/ultimate_lyra_v5/ULTIMATE_DASHBOARD_SIMPLE.py",
    "/home/ubuntu/ultimate_lyra_v5/iso_27001_compliance.md",
    "/home/ubuntu/ultimate_lyra_v5/performance_optimizer.py",
    "/home/ubuntu/ultimate_lyra_v5/production_config.py",
    "/home/ubuntu/ultimate_lyra_v5/.env.production",
    "/home/ubuntu/ultimate_lyra_v5/docker-compose.production.yml",
    "/home/ubuntu/ultimate_lyra_v5/nginx.conf",
    "/home/ubuntu/ultimate_lyra_v5/testing_framework.py",
    "/home/ubuntu/ultimate_lyra_v5/test_api_endpoints.py",
    "/home/ubuntu/ultimate_lyra_v5/test_trading_engine.py",
    "/home/ubuntu/ultimate_lyra_v5/test_security_monitoring.py",
    "/home/ubuntu/ultimate_lyra_v5/test_suite.py",
    "/home/ubuntu/ultimate_lyra_v5/MAXIMUM_AMPLIFICATION_SYSTEM.py",
    "/home/ubuntu/ultimate_lyra_v5/HUMMINGBOT_INTEGRATION_SYSTEM.py",
]

class AIValidator:
    """AI-powered validation using Grok and OpenRouter models."""

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key not provided.")
        self.api_key = api_key

    async def get_ai_feedback(self, model: str, prompt: str) -> Dict[str, Any]:
        """Get feedback from a specific AI model."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        print(f"Request Headers: {headers}")
        data = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert software engineer and security auditor. Your task is to review the provided code and configuration files for correctness, security vulnerabilities, and production readiness. Provide a detailed analysis and recommendations.",
                },
                {"role": "user", "content": prompt},
            ],
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{OPENROUTER_API_BASE}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=60.0,
                )
                response.raise_for_status()
                return {
                    "model": model,
                    "feedback": response.json()["choices"][0]["message"]["content"],
                }
            except httpx.HTTPStatusError as e:
                return {
                    "model": model,
                    "error": f"HTTP error: {e.response.status_code} - {e.response.text}",
                }
            except Exception as e:
                return {
                    "model": model,
                    "error": str(e),
                }

    async def run_validation(self) -> Dict[str, Any]:
        """Run the entire validation process."""
        file_contents = self._read_files()
        prompt = self._create_prompt(file_contents)

        # Get feedback from Grok
        grok_feedback = await self.get_ai_feedback(GROK_MODEL, prompt)

        # Get feedback from consensus models
        consensus_tasks = [self.get_ai_feedback(model, prompt) for model in CONSENSUS_MODELS]
        consensus_feedback = await asyncio.gather(*consensus_tasks)

        # Generate report
        report = await self._generate_report(grok_feedback, consensus_feedback)

        return report

    def _read_files(self) -> Dict[str, str]:
        """Read the contents of the files to be validated."""
        file_contents = {}
        for file_path in FILES_TO_VALIDATE:
            try:
                with open(file_path, "r") as f:
                    file_contents[file_path] = f.read()
            except FileNotFoundError:
                file_contents[file_path] = "File not found."
        return file_contents

    def _create_prompt(self, file_contents: Dict[str, str]) -> str:
        """Create the prompt for the AI models."""
        prompt = "Please review the following files for the Ultimate Lyra Trading System:\n\n"
        for file_path, content in file_contents.items():
            prompt += f"--- {file_path} ---\n{content}\n\n"
        prompt += "Please provide a detailed analysis and recommendations for each of the following areas:\n"
        prompt += "1. Correctness: Are there any bugs or logical errors?\n"
        prompt += "2. Security: Are there any security vulnerabilities?\n"
        prompt += "3. Production Readiness: Is the system ready for a production environment?\n"
        prompt += "4. ISO 27001 Compliance: Does the system meet the requirements of ISO 27001?\n"
        prompt += "5. Completeness: Are there any missing components or capabilities? Is the system absolutely complete?"
        return prompt

    async def _generate_report(self, grok_feedback: Dict[str, Any], consensus_feedback: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate the final validation report."""
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "grok_validation": grok_feedback,
            "consensus_validation": consensus_feedback,
            "summary": self._summarize_feedback(grok_feedback, consensus_feedback),
        }
        return report

    def _summarize_feedback(self, grok_feedback: Dict[str, Any], consensus_feedback: List[Dict[str, Any]]) -> str:
        """Summarize the feedback from all models."""
        summary = "## AI Consensus Summary\n\n"
        summary += "### Grok (Zephyr 7B Beta) Analysis\n"
        if "error" in grok_feedback:
            summary += f"Error: {grok_feedback['error']}\n"
        else:
            summary += grok_feedback['feedback'] + "\n"

        summary += "\n### Consensus Models Analysis\n"
        for feedback in consensus_feedback:
            summary += f"#### {feedback['model']}\n"
            if "error" in feedback:
                summary += f"Error: {feedback['error']}\n"
            else:
                summary += feedback['feedback'] + "\n"

        return summary

async def main():
    """Main function to run the validation."""
    print("🚀 Running Grok and OpenRouter AI Consensus Validation...")
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        validator = AIValidator(api_key=api_key)
        report = await validator.run_validation()

        with open("/home/ubuntu/ultimate_lyra_v5/validation_report.json", "w") as f:
            json.dump(report, f, indent=2)

        with open("/home/ubuntu/ultimate_lyra_v5/validation_report.md", "w") as f:
            f.write(report["summary"])

        print("📋 Validation report saved to: /home/ubuntu/ultimate_lyra_v5/validation_report.json")
        print("📋 Markdown report saved to: /home/ubuntu/ultimate_lyra_v5/validation_report.md")
        print("🎯 Validation completed successfully!")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())

