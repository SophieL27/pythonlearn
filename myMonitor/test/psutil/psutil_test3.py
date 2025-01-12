import psutil
#获取CPU使用率
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU使用率: {cpu_usage}%")

#获取内存使用情况
memory=psutil.virtual_memory()
print(f"总内存：{memory.total / (1024**3):.2f}GB")
print(f"已使用内存：{memory.used / (1024**3):.2f}GB")
print(f"内存使用率：{memory.percent}%")
