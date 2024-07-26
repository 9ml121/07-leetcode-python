def incrementing_generator(start=0):
    num = start
    while True:
        yield num
        num += 1


if __name__ == '__main__':
    my_iterator = incrementing_generator()
    print(next(my_iterator))  # 输出0
    print(next(my_iterator))  # 输出1
    print(next(my_iterator))  # 输出2


def fun():
    a = 3
    b = 4
    res = a + b
