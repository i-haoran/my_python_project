import time
import functools


def repeat(n=1):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            total_time = 0
            for i in range(n):
                start = time.time()
                try:
                    result = func(*args, **kwargs)
                    end = time.time()
                    run_time = end - start
                    total_time += run_time
                    results.append(result)
                    print(
                        f"第{i + 1}次执行成功,结果为:{result},运行时间为:{run_time:.2f}"
                    )
                except Exception as e:
                    print(f"第{i + 1}次执行失败,失败原因:{e}")
            print(f"总共执行{n}次,平均时间{total_time / n:.2f}")
            return results[-1]

        return wrapper

    return decorate


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Log]:{func.__name__}开始执行:")
        try:
            result = func(*args, **kwargs)
            print(f"[Log]:{func.__name__}执行成功,返回值:{result}")
            return result
        except Exception as e:
            print(f"[Log]:{func.__name__}执行失败,报错:{e}")
            raise

    return wrapper


@repeat(3)
@log
def add(a, b):
    """加法函数，返回两数之和"""
    return a + b


result = add(5, 3)
print(f"最终结果: {result}")
print(f"函数名: {add.__name__}")
print(f"文档: {add.__doc__}")
