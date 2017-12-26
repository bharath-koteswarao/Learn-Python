from collections import Counter as c

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    co = c(arr)
    ans = 0
    q = int(input().strip())
    for _ in range(q):
        a, b = [int(i) for i in input().strip().split(" ")]
        if co[a] > 0:
            ans += b
            co[a] -= 1
    print(ans)
