def test(a=4, b=10):
    return a * b


print(test())

print(test(100, 0.1))


def variable(*args):
    mul = 1
    for i in args:
        mul *= i
        print(mul)
    return mul


variable(1, 2, 3, 4)
