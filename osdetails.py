# import psutil

# print("""Operating System Details:""")
# print("Cpu Percent:", psutil.cpu_percent(interval=5))
# print("Memory Usage:", psutil.virtual_memory().percent)

import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)

    print("CPU Usage:", cpu, "%")

    time.sleep(1)