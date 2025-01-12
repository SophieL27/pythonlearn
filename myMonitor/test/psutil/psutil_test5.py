import psutil
#获取网络IO信息
net_io = psutil.net_io_counters()
print(f"发送字节数:{net_io.bytes_sent},接收字节数:{net_io.bytes_recv}")
#获取网络接口信息
net_if_addrs = psutil.net_if_addrs()
for interface,addresses in net_if_addrs.items():
    for addr in addresses:
        print(f"接口 {interface} IP {addr.address}")