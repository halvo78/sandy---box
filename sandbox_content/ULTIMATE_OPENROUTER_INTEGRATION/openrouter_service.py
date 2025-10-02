#!/usr/bin/env python3
'''
OpenRouter Integration Service - Port 8091
Provides AI assistance for the Ultimate Lyra Trading System
'''

import asyncio
from aiohttp import web
import json
from ULTIMATE_OPENROUTER_INTEGRATION import UltimateOpenRouterIntegration

integration = UltimateOpenRouterIntegration()

async def handle_consensus(request):
    data = await request.json()
    query = data.get('query', '')
    
    if not query:
        return web.json_response({'error': 'Query required'}, status=400)
    
    responses = await integration.get_ai_consensus(query)
    
    return web.json_response({
        'query': query,
        'responses': responses,
        'timestamp': '2025-10-01T07:37:40.352954'
    })

async def handle_system_status(request):
    return web.json_response(integration.system_context)

async def handle_ai_models(request):
    return web.json_response({
        'available_models': integration.models,
        'total_models': len(integration.models)
    })

app = web.Application()
app.router.add_post('/consensus', handle_consensus)
app.router.add_get('/status', handle_system_status)
app.router.add_get('/models', handle_ai_models)

if __name__ == '__main__':
    print("🤖 Starting OpenRouter Integration Service on port 8091...")
    web.run_app(app, host='0.0.0.0', port=8091)
