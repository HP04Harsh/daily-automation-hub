import psutil
import time

print("Checking inactive processes...\n")

for process in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent']):
    try:
        pid = process.info['pid']
        name = process.info['name']
        status = process.info['status']

        # Get CPU usage
        cpu = process.cpu_percent(interval=0.1)

        # Detect inactive processes
        if cpu == 0.0:
            print(f"PID: {pid}")
            print(f"Name: {name}")
            print(f"Status: {status}")
            print(f"CPU Usage: {cpu}%")
            print("-" * 30)

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass