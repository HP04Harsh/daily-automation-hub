import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Store data
cpu_data = []
net_data = []

# Network baseline
old_net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

# Graph setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

def update(frame):
    global old_net

    # Real CPU %
    cpu = psutil.cpu_percent()

    # Real Network Usage (KB/s)
    new_net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    net_speed = (new_net - old_net) / 1024
    old_net = new_net

    # Save latest values
    cpu_data.append(cpu)
    net_data.append(net_speed)

    # Keep last 20 points
    cpu_data[:] = cpu_data[-20:]
    net_data[:] = net_data[-20:]

    # Clear graphs
    ax1.clear()
    ax2.clear()

    # CPU Graph
    ax1.plot(cpu_data)
    ax1.set_title("CPU Usage (%)")
    ax1.set_ylim(0, 100)

    # Network Graph
    ax2.plot(net_data)
    ax2.set_title("Network Usage (KB/s)")

plt.tight_layout()

# Update every 1 second
ani = FuncAnimation(fig, update, interval=1000)

plt.show()