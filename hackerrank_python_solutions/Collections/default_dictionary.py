from collections import defaultdict as d

if __name__ == '__main__':
    dfd = d(list)
    n, m = [int(i) for i in input().strip().split(" ")]
    for i in range(n):
        dfd[input().strip()].append(i + 1)
    for i in range(m):
        inp = input().strip()
        if dfd[inp]:
            for j in dfd[inp]:
                print(j, end=" ")
            print()
        else:
            print(-1)
