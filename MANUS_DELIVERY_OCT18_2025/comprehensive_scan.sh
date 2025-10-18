#!/bin/bash
echo "=== COMPREHENSIVE FILE SCAN ==="
echo ""
echo "1. ALL FILE TYPES IN SANDBOX:"
find /home/ubuntu -maxdepth 1 -type f | wc -l
echo ""
echo "2. FILE TYPES BREAKDOWN:"
find /home/ubuntu -maxdepth 1 -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20
echo ""
echo "3. JSON/CONFIG FILES:"
find /home/ubuntu -maxdepth 1 \( -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name "*.ini" -o -name "*.conf" \) | head -20
echo ""
echo "4. MARKDOWN DOCUMENTATION:"
find /home/ubuntu -maxdepth 1 -name "*.md" | head -20
echo ""
echo "5. ALL REPOSITORY FILES:"
find /home/ubuntu/all_repos -type f | wc -l
echo ""
echo "6. REPOSITORY FILE TYPES:"
find /home/ubuntu/all_repos -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20
echo ""
echo "7. KEY CONFIGURATION FILES IN REPOS:"
find /home/ubuntu/all_repos \( -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "requirements.txt" -o -name "package.json" \) | head -30
echo ""
echo "8. DOCUMENTATION IN REPOS:"
find /home/ubuntu/all_repos -name "README.md" -o -name "CHANGELOG.md" -o -name "CONTRIBUTING.md" | head -20
