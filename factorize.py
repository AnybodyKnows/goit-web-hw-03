from time import time
from threading import Thread
import multiprocessing
import logging


def factorize_single(num, result):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    result.append(factors)


def factorize(* numbers):
    result = []
    threads = []

    for num in numbers:
        thread = Thread(name=f"Thread {num}", target=factorize_single, args=(num, result))
        thread.start()
        logging.info("Started")
        threads.append(thread)

    for thread in threads:
        logging.info("joining thread")
        thread.join()

    return result


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
timer_start = time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
timer_end = time()
print(time()-timer_start)
print(multiprocessing.cpu_count())

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]