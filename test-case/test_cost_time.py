import datetime


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        func_name = func.__name__
        over_time = datetime.datetime.now()  # 程序结束时间
        total_time = (over_time - start_time).total_seconds()
        print('程序 %s 共计耗时 %s 秒' % (func_name, total_time))

    return int_time


@count_time
def main():
    for i in range(1, 100):  # 可以是任意函数  ， 这里故意模拟函数的运行时间
        for j in range(i):
            print(j)

@count_time
def print_log():
    for i in range(100):
        for j in range(i):
            print(j)


if __name__ == '__main__':
    print_log()
