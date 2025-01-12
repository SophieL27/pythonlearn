import psutil
#获取当前登录用户列表
login_users = psutil.users()
for user in login_users:
    print("用户名:", user.name)
    print("终端:", user.terminal)
    print("主机:", user.host)
    print("启动(登录)时间:", user.started)
    print("进程ID:", user.pid)