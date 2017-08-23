def calculate_fib(n):
    a, b = 0, 1
    l = []
    while a < n:
        l.append(a)
        a, b = b, a + b
    return l


a = calculate_fib(int(input('Fibonacci series below ? ')))
print(a)
print(len(a))
