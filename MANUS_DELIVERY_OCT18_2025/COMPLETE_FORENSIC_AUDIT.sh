#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║         COMPLETE FORENSIC AUDIT - EVERYTHING                ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# 1. ALL GITHUB REPOSITORIES
echo "=========================================="
echo "1. ALL GITHUB REPOSITORIES"
echo "=========================================="
gh repo list halvo78 --limit 100 --json name,description,updatedAt | jq -r '.[] | "✓ \(.name) - \(.description // "No description")"'
echo ""

# 2. ALL CLONED REPOSITORIES
echo "=========================================="
echo "2. ALL CLONED REPOSITORIES IN SANDBOX"
echo "=========================================="
find /home/ubuntu -name ".git" -type d 2>/dev/null | while read gitdir; do
    repo=$(dirname "$gitdir")
    echo "✓ $repo"
    cd "$repo" && git log --oneline -1 2>/dev/null
done
echo ""

# 3. ALL PYTHON FILES (LYRA + TODAY'S WORK)
echo "=========================================="
echo "3. ALL PYTHON FILES IN SANDBOX"
echo "=========================================="
find /home/ubuntu -name "*.py" -type f 2>/dev/null | head -50 | while read file; do
    lines=$(wc -l < "$file")
    echo "✓ $file ($lines lines)"
done
echo ""

# 4. ALL MARKDOWN DOCUMENTATION
echo "=========================================="
echo "4. ALL MARKDOWN DOCUMENTATION"
echo "=========================================="
find /home/ubuntu -name "*.md" -type f 2>/dev/null | head -30 | while read file; do
    lines=$(wc -l < "$file")
    echo "✓ $file ($lines lines)"
done
echo ""

# 5. ALL PROCESSES (LYRA SYSTEMS)
echo "=========================================="
echo "5. ALL RUNNING PROCESSES (LYRA SYSTEMS)"
echo "=========================================="
ps aux | grep -E "python|lyra|trading" | grep -v grep | head -20
echo ""

# 6. ALL PORTS IN USE
echo "=========================================="
echo "6. ALL PORTS IN USE (LYRA PORTS)"
echo "=========================================="
netstat -tuln 2>/dev/null | grep LISTEN | head -20
echo ""

# 7. TODAY'S FILES
echo "=========================================="
echo "7. ALL FILES CREATED TODAY"
echo "=========================================="
find /home/ubuntu -type f -newermt "2025-10-17 00:00:00" 2>/dev/null | grep -v ".git" | head -50
echo ""

# 8. TOTAL CODE STATISTICS
echo "=========================================="
echo "8. TOTAL CODE STATISTICS"
echo "=========================================="
echo "Python files:"
find /home/ubuntu -name "*.py" -type f 2>/dev/null | wc -l
echo "Total Python lines:"
find /home/ubuntu -name "*.py" -type f -exec wc -l {} + 2>/dev/null | tail -1
echo "Markdown files:"
find /home/ubuntu -name "*.md" -type f 2>/dev/null | wc -l
echo "Total Markdown lines:"
find /home/ubuntu -name "*.md" -type f -exec wc -l {} + 2>/dev/null | tail -1
echo ""

echo "✅ FORENSIC AUDIT COMPLETE"
