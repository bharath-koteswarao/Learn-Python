if __name__ == '__main__':
    input()
    a = [int(i) for i in input().strip().split(" ")]
    a = list(set(a))
    a.sort()
    print(a[-2])
