import os

print("Zombie Processes:\n")

for pid in os.listdir("/proc"):
    if pid.isdigit():
        try:
            with open(f"/proc/{pid}/status", "r") as file:
                for line in file:
                    if line.startswith("State:"):
                        if "Z" in line:  # Z = Zombie
                            print(f"PID: {pid} -> {line.strip()}")
                        break
        except:
            pass