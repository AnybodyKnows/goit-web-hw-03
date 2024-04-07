from time import time
from threading import Thread
import multiprocessing


def factorize(* numbers):
    factorize_list = []
    for num in numbers:
        factors = [i for i in range(1, num+1) if num % i == 0]
        factorize_list.append(factors)
    return factorize_list


timer_start = time()
d = factorize(106510600)
timer_end = time()
print(time()-timer_start)


# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [[1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]]