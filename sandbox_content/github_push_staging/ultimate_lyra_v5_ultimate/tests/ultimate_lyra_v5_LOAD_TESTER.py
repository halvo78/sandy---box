
import asyncio
import aiohttp
import time
from datetime import datetime

async def load_test():
    urls = [
        "http://localhost:8800/api/health",
        "http://localhost:8105/api/health", 
        "http://localhost:8103/api/health",
        "http://localhost:8102/api/health"
    ]
    
    results = {
        "start_time": datetime.now().isoformat(),
        "total_requests": 0,
        "successful_requests": 0,
        "failed_requests": 0,
        "average_response_time": 0,
        "url_results": {}
    }
    
    async with aiohttp.ClientSession() as session:
        for url in urls:
            url_results = {"requests": 0, "successes": 0, "failures": 0, "response_times": []}
            
            for i in range(10):  # 10 requests per URL
                start_time = time.time()
                try:
                    async with session.get(url, timeout=5) as response:
                        response_time = time.time() - start_time
                        url_results["response_times"].append(response_time)
                        url_results["requests"] += 1
                        
                        if response.status == 200:
                            url_results["successes"] += 1
                            results["successful_requests"] += 1
                        else:
                            url_results["failures"] += 1
                            results["failed_requests"] += 1
                            
                except Exception as e:
                    url_results["failures"] += 1
                    results["failed_requests"] += 1
                
                results["total_requests"] += 1
            
            url_results["average_response_time"] = sum(url_results["response_times"]) / len(url_results["response_times"]) if url_results["response_times"] else 0
            results["url_results"][url] = url_results
    
    results["end_time"] = datetime.now().isoformat()
    results["success_rate"] = (results["successful_requests"] / results["total_requests"]) * 100 if results["total_requests"] > 0 else 0
    
    return results

if __name__ == "__main__":
    import json
    results = asyncio.run(load_test())
    with open('/home/ubuntu/ultimate_lyra_v5/load_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Load test completed. Success rate: {results['success_rate']:.1f}%")
