"""
With named tuples we can almost eliminate creating a class

"""
if __name__ == '__main__':
    n, ind, l = int(input().strip()), input().strip().split().index("MARKS"), []
    print("{:.2f}".format(sum([int(input().strip().split()[ind]) for i in range(n)]) / n))
