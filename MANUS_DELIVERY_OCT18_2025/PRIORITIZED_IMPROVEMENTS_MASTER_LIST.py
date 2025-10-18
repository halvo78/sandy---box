#!/usr/bin/env python3
"""
PRIORITIZED IMPROVEMENTS MASTER LIST

Analyze all 423,284 characters of expert wisdom to:
1. Extract ALL improvements
2. Categorize by domain
3. Rank by impact (CRITICAL, HIGH, MEDIUM, LOW)
4. Prioritize by SAFETY → PROFITABILITY → RELIABILITY
"""

import json
import re
from collections import defaultdict

def extract_improvements_from_text(text, role, focus_area):
    """Extract numbered improvements from expert text"""
    improvements = []
    
    # Find numbered items (1., 2., etc.)
    pattern = r'^\s*(\d+)\.\s*\*?\*?([^*\n]+)\*?\*?'
    matches = re.findall(pattern, text, re.MULTILINE)
    
    for num, title in matches:
        # Extract more context
        context_pattern = f"{num}\\..*?(?=\\n\\d+\\.|\\n\\n|$)"
        context_match = re.search(context_pattern, text, re.DOTALL)
        context = context_match.group(0) if context_match else title
        
        improvements.append({
            "number": int(num),
            "title": title.strip(),
            "context": context[:500],  # First 500 chars
            "role": role,
            "focus_area": focus_area
        })
    
    return improvements

def categorize_improvement(improvement):
    """Categorize improvement by domain and impact"""
    title = improvement["title"].lower()
    context = improvement["context"].lower()
    combined = title + " " + context
    
    # Determine domain
    domain = "OTHER"
    if any(word in combined for word in ["risk", "safety", "protect", "loss", "drawdown", "circuit"]):
        domain = "SAFETY & RISK"
    elif any(word in combined for word in ["profit", "alpha", "return", "sharpe", "strategy", "trading"]):
        domain = "PROFITABILITY"
    elif any(word in combined for word in ["reliability", "uptime", "failover", "redundancy", "monitoring"]):
        domain = "RELIABILITY"
    elif any(word in combined for word in ["ai", "ml", "model", "learning", "neural"]):
        domain = "AI/ML"
    elif any(word in combined for word in ["automation", "autonomous", "self-healing"]):
        domain = "AUTOMATION"
    elif any(word in combined for word in ["control", "interface", "dashboard", "user"]):
        domain = "CONTROL"
    elif any(word in combined for word in ["security", "compliance", "audit", "regulatory"]):
        domain = "SECURITY"
    
    # Determine impact level
    impact = "MEDIUM"
    if any(word in combined for word in ["critical", "essential", "must", "required", "catastrophic"]):
        impact = "CRITICAL"
    elif any(word in combined for word in ["high priority", "important", "significant", "major"]):
        impact = "HIGH"
    elif any(word in combined for word in ["low priority", "optional", "nice to have", "minor"]):
        impact = "LOW"
    
    # Determine priority score (1-100)
    priority_score = 50
    
    # Safety gets highest priority
    if domain == "SAFETY & RISK":
        priority_score += 30
    elif domain == "PROFITABILITY":
        priority_score += 20
    elif domain == "RELIABILITY":
        priority_score += 15
    
    # Impact level adjustment
    if impact == "CRITICAL":
        priority_score += 20
    elif impact == "HIGH":
        priority_score += 10
    elif impact == "LOW":
        priority_score -= 10
    
    improvement["domain"] = domain
    improvement["impact"] = impact
    improvement["priority_score"] = priority_score
    
    return improvement

def main():
    print("=" * 100)
    print("🎯 PRIORITIZING ALL 200+ IMPROVEMENTS")
    print("=" * 100)
    print("Analyzing 423,284 characters of expert wisdom...")
    print()
    
    all_improvements = []
    
    # Load all consultation results
    consultation_files = [
        "ULTIMATE_IMPROVEMENT_CONSULTATION_RESULTS.json",
        "1000X_DEEPER_CONSULTATION_RESULTS.json",
        "ULTIMATE_1000X_BETTER_RESULTS.json"
    ]
    
    for filename in consultation_files:
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                
            print(f"📄 Processing {filename}...")
            
            for result in data.get("results", []):
                if result.get("success"):
                    role = result.get("role", "Unknown")
                    focus_area = result.get("focus_area", "General")
                    response = result.get("response", "")
                    
                    improvements = extract_improvements_from_text(response, role, focus_area)
                    all_improvements.extend(improvements)
                    
                    if improvements:
                        print(f"   ✅ {role}: {len(improvements)} improvements found")
        
        except FileNotFoundError:
            print(f"   ⚠️  {filename} not found, skipping...")
            continue
    
    print()
    print(f"📊 Total improvements extracted: {len(all_improvements)}")
    print()
    
    # Categorize all improvements
    print("🔍 Categorizing and prioritizing...")
    categorized = [categorize_improvement(imp) for imp in all_improvements]
    
    # Sort by priority score (highest first)
    sorted_improvements = sorted(categorized, key=lambda x: x["priority_score"], reverse=True)
    
    # Group by domain and impact
    by_domain = defaultdict(list)
    by_impact = defaultdict(list)
    
    for imp in sorted_improvements:
        by_domain[imp["domain"]].append(imp)
        by_impact[imp["impact"]].append(imp)
    
    # Create prioritized master list
    output = {
        "total_improvements": len(sorted_improvements),
        "by_priority": sorted_improvements[:50],  # Top 50
        "by_domain": {domain: improvements for domain, improvements in by_domain.items()},
        "by_impact": {impact: len(improvements) for impact, improvements in by_impact.items()},
        "summary": {
            "critical": len(by_impact["CRITICAL"]),
            "high": len(by_impact["HIGH"]),
            "medium": len(by_impact["MEDIUM"]),
            "low": len(by_impact["LOW"])
        }
    }
    
    # Save to file
    with open("PRIORITIZED_IMPROVEMENTS_MASTER_LIST.json", "w") as f:
        json.dump(output, f, indent=2)
    
    # Print summary
    print()
    print("=" * 100)
    print("✅ PRIORITIZATION COMPLETE!")
    print("=" * 100)
    print()
    print("📊 IMPROVEMENTS BY IMPACT LEVEL:")
    print(f"   🔴 CRITICAL: {output['summary']['critical']}")
    print(f"   🟠 HIGH:     {output['summary']['high']}")
    print(f"   🟡 MEDIUM:   {output['summary']['medium']}")
    print(f"   🟢 LOW:      {output['summary']['low']}")
    print()
    print("📊 IMPROVEMENTS BY DOMAIN:")
    for domain, improvements in sorted(by_domain.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"   {domain}: {len(improvements)}")
    print()
    print("=" * 100)
    print("🎯 TOP 20 HIGHEST PRIORITY IMPROVEMENTS:")
    print("=" * 100)
    
    for i, imp in enumerate(sorted_improvements[:20], 1):
        impact_emoji = {
            "CRITICAL": "🔴",
            "HIGH": "🟠",
            "MEDIUM": "🟡",
            "LOW": "🟢"
        }
        
        print(f"\n{i}. {impact_emoji[imp['impact']]} [{imp['impact']}] {imp['title']}")
        print(f"   Domain: {imp['domain']}")
        print(f"   Priority Score: {imp['priority_score']}")
        print(f"   Expert: {imp['role']}")
    
    print()
    print("=" * 100)
    print(f"📄 Full list saved to: PRIORITIZED_IMPROVEMENTS_MASTER_LIST.json")
    print("=" * 100)

if __name__ == "__main__":
    main()

