#!/usr/bin/env python3
"""
Sanitize API keys and secrets from the repository
"""

import os
import re
from pathlib import Path

class SecretSanitizer:
    def __init__(self, repo_dir="/home/ubuntu/final_sandbox_archive"):
        self.repo_dir = Path(repo_dir)
        self.sanitized_count = 0
        
        # Patterns to detect and replace API keys
        self.secret_patterns = [
            # OpenAI API keys
            (r'sk-[a-zA-Z0-9]{48}', 'sk-OPENAI_API_KEY_PLACEHOLDER'),
            # Anthropic API keys  
            (r'sk-ant-[a-zA-Z0-9\-]{95,}', 'sk-ant-ANTHROPIC_API_KEY_PLACEHOLDER'),
            # OpenRouter API keys
            (r'sk-or-v1-[a-zA-Z0-9]{64}', 'sk-or-v1-OPENROUTER_API_KEY_PLACEHOLDER'),
            # GitHub tokens
            (r'ghu_[a-zA-Z0-9]{36}', 'ghu_GITHUB_TOKEN_PLACEHOLDER'),
            (r'ghp_[a-zA-Z0-9]{36}', 'ghp_GITHUB_TOKEN_PLACEHOLDER'),
            # Generic API key patterns
            (r'["\']?[Aa][Pp][Ii]_?[Kk][Ee][Yy]["\']?\s*[:=]\s*["\'][a-zA-Z0-9\-_]{20,}["\']', 'API_KEY="YOUR_API_KEY_HERE"'),
            # Bearer tokens
            (r'Bearer [a-zA-Z0-9\-_]{20,}', 'Bearer YOUR_TOKEN_HERE'),
        ]
        
        # File extensions to process
        self.file_extensions = ['.py', '.md', '.txt', '.json', '.yml', '.yaml', '.sh', '.env']

    def sanitize_file(self, file_path):
        """Sanitize a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_content = content
            
            # Apply all secret patterns
            for pattern, replacement in self.secret_patterns:
                content = re.sub(pattern, replacement, content)
            
            # If content changed, write it back
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.sanitized_count += 1
                print(f"Sanitized: {file_path}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    def sanitize_repository(self):
        """Sanitize all files in the repository"""
        print("Starting secret sanitization...")
        
        for file_path in self.repo_dir.rglob("*"):
            if file_path.is_file() and file_path.suffix in self.file_extensions:
                # Skip git files
                if '.git' in str(file_path):
                    continue
                    
                self.sanitize_file(file_path)
        
        print(f"Sanitization complete. {self.sanitized_count} files processed.")

    def remove_specific_files(self):
        """Remove files that contain only API keys"""
        files_to_remove = [
            "sandbox_content/api_key.txt",
            "sandbox_content/ultimate_lyra_v5/api_key.txt"
        ]
        
        for file_path in files_to_remove:
            full_path = self.repo_dir / file_path
            if full_path.exists():
                full_path.unlink()
                print(f"Removed: {full_path}")

if __name__ == "__main__":
    sanitizer = SecretSanitizer()
    sanitizer.remove_specific_files()
    sanitizer.sanitize_repository()
    print("✅ Repository sanitization completed!")
