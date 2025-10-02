
import psutil
import json
import time
from datetime import datetime

def collect_metrics():
    return {
        "timestamp": datetime.now().isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "load_average": list(psutil.getloadavg()),
        "network_io": psutil.net_io_counters()._asdict()
    }

if __name__ == "__main__":
    while True:
        metrics = collect_metrics()
        with open('/home/ubuntu/ultimate_lyra_v5/logs/system_metrics.json', 'w') as f:
            json.dump(metrics, f, indent=2)
        time.sleep(60)
