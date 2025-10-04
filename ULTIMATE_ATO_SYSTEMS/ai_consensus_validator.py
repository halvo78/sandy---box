#!/usr/bin/env python3
"""
AI Consensus Validation System for Ultimate Lyra Trading System
This script validates the AI consensus functionality using real OpenRouter API calls.
"""

import os
import json
import time
import requests
from datetime import datetime
from typing import Dict, List, Optional

class AIConsensusValidator:
    def __init__(self):
        """Initialize the AI Consensus Validator."""
        self.openrouter_keys = [
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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"
        ]
        
        self.models = [
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4o",
            "google/gemini-pro-1.5",
            "meta-llama/llama-3.1-70b-instruct",
            "mistralai/mistral-large",
            "qwen/qwen-2.5-72b-instruct",
            "deepseek/deepseek-chat",
            "x-ai/grok-beta"
        ]
        
        self.validation_results = []
        
    def test_single_model(self, api_key: str, model: str, test_prompt: str) -> Dict:
        """Test a single AI model with the given prompt."""
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert cryptocurrency trading AI. Respond with clear, actionable trading advice."
                    },
                    {
                        "role": "user",
                        "content": test_prompt
                    }
                ],
                "max_tokens": 300,
                "temperature": 0.7
            }
            
            start_time = time.time()
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result['choices'][0]['message']['content']
                
                return {
                    "model": model,
                    "status": "SUCCESS",
                    "response": ai_response,
                    "response_time": response_time,
                    "tokens_used": result.get('usage', {}).get('total_tokens', 0),
                    "error": None
                }
            else:
                return {
                    "model": model,
                    "status": "ERROR",
                    "response": None,
                    "response_time": response_time,
                    "tokens_used": 0,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
                
        except Exception as e:
            return {
                "model": model,
                "status": "ERROR",
                "response": None,
                "response_time": 0,
                "tokens_used": 0,
                "error": str(e)
            }
    
    def validate_api_keys(self) -> Dict:
        """Validate all OpenRouter API keys."""
        print("🔑 Validating OpenRouter API keys...")
        
        key_validation_results = []
        
        for i, api_key in enumerate(self.openrouter_keys):
            print(f"Testing API key {i+1}/8...")
            
            # Simple validation request
            test_result = self.test_single_model(
                api_key, 
                "openai/gpt-3.5-turbo",  # Use a basic model for validation
                "Hello, respond with 'API key working' if you can see this message."
            )
            
            key_validation_results.append({
                "key_index": i + 1,
                "key_prefix": api_key[:20] + "...",
                "status": test_result["status"],
                "error": test_result["error"]
            })
            
            if test_result["status"] == "SUCCESS":
                print(f"✅ API key {i+1}: Working")
            else:
                print(f"❌ API key {i+1}: {test_result['error']}")
            
            time.sleep(1)  # Rate limiting
        
        working_keys = sum(1 for result in key_validation_results if result["status"] == "SUCCESS")
        
        return {
            "total_keys": len(self.openrouter_keys),
            "working_keys": working_keys,
            "success_rate": working_keys / len(self.openrouter_keys),
            "details": key_validation_results
        }
    
    def test_ai_consensus(self, market_scenario: str) -> Dict:
        """Test AI consensus with a specific market scenario."""
        print(f"🤖 Testing AI consensus for scenario: {market_scenario}")
        
        test_prompt = f"""
        Market Scenario: {market_scenario}
        
        Current BTC data:
        - Price: $67,500
        - 24h Change: -2.3%
        - RSI: 32 (oversold)
        - Volume: Above average
        - MACD: Bullish divergence forming
        
        Provide a trading recommendation (BUY/SELL/HOLD) with confidence level (0-100%).
        Format your response as: "RECOMMENDATION: [BUY/SELL/HOLD], CONFIDENCE: [0-100]%, REASON: [brief explanation]"
        """
        
        consensus_results = []
        working_keys = 0
        
        for i, (api_key, model) in enumerate(zip(self.openrouter_keys, self.models)):
            if i >= len(self.openrouter_keys):
                break
                
            print(f"Getting opinion from {model}...")
            
            result = self.test_single_model(api_key, model, test_prompt)
            consensus_results.append(result)
            
            if result["status"] == "SUCCESS":
                working_keys += 1
                print(f"✅ {model}: {result['response'][:100]}...")
            else:
                print(f"❌ {model}: {result['error']}")
            
            time.sleep(2)  # Rate limiting between requests
        
        # Analyze consensus
        buy_votes = 0
        sell_votes = 0
        hold_votes = 0
        total_confidence = 0
        successful_responses = 0
        
        for result in consensus_results:
            if result["status"] == "SUCCESS" and result["response"]:
                response = result["response"].upper()
                if "BUY" in response:
                    buy_votes += 1
                elif "SELL" in response:
                    sell_votes += 1
                elif "HOLD" in response:
                    hold_votes += 1
                
                # Try to extract confidence
                try:
                    if "CONFIDENCE:" in response:
                        conf_part = response.split("CONFIDENCE:")[1].split("%")[0].strip()
                        confidence = float(conf_part.replace(",", ""))
                        total_confidence += confidence
                        successful_responses += 1
                except:
                    pass
        
        avg_confidence = total_confidence / successful_responses if successful_responses > 0 else 0
        
        # Determine consensus
        if buy_votes > sell_votes and buy_votes > hold_votes:
            consensus_action = "BUY"
        elif sell_votes > buy_votes and sell_votes > hold_votes:
            consensus_action = "SELL"
        else:
            consensus_action = "HOLD"
        
        return {
            "scenario": market_scenario,
            "total_models_tested": len(consensus_results),
            "successful_responses": successful_responses,
            "consensus_action": consensus_action,
            "votes": {
                "BUY": buy_votes,
                "SELL": sell_votes,
                "HOLD": hold_votes
            },
            "average_confidence": avg_confidence,
            "individual_results": consensus_results
        }
    
    def run_comprehensive_validation(self) -> Dict:
        """Run comprehensive validation of the AI consensus system."""
        print("🚀 Starting Comprehensive AI Consensus Validation...")
        print("="*60)
        
        validation_start = datetime.now()
        
        # Step 1: Validate API keys
        print("\n📋 Step 1: API Key Validation")
        key_validation = self.validate_api_keys()
        
        print(f"\n📊 API Key Validation Results:")
        print(f"✅ Working keys: {key_validation['working_keys']}/{key_validation['total_keys']}")
        print(f"📈 Success rate: {key_validation['success_rate']:.1%}")
        
        if key_validation['working_keys'] == 0:
            print("❌ No working API keys found. Cannot proceed with consensus testing.")
            return {
                "validation_timestamp": validation_start.isoformat(),
                "api_key_validation": key_validation,
                "consensus_tests": [],
                "overall_status": "FAILED - No working API keys"
            }
        
        # Step 2: Test AI consensus with different scenarios
        print("\n📋 Step 2: AI Consensus Testing")
        
        test_scenarios = [
            "BTC showing oversold conditions with potential reversal signals",
            "Strong bullish momentum in ETH with high volume breakout",
            "Market uncertainty with mixed signals across major cryptocurrencies"
        ]
        
        consensus_tests = []
        for scenario in test_scenarios:
            print(f"\n🔍 Testing scenario: {scenario}")
            test_result = self.test_ai_consensus(scenario)
            consensus_tests.append(test_result)
            
            print(f"📊 Consensus: {test_result['consensus_action']} "
                  f"(Confidence: {test_result['average_confidence']:.1f}%)")
            print(f"🗳️ Votes - BUY: {test_result['votes']['BUY']}, "
                  f"SELL: {test_result['votes']['SELL']}, "
                  f"HOLD: {test_result['votes']['HOLD']}")
        
        validation_end = datetime.now()
        validation_duration = (validation_end - validation_start).total_seconds()
        
        # Calculate overall success metrics
        total_successful_models = sum(test['successful_responses'] for test in consensus_tests)
        total_tested_models = sum(test['total_models_tested'] for test in consensus_tests)
        overall_success_rate = total_successful_models / total_tested_models if total_tested_models > 0 else 0
        
        # Determine overall status
        if key_validation['working_keys'] >= 4 and overall_success_rate >= 0.5:
            overall_status = "OPERATIONAL"
        elif key_validation['working_keys'] >= 2 and overall_success_rate >= 0.3:
            overall_status = "PARTIALLY_OPERATIONAL"
        else:
            overall_status = "DEGRADED"
        
        final_results = {
            "validation_timestamp": validation_start.isoformat(),
            "validation_duration_seconds": validation_duration,
            "api_key_validation": key_validation,
            "consensus_tests": consensus_tests,
            "overall_metrics": {
                "total_successful_models": total_successful_models,
                "total_tested_models": total_tested_models,
                "overall_success_rate": overall_success_rate,
                "working_api_keys": key_validation['working_keys']
            },
            "overall_status": overall_status
        }
        
        # Save results
        results_file = "/home/ubuntu/fresh_start/ai_consensus_validation_results.json"
        with open(results_file, 'w') as f:
            json.dump(final_results, f, indent=2)
        
        print("\n" + "="*60)
        print("🎉 AI CONSENSUS VALIDATION COMPLETE!")
        print("="*60)
        print(f"⏱️ Duration: {validation_duration:.1f} seconds")
        print(f"🔑 Working API keys: {key_validation['working_keys']}/{key_validation['total_keys']}")
        print(f"🤖 Model success rate: {overall_success_rate:.1%}")
        print(f"📊 Overall status: {overall_status}")
        print(f"💾 Results saved: {results_file}")
        print("="*60)
        
        return final_results

if __name__ == "__main__":
    validator = AIConsensusValidator()
    results = validator.run_comprehensive_validation()
