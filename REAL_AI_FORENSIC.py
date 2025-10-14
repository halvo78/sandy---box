#!/usr/bin/env python3
import os, json, requests
from datetime import datetime
from pathlib import Path

api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    print("❌ OPENROUTER_API_KEY not found!")
    exit(1)

# Find real code files
code_files = {}
for path in ["/home/ubuntu/upload", "/home/ubuntu"]:
    for py_file in Path(path).glob("*.py"):
        if py_file.stat().st_size > 1000 and py_file.stat().st_size < 50000:
            code_files[str(py_file)] = py_file.read_text()[:3000]  # First 3000 chars
            if len(code_files) >= 5:
                break
    if len(code_files) >= 5:
        break

print(f"📂 Found {len(code_files)} code files")

# Prepare code for AI
code_summary = "\n\n".join([f"FILE: {p}\n```\n{c[:1000]}...\n```" for p, c in list(code_files.items())[:3]])

# AI models
models = [
    ("GPT-4 Turbo", "openai/gpt-4-turbo"),
    ("Claude 3.5 Sonnet", "anthropic/claude-3.5-sonnet"),
    ("Llama 3.3 70B", "meta-llama/llama-3.3-70b-instruct")
]

results = {}

for name, model_id in models:
    print(f"\n🤖 Analyzing with {name}...")
    
    try:
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model_id,
                "messages": [{
                    "role": "user",
                    "content": f"""Forensically analyze this trading system code. Be brutally honest.

CODE:
{code_summary}

Provide:
1. Critical Issues (bugs, errors)
2. Performance Problems
3. Security Concerns
4. Improvements Needed

Be specific and actionable."""
                }],
                "max_tokens": 2000
            },
            timeout=60
        )
        
        if resp.status_code == 200:
            ai_response = resp.json()["choices"][0]["message"]["content"]
            results[name] = {"status": "success", "response": ai_response}
            print(f"   ✅ Got response ({len(ai_response)} chars)")
        else:
            results[name] = {"status": "failed", "error": resp.text}
            print(f"   ❌ Failed: {resp.status_code}")
    
    except Exception as e:
        results[name] = {"status": "failed", "error": str(e)}
        print(f"   ❌ Error: {e}")

# Save results
Path("/home/ubuntu/REAL_AI_ANALYSIS.json").write_text(json.dumps(results, indent=2))
print(f"\n✅ Results saved to REAL_AI_ANALYSIS.json")

# Print summary
successful = sum(1 for r in results.values() if r["status"] == "success")
print(f"\n🎯 {successful}/{len(models)} AIs responded successfully")

if successful > 0:
    print("\n📊 AI FINDINGS:\n")
    for name, result in results.items():
        if result["status"] == "success":
            print(f"### {name}:")
            print(result["response"][:500] + "...")
            print()
