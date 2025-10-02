"""
Ultimate Lyra Trading System - Commissioning Audit Phase 6: Performance & Scalability
====================================================================================
Performs stress testing on all system endpoints to measure performance under load.
"""

import asyncio
import httpx
import time
import json

# --- Configuration ---
REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/commissioning_phase6_report.md"

# Endpoints to test
ENDPOINTS = {
    "AI Enhanced Dashboard": "http://localhost:8751/health",
    "Maximum Amplification System": "http://localhost:9996/health",
    "Hummingbot Integration": "http://localhost:8400/health",
}

# Stress test parameters
CONCURRENT_REQUESTS = 100
TOTAL_REQUESTS = 1000

async def hit_endpoint(client, url):
    """Send a single GET request to an endpoint and return latency."""
    start_time = time.time()
    try:
        response = await client.get(url, timeout=10.0)
        latency = (time.time() - start_time) * 1000  # in ms
        if response.status_code == 200:
            return "success", latency
        else:
            return f"fail_{response.status_code}", latency
    except httpx.RequestError:
        latency = (time.time() - start_time) * 1000
        return "fail_connection", latency

async def stress_test_endpoint(endpoint_name, url):
    """Run a stress test on a single endpoint."""
    print(f"Stressing {endpoint_name} at {url}...")
    latencies = []
    status_counts = {"success": 0}

    async with httpx.AsyncClient() as client:
        # Create a semaphore to limit concurrency
        semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
        
        async def worker(request_num):
            async with semaphore:
                status, latency = await hit_endpoint(client, url)
                latencies.append(latency)
                status_counts[status] = status_counts.get(status, 0) + 1
                # Simple progress indicator
                if request_num % 100 == 0:
                    print(f"  {endpoint_name}: {request_num}/{TOTAL_REQUESTS} requests complete...")

        tasks = [worker(i) for i in range(TOTAL_REQUESTS)]
        await asyncio.gather(*tasks)

    # Calculate metrics
    successful_requests = status_counts.get("success", 0)
    failed_requests = TOTAL_REQUESTS - successful_requests
    success_rate = (successful_requests / TOTAL_REQUESTS) * 100 if TOTAL_REQUESTS > 0 else 0
    
    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        max_latency = max(latencies)
        min_latency = min(latencies)
        # Throughput: requests per second
        # This is a rough estimate as it doesn't account for ramp-up time
        total_time = sum(latencies) / 1000 / CONCURRENT_REQUESTS # Approximate total time
        throughput = TOTAL_REQUESTS / total_time if total_time > 0 else 0
    else:
        avg_latency = max_latency = min_latency = throughput = 0

    return {
        "name": endpoint_name,
        "total_requests": TOTAL_REQUESTS,
        "concurrent_requests": CONCURRENT_REQUESTS,
        "successful_requests": successful_requests,
        "failed_requests": failed_requests,
        "success_rate": f"{success_rate:.2f}%",
        "avg_latency_ms": f"{avg_latency:.2f}",
        "min_latency_ms": f"{min_latency:.2f}",
        "max_latency_ms": f"{max_latency:.2f}",
        "throughput_rps": f"{throughput:.2f}",
    }

async def generate_report():
    """Generate the final verification report for Phase 6."""
    report = "# Commissioning Audit Phase 6: Performance & Scalability Report\n\n"
    report += f"**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    report += f"**Test Parameters:** {TOTAL_REQUESTS} total requests with {CONCURRENT_REQUESTS} concurrent users per endpoint.\n\n"
    report += "## Stress Test Results\n\n"

    results = []
    for name, url in ENDPOINTS.items():
        result = await stress_test_endpoint(name, url)
        results.append(result)

    # Format results into a markdown table
    headers = ["Metric", "AI Enhanced Dashboard", "Maximum Amplification", "Hummingbot Integration"]
    keys = [
        ("Total Requests", "total_requests"),
        ("Concurrent Users", "concurrent_requests"),
        ("Successful Requests", "successful_requests"),
        ("Failed Requests", "failed_requests"),
        ("Success Rate", "success_rate"),
        ("Avg. Latency (ms)", "avg_latency_ms"),
        ("Min. Latency (ms)", "min_latency_ms"),
        ("Max. Latency (ms)", "max_latency_ms"),
        ("Throughput (RPS)", "throughput_rps"),
    ]
    
    report += f"| {' | '.join(headers)} |\n"
    report += f"|{'|'.join(['---'] * len(headers))}|\n"

    for metric_name, key in keys:
        row = [metric_name]
        for res in results:
            row.append(str(res.get(key, "N/A")))
        report += f"| {' | '.join(row)} |\n"

    with open(REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Phase 6 verification report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_report())

