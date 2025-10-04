#!/usr/bin/env python3
"""
ULTIMATE AI CONSENSUS EVERYTHING CONTAINERIZER
Every single component gets its own perfect container with 100% AI validation
"""

import os
import logging
import json
import shutil
import subprocess
from datetime import datetime
import requests
from pathlib import Path
import yaml
import docker
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class UltimateAIConsensusContainerizer:
    def __init__(self):
        """TODO: Add function documentation"""
        self.openrouter_keys = [
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # XAI Code
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Grok 4
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Chat Codex
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # DeepSeek
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # DeepSeek 2
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Multi-key
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Microsoft 4.0
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"   # All Models
        ]
        
        self.ai_models = [
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4-turbo", 
            "openai/gpt-4o",
            "google/gemini-pro-1.5",
            "google/gemini-flash-1.5",
            "meta-llama/llama-3.1-405b-instruct",
            "anthropic/claude-3-opus",
            "deepseek/deepseek-coder",
            "qwen/qwen-2.5-coder-32b-instruct",
            "microsoft/wizardlm-2-8x22b",
            "cohere/command-r-plus",
            "mistralai/mixtral-8x7b-instruct"
        ]
        
        self.base_dir = "/home/ubuntu"
        self.containers_dir = "/home/ubuntu/ULTIMATE_CONTAINERS"
        self.production_dir = "/home/ubuntu/PRODUCTION_READY_CONTAINERS"
        self.testing_dir = "/home/ubuntu/CONTAINER_TESTING"
        
        # Container categories - EVERYTHING gets containerized
        self.container_types = {
            "API_CONTAINERS": {
                "openrouter_ai": "OpenRouter AI integration container",
                "coinbase_api": "Coinbase exchange API container", 
                "okx_api": "OKX exchange API container",
                "binance_api": "Binance exchange API container",
                "gate_io_api": "Gate.io exchange API container",
                "polygon_api": "Polygon market data API container",
                "coingecko_api": "CoinGecko market data API container",
                "messari_api": "Messari crypto data API container",
                "dune_analytics": "Dune Analytics API container",
                "defillama_api": "DefiLlama DeFi data API container"
            },
            "TRADING_CONTAINERS": {
                "portfolio_manager": "Portfolio management engine container",
                "risk_manager": "Risk management system container",
                "strategy_engine": "Trading strategy execution container",
                "arbitrage_engine": "Arbitrage detection and execution container",
                "market_maker": "Market making strategy container",
                "momentum_trader": "Momentum trading strategy container",
                "mean_reversion": "Mean reversion strategy container",
                "breakout_trader": "Breakout trading strategy container"
            },
            "AI_CONTAINERS": {
                "consensus_engine": "AI consensus decision engine container",
                "sentiment_analyzer": "Market sentiment analysis container",
                "price_predictor": "AI price prediction container",
                "pattern_detector": "Technical pattern detection container",
                "news_analyzer": "News sentiment analysis container",
                "social_analyzer": "Social media sentiment container",
                "fear_greed_index": "Fear & Greed index calculator container",
                "volatility_predictor": "Volatility prediction container"
            },
            "DATA_CONTAINERS": {
                "price_feed": "Real-time price data container",
                "orderbook_manager": "Order book data container",
                "trade_history": "Historical trade data container",
                "market_data": "Market statistics container",
                "volume_analyzer": "Volume analysis container",
                "liquidity_tracker": "Liquidity tracking container",
                "correlation_analyzer": "Asset correlation container",
                "volatility_tracker": "Volatility tracking container"
            },
            "SECURITY_CONTAINERS": {
                "vault_manager": "Secure credential vault container",
                "encryption_service": "Encryption/decryption service container",
                "auth_manager": "Authentication service container",
                "firewall_manager": "Security firewall container",
                "audit_logger": "Security audit logging container",
                "compliance_checker": "Regulatory compliance container",
                "key_rotator": "API key rotation service container",
                "intrusion_detector": "Security intrusion detection container"
            },
            "INFRASTRUCTURE_CONTAINERS": {
                "load_balancer": "Load balancing service container",
                "message_queue": "Message queue service container",
                "cache_manager": "Caching service container",
                "database_manager": "Database management container",
                "backup_service": "Backup and recovery container",
                "monitoring_service": "System monitoring container",
                "logging_service": "Centralized logging container",
                "health_checker": "Health check service container"
            },
            "UTILITY_CONTAINERS": {
                "data_validator": "Data validation service container",
                "format_converter": "Data format conversion container",
                "notification_service": "Alert notification container",
                "scheduler_service": "Task scheduling container",
                "file_manager": "File management service container",
                "config_manager": "Configuration management container",
                "version_manager": "Version control service container",
                "deployment_manager": "Deployment automation container"
            }
        }
        
        self.consensus_threshold = 0.85  # 85% AI consensus required
        self.max_iterations = 10  # Maximum test-add-test cycles per container

    def query_openrouter_ai(self, prompt, model_index=0):
        """Query OpenRouter AI with error handling"""
        try:
            api_key = self.openrouter_keys[model_index % len(self.openrouter_keys)]
            model = self.ai_models[model_index % len(self.ai_models)]
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/halvo78/lyra-master-source",
                "X-Title": "Ultimate Lyra Trading System"
            }
            
            data = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 3000,
                "temperature": 0.2
            }
            
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", 
                                   headers=headers, json=data, timeout=45)
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "content": response.json()["choices"][0]["message"]["content"],
                    "model": model
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "model": model
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception: {str(e)}",
                "model": self.ai_models[model_index % len(self.ai_models)]
            }

    def get_ai_consensus(self, prompt, container_name, min_models=8):
        """Get AI consensus from multiple models"""
        logging.info(f"🤖 Getting AI consensus for {container_name}...")
        
        responses = []
        successful_responses = []
        
        # Query all available models
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(self.query_openrouter_ai, prompt, i): i 
                      for i in range(len(self.ai_models))}
            
            for future in as_completed(futures):
                result = future.result()
                responses.append(result)
                
                if result["success"]:
                    successful_responses.append(result)
                    logging.info(f"✅ {result['model']}: Success")
                else:
                    logging.info(f"❌ {result['model']}: {result['error']}")
        
        if len(successful_responses) < min_models:
            logging.info(f"⚠️  Only {len(successful_responses)} successful responses, need {min_models}")
            return {
                "consensus_reached": False,
                "confidence": len(successful_responses) / len(self.ai_models),
                "responses": successful_responses,
                "error": "Insufficient AI responses for consensus"
            }
        
        # Analyze consensus
        consensus_prompt = f"""
        Analyze these {len(successful_responses)} AI responses for container '{container_name}' and determine consensus:
        
        Responses:
        {json.dumps([r['content'] for r in successful_responses], indent=2)}
        
        Provide:
        1. Overall consensus score (0.0-1.0)
        2. Key agreements across models
        3. Any disagreements or concerns
        4. Final recommendation (APPROVE/REJECT/NEEDS_IMPROVEMENT)
        5. Specific improvements needed if any
        
        Format as JSON with these exact keys: consensus_score, agreements, disagreements, recommendation, improvements
        """
        
        consensus_result = self.query_openrouter_ai(consensus_prompt, 0)
        
        if consensus_result["success"]:
            try:
                consensus_data = json.loads(consensus_result["content"])
                return {
                    "consensus_reached": consensus_data.get("consensus_score", 0) >= self.consensus_threshold,
                    "confidence": consensus_data.get("consensus_score", 0),
                    "recommendation": consensus_data.get("recommendation", "UNKNOWN"),
                    "agreements": consensus_data.get("agreements", []),
                    "disagreements": consensus_data.get("disagreements", []),
                    "improvements": consensus_data.get("improvements", []),
                    "responses": successful_responses,
                    "total_models": len(successful_responses)
                }
            except json.JSONDecodeError:
                return {
                    "consensus_reached": False,
                    "confidence": 0.0,
                    "error": "Failed to parse consensus analysis",
                    "responses": successful_responses
                }
        
        return {
            "consensus_reached": False,
            "confidence": 0.0,
            "error": "Failed to get consensus analysis",
            "responses": successful_responses
        }

    def create_container_specification(self, container_name, container_type, category):
        """Create detailed container specification using AI consensus"""
        logging.info(f"📋 Creating specification for {container_name}...")
        
        spec_prompt = f"""
        Create a comprehensive container specification for: {container_name}
        Category: {category}
        Description: {container_type}
        
        This container is part of the Ultimate Lyra Trading System ecosystem.
        
        Provide a detailed specification including:
        1. Container purpose and functionality
        2. Required dependencies and packages
        3. Environment variables needed
        4. Exposed ports and services
        5. Volume mounts required
        6. Health check configuration
        7. Resource requirements (CPU, memory)
        8. Security considerations
        9. Integration points with other containers
        10. Dockerfile structure
        11. Docker-compose configuration
        12. Kubernetes deployment manifest
        13. Testing strategy
        14. Monitoring and logging setup
        15. Backup and recovery procedures
        
        Make this the BEST possible container for this specific purpose.
        Include all necessary components, optimizations, and best practices.
        
        Format as detailed JSON specification.
        """
        
        consensus = self.get_ai_consensus(spec_prompt, container_name)
        
        if consensus["consensus_reached"]:
            logging.info(f"✅ Specification approved for {container_name} (confidence: {consensus['confidence']:.2f})")
            return {
                "approved": True,
                "specification": consensus,
                "container_name": container_name,
                "category": category,
                "type": container_type
            }
        else:
            logging.info(f"❌ Specification needs improvement for {container_name}")
            return {
                "approved": False,
                "specification": consensus,
                "container_name": container_name,
                "category": category,
                "type": container_type,
                "improvements_needed": consensus.get("improvements", [])
            }

    def build_container_files(self, specification):
        """Build all container files based on AI specification"""
        container_name = specification["container_name"]
        container_dir = os.path.join(self.containers_dir, container_name)
        os.makedirs(container_dir, exist_ok=True)
        
        logging.info(f"🏗️  Building container files for {container_name}...")
        
        # Extract specification content from AI responses
        spec_content = ""
        if specification["approved"] and specification["specification"]["responses"]:
            # Use the first successful response as the base specification
            spec_content = specification["specification"]["responses"][0]["content"]
        
        # Generate Dockerfile
        dockerfile_prompt = f"""
        Based on this container specification:
        {spec_content}
        
        Create an optimized Dockerfile for {container_name}.
        Include:
        - Appropriate base image
        - All required dependencies
        - Security best practices
        - Multi-stage build if beneficial
        - Proper user permissions
        - Health checks
        - Minimal attack surface
        
        Provide ONLY the Dockerfile content, no explanations.
        """
        
        dockerfile_result = self.query_openrouter_ai(dockerfile_prompt, 0)
        if dockerfile_result["success"]:
            with open(os.path.join(container_dir, "Dockerfile"), 'w') as f:
                f.write(dockerfile_result["content"])
        
        # Generate docker-compose.yml
        compose_prompt = f"""
        Based on this container specification:
        {spec_content}
        
        Create a docker-compose.yml configuration for {container_name}.
        Include:
        - Service definition
        - Environment variables
        - Volume mounts
        - Port mappings
        - Network configuration
        - Dependencies
        - Health checks
        - Resource limits
        
        Provide ONLY the YAML content, no explanations.
        """
        
        compose_result = self.query_openrouter_ai(compose_prompt, 1)
        if compose_result["success"]:
            with open(os.path.join(container_dir, "docker-compose.yml"), 'w') as f:
                f.write(compose_result["content"])
        
        # Generate Kubernetes manifest
        k8s_prompt = f"""
        Based on this container specification:
        {spec_content}
        
        Create Kubernetes deployment and service manifests for {container_name}.
        Include:
        - Deployment configuration
        - Service definition
        - ConfigMap for configuration
        - Secret for sensitive data
        - Resource requests and limits
        - Health checks
        - Security context
        
        Provide ONLY the YAML content, no explanations.
        """
        
        k8s_result = self.query_openrouter_ai(k8s_prompt, 2)
        if k8s_result["success"]:
            with open(os.path.join(container_dir, "kubernetes.yml"), 'w') as f:
                f.write(k8s_result["content"])
        
        # Generate application code
        code_prompt = f"""
        Based on this container specification:
        {spec_content}
        
        Create the main application code for {container_name}.
        This should be production-ready code that implements the container's functionality.
        Include:
        - Main application logic
        - Error handling
        - Logging
        - Health check endpoints
        - Configuration management
        - Graceful shutdown
        
        Use Python unless another language is more appropriate.
        Provide complete, working code.
        """
        
        code_result = self.query_openrouter_ai(code_prompt, 3)
        if code_result["success"]:
            # Determine file extension based on content
            extension = ".py"  # Default to Python
            if "package.json" in code_result["content"] or "npm" in code_result["content"]:
                extension = ".js"
            elif "go mod" in code_result["content"] or "package main" in code_result["content"]:
                extension = ".go"
            
            with open(os.path.join(container_dir, f"main{extension}"), 'w') as f:
                f.write(code_result["content"])
        
        # Generate requirements/dependencies file
        deps_prompt = f"""
        Based on this container specification and code:
        {spec_content}
        
        Create the dependencies file (requirements.txt, package.json, go.mod, etc.)
        Include all necessary packages and their versions.
        Use stable, secure versions.
        
        Provide ONLY the dependencies file content.
        """
        
        deps_result = self.query_openrouter_ai(deps_prompt, 4)
        if deps_result["success"]:
            # Determine dependencies file name
            deps_file = "requirements.txt"  # Default
            if "package.json" in deps_result["content"] or "{" in deps_result["content"]:
                deps_file = "package.json"
            elif "go.mod" in deps_result["content"] or "module " in deps_result["content"]:
                deps_file = "go.mod"
            
            with open(os.path.join(container_dir, deps_file), 'w') as f:
                f.write(deps_result["content"])
        
        # Generate README
        readme_content = f"""# {container_name.replace('_', ' ').title()}

{specification['type']}

## Purpose
This container is part of the Ultimate Lyra Trading System ecosystem.

## Files
- `Dockerfile`: Container build configuration
- `docker-compose.yml`: Docker Compose configuration
- `kubernetes.yml`: Kubernetes deployment manifests
- `main.*`: Main application code
- `requirements.txt` or similar: Dependencies

## Usage

### Docker
```bash
docker build -t {container_name} .
docker run {container_name}
```

### Docker Compose
```bash
docker-compose up
```

### Kubernetes
```bash
kubectl apply -f kubernetes.yml
```

## AI Consensus
This container was created and validated using AI consensus from multiple models:
- Confidence Score: {specification['specification'].get('confidence', 0):.2f}
- Models Used: {specification['specification'].get('total_models', 0)}

## Integration
This container integrates with other components in the Ultimate Lyra Trading System ecosystem.
"""
        
        with open(os.path.join(container_dir, "README.md"), 'w') as f:
            f.write(readme_content)
        
        return container_dir

    def test_container(self, container_dir, container_name):
        """Test container using AI consensus validation"""
        logging.info(f"🧪 Testing container {container_name}...")
        
        # Read all container files for analysis
        container_files = {}
        for file in os.listdir(container_dir):
            file_path = os.path.join(container_dir, file)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        container_files[file] = f.read()
                except:
                    container_files[file] = f"Binary file: {file}"
        
        test_prompt = f"""
        Analyze this container implementation for {container_name} and provide comprehensive testing results:
        
        Container Files:
        {json.dumps(container_files, indent=2)}
        
        Evaluate:
        1. Code quality and best practices
        2. Security implementation
        3. Performance considerations
        4. Error handling
        5. Documentation completeness
        6. Container optimization
        7. Integration readiness
        8. Production readiness
        9. Scalability
        10. Maintainability
        
        Provide:
        - Overall quality score (0.0-1.0)
        - Specific issues found
        - Recommended improvements
        - Test results for each component
        - Production readiness assessment
        
        Format as JSON with keys: quality_score, issues, improvements, test_results, production_ready
        """
        
        consensus = self.get_ai_consensus(test_prompt, container_name)
        
        return {
            "container_name": container_name,
            "test_results": consensus,
            "passed": consensus.get("consensus_reached", False) and 
                     consensus.get("confidence", 0) >= self.consensus_threshold
        }

    def improve_container(self, container_dir, container_name, test_results):
        """Improve container based on AI feedback"""
        logging.info(f"🔧 Improving container {container_name}...")
        
        if not test_results["test_results"].get("improvements"):
            return True
        
        improvements = test_results["test_results"]["improvements"]
        
        # Apply improvements using AI
        for improvement in improvements[:3]:  # Apply top 3 improvements
            improve_prompt = f"""
            Apply this improvement to the container {container_name}:
            
            Improvement: {improvement}
            
            Current container files are in: {container_dir}
            
            Provide the specific file changes needed to implement this improvement.
            Include the complete updated file content.
            
            Format as JSON: {{"file_name": "updated_content"}}
            """
            
            improve_result = self.query_openrouter_ai(improve_prompt, 0)
            if improve_result["success"]:
                try:
                    updates = json.loads(improve_result["content"])
                    for file_name, content in updates.items():
                        file_path = os.path.join(container_dir, file_name)
                        with open(file_path, 'w') as f:
                            f.write(content)
                    logging.info(f"✅ Applied improvement: {improvement[:50]}...")
                except:
                    logging.info(f"❌ Failed to apply improvement: {improvement[:50]}...")
        
        return True

    def containerize_everything(self):
        """Main process: containerize everything with AI consensus"""
        logging.info("🚀 STARTING ULTIMATE AI CONSENSUS CONTAINERIZATION")
        logging.info("=" * 80)
        
        os.makedirs(self.containers_dir, exist_ok=True)
        os.makedirs(self.production_dir, exist_ok=True)
        os.makedirs(self.testing_dir, exist_ok=True)
        
        total_containers = sum(len(containers) for containers in self.container_types.values())
        processed_containers = 0
        production_ready = 0
        
        results = {
            "start_time": datetime.now().isoformat(),
            "containers": {},
            "production_ready": [],
            "needs_improvement": [],
            "failed": []
        }
        
        # Process each container category
        for category, containers in self.container_types.items():
            logging.info(f"\n📦 PROCESSING CATEGORY: {category}")
            logging.info("-" * 50)
            
            for container_name, container_type in containers.items():
                logging.info(f"\n🔄 Processing: {container_name}")
                processed_containers += 1
                
                # Step 1: Create specification with AI consensus
                specification = self.create_container_specification(
                    container_name, container_type, category
                )
                
                if not specification["approved"]:
                    logging.info(f"❌ Specification rejected for {container_name}")
                    results["failed"].append(container_name)
                    continue
                
                # Step 2: Build container files
                container_dir = self.build_container_files(specification)
                
                # Step 3: Test and improve iteratively
                iteration = 0
                while iteration < self.max_iterations:
                    iteration += 1
                    logging.info(f"🔄 Test iteration {iteration} for {container_name}")
                    
                    # Test container
                    test_results = self.test_container(container_dir, container_name)
                    
                    if test_results["passed"]:
                        logging.info(f"✅ Container {container_name} passed all tests!")
                        
                        # Move to production
                        production_path = os.path.join(self.production_dir, container_name)
                        if os.path.exists(production_path):
                            shutil.rmtree(production_path)
                        shutil.copytree(container_dir, production_path)
                        
                        results["production_ready"].append({
                            "name": container_name,
                            "category": category,
                            "path": production_path,
                            "iterations": iteration,
                            "confidence": test_results["test_results"].get("confidence", 0)
                        })
                        production_ready += 1
                        break
                    else:
                        logging.info(f"🔧 Container {container_name} needs improvement (iteration {iteration})")
                        
                        # Apply improvements
                        self.improve_container(container_dir, container_name, test_results)
                        
                        if iteration == self.max_iterations:
                            logging.info(f"⚠️  Container {container_name} reached max iterations")
                            results["needs_improvement"].append({
                                "name": container_name,
                                "category": category,
                                "issues": test_results["test_results"].get("improvements", [])
                            })
                
                results["containers"][container_name] = {
                    "category": category,
                    "specification": specification,
                    "final_test": test_results if 'test_results' in locals() else None,
                    "iterations": iteration,
                    "status": "production_ready" if test_results["passed"] else "needs_improvement"
                }
                
                logging.info(f"📊 Progress: {processed_containers}/{total_containers} containers processed")
                logging.info(f"✅ Production ready: {production_ready}")
        
        # Generate final summary
        results["end_time"] = datetime.now().isoformat()
        results["total_containers"] = total_containers
        results["production_ready_count"] = production_ready
        results["success_rate"] = production_ready / total_containers if total_containers > 0 else 0
        
        # Save results
        with open(os.path.join(self.production_dir, "CONTAINERIZATION_RESULTS.json"), 'w') as f:
            json.dump(results, f, indent=2)
        
        # Create master docker-compose for all production containers
        self.create_master_compose()
        
        # Create master Kubernetes deployment
        self.create_master_kubernetes()
        
        logging.info("\n" + "=" * 80)
        logging.info("🎉 ULTIMATE CONTAINERIZATION COMPLETE!")
        logging.info("=" * 80)
        logging.info(f"📦 Total Containers: {total_containers}")
        logging.info(f"✅ Production Ready: {production_ready}")
        logging.info(f"🔧 Need Improvement: {len(results['needs_improvement'])}")
        logging.info(f"❌ Failed: {len(results['failed'])}")
        logging.info(f"📈 Success Rate: {results['success_rate']:.1%}")
        logging.info(f"📁 Production Directory: {self.production_dir}")
        
        return results

    def create_master_compose(self):
        """Create master docker-compose.yml for all production containers"""
        logging.info("🐳 Creating master docker-compose.yml...")
        
        compose_content = {
            "version": "3.8",
            "services": {},
            "networks": {
                "lyra_network": {
                    "driver": "bridge"
                }
            },
            "volumes": {}
        }
        
        # Add each production container as a service
        for container_dir in os.listdir(self.production_dir):
            container_path = os.path.join(self.production_dir, container_dir)
            if os.path.isdir(container_path):
                compose_file = os.path.join(container_path, "docker-compose.yml")
                if os.path.exists(compose_file):
                    try:
                        with open(compose_file, 'r') as f:
                            container_compose = yaml.safe_load(f)
                        
                        if "services" in container_compose:
                            for service_name, service_config in container_compose["services"].items():
                                # Add to master compose
                                service_config["networks"] = ["lyra_network"]
                                compose_content["services"][f"{container_dir}_{service_name}"] = service_config
                    except:
                        logging.info(f"⚠️  Could not parse compose file for {container_dir}")
        
        # Save master compose
        with open(os.path.join(self.production_dir, "docker-compose.yml"), 'w') as f:
            yaml.dump(compose_content, f, default_flow_style=False)
        
        logging.info(f"✅ Master docker-compose.yml created with {len(compose_content['services'])} services")

    def create_master_kubernetes(self):
        """Create master Kubernetes deployment for all containers"""
        logging.info("☸️  Creating master Kubernetes deployment...")
        
        k8s_content = []
        
        # Add namespace
        k8s_content.append({
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": "lyra-trading-system"
            }
        })
        
        # Process each production container
        for container_dir in os.listdir(self.production_dir):
            container_path = os.path.join(self.production_dir, container_dir)
            if os.path.isdir(container_path):
                k8s_file = os.path.join(container_path, "kubernetes.yml")
                if os.path.exists(k8s_file):
                    try:
                        with open(k8s_file, 'r') as f:
                            container_k8s = yaml.safe_load_all(f)
                        
                        for resource in container_k8s:
                            if resource:
                                # Add namespace to resource
                                if "metadata" not in resource:
                                    resource["metadata"] = {}
                                resource["metadata"]["namespace"] = "lyra-trading-system"
                                k8s_content.append(resource)
                    except:
                        logging.info(f"⚠️  Could not parse Kubernetes file for {container_dir}")
        
        # Save master Kubernetes file
        with open(os.path.join(self.production_dir, "kubernetes-all.yml"), 'w') as f:
            yaml.dump_all(k8s_content, f, default_flow_style=False)
        
        logging.info(f"✅ Master Kubernetes deployment created with {len(k8s_content)} resources")

if __name__ == "__main__":
    containerizer = UltimateAIConsensusContainerizer()
    results = containerizer.containerize_everything()
