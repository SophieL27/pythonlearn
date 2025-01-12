import platform
#获取操作系统的平台
platform_name = platform.system()
print("Platform name:",platform_name)

#获取操作系统的版本
platform_version = platform.version()
print("Platform Version:", platform_version)

#获取操作系统发行版本
platform_release = platform.release()
print("Platform release:", platform_release)

#获取机器类型
machine_type = platform.machine()
print("Machine type:", machine_type)

#获取操作系统的处理器名称
processor_info = platform.processor()
print("Processor info:", processor_info)

#获取构建的python平台
python_build = platform.python_build()
print("Python build:", python_build)

#获取构建的python版本
python_version = platform.python_version()
print("Python version:", python_version)

#获取统一资源标识符（URI）的操作系统名称
uname = platform.uname()
print("Uname:", uname)