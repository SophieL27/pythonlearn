import threading
import time
import random

def sing_song(name, song):
    while True:  # 使用一个无限循环
        print(f"{name} 唱 : {song}")
        time.sleep(random.uniform(1, 3))  # 随机暂停1到3秒之间

# 定义不同人的祝福歌曲
songs = {
    '小红': '新年好呀,新年好呀!',
    '小黄': '祝福大家新年好!',
    '小蓝': '我们唱歌,我们跳舞,祝福大家新年好!'
}

# 创建多个线程
threads = []
for name, song in songs.items():
    thread = threading.Thread(target=sing_song, name=name, args=(name, song))
    threads.append(thread)
    thread.start()


# for thread in threads:
#     thread.join()