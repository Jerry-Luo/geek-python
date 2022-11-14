from timeit import timeit, repeat


def func():
    s = 0
    for i in range(1000):
        s += i
        print(s)


t = timeit('func()', 'from__main__import func', number=1000)
print(t)

t = repeat('func()', 'from __main__import func', number=100, repeat=5)
print(t)
print(min(t))
