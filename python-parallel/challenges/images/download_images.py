#!/usr/bin/env python3
"""Challenge: Download a collection of images"""

from queue import Queue
from threading import Thread
import time
from typing import Any, List
import urllib.request
import multiprocessing as mp
import concurrent.futures

""" sequential implementation of multiple image downloader
    returns total bytes from downloading all images in image_numbers list """


def seq_download_images(image_numbers):
    total_bytes = 0
    for num in image_numbers:
        total_bytes += _download_image(num)
    return total_bytes


""" helper function returns number of bytes from downloading image """


def _download_image(image_number):
    image_number = (abs(image_number) % 50) + 1  # force between 1 and 50
    image_url = "http://699340.youcanlearnit.net/image{:03d}.jpg".format(image_number)
    try:
        with urllib.request.urlopen(image_url, timeout=60) as conn:
            return len(conn.read())  # number of bytes in downloaded image
    except urllib.error.HTTPError:
        print("HTTPError: Could not retrieve image ", image_number)
    except Exception as e:
        print(e)


def split_into_chunks(iterable: List[Any], chunk_size: int) -> List[List[Any]]:
    return [
        iterable[k * chunk_size : (k + 1) * chunk_size]
        for k in range(1 + len(iterable) // chunk_size)
        if k * chunk_size < len(iterable)
    ]


""" parallel implementation of multiple image downloader
    returns total bytes from downloading all images in image_numbers list """


def download_worker(requests_queue, results_queue):
    while True:
        image_number = requests_queue.get()
        if image_number == -1:
            break
        results_queue.put(_download_image(image_number=image_number))


def number_of_workers():
    return 2 * mp.cpu_count()


def par_download_images_q(image_numbers):
    tasks = []

    requests_q = Queue[int]()
    results_q = Queue[int]()

    number_of_tasks = number_of_workers()

    for _ in range(number_of_tasks):
        tasks.append(Thread(target=download_worker, args=(requests_q, results_q)))

    for task in tasks:
        task.start()

    for image_number in image_numbers:
        requests_q.put(image_number)

    for task in tasks:
        requests_q.put(-1)

    for task in tasks:
        task.join()

    total = 0
    while not results_q.empty():
        total += results_q.get()

    return total


def par_download_images_pool(image_numbers):
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=number_of_workers()
    ) as executor:
        return sum(
            [
                result.result()
                for result in concurrent.futures.as_completed(
                    [
                        executor.submit(_download_image, number)
                        for number in image_numbers
                    ]
                )
            ]
        )


def par_download_images(image_numbers):
    return par_download_images_pool(image_numbers=image_numbers)


if __name__ == "__main__":
    NUM_EVAL_RUNS = 1
    IMAGE_NUMBERS = list(range(1, 10))

    print("Evaluating Sequential Implementation...")
    sequential_result = seq_download_images(IMAGE_NUMBERS)
    sequential_time = 0.0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_download_images(IMAGE_NUMBERS)
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print("Evaluating Parallel Implementation...")
    parallel_result = par_download_images(IMAGE_NUMBERS)
    parallel_time = 0.0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_download_images(IMAGE_NUMBERS)
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    print(f"Sequential result : {sequential_result}")
    print(f"Parallel result   : {parallel_result}")

    if sequential_result != parallel_result:
        raise Exception("sequential_result and parallel_result do not match.")

    print("Average Sequential Time: {:.2f} ms".format(sequential_time * 1000))
    print("Average Parallel Time: {:.2f} ms".format(parallel_time * 1000))
    print("Speedup: {:.2f}".format(sequential_time / parallel_time))
    print(
        "Efficiency: {:.2f}%".format(
            100 * (sequential_time / parallel_time) / mp.cpu_count()
        )
    )
