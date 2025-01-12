import threading
import time

def print_greeting(name,greeting):
    while True:#使用一个无限循环
        print(f"{greeting}, {name}!")
        time.sleep(1)#暂停1秒

thread1 = threading.Thread(target=print_greeting,
                           name="process_load_1",
                           kwargs={"name":"Alice","greeting":"Hello"})
thread2 = threading.Thread(target=print_greeting,
                           name='process_load_2',
                           kwargs={'name': 'Bob','greeting': 'Hi'})
thread1.start()
thread2.start()

thread1.join()
thread2.join()