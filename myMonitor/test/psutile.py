import psutil
pid=13724
try:
    proc = psutil.Process(pid)
    print(f"Process Name: {proc.name()}")
    print(f"Process Username: {proc.username()}")
    print(f"Process CPU Usage: {proc.cpu_percent()}%")
    print(f"Process Memory Usage: {proc.memory_percent()}")
except psutil.NoSuchProcess:
    print(f"No process found with PID {pid}")