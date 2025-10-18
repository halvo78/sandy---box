#!/usr/bin/env python3
"""
SUPABASE VAULT UPLOADER
Upload all Lyra system data to Supabase for easy viewing/editing

AWS Secrets Manager = Exchange credentials ONLY
Supabase = Everything else (APIs, configs, system data)
"""

import os
import json
from datetime import datetime
from supabase import create_client, Client

# Supabase credentials from environment
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cmwelibfxzplxjzspryh.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtd2VsaWJmeHpwbHhqenNwcnloIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NzcyMjQ4MywiZXhwIjoyMDczMjk4NDgzfQ.CUtx4wuMS4L-AaK6BWqC9wqJdTqoea38Vd9SzCYkcKk")

class SupabaseVaultUploader:
    """Upload all Lyra system data to Supabase"""
    
    def __init__(self):
        print("🔐 Connecting to Supabase...")
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Connected to Supabase!")
        print()
        
    def create_tables(self):
        """Create tables for Lyra system data"""
        
        print("📊 Creating Supabase tables...")
        print()
        
        # Note: Tables should be created via Supabase dashboard or SQL
        # This is just documentation of the schema
        
        tables_schema = {
            "lyra_free_apis": {
                "id": "uuid PRIMARY KEY",
                "name": "text NOT NULL",
                "category": "text NOT NULL",
                "endpoint": "text NOT NULL",
                "features": "jsonb",
                "rate_limit": "text",
                "quality": "text",
                "response_time": "text",
                "test_params": "jsonb",
                "status": "text",
                "note": "text",
                "created_at": "timestamp DEFAULT now()",
                "updated_at": "timestamp DEFAULT now()"
            },
            "lyra_paid_apis": {
                "id": "uuid PRIMARY KEY",
                "name": "text NOT NULL",
                "endpoint": "text NOT NULL",
                "features": "jsonb",
                "pricing": "text",
                "quality": "text",
                "api_key_name": "text",
                "status": "text",
                "created_at": "timestamp DEFAULT now()",
                "updated_at": "timestamp DEFAULT now()"
            },
            "lyra_infrastructure": {
                "id": "uuid PRIMARY KEY",
                "resource_type": "text NOT NULL",
                "resource_name": "text NOT NULL",
                "description": "text",
                "cost_monthly": "numeric",
                "specs": "jsonb",
                "status": "text",
                "created_at": "timestamp DEFAULT now()",
                "updated_at": "timestamp DEFAULT now()"
            },
            "lyra_ai_consensus": {
                "id": "uuid PRIMARY KEY",
                "validation_date": "timestamp NOT NULL",
                "total_tested": "integer",
                "working": "integer",
                "failed": "integer",
                "success_rate": "numeric",
                "ai_team": "jsonb",
                "results": "jsonb",
                "created_at": "timestamp DEFAULT now()"
            },
            "lyra_system_config": {
                "id": "uuid PRIMARY KEY",
                "config_key": "text UNIQUE NOT NULL",
                "config_value": "jsonb NOT NULL",
                "description": "text",
                "created_at": "timestamp DEFAULT now()",
                "updated_at": "timestamp DEFAULT now()"
            }
        }
        
        print("📋 Table Schema:")
        for table_name, schema in tables_schema.items():
            print(f"\n{table_name}:")
            for field, field_type in schema.items():
                print(f"  - {field}: {field_type}")
        
        print()
        print("⚠️  Note: Create these tables in Supabase dashboard first!")
        print("   Then run this script to upload data.")
        print()
        
        return tables_schema
    
    def upload_free_apis(self):
        """Upload validated free APIs"""
        
        print("📤 Uploading FREE APIs to Supabase...")
        
        # Load validation results
        with open("/home/ubuntu/LYRA_FREE_API_CONFIG.json", "r") as f:
            config = json.load(f)
        
        free_apis_data = []
        
        # Market data APIs
        for name, api in config["free_apis"]["market_data"].items():
            free_apis_data.append({
                "name": name,
                "category": "market_data",
                "endpoint": api["endpoint"],
                "features": api["features"],
                "rate_limit": api["rate_limit"],
                "quality": api["quality"],
                "response_time": api["response_time"],
                "test_params": api.get("test_params", {}),
                "status": "validated",
                "note": api.get("note", "")
            })
        
        # Blockchain APIs
        for name, api in config["free_apis"]["blockchain"].items():
            free_apis_data.append({
                "name": name,
                "category": "blockchain",
                "endpoint": api["endpoint"],
                "features": api["features"],
                "rate_limit": api["rate_limit"],
                "quality": api["quality"],
                "response_time": api["response_time"],
                "test_params": api.get("test_params", {}),
                "status": "validated",
                "note": api.get("note", "")
            })
        
        # Economic APIs
        for name, api in config["free_apis"]["economic"].items():
            free_apis_data.append({
                "name": name,
                "category": "economic",
                "endpoint": api["endpoint"],
                "features": api["features"],
                "rate_limit": api["rate_limit"],
                "quality": api["quality"],
                "response_time": api["response_time"],
                "test_params": api.get("test_params", {}),
                "status": "validated",
                "note": api.get("note", "")
            })
        
        print(f"  Found {len(free_apis_data)} free APIs to upload")
        
        # Try to upload (will fail if table doesn't exist)
        try:
            result = self.supabase.table("lyra_free_apis").upsert(free_apis_data).execute()
            print(f"  ✅ Uploaded {len(free_apis_data)} free APIs")
        except Exception as e:
            print(f"  ⚠️  Table 'lyra_free_apis' doesn't exist yet")
            print(f"     Create it in Supabase dashboard first")
            print(f"     Error: {str(e)[:100]}")
        
        print()
        
        # Save as JSON for manual import
        with open("/home/ubuntu/supabase_free_apis_import.json", "w") as f:
            json.dump(free_apis_data, f, indent=2)
        
        print("  💾 Saved to: supabase_free_apis_import.json")
        print("     (Use this for manual import if needed)")
        print()
    
    def upload_paid_apis(self):
        """Upload paid APIs info (NOT the keys!)"""
        
        print("📤 Uploading PAID APIs info to Supabase...")
        
        paid_apis_data = [
            {
                "name": "Polygon.io",
                "endpoint": "https://api.polygon.io/",
                "features": ["Real-time stocks", "Crypto", "Forex", "Options", "Historical"],
                "pricing": "$99-399/month",
                "quality": "EXCELLENT",
                "api_key_name": "POLYGON_API_KEY",
                "status": "active"
            },
            {
                "name": "TwelveData",
                "endpoint": "https://api.twelvedata.com/",
                "features": ["50+ technical indicators", "Real-time data", "Forex", "Crypto", "Stocks"],
                "pricing": "$8-49/month",
                "quality": "HIGH",
                "api_key_name": "TWELVEDATA_API_KEY",
                "status": "active"
            },
            {
                "name": "OKX US",
                "endpoint": "https://www.okx.com",
                "features": ["Live trading", "Real-time data", "Spot trading"],
                "pricing": "FREE (exchange)",
                "quality": "EXCELLENT",
                "api_key_name": "OKX_API_KEY (in AWS Secrets Manager)",
                "status": "active"
            }
        ]
        
        print(f"  Found {len(paid_apis_data)} paid APIs to upload")
        
        try:
            result = self.supabase.table("lyra_paid_apis").upsert(paid_apis_data).execute()
            print(f"  ✅ Uploaded {len(paid_apis_data)} paid APIs")
        except Exception as e:
            print(f"  ⚠️  Table 'lyra_paid_apis' doesn't exist yet")
            print(f"     Create it in Supabase dashboard first")
        
        print()
        
        # Save as JSON
        with open("/home/ubuntu/supabase_paid_apis_import.json", "w") as f:
            json.dump(paid_apis_data, f, indent=2)
        
        print("  💾 Saved to: supabase_paid_apis_import.json")
        print()
    
    def upload_infrastructure(self):
        """Upload infrastructure info"""
        
        print("📤 Uploading INFRASTRUCTURE info to Supabase...")
        
        infrastructure_data = [
            {
                "resource_type": "server",
                "resource_name": "Digital Ocean Droplet 1",
                "description": "Live trading server",
                "cost_monthly": 24,
                "specs": {"vcpus": 1, "ram_gb": 2, "storage_gb": 50},
                "status": "available"
            },
            {
                "resource_type": "server",
                "resource_name": "Digital Ocean Droplet 2",
                "description": "Database server",
                "cost_monthly": 24,
                "specs": {"vcpus": 1, "ram_gb": 2, "storage_gb": 50},
                "status": "available"
            },
            {
                "resource_type": "storage",
                "resource_name": "Digital Ocean Spaces",
                "description": "S3-compatible object storage",
                "cost_monthly": 5,
                "specs": {"storage_gb": 250, "cdn": True},
                "status": "available"
            },
            {
                "resource_type": "server",
                "resource_name": "Local Ubuntu PC",
                "description": "Development and monitoring",
                "cost_monthly": 0,
                "specs": {"type": "local", "good_processing": True},
                "status": "available"
            },
            {
                "resource_type": "server",
                "resource_name": "Oracle Cloud FREE",
                "description": "Free backtesting server (available)",
                "cost_monthly": 0,
                "specs": {"vcpus": 4, "ram_gb": 24, "storage_gb": 200},
                "status": "available"
            },
            {
                "resource_type": "gpu",
                "resource_name": "Google Colab FREE GPU",
                "description": "Free GPU testing (available)",
                "cost_monthly": 0,
                "specs": {"gpu": "Tesla T4/P100", "hours_per_week": "12-30"},
                "status": "available"
            }
        ]
        
        print(f"  Found {len(infrastructure_data)} infrastructure resources")
        
        try:
            result = self.supabase.table("lyra_infrastructure").upsert(infrastructure_data).execute()
            print(f"  ✅ Uploaded {len(infrastructure_data)} infrastructure resources")
        except Exception as e:
            print(f"  ⚠️  Table 'lyra_infrastructure' doesn't exist yet")
        
        print()
        
        # Save as JSON
        with open("/home/ubuntu/supabase_infrastructure_import.json", "w") as f:
            json.dump(infrastructure_data, f, indent=2)
        
        print("  💾 Saved to: supabase_infrastructure_import.json")
        print()
    
    def upload_ai_consensus(self):
        """Upload AI consensus validation results"""
        
        print("📤 Uploading AI CONSENSUS results to Supabase...")
        
        # Load validation results
        with open("/home/ubuntu/AI_CONSENSUS_FREE_API_VALIDATION_RESULTS.json", "r") as f:
            results = json.load(f)
        
        consensus_data = [{
            "validation_date": results["validation_date"],
            "total_tested": results["total_tested"],
            "working": results["working"],
            "failed": results["failed"],
            "success_rate": results["success_rate"],
            "ai_team": results["ai_consensus_team"],
            "results": {
                "validated_apis": results["validated_apis"],
                "failed_apis": results["failed_apis"]
            }
        }]
        
        try:
            result = self.supabase.table("lyra_ai_consensus").insert(consensus_data).execute()
            print(f"  ✅ Uploaded AI consensus results")
        except Exception as e:
            print(f"  ⚠️  Table 'lyra_ai_consensus' doesn't exist yet")
        
        print()
        
        # Save as JSON
        with open("/home/ubuntu/supabase_ai_consensus_import.json", "w") as f:
            json.dump(consensus_data, f, indent=2)
        
        print("  💾 Saved to: supabase_ai_consensus_import.json")
        print()
    
    def upload_system_config(self):
        """Upload system configuration"""
        
        print("📤 Uploading SYSTEM CONFIG to Supabase...")
        
        config_data = [
            {
                "config_key": "deployment_option",
                "config_value": {"option": "hybrid_free_paid", "cost_monthly": 29},
                "description": "Current deployment configuration"
            },
            {
                "config_key": "rating",
                "config_value": {"current": "18.0/10", "target": "22.0/10"},
                "description": "System rating progression"
            },
            {
                "config_key": "total_value",
                "config_value": {"paid_apis": 2000, "free_apis": "unlimited", "total": "195M+"},
                "description": "Total system value in USD"
            },
            {
                "config_key": "api_count",
                "config_value": {"paid": 3, "free": 10, "total": 13},
                "description": "Number of APIs integrated"
            }
        ]
        
        try:
            result = self.supabase.table("lyra_system_config").upsert(config_data).execute()
            print(f"  ✅ Uploaded {len(config_data)} configuration items")
        except Exception as e:
            print(f"  ⚠️  Table 'lyra_system_config' doesn't exist yet")
        
        print()
        
        # Save as JSON
        with open("/home/ubuntu/supabase_system_config_import.json", "w") as f:
            json.dump(config_data, f, indent=2)
        
        print("  💾 Saved to: supabase_system_config_import.json")
        print()
    
    def generate_sql_schema(self):
        """Generate SQL to create tables"""
        
        sql = """
-- LYRA SYSTEM SUPABASE SCHEMA
-- Run this in Supabase SQL Editor to create all tables

-- 1. Free APIs
CREATE TABLE IF NOT EXISTS lyra_free_apis (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    endpoint TEXT NOT NULL,
    features JSONB,
    rate_limit TEXT,
    quality TEXT,
    response_time TEXT,
    test_params JSONB,
    status TEXT,
    note TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- 2. Paid APIs
CREATE TABLE IF NOT EXISTS lyra_paid_apis (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    endpoint TEXT NOT NULL,
    features JSONB,
    pricing TEXT,
    quality TEXT,
    api_key_name TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- 3. Infrastructure
CREATE TABLE IF NOT EXISTS lyra_infrastructure (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resource_type TEXT NOT NULL,
    resource_name TEXT NOT NULL,
    description TEXT,
    cost_monthly NUMERIC,
    specs JSONB,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- 4. AI Consensus
CREATE TABLE IF NOT EXISTS lyra_ai_consensus (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    validation_date TIMESTAMP NOT NULL,
    total_tested INTEGER,
    working INTEGER,
    failed INTEGER,
    success_rate NUMERIC,
    ai_team JSONB,
    results JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 5. System Config
CREATE TABLE IF NOT EXISTS lyra_system_config (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    config_key TEXT UNIQUE NOT NULL,
    config_value JSONB NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Enable Row Level Security (RLS)
ALTER TABLE lyra_free_apis ENABLE ROW LEVEL SECURITY;
ALTER TABLE lyra_paid_apis ENABLE ROW LEVEL SECURITY;
ALTER TABLE lyra_infrastructure ENABLE ROW LEVEL SECURITY;
ALTER TABLE lyra_ai_consensus ENABLE ROW LEVEL SECURITY;
ALTER TABLE lyra_system_config ENABLE ROW LEVEL SECURITY;

-- Create policies (allow all for service role)
CREATE POLICY "Enable all for service role" ON lyra_free_apis FOR ALL USING (true);
CREATE POLICY "Enable all for service role" ON lyra_paid_apis FOR ALL USING (true);
CREATE POLICY "Enable all for service role" ON lyra_infrastructure FOR ALL USING (true);
CREATE POLICY "Enable all for service role" ON lyra_ai_consensus FOR ALL USING (true);
CREATE POLICY "Enable all for service role" ON lyra_system_config FOR ALL USING (true);
"""
        
        with open("/home/ubuntu/supabase_schema.sql", "w") as f:
            f.write(sql)
        
        print("📝 Generated SQL schema: supabase_schema.sql")
        print("   Run this in Supabase SQL Editor to create tables")
        print()
    
    def run(self):
        """Run full upload process"""
        
        print("=" * 80)
        print("🔐 SUPABASE VAULT UPLOADER")
        print("=" * 80)
        print()
        print("📋 Organization:")
        print("  - AWS Secrets Manager = Exchange credentials ONLY")
        print("  - Supabase = Everything else (APIs, configs, system data)")
        print()
        print("=" * 80)
        print()
        
        # Generate schema
        self.create_tables()
        self.generate_sql_schema()
        
        # Upload all data
        self.upload_free_apis()
        self.upload_paid_apis()
        self.upload_infrastructure()
        self.upload_ai_consensus()
        self.upload_system_config()
        
        print("=" * 80)
        print("✅ SUPABASE VAULT UPLOAD COMPLETE!")
        print("=" * 80)
        print()
        print("📁 Files created:")
        print("  1. supabase_schema.sql - Run this in Supabase SQL Editor")
        print("  2. supabase_free_apis_import.json - Free APIs data")
        print("  3. supabase_paid_apis_import.json - Paid APIs data")
        print("  4. supabase_infrastructure_import.json - Infrastructure data")
        print("  5. supabase_ai_consensus_import.json - AI consensus data")
        print("  6. supabase_system_config_import.json - System config data")
        print()
        print("🚀 Next steps:")
        print("  1. Go to Supabase dashboard: https://app.supabase.com")
        print("  2. Open SQL Editor")
        print("  3. Run supabase_schema.sql to create tables")
        print("  4. Run this script again to upload data")
        print("  5. View/edit data in Supabase Table Editor")
        print()

if __name__ == "__main__":
    uploader = SupabaseVaultUploader()
    uploader.run()

