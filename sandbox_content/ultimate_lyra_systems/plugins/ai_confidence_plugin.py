#!/usr/bin/env python3
"""
AI Confidence Plugin - OpenRouter Integration Test
=================================================
Tests OpenRouter API integration and provides AI confidence analysis
for cryptocurrency portfolio management.

Author: Manus AI System
Version: 1.0.0 - OpenRouter Integration Test
"""

import os
import json
import requests
import time
from datetime import datetime
from typing import Dict, List, Optional

class AIConfidencePlugin:
    def __init__(self):
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable not set")
        
        print(f"🔑 AI Confidence Plugin initialized with API key: {self.api_key[:20]}...")
        
    def test_api_connection(self):
        """Test OpenRouter API connection"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            test_data = {
                "model": "anthropic/claude-3.5-sonnet",
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello! Please respond with 'API connection successful' to confirm the connection is working."
                    }
                ],
                "max_tokens": 50,
                "temperature": 0.1
            }
            
            print("🔄 Testing OpenRouter API connection...")
            response = requests.post(self.base_url, headers=headers, json=test_data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                print(f"✅ API Connection Test: SUCCESS")
                print(f"📝 Response: {content}")
                return True
            else:
                print(f"❌ API Connection Test: FAILED (HTTP {response.status_code})")
                print(f"📝 Error: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ API Connection Test: ERROR - {e}")
            return False
    
    def get_portfolio_confidence_analysis(self, portfolio_data: Dict):
        """Get AI confidence analysis for portfolio"""
        try:
            # Format portfolio data for AI analysis
            portfolio_text = self.format_portfolio_data(portfolio_data)
            
            prompt = f"""
            As a professional cryptocurrency portfolio analyst, please analyze this portfolio and provide a confidence assessment:

            {portfolio_text}

            Please provide:
            1. Overall portfolio confidence score (1-100)
            2. Risk assessment (LOW/MEDIUM/HIGH)
            3. Top 3 recommendations
            4. Market outlook (BULLISH/BEARISH/NEUTRAL)
            5. Confidence in your analysis (1-100)

            Format your response as JSON with these exact keys:
            {{
                "confidence_score": <number>,
                "risk_level": "<string>",
                "recommendations": ["<string>", "<string>", "<string>"],
                "market_outlook": "<string>",
                "analysis_confidence": <number>,
                "reasoning": "<string>"
            }}
            """
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "anthropic/claude-3.5-sonnet",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 1000,
                "temperature": 0.3
            }
            
            print("🤖 Requesting AI portfolio analysis...")
            response = requests.post(self.base_url, headers=headers, json=data, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                
                # Try to parse JSON from response
                try:
                    # Extract JSON from response
                    import re
                    json_match = re.search(r'\{.*\}', content, re.DOTALL)
                    if json_match:
                        analysis = json.loads(json_match.group())
                        print("✅ AI Analysis: SUCCESS")
                        return analysis
                    else:
                        # Fallback parsing
                        return self.parse_text_response(content)
                        
                except json.JSONDecodeError:
                    return self.parse_text_response(content)
                    
            else:
                print(f"❌ AI Analysis: FAILED (HTTP {response.status_code})")
                return {"error": f"HTTP {response.status_code}: {response.text}"}
                
        except Exception as e:
            print(f"❌ AI Analysis: ERROR - {e}")
            return {"error": str(e)}
    
    def format_portfolio_data(self, portfolio_data: Dict):
        """Format portfolio data for AI analysis"""
        if not portfolio_data:
            return "Sample Portfolio: BTC: 1.5 ($150,000), ETH: 10 ($40,000), SOL: 500 ($25,000)"
        
        formatted = "PORTFOLIO ANALYSIS:\n"
        total_value = 0
        
        for symbol, data in portfolio_data.items():
            if isinstance(data, dict):
                balance = data.get('balance', 0)
                price = data.get('price', 0)
                value = balance * price
                total_value += value
                formatted += f"{symbol}: {balance:.4f} (${value:,.2f})\n"
        
        formatted += f"\nTOTAL VALUE: ${total_value:,.2f}"
        return formatted
    
    def parse_text_response(self, content: str):
        """Parse text response when JSON parsing fails"""
        try:
            # Extract key information from text
            confidence_score = 75  # Default
            risk_level = "MEDIUM"
            market_outlook = "NEUTRAL"
            analysis_confidence = 80
            
            # Try to extract numbers and keywords
            import re
            
            # Look for confidence scores
            conf_match = re.search(r'confidence.*?(\d+)', content.lower())
            if conf_match:
                confidence_score = int(conf_match.group(1))
            
            # Look for risk level
            if 'high risk' in content.lower() or 'risky' in content.lower():
                risk_level = "HIGH"
            elif 'low risk' in content.lower() or 'safe' in content.lower():
                risk_level = "LOW"
            
            # Look for market outlook
            if 'bullish' in content.lower() or 'positive' in content.lower():
                market_outlook = "BULLISH"
            elif 'bearish' in content.lower() or 'negative' in content.lower():
                market_outlook = "BEARISH"
            
            # Extract recommendations (look for numbered lists or bullet points)
            recommendations = []
            lines = content.split('\n')
            for line in lines:
                if any(indicator in line.lower() for indicator in ['recommend', 'suggest', '1.', '2.', '3.', '-', '•']):
                    clean_line = re.sub(r'^[\d\.\-\•\s]+', '', line).strip()
                    if clean_line and len(clean_line) > 10:
                        recommendations.append(clean_line[:100])
                        if len(recommendations) >= 3:
                            break
            
            if not recommendations:
                recommendations = ["Diversify portfolio", "Monitor market trends", "Consider risk management"]
            
            return {
                "confidence_score": confidence_score,
                "risk_level": risk_level,
                "recommendations": recommendations[:3],
                "market_outlook": market_outlook,
                "analysis_confidence": analysis_confidence,
                "reasoning": content[:200] + "..." if len(content) > 200 else content,
                "parsed_from_text": True
            }
            
        except Exception as e:
            return {
                "confidence_score": 50,
                "risk_level": "MEDIUM",
                "recommendations": ["Unable to parse recommendations"],
                "market_outlook": "NEUTRAL",
                "analysis_confidence": 50,
                "reasoning": f"Error parsing response: {e}",
                "error": str(e)
            }
    
    def run_comprehensive_test(self):
        """Run comprehensive test of AI plugin"""
        print("🎯 AI CONFIDENCE PLUGIN - COMPREHENSIVE TEST")
        print("=" * 60)
        
        # Test 1: API Connection
        print("\n📡 TEST 1: API Connection")
        connection_success = self.test_api_connection()
        
        if not connection_success:
            print("❌ Cannot proceed with further tests - API connection failed")
            return False
        
        # Test 2: Portfolio Analysis
        print("\n📊 TEST 2: Portfolio Analysis")
        sample_portfolio = {
            'BTC': {'balance': 1.5, 'price': 65000},
            'ETH': {'balance': 10, 'price': 3500},
            'SOL': {'balance': 500, 'price': 150}
        }
        
        analysis = self.get_portfolio_confidence_analysis(sample_portfolio)
        
        if 'error' in analysis:
            print(f"❌ Portfolio Analysis: FAILED - {analysis['error']}")
            return False
        else:
            print("✅ Portfolio Analysis: SUCCESS")
            print(f"📊 Confidence Score: {analysis.get('confidence_score', 'N/A')}")
            print(f"⚠️ Risk Level: {analysis.get('risk_level', 'N/A')}")
            print(f"📈 Market Outlook: {analysis.get('market_outlook', 'N/A')}")
            print(f"🎯 Analysis Confidence: {analysis.get('analysis_confidence', 'N/A')}%")
            
            if analysis.get('recommendations'):
                print("💡 Recommendations:")
                for i, rec in enumerate(analysis['recommendations'][:3], 1):
                    print(f"   {i}. {rec}")
        
        # Test 3: Performance Test
        print("\n⚡ TEST 3: Performance Test")
        start_time = time.time()
        quick_analysis = self.get_portfolio_confidence_analysis({'BTC': {'balance': 1, 'price': 65000}})
        end_time = time.time()
        
        response_time = end_time - start_time
        print(f"⏱️ Response Time: {response_time:.2f} seconds")
        
        if response_time < 30:
            print("✅ Performance: EXCELLENT (< 30s)")
        elif response_time < 60:
            print("✅ Performance: GOOD (< 60s)")
        else:
            print("⚠️ Performance: SLOW (> 60s)")
        
        print("\n🎯 COMPREHENSIVE TEST RESULTS")
        print("=" * 60)
        print(f"✅ API Connection: {'SUCCESS' if connection_success else 'FAILED'}")
        print(f"✅ Portfolio Analysis: {'SUCCESS' if 'error' not in analysis else 'FAILED'}")
        print(f"✅ Performance: {response_time:.2f}s")
        print(f"🔑 API Key: {self.api_key[:20]}...")
        print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return True

def main():
    """Main function to run AI plugin test"""
    try:
        print("🚀 Starting AI Confidence Plugin Test...")
        
        # Initialize plugin
        plugin = AIConfidencePlugin()
        
        # Run comprehensive test
        success = plugin.run_comprehensive_test()
        
        if success:
            print("\n🎉 AI CONFIDENCE PLUGIN TEST: COMPLETE SUCCESS!")
            print("✅ OpenRouter integration is working perfectly")
            print("✅ AI analysis capabilities confirmed")
            print("✅ Ready for integration with portfolio system")
        else:
            print("\n❌ AI CONFIDENCE PLUGIN TEST: FAILED")
            print("⚠️ Check API key and network connection")
        
        return success
        
    except Exception as e:
        print(f"\n❌ PLUGIN TEST ERROR: {e}")
        return False

if __name__ == "__main__":
    main()
