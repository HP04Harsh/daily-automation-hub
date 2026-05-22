import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    net = psutil.net_io_counters()

    print("\n===== SYSTEM MONITOR =====")
    print(f"CPU Usage : {cpu}%")
    print(f"RAM Usage : {ram}%")
    print(f"Upload    : {net.bytes_sent // (1024*1024)} MB")
    print(f"Download  : {net.bytes_recv // (1024*1024)} MB")

    time.sleep(5)