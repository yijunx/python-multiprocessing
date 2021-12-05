import time
import multiprocessing
from typing import List


def do_something(seconds: int):
    print(f"Sleep {seconds} seconds")
    time.sleep(seconds)
    print(f"Done sleeping {seconds}")


if __name__ == "__main__":
    start = time.perf_counter()
    processes: List[multiprocessing.Process] = []
    for _ in range(10):
        # even though we have more processes than cores
        # computer can switch between cores when some core isnt too busy
        p = multiprocessing.Process(target=do_something, args=[1.5])
        # argument must be able to serialized with pickle!
        # it will be picked and back to normal at another process!
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")
