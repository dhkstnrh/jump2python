# thread_test.py
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"Working: {i}\n")

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End")
