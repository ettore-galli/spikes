import threading
import time
from datetime import datetime


class Subprocess(threading.Thread):
    def run(self):
        log("Subprocess started")
        time.sleep(5)
        log("Subprocess finished")


def log(*args, **kwargs):
    print(datetime.now(), *args, **kwargs)


def print_subprocess_status(subprocess: threading.Thread):
    log(
        f"...Subprocess {subprocess.name} is {'still' if subprocess.is_alive() else 'NOT'} running"
    )


def monitor_subprocess(subprocess: threading.Thread):
    while subprocess.is_alive():
        log(
            f"...Subprocess {subprocess.name} is {'still' if subprocess.is_alive() else 'NOT'} running"
        )
        time.sleep(0.1)
    log(f"...Subprocess {subprocess.name} has finished.")


def main():
    log("Main thread started")

    subprocess = Subprocess(name="sottoprocesso")
    
    monitor = threading.Thread(
        target=monitor_subprocess,
        args=(subprocess,),
        name="monitor_thread",
    )
    

    # print_subprocess_status(subprocess)
    subprocess.start()
    monitor.start()
    # print_subprocess_status(subprocess)

    log("Main thread is doing other work")
    time.sleep(2)
    log("Main thread finished")
    # print_subprocess_status(subprocess)
    subprocess.join()  # Wait for the subprocess to finish
    monitor.join()  # Wait for the monitor thread to finish
    # print_subprocess_status(subprocess)
    # log("Subprocess has finished")


if __name__ == "__main__":
    main()
    log("All threads have completed")
