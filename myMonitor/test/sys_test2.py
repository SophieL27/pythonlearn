import sys
#获取操作系统平台信息
platform_info= sys.platform
print("Platform:",platform_info)
if platform_info == "linux" or platform_info == "linux2":
    print("Running on Linux")
elif platform_info == "darwin":
    print("Running on macOS")
elif platform_info == "win32":
    print("Running on Windows")
else:
    print("Running on:",platform_info)



