import time
import concurrent.futures


def do_something(seconds: int):
    print(f"Sleep {seconds} seconds")
    time.sleep(seconds)
    return f"Done sleeping {seconds}"


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # context manager will always join for you!!
        
        secs = [5, 4, 3, 2, 1]

        # with map
        results = executor.map(do_something, secs)
        # thought each task do not finish at some time
        # they will come out together with this method
        # the print order will be the order they started!
        # if there is exception, it will be raised below in the iterator below
        for r in results:
            print(r)

        # normal..
        # futures = [executor.submit(do_something, sec) for sec in secs]
        # for f in concurrent.futures.as_completed(futures):
        #     print(f.result())

        # manually...
        # f1 = executor.submit(do_something, 2)
        # f2 = executor.submit(do_something, 1)
        # print(f1.result())
        # print(f2.result())

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")
