import multiprocessing
import time


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == '__main__':
    b = multiprocessing.Value('i', 200)
    l = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(b,l))
    w = multiprocessing.Process(target=withdraw, args=(b,l))

    d.start()
    w.start()

    d.join()
    w.join()

    print("balance: ", b.value)
