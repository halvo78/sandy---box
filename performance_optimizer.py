
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any

class PerformanceOptimizer:
    """Performance optimization utilities"""
    
    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(max_workers=20)
        self.async_semaphore = asyncio.Semaphore(50)  # Limit concurrent operations
        
    async def batch_execute(self, operations: List[Callable], batch_size: int = 10) -> List[Any]:
        """Execute operations in batches to prevent overload"""
        results = []
        
        for i in range(0, len(operations), batch_size):
            batch = operations[i:i + batch_size]
            
            async with self.async_semaphore:
                batch_results = await asyncio.gather(
                    *[self.execute_with_timeout(op) for op in batch],
                    return_exceptions=True
                )
                results.extend(batch_results)
                
            # Small delay between batches to prevent overwhelming
            await asyncio.sleep(0.1)
            
        return results
        
    async def execute_with_timeout(self, operation: Callable, timeout: float = 30.0) -> Any:
        """Execute operation with timeout"""
        try:
            return await asyncio.wait_for(operation(), timeout=timeout)
        except asyncio.TimeoutError:
            raise Exception(f"Operation timed out after {timeout} seconds")
            
    def optimize_cpu_usage(self):
        """Optimize CPU usage patterns"""
        # Set thread pool size based on CPU cores
        import os
        cpu_count = os.cpu_count() or 4
        optimal_threads = min(cpu_count * 2, 20)  # 2x CPU cores, max 20
        
        self.thread_pool._max_workers = optimal_threads
        
    async def memory_efficient_processing(self, data_stream, processor: Callable, chunk_size: int = 1000):
        """Process large datasets in memory-efficient chunks"""
        results = []
        chunk = []
        
        async for item in data_stream:
            chunk.append(item)
            
            if len(chunk) >= chunk_size:
                # Process chunk
                chunk_results = await processor(chunk)
                results.extend(chunk_results)
                
                # Clear chunk to free memory
                chunk.clear()
                
                # Allow other tasks to run
                await asyncio.sleep(0)
                
        # Process remaining items
        if chunk:
            chunk_results = await processor(chunk)
            results.extend(chunk_results)
            
        return results
