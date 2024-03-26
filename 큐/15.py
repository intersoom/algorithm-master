# 요세푸스 문제

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split(' '))

Q = deque([])
result = []

for i in range(1, N+1): Q.append(i)

count = 0

while len(Q) > 1:
  count += 1
  poped = Q.popleft()
  if count == K:
    result.append(str(poped))
    count = 0
  else:
    Q.append(poped)

result.append(str(Q.pop()))

print('<', end='')
print(', '.join(result), end='')
print('>')