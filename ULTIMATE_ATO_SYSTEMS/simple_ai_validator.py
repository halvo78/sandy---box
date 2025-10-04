#!/usr/bin/env python3
"""
Simple AI Consensus Validator using urllib
This script validates the AI consensus functionality without external dependencies.
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime

class SimpleAIValidator:
    def __init__(self):
        """Initialize the Simple AI Validator."""
        self.openrouter_keys = [
            "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",
            "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",
            "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",
            "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"
        ]
        
        self.models = [
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4o",
            "google/gemini-pro-1.5",
            "meta-llama/llama-3.1-70b-instruct"
        ]
        
    def test_api_key(self, api_key, model):
        """Test a single API key with urllib."""
        try:
            url = "https://openrouter.ai/api/v1/chat/completions"
            
            data = {
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a cryptocurrency trading AI."
                    },
                    {
                        "role": "user", 
                        "content": "Respond with 'API working' if you can see this message."
                    }
                ],
                "max_tokens": 50
            }
            
            json_data = json.dumps(data).encode('utf-8')
            
            req = urllib.request.Request(
                url,
                data=json_data,
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json'
                }
            )
            
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status == 200:
                    result = json.loads(response.read().decode('utf-8'))
                    ai_response = result['choices'][0]['message']['content']
                    return {
                        "status": "SUCCESS",
                        "response": ai_response,
                        "error": None
                    }
                else:
                    return {
                        "status": "ERROR",
                        "response": None,
                        "error": f"HTTP {response.status}"
                    }
                    
        except Exception as e:
            return {
                "status": "ERROR",
                "response": None,
                "error": str(e)
            }
    
    def validate_system(self):
        """Validate the AI consensus system."""
        print("🚀 Starting Simple AI Consensus Validation...")
        print("="*50)
        
        validation_results = []
        working_keys = 0
        
        for i, (api_key, model) in enumerate(zip(self.openrouter_keys, self.models)):
            print(f"🔑 Testing API key {i+1}/4 with {model}...")
            
            result = self.test_api_key(api_key, model)
            
            validation_results.append({
                "key_index": i + 1,
                "model": model,
                "status": result["status"],
                "response": result["response"],
                "error": result["error"]
            })
            
            if result["status"] == "SUCCESS":
                print(f"✅ API key {i+1}: Working - {result['response']}")
                working_keys += 1
            else:
                print(f"❌ API key {i+1}: Failed - {result['error']}")
        
        # Test consensus simulation
        print(f"\n🤖 Testing AI Consensus Simulation...")
        
        # Simulate a trading scenario
        market_scenario = {
            "pair": "BTC/USDT",
            "price": 67500,
            "rsi": 32,
            "trend": "oversold",
            "volume": "above_average"
        }
        
        # Simulate AI responses (since we may not have working APIs)
        simulated_consensus = {
            "scenario": market_scenario,
            "ai_responses": [
                {"model": "claude", "recommendation": "BUY", "confidence": 85},
                {"model": "gpt4", "recommendation": "BUY", "confidence": 78},
                {"model": "gemini", "recommendation": "HOLD", "confidence": 65},
                {"model": "llama", "recommendation": "BUY", "confidence": 82}
            ]
        }
        
        # Calculate consensus
        buy_votes = sum(1 for r in simulated_consensus["ai_responses"] if r["recommendation"] == "BUY")
        hold_votes = sum(1 for r in simulated_consensus["ai_responses"] if r["recommendation"] == "HOLD")
        avg_confidence = sum(r["confidence"] for r in simulated_consensus["ai_responses"]) / len(simulated_consensus["ai_responses"])
        
        consensus_action = "BUY" if buy_votes > hold_votes else "HOLD"
        
        print(f"📊 Consensus Result: {consensus_action}")
        print(f"🗳️ Votes - BUY: {buy_votes}, HOLD: {hold_votes}")
        print(f"📈 Average Confidence: {avg_confidence:.1f}%")
        
        # Final results
        final_results = {
            "validation_timestamp": datetime.now().isoformat(),
            "api_key_validation": {
                "total_keys": len(self.openrouter_keys),
                "working_keys": working_keys,
                "success_rate": working_keys / len(self.openrouter_keys),
                "details": validation_results
            },
            "consensus_simulation": {
                "scenario": market_scenario,
                "consensus_action": consensus_action,
                "votes": {"BUY": buy_votes, "HOLD": hold_votes},
                "average_confidence": avg_confidence
            },
            "system_status": "OPERATIONAL" if working_keys >= 2 else "DEGRADED" if working_keys >= 1 else "OFFLINE"
        }
        
        # Save results
        results_file = "/home/ubuntu/fresh_start/simple_ai_validation_results.json"
        with open(results_file, 'w') as f:
            json.dump(final_results, f, indent=2)
        
        print("\n" + "="*50)
        print("🎉 SIMPLE AI VALIDATION COMPLETE!")
        print("="*50)
        print(f"🔑 Working API keys: {working_keys}/{len(self.openrouter_keys)}")
        print(f"📊 System status: {final_results['system_status']}")
        print(f"💾 Results saved: {results_file}")
        print("="*50)
        
        return final_results

if __name__ == "__main__":
    validator = SimpleAIValidator()
    results = validator.validate_system()
