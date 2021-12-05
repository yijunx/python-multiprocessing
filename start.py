import time

start = time.perf_counter()


def do_something():
    print("Sleep 1 seconds")
    time.sleep(1)
    print("Done sleeping")


do_something()
do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
