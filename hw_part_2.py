import time
from multiprocessing import cpu_count, Pool


def factorize(*number):
    res = []
    for num in number:
        lst = []
        for n in range(1, num + 1):
            if num % n == 0:
                lst.append(n)
        res.append(lst)
    return res


if __name__ == '__main__':

    start = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    finish = time.time()
    print(f'Time: {finish - start}')

    start_pool = time.time()
    with Pool(cpu_count()) as pool:
        a, b, c, d = pool.map(factorize, [128, 255, 99999, 10651060])
        pool.close()
        pool.join()
    finish_pool = time.time()
    print(f'Pool time: {finish_pool - start_pool}')
