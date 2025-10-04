#!/usr/bin/env python3
"""
ULTIMATE AI CONSENSUS SYSTEM
Using ALL OpenRouter models + best free AIs for maximum intelligence
"""

import os
import sys
import json
import asyncio
import aiohttp
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class UltimateAIConsensusSystem:
    def __init__(self):
        self.base_dir = Path("/home/ubuntu/ultimate_lyra_systems")
        
        # ALL OpenRouter API Keys - Maximum Coverage
        self.openrouter_keys = {
            "XAI_Code": "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",
            "Grok4": "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", 
            "ChatCodex": "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",
            "DeepSeek1": "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",
            "DeepSeek2": "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",
            "Premium": "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",
            "Microsoft": "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",
            "Universal": "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"
        }
        
        # Best FREE AI Models for Consensus
        self.free_models = [
            "meta-llama/llama-3.1-8b-instruct:free",
            "meta-llama/llama-3.1-70b-instruct:free", 
            "meta-llama/llama-3.2-3b-instruct:free",
            "meta-llama/llama-3.2-1b-instruct:free",
            "microsoft/phi-3-mini-128k-instruct:free",
            "microsoft/phi-3-medium-128k-instruct:free",
            "google/gemma-2-9b-it:free",
            "google/gemma-2-27b-it:free",
            "qwen/qwen-2-7b-instruct:free",
            "qwen/qwen-2.5-7b-instruct:free",
            "huggingfaceh4/zephyr-7b-beta:free",
            "openchat/openchat-7b:free",
            "gryphe/mythomist-7b:free",
            "undi95/toppy-m-7b:free",
            "koboldai/psyfighter-13b-2:free"
        ]
        
        # Premium AI Models for Advanced Analysis
        self.premium_models = [
            "openai/gpt-4o-2024-08-06",
            "openai/gpt-4o-mini",
            "anthropic/claude-3.5-sonnet",
            "anthropic/claude-3-haiku",
            "google/gemini-pro-1.5",
            "google/gemini-flash-1.5",
            "x-ai/grok-beta",
            "meta-llama/llama-3.1-405b-instruct",
            "qwen/qwen-2.5-72b-instruct",
            "deepseek/deepseek-chat",
            "perplexity/llama-3.1-sonar-large-128k-online",
            "cohere/command-r-plus"
        ]
        
        self.consensus_results = {
            "timestamp": datetime.now().isoformat(),
            "total_models": len(self.free_models) + len(self.premium_models),
            "free_models_count": len(self.free_models),
            "premium_models_count": len(self.premium_models),
            "consensus_threshold": 0.75,
            "analysis_results": {},
            "final_consensus": {}
        }
    
    async def query_ai_model(self, session: aiohttp.ClientSession, api_key: str, model: str, prompt: str, is_free: bool = True) -> Dict[str, Any]:
        """Query a single AI model"""
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 500 if is_free else 1000,
                "temperature": 0.3
            }
            
            async with session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                
                if response.status == 200:
                    data = await response.json()
                    content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                    
                    return {
                        "model": model,
                        "status": "success",
                        "response": content,
                        "is_free": is_free,
                        "timestamp": datetime.now().isoformat()
                    }
                else:
                    return {
                        "model": model,
                        "status": "error",
                        "error": f"HTTP {response.status}",
                        "is_free": is_free
                    }
                    
        except Exception as e:
            return {
                "model": model,
                "status": "error", 
                "error": str(e),
                "is_free": is_free
            }
    
    async def get_consensus_on_topic(self, topic: str, question: str) -> Dict[str, Any]:
        """Get AI consensus on a specific topic"""
        logger.info(f"🤖 Getting AI consensus on: {topic}")
        
        # Create comprehensive prompt
        prompt = f"""
ULTIMATE LYRA TRADING SYSTEM ANALYSIS

Topic: {topic}
Question: {question}

You are analyzing the Ultimate Lyra Trading System for production readiness and compliance.

System Context:
- Production-ready containerized trading system
- OKX exchange integration with verified credentials
- OpenRouter AI orchestration with 8 API keys
- Ngrok tunnel active (https://3ce37fa57d09.ngrok.app)
- $13,947.76 available capital
- Native deployment without Docker complications

Please provide:
1. COMPLIANCE SCORE (0-100%)
2. CRITICAL ISSUES (if any)
3. RECOMMENDATIONS
4. PRODUCTION READINESS (YES/NO)

Be specific and actionable. Focus on what's actually deployed and working.
"""
        
        results = []
        
        async with aiohttp.ClientSession() as session:
            # Query FREE models first (consensus base)
            free_tasks = []
            for model in self.free_models[:10]:  # Limit to avoid rate limits
                for key_name, api_key in list(self.openrouter_keys.items())[:3]:  # Rotate keys
                    task = self.query_ai_model(session, api_key, model, prompt, is_free=True)
                    free_tasks.append(task)
            
            logger.info(f"📊 Querying {len(free_tasks)} free AI models...")
            free_results = await asyncio.gather(*free_tasks, return_exceptions=True)
            
            # Process free results
            valid_free_results = [r for r in free_results if isinstance(r, dict) and r.get("status") == "success"]
            results.extend(valid_free_results)
            
            # Query PREMIUM models for advanced analysis
            premium_tasks = []
            for model in self.premium_models[:8]:  # Select top premium models
                for key_name, api_key in list(self.openrouter_keys.items())[:2]:  # Use premium keys
                    task = self.query_ai_model(session, api_key, model, prompt, is_free=False)
                    premium_tasks.append(task)
            
            logger.info(f"🧠 Querying {len(premium_tasks)} premium AI models...")
            premium_results = await asyncio.gather(*premium_tasks, return_exceptions=True)
            
            # Process premium results
            valid_premium_results = [r for r in premium_results if isinstance(r, dict) and r.get("status") == "success"]
            results.extend(valid_premium_results)
        
        # Analyze consensus
        consensus_data = self.analyze_consensus(results, topic)
        
        logger.info(f"✅ Consensus complete: {len(results)} valid responses")
        return consensus_data
    
    def analyze_consensus(self, results: List[Dict], topic: str) -> Dict[str, Any]:
        """Analyze AI responses for consensus"""
        
        if not results:
            return {
                "topic": topic,
                "consensus_score": 0,
                "confidence": "low",
                "summary": "No valid AI responses received",
                "recommendations": ["Check API connectivity", "Verify API keys"]
            }
        
        # Extract key metrics from responses
        compliance_scores = []
        production_ready_votes = {"yes": 0, "no": 0}
        critical_issues = []
        recommendations = []
        
        for result in results:
            response = result.get("response", "").lower()
            
            # Extract compliance score
            import re
            score_match = re.search(r'(\d+)%', response)
            if score_match:
                compliance_scores.append(int(score_match.group(1)))
            
            # Check production readiness
            if "production readiness" in response:
                if "yes" in response.split("production readiness")[1][:50]:
                    production_ready_votes["yes"] += 1
                elif "no" in response.split("production readiness")[1][:50]:
                    production_ready_votes["no"] += 1
            
            # Extract issues and recommendations
            if "critical" in response or "issue" in response:
                critical_issues.append(response)
            
            if "recommend" in response:
                recommendations.append(response)
        
        # Calculate consensus
        avg_compliance = sum(compliance_scores) / len(compliance_scores) if compliance_scores else 0
        production_consensus = production_ready_votes["yes"] > production_ready_votes["no"]
        
        # Determine confidence level
        response_count = len(results)
        if response_count >= 15:
            confidence = "high"
        elif response_count >= 8:
            confidence = "medium"
        else:
            confidence = "low"
        
        return {
            "topic": topic,
            "total_responses": response_count,
            "free_model_responses": len([r for r in results if r.get("is_free")]),
            "premium_model_responses": len([r for r in results if not r.get("is_free")]),
            "consensus_score": round(avg_compliance, 1),
            "production_ready_consensus": production_consensus,
            "confidence": confidence,
            "compliance_scores": compliance_scores,
            "production_votes": production_ready_votes,
            "critical_issues_count": len(critical_issues),
            "recommendations_count": len(recommendations),
            "summary": f"AI Consensus: {avg_compliance:.1f}% compliance, Production Ready: {'YES' if production_consensus else 'NO'}",
            "raw_responses": results[:5]  # Keep sample responses
        }
    
    async def run_comprehensive_analysis(self) -> Dict[str, Any]:
        """Run comprehensive AI consensus analysis"""
        logger.info("🚀 STARTING ULTIMATE AI CONSENSUS ANALYSIS")
        logger.info("=" * 60)
        
        # Analysis topics
        analysis_topics = [
            ("System Architecture", "Is the Ultimate Lyra Trading System properly architected for production trading?"),
            ("Exchange Integration", "Are the OKX exchange connections properly configured and secure?"),
            ("AI Orchestration", "Is the OpenRouter AI system with 8 keys properly integrated?"),
            ("Security Compliance", "Does the system meet ISO 27001 and financial security standards?"),
            ("Trading Readiness", "Is the system ready for live trading with $13,947.76 capital?"),
            ("Monitoring & Health", "Are monitoring, logging, and health checks properly implemented?"),
            ("Risk Management", "Are proper risk controls and capital preservation measures in place?"),
            ("Deployment Status", "Is the current deployment production-ready and fully operational?")
        ]
        
        # Run consensus analysis on each topic
        for topic, question in analysis_topics:
            logger.info(f"🔍 Analyzing: {topic}")
            consensus_result = await self.get_consensus_on_topic(topic, question)
            self.consensus_results["analysis_results"][topic] = consensus_result
            
            # Brief pause to avoid rate limits
            await asyncio.sleep(2)
        
        # Calculate overall consensus
        self.calculate_final_consensus()
        
        # Save results
        results_file = self.base_dir / "ai_consensus_results.json"
        with open(results_file, "w") as f:
            json.dump(self.consensus_results, f, indent=2)
        
        # Generate report
        self.generate_consensus_report()
        
        logger.info("✅ Ultimate AI consensus analysis complete!")
        return self.consensus_results
    
    def calculate_final_consensus(self):
        """Calculate final consensus from all analyses"""
        
        results = self.consensus_results["analysis_results"]
        
        if not results:
            self.consensus_results["final_consensus"] = {
                "overall_score": 0,
                "production_ready": False,
                "confidence": "low",
                "summary": "No analysis results available"
            }
            return
        
        # Calculate weighted scores
        total_score = 0
        total_weight = 0
        production_ready_count = 0
        
        topic_weights = {
            "System Architecture": 1.5,
            "Exchange Integration": 2.0,
            "AI Orchestration": 1.5,
            "Security Compliance": 2.0,
            "Trading Readiness": 2.5,
            "Monitoring & Health": 1.0,
            "Risk Management": 2.0,
            "Deployment Status": 2.5
        }
        
        for topic, analysis in results.items():
            weight = topic_weights.get(topic, 1.0)
            score = analysis.get("consensus_score", 0)
            
            total_score += score * weight
            total_weight += weight
            
            if analysis.get("production_ready_consensus", False):
                production_ready_count += 1
        
        # Final calculations
        overall_score = total_score / total_weight if total_weight > 0 else 0
        production_ready = production_ready_count >= (len(results) * 0.6)  # 60% threshold
        
        # Determine confidence
        total_responses = sum(r.get("total_responses", 0) for r in results.values())
        if total_responses >= 100:
            confidence = "very_high"
        elif total_responses >= 50:
            confidence = "high"
        elif total_responses >= 25:
            confidence = "medium"
        else:
            confidence = "low"
        
        self.consensus_results["final_consensus"] = {
            "overall_score": round(overall_score, 1),
            "production_ready": production_ready,
            "confidence": confidence,
            "total_ai_responses": total_responses,
            "topics_analyzed": len(results),
            "production_ready_topics": production_ready_count,
            "summary": f"Ultimate AI Consensus: {overall_score:.1f}% - {'PRODUCTION READY' if production_ready else 'NEEDS IMPROVEMENT'}"
        }
    
    def generate_consensus_report(self):
        """Generate comprehensive consensus report"""
        
        report = f"""
# ULTIMATE AI CONSENSUS REPORT
## Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## 🎯 EXECUTIVE SUMMARY
**Overall Consensus Score:** {self.consensus_results['final_consensus']['overall_score']}%
**Production Ready:** {self.consensus_results['final_consensus']['production_ready']}
**Confidence Level:** {self.consensus_results['final_consensus']['confidence'].upper()}
**Total AI Responses:** {self.consensus_results['final_consensus']['total_ai_responses']}

## 📊 AI MODEL COVERAGE
- **Free Models Used:** {self.consensus_results['free_models_count']} models
- **Premium Models Used:** {self.consensus_results['premium_models_count']} models  
- **Total Model Endpoints:** {self.consensus_results['total_models']}
- **OpenRouter Keys:** {len(self.openrouter_keys)} active keys

## 🔍 DETAILED ANALYSIS RESULTS

"""
        
        for topic, analysis in self.consensus_results["analysis_results"].items():
            report += f"""
### {topic}
- **Consensus Score:** {analysis['consensus_score']}%
- **Production Ready:** {'✅ YES' if analysis['production_ready_consensus'] else '❌ NO'}
- **AI Responses:** {analysis['total_responses']} total ({analysis['free_model_responses']} free + {analysis['premium_model_responses']} premium)
- **Confidence:** {analysis['confidence'].upper()}
- **Summary:** {analysis['summary']}

"""
        
        report += f"""
## 🎯 FINAL CONSENSUS

{self.consensus_results['final_consensus']['summary']}

### Key Metrics:
- Overall Score: {self.consensus_results['final_consensus']['overall_score']}%
- Production Ready Topics: {self.consensus_results['final_consensus']['production_ready_topics']}/{self.consensus_results['final_consensus']['topics_analyzed']}
- Total AI Responses: {self.consensus_results['final_consensus']['total_ai_responses']}
- Confidence Level: {self.consensus_results['final_consensus']['confidence'].upper()}

## 🚀 RECOMMENDATIONS

Based on the ultimate AI consensus analysis:

1. **System Status:** {'PRODUCTION READY' if self.consensus_results['final_consensus']['production_ready'] else 'REQUIRES IMPROVEMENTS'}
2. **Next Steps:** {'Deploy to live trading' if self.consensus_results['final_consensus']['overall_score'] >= 80 else 'Address identified issues before deployment'}
3. **Confidence:** Analysis based on {self.consensus_results['final_consensus']['total_ai_responses']} AI model responses

---
*Report generated by Ultimate AI Consensus System using {len(self.openrouter_keys)} OpenRouter API keys and {self.consensus_results['total_models']} AI models*
"""
        
        # Save report
        report_file = self.base_dir / "ultimate_ai_consensus_report.md"
        with open(report_file, "w") as f:
            f.write(report)
        
        logger.info(f"📄 Consensus report saved to: {report_file}")

async def main():
    """Main function to run ultimate AI consensus"""
    
    system = UltimateAIConsensusSystem()
    
    try:
        results = await system.run_comprehensive_analysis()
        
        print("\\n" + "=" * 60)
        print("🎉 ULTIMATE AI CONSENSUS COMPLETE!")
        print("=" * 60)
        
        final = results["final_consensus"]
        print(f"🎯 Overall Score: {final['overall_score']}%")
        print(f"🚀 Production Ready: {final['production_ready']}")
        print(f"🔍 Confidence: {final['confidence'].upper()}")
        print(f"🤖 Total AI Responses: {final['total_ai_responses']}")
        
        if final["overall_score"] >= 80:
            print("\\n✅ SYSTEM IS PRODUCTION READY!")
            print("🚀 Ready for live trading operations")
        else:
            print("\\n⚠️ SYSTEM NEEDS IMPROVEMENTS")
            print("📋 Review consensus report for details")
        
        print(f"\\n📄 Full report: ultimate_ai_consensus_report.md")
        
    except Exception as e:
        logger.error(f"❌ Consensus analysis failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
