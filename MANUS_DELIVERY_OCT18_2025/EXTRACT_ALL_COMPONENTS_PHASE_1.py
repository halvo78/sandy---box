#!/usr/bin/env python3
"""
PHASE 1: COMPREHENSIVE COMPONENT EXTRACTION AND CATALOGING
Extract and catalog ALL components from sandbox and GitHub repositories
for integration into the world's best trading system.
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class ComponentExtractor:
    def __init__(self):
        self.base_dir = Path("/home/ubuntu")
        self.results = {
            "extraction_timestamp": datetime.now().isoformat(),
            "sandbox_components": {},
            "github_repositories": {},
            "json_configs": [],
            "markdown_docs": [],
            "python_systems": [],
            "key_systems": {},
            "research_findings": {},
            "statistics": {}
        }
        
    def extract_sandbox_components(self):
        """Extract all components from sandbox"""
        print("=" * 80)
        print("EXTRACTING SANDBOX COMPONENTS")
        print("=" * 80)
        
        # Find all JSON config files
        json_files = list(self.base_dir.rglob("*.json"))
        self.results["json_configs"] = [
            {
                "path": str(f),
                "size": f.stat().st_size,
                "name": f.name
            }
            for f in json_files if f.is_file()
        ]
        print(f"✓ Found {len(self.results['json_configs'])} JSON configuration files")
        
        # Find all Markdown documentation
        md_files = list(self.base_dir.rglob("*.md"))
        self.results["markdown_docs"] = [
            {
                "path": str(f),
                "size": f.stat().st_size,
                "name": f.name
            }
            for f in md_files if f.is_file()
        ]
        print(f"✓ Found {len(self.results['markdown_docs'])} Markdown documentation files")
        
        # Find all Python systems
        py_files = list(self.base_dir.rglob("*.py"))
        self.results["python_systems"] = [
            {
                "path": str(f),
                "size": f.stat().st_size,
                "name": f.name,
                "lines": self._count_lines(f)
            }
            for f in py_files if f.is_file() and f.stat().st_size > 1000  # > 1KB
        ]
        print(f"✓ Found {len(self.results['python_systems'])} Python system files")
        
    def extract_key_systems(self):
        """Extract the key trading systems built so far"""
        print("\n" + "=" * 80)
        print("EXTRACTING KEY TRADING SYSTEMS")
        print("=" * 80)
        
        key_files = [
            "ULTIMATE_INTEGRATED_LYRA_SYSTEM.py",
            "UNIFIED_DATA_ENGINE.py",
            "PERFECT_BACKTESTING_ENGINE_V2.py",
            "COMPLETE_PRODUCTION_AUTOMATED_TRADING_SYSTEM.py",
            "ABSOLUTE_BEST_TRADING_SYSTEM_WORLD_CLASS_10_10.py",
            "PERFECT_10_COMPLETE_SYSTEM.py",
            "WORLDS_BEST_PAPER_TRADING_SYSTEM.py",
            "ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py",
            "ULTIMATE_AI_TRADING_SYSTEM_COMPLETE.py",
            "ULTIMATE_LYRA_COMPLETE_SYSTEM.py",
            "ULTIMATE_LYRA_FINAL.py",
            "ABSOLUTE_BEST_IN_WORLD_TRADING_SYSTEM.py"
        ]
        
        for filename in key_files:
            filepath = self.base_dir / filename
            if filepath.exists():
                self.results["key_systems"][filename] = {
                    "path": str(filepath),
                    "size": filepath.stat().st_size,
                    "lines": self._count_lines(filepath),
                    "exists": True
                }
                print(f"✓ Found: {filename} ({self._count_lines(filepath)} lines)")
            else:
                self.results["key_systems"][filename] = {
                    "exists": False
                }
                
    def extract_research_findings(self):
        """Extract research findings and documentation"""
        print("\n" + "=" * 80)
        print("EXTRACTING RESEARCH FINDINGS")
        print("=" * 80)
        
        research_files = [
            "ULTIMATE_FINDINGS_WORLDS_BEST.md",
            "100X_AMPLIFICATION_MASTER_PLAN.md",
            "COMPLETE_EXTRACTION_INTEGRATION_PLAN.md",
            "ULTIMATE_DEEP_RESEARCH_SYNTHESIS.md",
            "ULTIMATE_WORLD_CLASS_OPEN_SOURCE_ANALYSIS.md",
            "FREQTRADE_INTEGRATION_COMPLETE.md",
            "HUMMINGBOT_INTEGRATION_RESEARCH.md",
            "NAUTILUS_INSTITUTIONAL_FEATURES.md",
            "PORTFOLIO_RISK_LIBRARIES.md",
            "ALL_TRADING_STRATEGY_TYPES_COMPREHENSIVE.md"
        ]
        
        for filename in research_files:
            filepath = self.base_dir / filename
            if filepath.exists():
                self.results["research_findings"][filename] = {
                    "path": str(filepath),
                    "size": filepath.stat().st_size,
                    "exists": True
                }
                print(f"✓ Found: {filename}")
            else:
                self.results["research_findings"][filename] = {
                    "exists": False
                }
                
    def analyze_github_repos(self):
        """Analyze GitHub repositories"""
        print("\n" + "=" * 80)
        print("ANALYZING GITHUB REPOSITORIES")
        print("=" * 80)
        
        repos = [
            "halvo78/files-for-build",
            "halvo78/lyra-files",
            "halvo78/lyra-master-source",
            "halvo78/sandy---box"
        ]
        
        for repo in repos:
            repo_name = repo.split('/')[-1]
            repo_path = self.base_dir / repo_name
            
            if repo_path.exists():
                # Count Python files and lines
                py_files = list(repo_path.rglob("*.py"))
                total_lines = sum(self._count_lines(f) for f in py_files if f.is_file())
                
                self.results["github_repositories"][repo] = {
                    "path": str(repo_path),
                    "python_files": len(py_files),
                    "total_lines": total_lines,
                    "cloned": True
                }
                print(f"✓ {repo}: {len(py_files)} Python files, {total_lines:,} lines")
            else:
                self.results["github_repositories"][repo] = {
                    "cloned": False,
                    "needs_cloning": True
                }
                print(f"⚠ {repo}: Not cloned yet")
                
    def clone_missing_repos(self):
        """Clone any missing GitHub repositories"""
        print("\n" + "=" * 80)
        print("CLONING MISSING REPOSITORIES")
        print("=" * 80)
        
        for repo, info in self.results["github_repositories"].items():
            if not info.get("cloned", False):
                print(f"Cloning {repo}...")
                try:
                    result = subprocess.run(
                        ["gh", "repo", "clone", repo],
                        cwd=str(self.base_dir),
                        capture_output=True,
                        text=True,
                        timeout=120
                    )
                    if result.returncode == 0:
                        print(f"✓ Successfully cloned {repo}")
                        # Re-analyze after cloning
                        repo_name = repo.split('/')[-1]
                        repo_path = self.base_dir / repo_name
                        py_files = list(repo_path.rglob("*.py"))
                        total_lines = sum(self._count_lines(f) for f in py_files if f.is_file())
                        
                        info.update({
                            "path": str(repo_path),
                            "python_files": len(py_files),
                            "total_lines": total_lines,
                            "cloned": True
                        })
                    else:
                        print(f"✗ Failed to clone {repo}: {result.stderr}")
                except Exception as e:
                    print(f"✗ Error cloning {repo}: {e}")
                    
    def calculate_statistics(self):
        """Calculate overall statistics"""
        print("\n" + "=" * 80)
        print("CALCULATING STATISTICS")
        print("=" * 80)
        
        stats = {
            "total_json_configs": len(self.results["json_configs"]),
            "total_markdown_docs": len(self.results["markdown_docs"]),
            "total_python_files": len(self.results["python_systems"]),
            "total_python_lines": sum(f["lines"] for f in self.results["python_systems"]),
            "key_systems_found": sum(1 for s in self.results["key_systems"].values() if s.get("exists")),
            "research_docs_found": sum(1 for r in self.results["research_findings"].values() if r.get("exists")),
            "github_repos_cloned": sum(1 for r in self.results["github_repositories"].values() if r.get("cloned")),
            "github_total_lines": sum(r.get("total_lines", 0) for r in self.results["github_repositories"].values()),
            "github_total_files": sum(r.get("python_files", 0) for r in self.results["github_repositories"].values())
        }
        
        self.results["statistics"] = stats
        
        print(f"✓ Total JSON configs: {stats['total_json_configs']}")
        print(f"✓ Total Markdown docs: {stats['total_markdown_docs']}")
        print(f"✓ Total Python files (sandbox): {stats['total_python_files']}")
        print(f"✓ Total Python lines (sandbox): {stats['total_python_lines']:,}")
        print(f"✓ Key systems found: {stats['key_systems_found']}")
        print(f"✓ Research docs found: {stats['research_docs_found']}")
        print(f"✓ GitHub repos cloned: {stats['github_repos_cloned']}")
        print(f"✓ GitHub total files: {stats['github_total_files']}")
        print(f"✓ GitHub total lines: {stats['github_total_lines']:,}")
        
    def _count_lines(self, filepath):
        """Count lines in a file"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return sum(1 for _ in f)
        except:
            return 0
            
    def save_results(self):
        """Save extraction results"""
        output_file = self.base_dir / "PHASE_1_EXTRACTION_RESULTS.json"
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n✓ Results saved to: {output_file}")
        
        # Also create a summary markdown
        self.create_summary_markdown()
        
    def create_summary_markdown(self):
        """Create a human-readable summary"""
        stats = self.results["statistics"]
        
        summary = f"""# PHASE 1: COMPONENT EXTRACTION COMPLETE

**Extraction Date:** {self.results['extraction_timestamp']}

## Summary Statistics

- **JSON Configuration Files:** {stats['total_json_configs']}
- **Markdown Documentation:** {stats['total_markdown_docs']}
- **Python Files (Sandbox):** {stats['total_python_files']} ({stats['total_python_lines']:,} lines)
- **Key Trading Systems:** {stats['key_systems_found']} found
- **Research Documents:** {stats['research_docs_found']} found
- **GitHub Repositories:** {stats['github_repos_cloned']} cloned
- **GitHub Python Files:** {stats['github_total_files']}
- **GitHub Total Lines:** {stats['github_total_lines']:,}

## Total Code Base

**Combined Lines of Code:** {stats['total_python_lines'] + stats['github_total_lines']:,}

## Key Trading Systems Found

"""
        
        for name, info in self.results["key_systems"].items():
            if info.get("exists"):
                summary += f"- ✓ **{name}** ({info['lines']:,} lines)\n"
                
        summary += "\n## Research Documentation Found\n\n"
        
        for name, info in self.results["research_findings"].items():
            if info.get("exists"):
                summary += f"- ✓ **{name}**\n"
                
        summary += "\n## GitHub Repositories\n\n"
        
        for repo, info in self.results["github_repositories"].items():
            if info.get("cloned"):
                summary += f"- ✓ **{repo}** ({info['python_files']} files, {info['total_lines']:,} lines)\n"
            else:
                summary += f"- ⚠ **{repo}** (not cloned)\n"
                
        summary += "\n## Next Steps\n\n"
        summary += "1. Conduct full AI hive mind consultation for integration strategy\n"
        summary += "2. Begin Phase 2: Integrate existing code from repositories\n"
        summary += "3. Begin Phase 3: Integrate open source components\n"
        summary += "4. Apply 100X amplification optimizations\n"
        
        output_file = self.base_dir / "PHASE_1_EXTRACTION_SUMMARY.md"
        with open(output_file, 'w') as f:
            f.write(summary)
        print(f"✓ Summary saved to: {output_file}")
        
    def run(self):
        """Run complete extraction process"""
        print("\n" + "=" * 80)
        print("PHASE 1: COMPREHENSIVE COMPONENT EXTRACTION")
        print("Building the World's Best Algorithmic Trading System")
        print("=" * 80 + "\n")
        
        self.extract_sandbox_components()
        self.extract_key_systems()
        self.extract_research_findings()
        self.analyze_github_repos()
        self.clone_missing_repos()
        self.calculate_statistics()
        self.save_results()
        
        print("\n" + "=" * 80)
        print("PHASE 1 COMPLETE - READY FOR AI HIVE MIND CONSULTATION")
        print("=" * 80 + "\n")

if __name__ == "__main__":
    extractor = ComponentExtractor()
    extractor.run()

