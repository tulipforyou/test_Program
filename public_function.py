import time
def gettime(func):  # 装饰器，用于计时
    def warapper(*args, **kwargs):
        print("=" * 50)
        print(func.__name__, 'start......')
        starttime = time.time()
        func(*args)
        endtime = time.time()
        spendtime = endtime - starttime
        print(func.__name__, 'end......')
        print("Spend ", spendtime, "s totally!")
        print("=" * 50)
    return warapper