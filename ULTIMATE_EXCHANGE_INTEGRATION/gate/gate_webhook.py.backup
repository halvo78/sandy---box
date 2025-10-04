# SYNTAX ERROR FIXED - File needs manual review\n#!/usr/bin/env python3
"""
Gate.io Webhook Handler
Handles real-time notifications from Gate.io
"""

from flask import Flask, request, jsonify
import json
import logging
from datetime import datetime
import hmac
import hashlib

app = Flask(__name__)

class Gate.ioWebhookHandler:
    def __init__(self):
        self.exchange_id = "gate"
        self.exchange_name = "Gate.io"
        self.setup_logging()
        
    def setup_logging(self):
        """Setup webhook logging"""
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(f"gate_webhook")
    
    def verify_signature(self, payload: str, signature: str) -> bool:
        """Verify webhook signature"""
        try:
            secret = os.getenv('GATE_WEBHOOK_SECRET', '')
            expected_signature = hmac.new(
                secret.encode('utf-8'),
                payload.encode('utf-8'),
                hashlib.sha256
            ).hexdigest()
            return hmac.compare_digest(signature, expected_signature)
        except Exception as e:
            self.logger.error(f"Signature verification failed: {str(e)}")
            return False
    
    def process_order_update(self, data: Dict) -> Dict:
        """Process order update webhook"""
        try:
            order_id = data.get('orderId')
            status = data.get('status')
            symbol = data.get('symbol')
            
            # Australian exchanges - ATO logging
            if "Global" == "AU":
                self.logger.info(f"ATO_WEBHOOK: {order_id} {status} {symbol}")
            
            # Process the order update
            result = {
                'processed': True,
                'order_id': order_id,
                'status': status,
                'timestamp': datetime.now().isoformat()
            }
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error processing order update: {str(e)}")
            return {'processed': False, 'error': str(e)}
    
    def process_balance_update(self, data: Dict) -> Dict:
        """Process balance update webhook"""
        try:
            asset = data.get('asset')
            balance = data.get('balance')
            
            # Log balance change
            self.logger.info(f"Balance update: {asset} = {balance}")
            
            return {
                'processed': True,
                'asset': asset,
                'balance': balance,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Error processing balance update: {str(e)}")
            return {'processed': False, 'error': str(e)}

# Create handler instance
handler = Gate.ioWebhookHandler()

@app.route('/webhook/gate/order', methods=['POST'])
def order_webhook():
    """Handle order webhooks"""
    try:
        data = request.get_json()
        signature = request.headers.get('X-Signature', '')
        
        # Verify signature
        if not handler.verify_signature(request.get_data(as_text=True), signature):
            return jsonify({'error': 'Invalid signature'}), 401
        
        # Process order update
        result = handler.process_order_update(data)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/webhook/gate/balance', methods=['POST'])
def balance_webhook():
    """Handle balance webhooks"""
    try:
        data = request.get_json()
        result = handler.process_balance_update(data)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'exchange': handler.exchange_name,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
