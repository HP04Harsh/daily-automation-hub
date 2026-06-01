import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

# Store last 50 data points
x_data = deque(maxlen=50)
cpu_data = deque(maxlen=50)
mem_data = deque(maxlen=50)

fig, ax = plt.subplots(figsize=(10, 5))

def update(frame):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    x_data.append(len(x_data))
    cpu_data.append(cpu)
    mem_data.append(mem)

    ax.clear()
    ax.plot(cpu_data, label="CPU Usage (%)")
    ax.plot(mem_data, label="Memory Usage (%)")

    ax.set_ylim(0, 100)
    ax.set_title("Real-Time CPU & Memory Monitoring")
    ax.set_xlabel("Time")
    ax.set_ylabel("Usage (%)")
    ax.legend()
    ax.grid(True)

ani = FuncAnimation(fig, update, interval=1000)

plt.tight_layout()
plt.show()