import multiprocessing
import time


def f(n):
    sum = 0
    for i in range(10000):
        sum += i * i
    return sum


if __name__ == '__main__':
    array = [2, 3, 4]

    t1 = time.time()
    p = multiprocessing.Pool()
    result = p.map(f, range(10000))
    p.close()
    p.join()
    print("Pool took: ", time.time()-t1)

    t2 = time.time()
    r = []
    for i in range(10000):
        r.append(f(i))
    print("Serial processing took: ", time.time()-t2)
