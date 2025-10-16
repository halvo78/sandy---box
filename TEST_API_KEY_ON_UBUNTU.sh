#!/bin/bash

echo "🔍 TESTING OPENROUTER API KEY FROM YOUR UBUNTU"
echo "=============================================="
echo ""

echo "Test 1: List models (GET request)..."
curl -s "https://openrouter.ai/api/v1/models" \
  -H "Authorization: Bearer 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" \
  | head -20

echo ""
echo ""
echo "Test 2: Chat completion (POST request)..."
curl -s "https://openrouter.ai/api/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
    "model": "meta-llama/llama-3.2-3b-instruct:free",
    "messages": [{"role": "user", "content": "Say hello"}]
  }'

echo ""
echo ""
echo "Test 3: Check key status..."
curl -s "https://openrouter.ai/api/v1/auth/key" \
  -H "Authorization: Bearer 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"

echo ""
echo ""
echo "=============================================="
echo "✅ Tests complete!"
echo ""
echo "If all tests show 'User not found', the issue is with OpenRouter account."
echo "If tests work from your Ubuntu but not from Manus, it's an IP restriction."

