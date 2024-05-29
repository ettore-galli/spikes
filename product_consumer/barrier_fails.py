import threading
import queue
import time

q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(f"Working on {item}")
        print(f"Finished {item}")
        q.task_done()


def producer():
    for item in range(30):
        time.sleep(1)
        q.put(item)


# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
threading.Thread(target=producer, daemon=True).start()

# Block until all tasks are done.
q.join()

print("All work completed")
