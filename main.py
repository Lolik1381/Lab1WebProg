import math


def task1(number):
    return True if number == str(number)[::-1] else False


def task2(param):
    resultA = []
    resultB = []
    resultC = []
    for i in param:
        if i % 2 == 0:
            resultA.append(i)
        if i % 3 == 0:
            resultB.append(i)
        if i % 5 == 0:
            resultC.append(i)

    return resultA, resultB, resultC


def task3(number):
    if number >= 0:
        return int(str(number)[::-1])
    else:
        return -int(str(-number)[::-1])


def task4(power, number):
    startX = 1
    ep = 0.01
    power = float(power)

    def function():
        return 1 / power * ((power - 1) * startX + number / math.pow(startX, power - 1))

    while True:
        endX = function()
        if math.fabs(endX - startX) < ep:
            startX = endX
            break
        else:
            startX = endX

    return startX


def task5(number):
    for i in range(2, int(number / 2)):
        if number % i == 0:
            return False

    return True if number > 1 else False


def decorator2(count):
    def decorator(function):
        cache = {}
        countCache = {}

        def wrapper(*args, **kwargs):
            key = '{0} - {1}'.format(function.__name__, args)

            if not cache.get(key):
                result = function(*args, **kwargs)
                cache[key] = result
                countCache[key] = 1
                return result
            else:
                countCache[key] = countCache[key] + 1
                if countCache[key] > count:
                    countCache[key] = 0
                    cache[key] = None

                return cache[key]

        return wrapper

    return decorator
