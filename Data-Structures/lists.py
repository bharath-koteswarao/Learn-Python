from collections import deque

q = deque([])
for i in range(0, 10):
    q.append(i)
print(q)

q.popleft()

print(q)

"""deque can be used as stack as well as queue"""

print(q.pop())
print(q)
