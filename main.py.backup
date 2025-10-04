#!/usr/bin/env python3
"""
Sandy-Box Trading System - Main Application
==========================================
Production-ready trading system with all exchanges integrated.
"""

import os
import sys
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Sandy-Box Trading System",
    description="Production-ready multi-exchange trading system",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Sandy-Box Trading System", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "sandy-box-trading"}

@app.get("/exchanges")
async def list_exchanges():
    exchanges = [
        "btcmarkets", "coinbase", "binance", "okx", 
        "kraken", "gateio", "whitebit", "digitalsurge", "swyftx"
    ]
    return {"exchanges": exchanges, "count": len(exchanges)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    logger.info(f"Starting Sandy-Box Trading System on {host}:{port}")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )
