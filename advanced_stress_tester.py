
import asyncio
import aiohttp
import time
import gc
import psutil
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Any

class AdvancedStressTester:
    """
    Advanced stress testing suite for production readiness validation
    """
    
    def __init__(self):
        self.results = {}
        self.max_concurrent = 100
        self.test_duration = 60  # seconds
        
    async def concurrent_api_stress_test(self) -> Dict[str, Any]:
        """Test concurrent API operations"""
        start_time = time.time()
        successful_requests = 0
        failed_requests = 0
        response_times = []
        
        async def make_test_request(session, url):
            try:
                start = time.time()
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    end = time.time()
                    response_times.append(end - start)
                    if response.status == 200:
                        return True
                    else:
                        return False
            except Exception:
                return False
                
        async with aiohttp.ClientSession() as session:
            tasks = []
            test_urls = [
                "https://api.coinbase.com/v2/time",
                "https://api.polygon.io/v1/marketstatus/now",
                "https://api.coingecko.com/api/v3/ping"
            ]
            
            # Create concurrent requests
            for _ in range(self.max_concurrent):
                for url in test_urls:
                    task = make_test_request(session, url)
                    tasks.append(task)
                    
            # Execute all requests concurrently
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for result in results:
                if result is True:
                    successful_requests += 1
                else:
                    failed_requests += 1
                    
        end_time = time.time()
        
        return {
            "test_name": "Concurrent API Stress Test",
            "duration": end_time - start_time,
            "total_requests": len(tasks),
            "successful_requests": successful_requests,
            "failed_requests": failed_requests,
            "success_rate": (successful_requests / len(tasks)) * 100,
            "average_response_time": sum(response_times) / len(response_times) if response_times else 0,
            "max_response_time": max(response_times) if response_times else 0,
            "min_response_time": min(response_times) if response_times else 0
        }
        
    def memory_stress_test(self) -> Dict[str, Any]:
        """Test memory management under stress"""
        initial_memory = psutil.virtual_memory().percent
        
        # Allocate large amounts of memory
        test_data = []
        for i in range(1000):
            test_data.append([0] * 10000)  # Allocate memory
            
        peak_memory = psutil.virtual_memory().percent
        
        # Clean up explicitly
        del test_data
        gc.collect()
        
        # Wait for cleanup
        time.sleep(2)
        
        final_memory = psutil.virtual_memory().percent
        memory_recovered = (peak_memory - final_memory) > (peak_memory - initial_memory) * 0.8
        
        return {
            "test_name": "Memory Stress Test",
            "initial_memory_percent": initial_memory,
            "peak_memory_percent": peak_memory,
            "final_memory_percent": final_memory,
            "memory_increase": peak_memory - initial_memory,
            "memory_recovered": memory_recovered,
            "cleanup_effective": final_memory <= initial_memory + 1.0
        }
        
    def error_recovery_test(self) -> Dict[str, Any]:
        """Test error recovery mechanisms"""
        recovery_tests = []
        
        # Test 1: Network timeout recovery
        try:
            response = requests.get("http://httpbin.org/delay/10", timeout=2)
        except requests.exceptions.Timeout:
            recovery_tests.append({"test": "timeout_recovery", "passed": True})
        except Exception:
            recovery_tests.append({"test": "timeout_recovery", "passed": False})
            
        # Test 2: Invalid URL recovery
        try:
            response = requests.get("http://invalid-url-that-does-not-exist.com")
        except requests.exceptions.RequestException:
            recovery_tests.append({"test": "invalid_url_recovery", "passed": True})
        except Exception:
            recovery_tests.append({"test": "invalid_url_recovery", "passed": False})
            
        # Test 3: Memory allocation failure recovery
        try:
            # Try to allocate huge amount of memory
            huge_list = [0] * (10**9)  # This should fail
            recovery_tests.append({"test": "memory_allocation_recovery", "passed": False})
        except MemoryError:
            recovery_tests.append({"test": "memory_allocation_recovery", "passed": True})
        except Exception:
            recovery_tests.append({"test": "memory_allocation_recovery", "passed": True})
            
        passed_tests = sum(1 for test in recovery_tests if test["passed"])
        
        return {
            "test_name": "Error Recovery Test",
            "total_tests": len(recovery_tests),
            "passed_tests": passed_tests,
            "success_rate": (passed_tests / len(recovery_tests)) * 100,
            "individual_results": recovery_tests
        }
        
    def run_all_stress_tests(self) -> Dict[str, Any]:
        """Run all stress tests"""
        results = {}
        
        # Run concurrent API test
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            results["concurrent_api"] = loop.run_until_complete(self.concurrent_api_stress_test())
        finally:
            loop.close()
            
        # Run memory stress test
        results["memory_stress"] = self.memory_stress_test()
        
        # Run error recovery test
        results["error_recovery"] = self.error_recovery_test()
        
        return results

# Global instance
stress_tester = AdvancedStressTester()
