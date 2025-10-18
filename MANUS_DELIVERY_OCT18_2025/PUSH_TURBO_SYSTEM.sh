#!/bin/bash

echo "🚀 PUSHING ULTIMATE TURBO SYSTEM TO LOCAL UBUNTU"
echo "================================================"
echo ""

# File to push
FILE="/home/ubuntu/ULTIMATE_TURBO_COMPLETE_PACKAGE.tar.gz"
FILE_SIZE=$(ls -lh "$FILE" | awk '{print $5}')

echo "📦 Package: ULTIMATE_TURBO_COMPLETE_PACKAGE.tar.gz"
echo "📊 Size: $FILE_SIZE"
echo ""

# Ask for ngrok URL
echo "Please provide your ngrok upload receiver URL"
echo "(e.g., https://xxxxx.ngrok.app)"
echo ""
read -p "Ngrok URL: " NGROK_URL

if [ -z "$NGROK_URL" ]; then
    echo "❌ No URL provided"
    exit 1
fi

# Remove trailing slash
NGROK_URL="${NGROK_URL%/}"

echo ""
echo "🌐 Target: $NGROK_URL/upload"
echo ""

# Test connection
echo "🔍 Testing connection..."
if curl -s -f "$NGROK_URL/health" > /dev/null 2>&1; then
    echo "✅ Upload receiver is healthy"
else
    echo "⚠️  Warning: Could not reach health endpoint"
    echo "   Trying upload anyway..."
fi
echo ""

# Push the file
echo "📤 Pushing package..."
echo ""

RESPONSE=$(curl -X POST -F "file=@$FILE" "$NGROK_URL/upload" -w "\n%{http_code}" -s)
HTTP_CODE=$(echo "$RESPONSE" | tail -n 1)
BODY=$(echo "$RESPONSE" | head -n -1)

echo ""
if [ "$HTTP_CODE" = "200" ]; then
    echo "="*60
    echo "✅ SUCCESS! Package pushed to local Ubuntu"
    echo "="*60
    echo ""
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
    echo ""
    echo "📋 Next steps on your local Ubuntu:"
    echo ""
    echo "1. Extract the package:"
    echo "   cd ~/ultimate_lyra_systems"
    echo "   tar -xzf ULTIMATE_TURBO_COMPLETE_PACKAGE.tar.gz"
    echo ""
    echo "2. Deploy:"
    echo "   chmod +x DEPLOY_ON_LOCAL_UBUNTU.sh"
    echo "   ./DEPLOY_ON_LOCAL_UBUNTU.sh"
    echo ""
    echo "="*60
else
    echo "="*60
    echo "❌ FAILED (HTTP $HTTP_CODE)"
    echo "="*60
    echo ""
    echo "$BODY"
    echo ""
    echo "Troubleshooting:"
    echo "1. Make sure upload receiver is running on your local Ubuntu"
    echo "2. Check ngrok tunnel is active"
    echo "3. Verify the URL is correct"
    echo ""
fi

