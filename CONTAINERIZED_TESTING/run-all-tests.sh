#!/bin/bash
# Master Test Runner for All Components
set -e

echo "🚀 STARTING ULTIMATE CONTAINERIZED TESTING"
echo "============================================"

# Build all containers
echo "🏗️ Building all component containers..."
docker-compose build

# Run all tests in parallel
echo "🔍 Running all component tests..."
docker-compose up --abort-on-container-exit

# Collect results
echo "📊 Collecting test results..."
docker-compose down

# Generate comprehensive report
echo "📋 Generating comprehensive report..."
python3 ../generate-comprehensive-report.py

echo "🎉 ALL CONTAINERIZED TESTING COMPLETED!"
