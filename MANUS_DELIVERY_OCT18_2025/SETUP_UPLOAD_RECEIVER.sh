#!/bin/bash

echo "🚀 SETTING UP UPLOAD RECEIVER ON LOCAL UBUNTU"
echo "=============================================="
echo ""

# Create upload receiver Python script
cat > /tmp/ultimate_upload_receiver.py << 'EOF'
#!/usr/bin/env python3
"""
Ultimate Upload Receiver
Receives files via HTTP POST and saves them to the target directory.
"""

from flask import Flask, request, jsonify
import os
import sys

app = Flask(__name__)

# Target directory for uploads
UPLOAD_DIR = os.path.expanduser("~/ultimate_lyra_systems")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads."""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400
        
        # Save the file
        filepath = os.path.join(UPLOAD_DIR, file.filename)
        file.save(filepath)
        
        # Get file size
        file_size = os.path.getsize(filepath)
        
        print(f"✅ Received: {file.filename} ({file_size} bytes)")
        print(f"✅ Saved to: {filepath}")
        
        return jsonify({
            "status": "success",
            "filename": file.filename,
            "filepath": filepath,
            "size": file_size
        }), 200
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "upload_dir": UPLOAD_DIR}), 200

@app.route('/', methods=['GET'])
def index():
    """Root endpoint."""
    return """
    <html>
    <body>
    <h1>🚀 Ultimate Upload Receiver</h1>
    <p>Upload endpoint: <code>POST /upload</code></p>
    <p>Health check: <code>GET /health</code></p>
    <p>Upload directory: <code>{}</code></p>
    </body>
    </html>
    """.format(UPLOAD_DIR), 200

if __name__ == '__main__':
    print("="*60)
    print("🚀 ULTIMATE UPLOAD RECEIVER")
    print("="*60)
    print(f"📁 Upload directory: {UPLOAD_DIR}")
    print(f"🌐 Server starting on http://0.0.0.0:9000")
    print(f"📤 Upload endpoint: POST /upload")
    print(f"❤️  Health check: GET /health")
    print("="*60)
    print("")
    
    app.run(host='0.0.0.0', port=9000, debug=False)
EOF

# Make it executable
chmod +x /tmp/ultimate_upload_receiver.py

# Check if Flask is installed
echo "📦 Checking Flask..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing Flask..."
    pip3 install flask
else
    echo "✅ Flask is already installed"
fi
echo ""

# Instructions
echo "="*60
echo "📋 SETUP COMPLETE!"
echo "="*60
echo ""
echo "To start the upload receiver, run:"
echo ""
echo "  python3 /tmp/ultimate_upload_receiver.py"
echo ""
echo "This will start a server on port 9000 that can receive file uploads."
echo ""
echo "Make sure your ngrok is configured to forward port 9000:"
echo ""
echo "  In your ngrok.yml, add:"
echo "    - proto: http"
echo "      addr: 9000"
echo "      name: upload_receiver"
echo ""
echo "Then restart ngrok:"
echo "  sudo systemctl restart ngrok-permanent"
echo ""
echo "="*60
echo ""

# Offer to start now
read -p "Start upload receiver now? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🚀 Starting upload receiver..."
    echo ""
    python3 /tmp/ultimate_upload_receiver.py
else
    echo ""
    echo "✅ Setup complete. Start the receiver manually when ready:"
    echo "  python3 /tmp/ultimate_upload_receiver.py"
    echo ""
fi

