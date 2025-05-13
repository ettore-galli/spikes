import random
import time
from typing import Any, Generator, List

import concurrent.futures


def generate_data(number_of_entries: int):
    """
    Generate a list of dictionaries with random data.
    Each dictionary contains:
        - name: a random name
        - age: a random age between 18 and 99
        - email: a random email address
    """
    import random
    import string

    def random_name():
        return "".join(
            random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)
        )

    def random_age():
        return random.randint(18, 99)

    def random_email():
        return "".join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"

    data = []
    for _ in range(number_of_entries):
        data.append(
            {"name": random_name(), "age": random_age(), "email": random_email()}
        )

    return data


def load_domain_parallel(n_streams: int = 4) -> List[Generator[Any, None, None]]:
    """
    Distribuisce i record del dominio in n stream paralleli in modo equidistribuito.

    Args:
        n_streams: Numero di stream paralleli da generare

    Returns:
        Lista di generatori, ciascuno contenente una porzione equidistribuita dei record
    """
    # Prima carica tutti i record in memoria
    all_records = generate_data(number_of_entries=100)

    # Crea n bucket vuoti
    buckets = [[] for _ in range(n_streams)]

    # Distribuisce i record nei bucket (round-robin)
    for i, record in enumerate(all_records):
        bucket_idx = i % n_streams
        buckets[bucket_idx].append(record)

    # Crea un generatore per ogni bucket
    def create_generator(records):
        for record in records:
            yield record

    return [create_generator(bucket) for bucket in buckets]


def process_generator(gen_id, gen):
    print(f"Thread {gen_id} starting")
    for entry in gen:
        print(f"Generator {gen_id}: {entry}")
        time.sleep(random.random())  # Simulate some processing time
    print(f"Thread {gen_id} completed")


if __name__ == "__main__":

    generators = load_domain_parallel(n_streams=4)

    # Creazione di un thread pool per elaborare i generatori in parallelo
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Sottometti ciascun generatore al thread pool
        futures = [
            executor.submit(process_generator, i, gen)
            for i, gen in enumerate(generators)
        ]

        # Attendi il completamento di tutti i thread
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Thread error: {e}")
