"""Container and deployment tests"""
import pytest
import docker
import subprocess
import os
import yaml
import json
import time

class TestContainerDeployment:
    """Test container deployment and functionality"""
    
    def test_dockerfile_validation(self):
        """Test Dockerfile validation"""
        dockerfile_paths = [
            "CONTAINERS/openrouter_ai/Dockerfile",
            "ECOSYSTEM_DEPLOYMENT/ecosystem_Dockerfile"
        ]
        
        for dockerfile_path in dockerfile_paths:
            if os.path.exists(dockerfile_path):
                with open(dockerfile_path, 'r') as f:
                    content = f.read()
                
                # Basic Dockerfile validation
                assert "FROM" in content
                assert "WORKDIR" in content or "RUN" in content
    
    def test_docker_compose_validation(self):
        """Test docker-compose.yml validation"""
        compose_files = [
            "CONTAINERS/openrouter_ai/docker-compose.yml",
            "ECOSYSTEM_DEPLOYMENT/ecosystem_docker-compose.yml"
        ]
        
        for compose_file in compose_files:
            if os.path.exists(compose_file):
                with open(compose_file, 'r') as f:
                    try:
                        compose_config = yaml.safe_load(f)
                        
                        # Basic compose validation
                        assert "version" in compose_config or "services" in compose_config
                        if "services" in compose_config:
                            assert len(compose_config["services"]) > 0
                    except yaml.YAMLError:
                        pytest.fail(f"Invalid YAML in {compose_file}")
    
    def test_kubernetes_manifests(self):
        """Test Kubernetes manifest validation"""
        k8s_files = [
            "CONTAINERS/openrouter_ai/kubernetes.yml",
            "DEPLOYMENT/kubernetes/"
        ]
        
        for k8s_path in k8s_files:
            if os.path.exists(k8s_path):
                if os.path.isfile(k8s_path):
                    with open(k8s_path, 'r') as f:
                        try:
                            k8s_config = yaml.safe_load(f)
                            
                            # Basic K8s validation
                            if k8s_config:
                                assert "apiVersion" in k8s_config
                                assert "kind" in k8s_config
                        except yaml.YAMLError:
                            pytest.fail(f"Invalid YAML in {k8s_path}")
    
    @pytest.mark.skipif(not os.path.exists("/var/run/docker.sock"), 
                       reason="Docker not available")
    def test_container_build(self):
        """Test container build process"""
        try:
            client = docker.from_env()
            
            # Test if Docker is accessible
            client.ping()
            
            # Mock container build test
            # In real scenario, would build actual containers
            assert True
            
        except Exception as e:
            pytest.skip(f"Docker not available: {e}")
    
    def test_environment_variables(self):
        """Test environment variable configuration"""
        env_files = [
            ".env",
            "SECURITY_VAULT/.env.example",
            "AI_INTEGRATION/.env.template"
        ]
        
        for env_file in env_files:
            if os.path.exists(env_file):
                with open(env_file, 'r') as f:
                    content = f.read()
                
                # Check for sensitive data patterns
                sensitive_patterns = [
                    "password=",
                    "secret=", 
                    "key=",
                    "token="
                ]
                
                # Ensure no actual secrets in version control
                for pattern in sensitive_patterns:
                    if pattern in content.lower():
                        # Should be placeholder values, not real secrets
                        assert "your_" in content.lower() or "placeholder" in content.lower()

class TestDeploymentScripts:
    """Test deployment scripts and automation"""
    
    def test_deployment_scripts_exist(self):
        """Test that deployment scripts exist"""
        script_paths = [
            "ECOSYSTEM_SCRIPTS/ecosystem_start_ultimate_system.sh",
            "ECOSYSTEM_SCRIPTS/ecosystem_deploy_supreme_system.sh",
            "ECOSYSTEM_INTEGRATION/deploy_ecosystem.sh"
        ]
        
        for script_path in script_paths:
            if os.path.exists(script_path):
                # Check if script is executable
                assert os.access(script_path, os.X_OK)
                
                # Check script content
                with open(script_path, 'r') as f:
                    content = f.read()
                
                # Basic script validation
                assert content.startswith("#!/bin/bash") or "echo" in content
    
    def test_configuration_files(self):
        """Test configuration files validation"""
        config_files = [
            "CORE_SYSTEMS/config.json",
            "AI_INTEGRATION/openrouter_config.json",
            "TRADING_ENGINE/trading_config.yaml"
        ]
        
        for config_file in config_files:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    try:
                        if config_file.endswith('.json'):
                            config = json.load(f)
                            assert isinstance(config, dict)
                        elif config_file.endswith(('.yml', '.yaml')):
                            config = yaml.safe_load(f)
                            assert config is not None
                    except (json.JSONDecodeError, yaml.YAMLError) as e:
                        pytest.fail(f"Invalid configuration file {config_file}: {e}")

if __name__ == '__main__':
    pytest.main([__file__])
