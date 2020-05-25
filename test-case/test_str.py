def test1():
    for i in range(3):
        print(i)


def my_func(*args):
    fs = []
    for i in range(3):
        def func():
            return i * i

        fs.append(func)
    return fs


def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()

    return wrapper


def say_hello():
    print("hello!")


def test_exception(num):
    try:
        a = 1 / num
        return a
    except Exception as e:
        print(e)
    finally:
        print(" ========= ")


if __name__ == '__main__':
    print(test_exception(1))
