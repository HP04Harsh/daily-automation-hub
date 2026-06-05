import psutil
import time

# CPU threshold
CPU_THRESHOLD = 80

# Processes to kill if CPU is too high
UNWANTED_PROCESSES = [
    "chrome.exe",
    "spotify.exe",
    "discord.exe"
]

def get_network_usage():
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    upload = (net2.bytes_sent - net1.bytes_sent) / 1024 / 1024
    download = (net2.bytes_recv - net1.bytes_recv) / 1024 / 1024

    return upload, download

def kill_unwanted_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in UNWANTED_PROCESSES:
                print(f"Killing: {proc.info['name']}")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    upload, download = get_network_usage()

    print("\n===== System Monitor =====")
    print(f"CPU Usage      : {cpu_usage}%")
    print(f"Upload Speed   : {upload:.2f} MB/s")
    print(f"Download Speed : {download:.2f} MB/s")

    if cpu_usage > CPU_THRESHOLD:
        print("\n⚠ High CPU Usage Detected!")
        kill_unwanted_processes()

    time.sleep(5)