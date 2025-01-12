import threading
import time

def print_numbers():
    for i in range(1,6):
        time.sleep(1)
        print(i)
    # while True:#会一直打印
    #     for i in range(1, 6):
    #         time.sleep(1)
    #         print(i)


# 创建两个线程
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# 启动两个线程
thread1.start()
thread2.start()

# 等待两个线程结束
thread1.join()
thread2.join()

print("All threads have finished.")