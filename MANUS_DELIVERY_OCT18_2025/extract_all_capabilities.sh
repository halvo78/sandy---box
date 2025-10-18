#!/bin/bash

echo "=== COMPREHENSIVE CAPABILITY EXTRACTION ==="
echo ""

echo "1. SANDBOX PYTHON FILES:"
find /home/ubuntu -maxdepth 1 -name "*.py" -type f | wc -l
echo ""

echo "2. SANDBOX KEY MODULES:"
find /home/ubuntu -maxdepth 1 -name "*ULTIMATE*.py" -o -name "*PERFECT*.py" -o -name "*WORLD*.py" -o -name "*lyra*.py" | head -20
echo ""

echo "3. ALL REPOSITORIES PYTHON FILES:"
find /home/ubuntu/all_repos -name "*.py" -type f | wc -l
echo ""

echo "4. KEY REPOSITORY MODULES:"
find /home/ubuntu/all_repos -name "*ULTIMATE*.py" -o -name "*trading*.py" -o -name "*engine*.py" -o -name "*system*.py" | head -30
echo ""

echo "5. CONFIGURATION FILES:"
find /home/ubuntu -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.toml" | grep -v node_modules | head -20
echo ""

echo "6. DOCUMENTATION FILES:"
find /home/ubuntu -name "*.md" -type f | grep -v node_modules | head -20
echo ""

echo "7. TOTAL LINES OF CODE:"
echo "Sandbox:"
find /home/ubuntu -maxdepth 1 -name "*.py" -type f -exec wc -l {} + 2>/dev/null | tail -1
echo "Repositories:"
find /home/ubuntu/all_repos -name "*.py" -type f -exec wc -l {} + 2>/dev/null | tail -1
echo ""

echo "=== EXTRACTION COMPLETE ==="
