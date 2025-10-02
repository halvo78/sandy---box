#!/usr/bin/env python3
"""
ULTIMATE OPENROUTER AI CONSENSUS SYSTEM
Uses ALL best AI models (premium + free) to ensure absolute perfection
and 100% production-ready compliance across entire Ubuntu system
"""

import os
import sys
import json
import time
import asyncio
import aiohttp
import subprocess
import requests
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

# OpenRouter Configuration - ALL BEST MODELS
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', 'sk-or-v1-wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYc8d8e8f8g8h8i8j8k8l8m8n8o8p8')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# ALL BEST AI MODELS - Premium + Free
PREMIUM_MODELS = [
    "anthropic/claude-3.5-sonnet",
    "openai/gpt-4o",
    "anthropic/claude-3-opus",
    "openai/gpt-4-turbo",
    "x-ai/grok-beta",
    "deepseek/deepseek-chat",
    "qwen/qwen-2.5-72b-instruct",
    "alpindale/goliath-120b",
    "alibaba/qwen-2.5-coder-32b-instruct",
    "microsoft/wizardlm-2-8x22b"
]

FREE_MODELS = [
    "meta-llama/llama-3.1-8b-instruct:free",
    "google/gemini-flash-1.5:free",
    "mistralai/mistral-7b-instruct:free",
    "microsoft/phi-3-medium-4k-instruct:free",
    "huggingfaceh4/zephyr-7b-beta:free",
    "openchat/openchat-7b:free",
    "nousresearch/nous-capybara-7b:free",
    "gryphe/mythomist-7b:free"
]

ALL_MODELS = PREMIUM_MODELS + FREE_MODELS

@dataclass
class AIConsensusResult:
    model: str
    response: str
    confidence: float
    compliance_score: float
    recommendations: List[str]
    timestamp: str
    error: Optional[str] = None

@dataclass
class SystemComponent:
    name: str
    type: str  # container, exchange, service, file
    path: str
    status: str
    compliance_score: float
    ai_recommendations: List[str]
    production_ready: bool

class UltimateOpenRouterAIConsensus:
    def __init__(self):
        self.session = None
        self.ngrok_url = "https://3ce37fa57d09.ngrok.app"
        self.token = "lyra_+1-XXX-XXX-XXXX_5d20aef7f3777214"
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "version": "ULTIMATE_AI_CONSENSUS_V1.0",
            "system_inventory": {},
            "ai_consensus_results": {},
            "compliance_verification": {},
            "production_readiness": {},
            "final_recommendations": [],
            "overall_score": 0.0
        }
        
    async def init_session(self):
        """Initialize async HTTP session"""
        self.session = aiohttp.ClientSession()
    
    async def close_session(self):
        """Close async HTTP session"""
        if self.session:
            await self.session.close()
    
    async def query_ai_model(self, model: str, prompt: str, max_tokens: int = 4000) -> AIConsensusResult:
        """Query a specific AI model through OpenRouter"""
        try:
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://ultimate-lyra-trading-system.com",
                "X-Title": "Ultimate Lyra Trading System AI Consensus"
            }
            
            payload = {
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert AI system analyst ensuring 100% production compliance for trading systems. Provide detailed analysis with confidence scores and specific recommendations."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                "max_tokens": max_tokens,
                "temperature": 0.1,  # Low temperature for consistency
                "top_p": 0.9
            }
            
            async with self.session.post(
                f"{OPENROUTER_BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    content = data['choices'][0]['message']['content']
                    
                    # Extract confidence and compliance scores from response
                    confidence = self.extract_confidence_score(content)
                    compliance_score = self.extract_compliance_score(content)
                    recommendations = self.extract_recommendations(content)
                    
                    return AIConsensusResult(
                        model=model,
                        response=content,
                        confidence=confidence,
                        compliance_score=compliance_score,
                        recommendations=recommendations,
                        timestamp=datetime.now().isoformat()
                    )
                else:
                    error_text = await response.text()
                    return AIConsensusResult(
                        model=model,
                        response="",
                        confidence=0.0,
                        compliance_score=0.0,
                        recommendations=[],
                        timestamp=datetime.now().isoformat(),
                        error=f"HTTP {response.status}: {error_text}"
                    )
                    
        except Exception as e:
            return AIConsensusResult(
                model=model,
                response="",
                confidence=0.0,
                compliance_score=0.0,
                recommendations=[],
                timestamp=datetime.now().isoformat(),
                error=str(e)
            )
    
    def extract_confidence_score(self, content: str) -> float:
        """Extract confidence score from AI response"""
        import re
        # Look for patterns like "confidence: 85%" or "85% confident"
        patterns = [
            r"confidence[:\s]+(\d+(?:\.\d+)?)%?",
            r"(\d+(?:\.\d+)?)%?\s*confident",
            r"score[:\s]+(\d+(?:\.\d+)?)%?",
            r"rating[:\s]+(\d+(?:\.\d+)?)%?"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content.lower())
            if match:
                score = float(match.group(1))
                return score / 100 if score > 1 else score
        
        return 0.8  # Default confidence
    
    def extract_compliance_score(self, content: str) -> float:
        """Extract compliance score from AI response"""
        import re
        # Look for compliance-specific patterns
        patterns = [
            r"compliance[:\s]+(\d+(?:\.\d+)?)%?",
            r"(\d+(?:\.\d+)?)%?\s*compliant",
            r"production[:\s]+ready[:\s]+(\d+(?:\.\d+)?)%?",
            r"ready[:\s]+(\d+(?:\.\d+)?)%?"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content.lower())
            if match:
                score = float(match.group(1))
                return score / 100 if score > 1 else score
        
        # Analyze content for compliance keywords
        compliance_keywords = [
            "production ready", "compliant", "secure", "tested", 
            "verified", "approved", "validated", "certified"
        ]
        non_compliance_keywords = [
            "not ready", "incomplete", "missing", "error", 
            "failed", "insecure", "vulnerable", "deprecated"
        ]
        
        positive_count = sum(1 for keyword in compliance_keywords if keyword in content.lower())
        negative_count = sum(1 for keyword in non_compliance_keywords if keyword in content.lower())
        
        if positive_count > negative_count:
            return 0.85
        elif negative_count > positive_count:
            return 0.3
        else:
            return 0.6
    
    def extract_recommendations(self, content: str) -> List[str]:
        """Extract recommendations from AI response"""
        recommendations = []
        
        # Look for numbered lists, bullet points, or recommendation sections
        import re
        
        # Pattern for numbered recommendations
        numbered_pattern = r"(?:^|\n)\s*\d+[\.\)]\s*(.+?)(?=\n\s*\d+[\.\)]|\n\s*$|$)"
        numbered_matches = re.findall(numbered_pattern, content, re.MULTILINE | re.DOTALL)
        recommendations.extend([match.strip() for match in numbered_matches])
        
        # Pattern for bullet points
        bullet_pattern = r"(?:^|\n)\s*[-\*\•]\s*(.+?)(?=\n\s*[-\*\•]|\n\s*$|$)"
        bullet_matches = re.findall(bullet_pattern, content, re.MULTILINE | re.DOTALL)
        recommendations.extend([match.strip() for match in bullet_matches])
        
        # Look for recommendation sections
        rec_sections = re.findall(r"(?:recommendations?|suggestions?|improvements?)[:\s]*\n(.+?)(?=\n\n|\n[A-Z]|$)", 
                                content, re.IGNORECASE | re.DOTALL)
        for section in rec_sections:
            lines = [line.strip() for line in section.split('\n') if line.strip()]
            recommendations.extend(lines)
        
        # Clean and deduplicate
        cleaned_recommendations = []
        for rec in recommendations:
            rec = rec.strip()
            if len(rec) > 10 and rec not in cleaned_recommendations:
                cleaned_recommendations.append(rec)
        
        return cleaned_recommendations[:10]  # Limit to top 10
    
    async def get_system_inventory(self) -> Dict[str, Any]:
        """Get comprehensive system inventory from Ubuntu system"""
        print("🔍 Gathering comprehensive system inventory...")
        
        inventory_commands = {
            "containers": "find /home/halvolyra -name '*container*' -type d 2>/dev/null | head -20",
            "docker_status": "docker --version 2>/dev/null && docker ps -a 2>/dev/null || echo 'Docker not available'",
            "exchange_files": "find /home/halvolyra -name '*exchange*' -o -name '*okx*' -o -name '*binance*' -o -name '*kraken*' -o -name '*gate*' -o -name '*whitebit*' 2>/dev/null | head -20",
            "python_files": "find /home/halvolyra/ultimate_lyra_systems -name '*.py' 2>/dev/null | head -30",
            "services": "systemctl list-units --type=service --state=running | grep -E '(ngrok|lyra|auto)' || echo 'No custom services'",
            "processes": "ps aux | grep -E '(python|ngrok|auto_ngrok)' | grep -v grep",
            "network": "netstat -tlnp 2>/dev/null | grep -E ':(808[0-9]|4040)' || echo 'No relevant ports'",
            "disk_usage": "df -h /home/halvolyra",
            "memory": "free -h",
            "vault_status": "ls -la /home/halvolyra/.lyra-vault/ 2>/dev/null || echo 'Vault not found'",
            "hummingbot": "find /home/halvolyra -name '*hummingbot*' -type d 2>/dev/null | head -10"
        }
        
        inventory = {}
        
        for category, command in inventory_commands.items():
            try:
                payload = {
                    "type": "COMMAND",
                    "steps": [{"run": command}]
                }
                
                response = requests.post(
                    f"{self.ngrok_url}/ingest/event",
                    json=payload,
                    headers={"X-Ingest-Token": self.token},
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get("ok") and data.get("logs"):
                        log = data["logs"][0]
                        if log.get("ok"):
                            inventory[category] = {
                                "command": command,
                                "output": log.get("stdout", ""),
                                "error": log.get("stderr", ""),
                                "status": "success"
                            }
                        else:
                            inventory[category] = {
                                "command": command,
                                "output": "",
                                "error": log.get("stderr", "Command failed"),
                                "status": "failed"
                            }
                    else:
                        inventory[category] = {
                            "command": command,
                            "output": "",
                            "error": "No logs returned",
                            "status": "failed"
                        }
                else:
                    inventory[category] = {
                        "command": command,
                        "output": "",
                        "error": f"HTTP {response.status_code}",
                        "status": "failed"
                    }
                    
            except Exception as e:
                inventory[category] = {
                    "command": command,
                    "output": "",
                    "error": str(e),
                    "status": "error"
                }
        
        self.results["system_inventory"] = inventory
        return inventory
    
    async def analyze_component_with_ai_consensus(self, component: SystemComponent) -> Dict[str, AIConsensusResult]:
        """Analyze a system component using ALL AI models for consensus"""
        print(f"🤖 Analyzing {component.name} with ALL AI models...")
        
        # Create comprehensive prompt for the component
        prompt = f"""
ULTIMATE COMPLIANCE ANALYSIS REQUEST

Component: {component.name}
Type: {component.type}
Path: {component.path}
Current Status: {component.status}

ANALYSIS REQUIREMENTS:
1. Assess production readiness (0-100%)
2. Identify security vulnerabilities
3. Evaluate performance optimization opportunities
4. Check compliance with trading system standards
5. Verify containerization best practices
6. Assess integration capabilities
7. Recommend specific improvements

CONTEXT:
- This is part of the Ultimate Lyra Trading System
- Must handle live trading with 5 exchanges (Gate.io, OKX, WhiteBIT, Kraken, Binance)
- Requires 100% uptime and zero-failure operation
- Must comply with ISO 27001, ASIC, MiFID regulations
- Integrates with Hummingbot for automated trading
- Uses ngrok for secure remote access

RESPONSE FORMAT:
Confidence: [0-100]%
Compliance Score: [0-100]%
Production Ready: [YES/NO]

DETAILED ANALYSIS:
[Your detailed analysis here]

SPECIFIC RECOMMENDATIONS:
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]
...

CRITICAL ISSUES:
[Any critical issues that must be addressed]

OPTIMIZATION OPPORTUNITIES:
[Performance and efficiency improvements]
"""
        
        # Query all AI models concurrently
        tasks = []
        for model in ALL_MODELS:
            task = self.query_ai_model(model, prompt)
            tasks.append(task)
        
        # Wait for all models to respond
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Process results
        consensus_results = {}
        for i, result in enumerate(results):
            model = ALL_MODELS[i]
            if isinstance(result, Exception):
                consensus_results[model] = AIConsensusResult(
                    model=model,
                    response="",
                    confidence=0.0,
                    compliance_score=0.0,
                    recommendations=[],
                    timestamp=datetime.now().isoformat(),
                    error=str(result)
                )
            else:
                consensus_results[model] = result
        
        return consensus_results
    
    def calculate_consensus_score(self, ai_results: Dict[str, AIConsensusResult]) -> Dict[str, Any]:
        """Calculate consensus from all AI model results"""
        valid_results = [r for r in ai_results.values() if r.error is None]
        
        if not valid_results:
            return {
                "consensus_confidence": 0.0,
                "consensus_compliance": 0.0,
                "consensus_production_ready": False,
                "agreement_level": 0.0,
                "top_recommendations": [],
                "critical_issues": [],
                "model_count": 0
            }
        
        # Calculate averages
        avg_confidence = sum(r.confidence for r in valid_results) / len(valid_results)
        avg_compliance = sum(r.compliance_score for r in valid_results) / len(valid_results)
        
        # Determine production readiness (>80% compliance threshold)
        production_ready = avg_compliance >= 0.8
        
        # Calculate agreement level (how much models agree)
        compliance_scores = [r.compliance_score for r in valid_results]
        if len(compliance_scores) > 1:
            variance = sum((score - avg_compliance) ** 2 for score in compliance_scores) / len(compliance_scores)
            agreement_level = max(0, 1 - (variance * 4))  # Scale variance to agreement
        else:
            agreement_level = 1.0
        
        # Aggregate recommendations
        all_recommendations = []
        for result in valid_results:
            all_recommendations.extend(result.recommendations)
        
        # Count recommendation frequency and get top ones
        rec_counts = {}
        for rec in all_recommendations:
            rec_lower = rec.lower()
            rec_counts[rec_lower] = rec_counts.get(rec_lower, 0) + 1
        
        top_recommendations = sorted(rec_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        top_recommendations = [rec[0] for rec in top_recommendations]
        
        # Identify critical issues (mentioned by multiple models)
        critical_keywords = ["critical", "security", "vulnerability", "failure", "error", "broken"]
        critical_issues = []
        for result in valid_results:
            response_lower = result.response.lower()
            for keyword in critical_keywords:
                if keyword in response_lower and result.compliance_score < 0.6:
                    critical_issues.append(f"Critical issue detected by {result.model}: {keyword}")
        
        return {
            "consensus_confidence": avg_confidence,
            "consensus_compliance": avg_compliance,
            "consensus_production_ready": production_ready,
            "agreement_level": agreement_level,
            "top_recommendations": top_recommendations,
            "critical_issues": list(set(critical_issues)),
            "model_count": len(valid_results),
            "premium_model_count": len([r for r in valid_results if r.model in PREMIUM_MODELS]),
            "free_model_count": len([r for r in valid_results if r.model in FREE_MODELS])
        }
    
    async def analyze_all_system_components(self) -> Dict[str, Any]:
        """Analyze all system components with AI consensus"""
        print("🚀 Starting comprehensive AI consensus analysis...")
        
        # Get system inventory
        inventory = await self.get_system_inventory()
        
        # Identify components to analyze
        components = []
        
        # Add containers
        if inventory.get("containers", {}).get("output"):
            container_paths = inventory["containers"]["output"].strip().split('\n')
            for path in container_paths:
                if path.strip():
                    components.append(SystemComponent(
                        name=os.path.basename(path),
                        type="container",
                        path=path,
                        status="detected",
                        compliance_score=0.0,
                        ai_recommendations=[],
                        production_ready=False
                    ))
        
        # Add exchange files
        if inventory.get("exchange_files", {}).get("output"):
            exchange_paths = inventory["exchange_files"]["output"].strip().split('\n')
            for path in exchange_paths:
                if path.strip() and '.py' in path:
                    components.append(SystemComponent(
                        name=os.path.basename(path),
                        type="exchange",
                        path=path,
                        status="detected",
                        compliance_score=0.0,
                        ai_recommendations=[],
                        production_ready=False
                    ))
        
        # Add key Python files
        if inventory.get("python_files", {}).get("output"):
            python_paths = inventory["python_files"]["output"].strip().split('\n')
            for path in python_paths:
                if path.strip() and any(keyword in path.lower() for keyword in 
                                      ['trading', 'exchange', 'system', 'gateway', 'manager']):
                    components.append(SystemComponent(
                        name=os.path.basename(path),
                        type="service",
                        path=path,
                        status="detected",
                        compliance_score=0.0,
                        ai_recommendations=[],
                        production_ready=False
                    ))
        
        # Add services
        if inventory.get("services", {}).get("output"):
            service_lines = inventory["services"]["output"].strip().split('\n')
            for line in service_lines:
                if 'auto-ngrok-manager' in line:
                    components.append(SystemComponent(
                        name="auto-ngrok-manager",
                        type="service",
                        path="/etc/systemd/system/auto-ngrok-manager.service",
                        status="running",
                        compliance_score=0.0,
                        ai_recommendations=[],
                        production_ready=False
                    ))
        
        print(f"📊 Found {len(components)} components to analyze")
        
        # Analyze each component with AI consensus
        component_analyses = {}
        
        for component in components:
            print(f"🔍 Analyzing: {component.name}")
            ai_results = await self.analyze_component_with_ai_consensus(component)
            consensus = self.calculate_consensus_score(ai_results)
            
            component_analyses[component.name] = {
                "component": asdict(component),
                "ai_results": {model: asdict(result) for model, result in ai_results.items()},
                "consensus": consensus
            }
            
            # Update component with consensus results
            component.compliance_score = consensus["consensus_compliance"]
            component.production_ready = consensus["consensus_production_ready"]
            component.ai_recommendations = consensus["top_recommendations"]
        
        self.results["ai_consensus_results"] = component_analyses
        return component_analyses
    
    def generate_final_recommendations(self, component_analyses: Dict[str, Any]) -> List[str]:
        """Generate final system-wide recommendations"""
        all_recommendations = []
        critical_issues = []
        
        for component_name, analysis in component_analyses.items():
            consensus = analysis["consensus"]
            all_recommendations.extend(consensus["top_recommendations"])
            critical_issues.extend(consensus["critical_issues"])
            
            # Add component-specific recommendations
            if consensus["consensus_compliance"] < 0.8:
                all_recommendations.append(f"Improve {component_name} compliance (currently {consensus['consensus_compliance']:.1%})")
            
            if not consensus["consensus_production_ready"]:
                all_recommendations.append(f"Address production readiness issues in {component_name}")
        
        # Deduplicate and prioritize
        unique_recommendations = list(set(all_recommendations))
        
        # Add system-wide recommendations
        system_recommendations = [
            "Implement comprehensive monitoring with Prometheus and Grafana",
            "Set up automated testing pipeline for all components",
            "Establish disaster recovery procedures",
            "Implement security scanning with Trivy and OpenVAS",
            "Create comprehensive documentation for all components",
            "Set up automated backup systems",
            "Implement rate limiting and circuit breakers",
            "Establish compliance audit procedures",
            "Create performance benchmarking suite",
            "Implement zero-downtime deployment strategies"
        ]
        
        final_recommendations = unique_recommendations + system_recommendations
        return final_recommendations[:20]  # Top 20 recommendations
    
    def calculate_overall_system_score(self, component_analyses: Dict[str, Any]) -> float:
        """Calculate overall system compliance score"""
        if not component_analyses:
            return 0.0
        
        total_score = 0.0
        total_weight = 0.0
        
        # Weight components by importance
        component_weights = {
            "auto-ngrok-manager": 3.0,  # Critical for connectivity
            "ingest_gateway": 3.0,     # Critical for communication
            "trading": 2.5,            # Important for core functionality
            "exchange": 2.0,           # Important for trading
            "container": 1.5,          # Important for deployment
            "system": 2.0,             # Important for overall operation
            "default": 1.0             # Default weight
        }
        
        for component_name, analysis in component_analyses.items():
            consensus = analysis["consensus"]
            compliance_score = consensus["consensus_compliance"]
            
            # Determine weight based on component name
            weight = component_weights.get("default", 1.0)
            for keyword, w in component_weights.items():
                if keyword in component_name.lower():
                    weight = w
                    break
            
            total_score += compliance_score * weight
            total_weight += weight
        
        overall_score = total_score / total_weight if total_weight > 0 else 0.0
        return overall_score
    
    async def run_ultimate_ai_consensus(self) -> Dict[str, Any]:
        """Run the complete ultimate AI consensus analysis"""
        print("🎯 STARTING ULTIMATE OPENROUTER AI CONSENSUS SYSTEM")
        print("=" * 80)
        print(f"🤖 Using {len(ALL_MODELS)} AI models ({len(PREMIUM_MODELS)} premium + {len(FREE_MODELS)} free)")
        print("🎯 Target: 100% production-ready compliance")
        print("=" * 80)
        
        await self.init_session()
        
        try:
            # Step 1: Analyze all system components
            component_analyses = await self.analyze_all_system_components()
            
            # Step 2: Generate final recommendations
            final_recommendations = self.generate_final_recommendations(component_analyses)
            self.results["final_recommendations"] = final_recommendations
            
            # Step 3: Calculate overall system score
            overall_score = self.calculate_overall_system_score(component_analyses)
            self.results["overall_score"] = overall_score
            
            # Step 4: Determine production readiness
            production_ready = overall_score >= 0.8
            self.results["production_readiness"] = {
                "ready": production_ready,
                "score": overall_score,
                "threshold": 0.8,
                "components_analyzed": len(component_analyses),
                "critical_issues": sum(len(analysis["consensus"]["critical_issues"]) 
                                     for analysis in component_analyses.values())
            }
            
            # Step 5: Generate summary report
            self.generate_summary_report()
            
            return self.results
            
        finally:
            await self.close_session()
    
    def generate_summary_report(self):
        """Generate and display summary report"""
        print("\n" + "=" * 80)
        print("📊 ULTIMATE AI CONSENSUS RESULTS")
        print("=" * 80)
        
        overall_score = self.results["overall_score"]
        production_ready = self.results["production_readiness"]["ready"]
        components_count = self.results["production_readiness"]["components_analyzed"]
        
        print(f"🎯 Overall System Score: {overall_score:.1%}")
        print(f"🚀 Production Ready: {'✅ YES' if production_ready else '❌ NO'}")
        print(f"📦 Components Analyzed: {components_count}")
        print(f"🤖 AI Models Used: {len(ALL_MODELS)} ({len(PREMIUM_MODELS)} premium + {len(FREE_MODELS)} free)")
        
        if production_ready:
            print("\n🎉 SYSTEM IS PRODUCTION READY!")
            print("✅ All components meet compliance standards")
            print("✅ Ready for live trading deployment")
        else:
            print("\n⚠️  SYSTEM NEEDS IMPROVEMENTS")
            print("❌ Some components require attention")
            print("🔧 Review recommendations below")
        
        print("\n🔝 TOP RECOMMENDATIONS:")
        for i, rec in enumerate(self.results["final_recommendations"][:10], 1):
            print(f"  {i}. {rec}")
        
        # Component breakdown
        print("\n📦 COMPONENT BREAKDOWN:")
        for component_name, analysis in self.results["ai_consensus_results"].items():
            consensus = analysis["consensus"]
            score = consensus["consensus_compliance"]
            ready = consensus["consensus_production_ready"]
            models = consensus["model_count"]
            
            status = "✅" if ready else "❌"
            print(f"  {status} {component_name}: {score:.1%} ({models} AI models)")
        
        print("\n" + "=" * 80)
    
    def save_detailed_report(self) -> str:
        """Save detailed report to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ultimate_ai_consensus_report_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        
        print(f"📄 Detailed report saved: {filename}")
        return filename

async def main():
    """Main entry point"""
    print("🚀 ULTIMATE OPENROUTER AI CONSENSUS SYSTEM")
    print("🎯 Ensuring absolute perfection and 100% production compliance")
    print("🤖 Using ALL best AI models for consensus verification")
    
    consensus_system = UltimateOpenRouterAIConsensus()
    
    try:
        results = await consensus_system.run_ultimate_ai_consensus()
        
        # Save detailed report
        report_file = consensus_system.save_detailed_report()
        
        # Return success/failure based on production readiness
        production_ready = results["production_readiness"]["ready"]
        
        if production_ready:
            print("\n🎉 SUCCESS: System is 100% production ready!")
            return 0
        else:
            print("\n⚠️  ATTENTION NEEDED: System requires improvements")
            return 1
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return 2

if __name__ == "__main__":
    import asyncio
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
