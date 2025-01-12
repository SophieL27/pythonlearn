import psutil
#获取磁盘分区信息
partitions = psutil.disk_partitions()
for partition in partitions:
    print("分区:", partition)
#获取磁盘总容量
disk_usage = psutil.disk_usage("/")
print(f"磁盘使用情况：总容量{disk_usage.total/1024**3:.2f}GB,"
      f""f" 已用空间{disk_usage.used/1024**3:.2f}GB,"
      f"可用{disk_usage.free/1024**3:.2f}GB")
#获得磁盘IO信息
disk_io = psutil.disk_io_counters()
print(f"读取次数：{disk_io.read_count},"
      f"写入次数：{disk_io.write_count}")