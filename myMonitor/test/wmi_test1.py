import wmi
#创建wmi客户端
c = wmi.WMI()
#查询操作系统名称
for os in c.Win32_OperatingSystem():
    print("操作系统名称:",os.Caption)