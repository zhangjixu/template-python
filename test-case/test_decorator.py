import datetime


def count_time(fun):
    """
    统计函数运行时间
    Args:
        fun:

    Returns:

    """

    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        rs = fun(*args, **kwargs)
        end_time = datetime.datetime.now()  # 程序结束时间
        cost_time = (end_time - start_time).total_seconds()
        print(' funtion: %s cost_time: %s s' % (fun.__name__, cost_time))
        return rs

    return wrapper


@count_time
def test_count_time(num):
    return num


if __name__ == '__main__':
    print(test_count_time(10000))
