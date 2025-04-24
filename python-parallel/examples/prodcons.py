from dataclasses import dataclass

from queue import Queue
from typing import Union


@dataclass
class InputItemPayload:
    input: str


@dataclass
class ProcessedItemPayload:
    input: str


class PoisonPill: ...


InputQueue = Queue[Union[InputItemPayload, PoisonPill]]
OutputQueue = Queue[Union[ProcessedItemPayload, PoisonPill]]


class ChainableProcessor:

    def producer_worker(input_queue: InputQueue):
        pass


    def processor_worker(input_queue: InputQueue, output_queue: OutputQueue):
        pass


    def consumer_worker(output_queue: OutputQueue):
        pass


def main():
    inputQueue: InputQueue = InputQueue()
    outputQueue: OutputQueue = OutputQueue()

    # log("Main thread started")

    # subprocess = Subprocess(name="sottoprocesso")

    # monitor = threading.Thread(
    #     target=monitor_subprocess,
    #     args=(subprocess,),
    #     name="monitor_thread",
    # )

    # # print_subprocess_status(subprocess)
    # subprocess.start()
    # monitor.start()
    # # print_subprocess_status(subprocess)

    # log("Main thread is doing other work")
    # time.sleep(2)
    # log("Main thread finished")
    # # print_subprocess_status(subprocess)
    # subprocess.join()  # Wait for the subprocess to finish
    # monitor.join()  # Wait for the monitor thread to finish
    # # print_subprocess_status(subprocess)
    # # log("Subprocess has finished")


if __name__ == "__main__":
    main()
