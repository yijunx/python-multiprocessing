import time
import multiprocessing


def do_something():
    print("Sleep 1 seconds")
    time.sleep(1)
    print("Done sleeping")


if __name__ == "__main__":
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)
    p1.start()
    p2.start()

    # back here!!!
    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")
