from time import time
from threading import Thread, current_thread
import multiprocessing
import logging


def factorize_single(start_num, end_num, whole_num, result):
    timer_start=time()
    factors = [i for i in range(start_num, end_num + 1) if whole_num % i == 0]
    for el in factors:
        result.append(el)
    logging.info(f'Finished factorizing at {time()}, time_consumed {time()-timer_start}')
    logging.info(f"Result: {factors}\n")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    result = []
    threads = []

    timer_start = time()
    whole_num = 106510600
    number_part = round(whole_num / multiprocessing.cpu_count())
    cpu_count = multiprocessing.cpu_count()
    for i in range(1, cpu_count+1):
        thread = Thread(name=f"Thread {i}", target=factorize_single, args=((i-1)*number_part+1, i*number_part, whole_num, result))
        thread.start()
        # threads.append(thread)

    # for thread in threads:
    #     logging.info("joining thread")
    #     thread.join()


    logging.info(time() - timer_start)
    logging.info(result)


# assert result == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]