import multiprocessing

result = []


def cal_square(x, result, v):
    v.value = 5.67
    for idx, i in enumerate(x):
        result[idx] = i * i
        print("inside process: ", result[:])


if __name__ == '__main__':
    l = [2, 3, 4, 5]
    result = multiprocessing.Array('i', len(l))
    v = multiprocessing.Value('d', 0.0)

    p1 = multiprocessing.Process(target=cal_square, args=(l, result, v))
    p1.start()
    p1.join()
    print("outside process: ", str(result))
    print(result[:])
    print(v.value)
