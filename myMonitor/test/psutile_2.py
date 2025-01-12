import psutil
count=0
for proc in psutil.process_iter(['pid',
                                'name','cpu_percent',
                                'memory_percent','status']):
    count+=1

    #获取进程信息
    pid=proc.info['pid']
    name=proc.info['name']
    cpu_percent=proc.info['cpu_percent']
    memory_percent=proc.info['memory_percent']
    status=proc.info['status']

    sys_info=f'pid={pid}'
    sys_info+=f' name={name}'
    sys_info+=(f' cpu_percent='
               f'{cpu_percent if cpu_percent is not None else 0.00}')
    sys_info+=(f' memory_percent='
               f'{memory_percent if memory_percent is not None else 0.00}')
    sys_info+=f' status={status}'

    print(sys_info)