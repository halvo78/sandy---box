
-- ULTIMATE ALL APIs - SUPABASE SCHEMA
-- Built by 14 AI Models in Consensus
-- Run this in Supabase SQL Editor

-- Create table
CREATE TABLE IF NOT EXISTS lyra_all_apis (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    api_id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    category TEXT NOT NULL,
    endpoint TEXT,
    features JSONB,
    pricing TEXT,
    rate_limit TEXT,
    quality TEXT,
    status TEXT,
    consensus TEXT,
    sources JSONB,
    api_key_env TEXT,
    api_key_location TEXT,
    library TEXT,
    note TEXT,
    response_time TEXT,
    portfolio_value TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Enable RLS
ALTER TABLE lyra_all_apis ENABLE ROW LEVEL SECURITY;

-- Create policy
CREATE POLICY "Enable all for service role" ON lyra_all_apis FOR ALL USING (true);

-- Create indexes
CREATE INDEX idx_lyra_all_apis_type ON lyra_all_apis(type);
CREATE INDEX idx_lyra_all_apis_category ON lyra_all_apis(category);
CREATE INDEX idx_lyra_all_apis_status ON lyra_all_apis(status);
CREATE INDEX idx_lyra_all_apis_quality ON lyra_all_apis(quality);
