#!/usr/bin/env python3
"""
Comprehensive AI-Powered Code Analyzer for Ultimate Lyra Trading System
Uses OpenRouter's best AI models to analyze, categorize, rate, and document the entire codebase.
"""

import os
import json
import subprocess
import time
from pathlib import Path
from collections import defaultdict
import hashlib

class UltimateLyraCodeAnalyzer:
    def __init__(self):
        self.codebase_path = "/home/ubuntu/github_push_staging"
        self.output_dir = "/home/ubuntu/ai_analysis_results"
        self.openrouter_keys = [
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # XAI Code
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Grok 4
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Chat Codex
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # DeepSeek
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # DeepSeek 2
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Multi-key
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER",  # Microsoft 4.0
            "sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER"   # All Models
        ]
        self.models = [
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4o",
            "google/gemini-pro-1.5",
            "meta-llama/llama-3.1-405b-instruct",
            "deepseek/deepseek-coder",
            "qwen/qwen-2.5-coder-32b-instruct"
        ]
        self.analysis_results = []
        self.file_categories = defaultdict(list)
        self.quality_ratings = defaultdict(list)
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_file_hash(self, file_path):
        """Generate a hash for the file to avoid duplicate analysis."""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return None
    
    def analyze_with_openrouter(self, file_path, content, model, api_key):
        """Analyze a file using OpenRouter API."""
        try:
            prompt = f"""
            You are an expert code analyst. Analyze this file from the Ultimate Lyra Trading System and provide a comprehensive analysis in JSON format.

            File: {file_path}
            Content:
            ```
            {content[:8000]}  # Limit content to avoid token limits
            ```

            Provide analysis in this exact JSON format:
            {{
                "file_path": "{file_path}",
                "category": "one of: Core Trading Logic, AI/ML Components, API Integration, Configuration, Documentation, Testing, Deployment, Security, Monitoring, Utilities, Data Processing, UI/Dashboard, Other",
                "subcategory": "specific subcategory within the main category",
                "summary": "concise 2-3 sentence summary of file purpose and functionality",
                "quality_rating": "integer from 1-10 for code quality, readability, and maintainability",
                "complexity_rating": "integer from 1-10 for code complexity",
                "importance_rating": "integer from 1-10 for importance to the overall system",
                "language": "programming language or file type",
                "lines_of_code": "estimated lines of code",
                "key_functions": ["list", "of", "key", "functions", "or", "features"],
                "dependencies": ["list", "of", "key", "dependencies", "or", "imports"],
                "suggestions": ["list", "of", "improvement", "suggestions"],
                "refactor_priority": "High/Medium/Low priority for refactoring",
                "documentation_status": "Excellent/Good/Fair/Poor/None",
                "test_coverage": "Excellent/Good/Fair/Poor/None/Unknown",
                "security_concerns": ["list", "of", "potential", "security", "issues"],
                "performance_notes": "notes about performance characteristics",
                "integration_points": ["list", "of", "system", "integration", "points"]
            }}
            """

            url = "https://openrouter.ai/api/v1/chat/completions"
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/halvo78/lyra-files",
                "X-Title": "Ultimate Lyra Trading System Analysis"
            }

            data = {
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 2000,
                "temperature": 0.1
            }

            response = subprocess.run(
                ['curl', '-s', '-X', 'POST', '-H', f'Authorization: Bearer {api_key}',
                 '-H', 'Content-Type: application/json', '-H', f'HTTP-Referer: https://github.com/halvo78/lyra-files',
                 '-H', 'X-Title: Ultimate Lyra Trading System Analysis',
                 '-d', json.dumps(data), url],
                capture_output=True,
                text=True
            )

            if response.returncode == 0:
                try:
                    result = json.loads(response.stdout)
                    if 'choices' in result and len(result['choices']) > 0:
                        content = result['choices'][0]['message']['content']
                        # Try to extract JSON from the response
                        if content.strip().startswith('{'):
                            return json.loads(content)
                        else:
                            # Look for JSON within the response
                            start = content.find('{')
                            end = content.rfind('}') + 1
                            if start != -1 and end != 0:
                                return json.loads(content[start:end])
                except json.JSONDecodeError:
                    pass
            
            return None

        except Exception as e:
            print(f"Error analyzing {file_path} with {model}: {e}")
            return None

    def analyze_file(self, file_path):
        """Analyze a single file using multiple AI models."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if not content.strip():
                return {
                    "file_path": file_path,
                    "category": "Empty File",
                    "summary": "This file is empty.",
                    "quality_rating": 0,
                    "analysis_method": "static"
                }

            # Use different models and keys for analysis
            for i, (model, api_key) in enumerate(zip(self.models, self.openrouter_keys)):
                result = self.analyze_with_openrouter(file_path, content, model, api_key)
                if result:
                    result["analysis_model"] = model
                    result["analysis_timestamp"] = time.time()
                    return result
                
                # Small delay between API calls
                time.sleep(0.5)

            # Fallback analysis if all AI models fail
            return self.fallback_analysis(file_path, content)

        except Exception as e:
            print(f"Error analyzing file {file_path}: {e}")
            return None

    def fallback_analysis(self, file_path, content):
        """Fallback analysis when AI models are unavailable."""
        file_ext = Path(file_path).suffix.lower()
        
        # Basic categorization based on file extension and path
        if any(x in file_path.lower() for x in ['trading', 'strategy', 'order', 'position']):
            category = "Core Trading Logic"
        elif any(x in file_path.lower() for x in ['ai', 'ml', 'model', 'neural']):
            category = "AI/ML Components"
        elif any(x in file_path.lower() for x in ['api', 'client', 'request']):
            category = "API Integration"
        elif file_ext in ['.json', '.yaml', '.yml', '.ini', '.conf']:
            category = "Configuration"
        elif file_ext in ['.md', '.txt', '.rst']:
            category = "Documentation"
        elif any(x in file_path.lower() for x in ['test', 'spec']):
            category = "Testing"
        elif any(x in file_path.lower() for x in ['deploy', 'docker', 'k8s']):
            category = "Deployment"
        elif any(x in file_path.lower() for x in ['security', 'auth', 'crypto']):
            category = "Security"
        elif any(x in file_path.lower() for x in ['monitor', 'log', 'metric']):
            category = "Monitoring"
        elif any(x in file_path.lower() for x in ['dashboard', 'ui', 'frontend']):
            category = "UI/Dashboard"
        else:
            category = "Other"

        return {
            "file_path": file_path,
            "category": category,
            "summary": f"File in {category} category",
            "quality_rating": 5,  # Default rating
            "analysis_method": "fallback",
            "file_size": len(content),
            "lines_of_code": len(content.split('\n'))
        }

    def scan_codebase(self):
        """Scan the entire codebase and analyze all files."""
        print("🔍 Starting comprehensive codebase analysis...")
        
        file_count = 0
        for root, _, files in os.walk(self.codebase_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_count += 1
                
                print(f"Analyzing ({file_count}): {file_path}")
                
                result = self.analyze_file(file_path)
                if result:
                    self.analysis_results.append(result)
                    
                    # Categorize results
                    category = result.get('category', 'Other')
                    self.file_categories[category].append(result)
                    
                    # Track quality ratings
                    rating = result.get('quality_rating', 0)
                    if isinstance(rating, (int, float)):
                        self.quality_ratings[category].append(rating)

        print(f"✅ Analysis complete! Processed {file_count} files.")

    def generate_comprehensive_report(self):
        """Generate a comprehensive analysis report."""
        report = {
            "analysis_metadata": {
                "total_files": len(self.analysis_results),
                "analysis_timestamp": time.time(),
                "analyzer_version": "1.0.0",
                "codebase_path": self.codebase_path
            },
            "category_summary": {},
            "quality_overview": {},
            "top_priority_files": [],
            "refactoring_recommendations": [],
            "security_findings": [],
            "detailed_analysis": self.analysis_results
        }

        # Generate category summary
        for category, files in self.file_categories.items():
            ratings = self.quality_ratings.get(category, [])
            avg_rating = sum(ratings) / len(ratings) if ratings else 0
            
            report["category_summary"][category] = {
                "file_count": len(files),
                "average_quality": round(avg_rating, 2),
                "files": [f["file_path"] for f in files[:10]]  # Top 10 files
            }

        # Generate quality overview
        all_ratings = [r for ratings in self.quality_ratings.values() for r in ratings]
        if all_ratings:
            report["quality_overview"] = {
                "overall_average": round(sum(all_ratings) / len(all_ratings), 2),
                "high_quality_files": len([r for r in all_ratings if r >= 8]),
                "medium_quality_files": len([r for r in all_ratings if 5 <= r < 8]),
                "low_quality_files": len([r for r in all_ratings if r < 5])
            }

        # Find high-priority files for refactoring
        high_priority = [f for f in self.analysis_results 
                        if f.get('refactor_priority') == 'High' or f.get('quality_rating', 0) < 4]
        report["top_priority_files"] = high_priority[:20]

        # Collect security findings
        security_issues = []
        for result in self.analysis_results:
            if result.get('security_concerns'):
                security_issues.extend(result['security_concerns'])
        report["security_findings"] = list(set(security_issues))

        return report

    def save_results(self):
        """Save all analysis results to files."""
        # Save comprehensive report
        report = self.generate_comprehensive_report()
        
        with open(os.path.join(self.output_dir, "comprehensive_analysis_report.json"), "w") as f:
            json.dump(report, f, indent=2)

        # Save categorized files
        with open(os.path.join(self.output_dir, "file_categories.json"), "w") as f:
            json.dump(dict(self.file_categories), f, indent=2, default=str)

        # Save detailed results
        with open(os.path.join(self.output_dir, "detailed_analysis.json"), "w") as f:
            json.dump(self.analysis_results, f, indent=2)

        print(f"📊 Results saved to {self.output_dir}/")
        print(f"📈 Analyzed {len(self.analysis_results)} files")
        print(f"📂 Found {len(self.file_categories)} categories")

def main():
    analyzer = UltimateLyraCodeAnalyzer()
    analyzer.scan_codebase()
    analyzer.save_results()
    
    print("\n🎯 ULTIMATE LYRA TRADING SYSTEM - AI ANALYSIS COMPLETE!")
    print("=" * 60)
    print("✅ Comprehensive codebase analysis finished")
    print("📊 Reports generated with AI-powered insights")
    print("🔧 Ready for refactoring and optimization")

if __name__ == "__main__":
    main()
