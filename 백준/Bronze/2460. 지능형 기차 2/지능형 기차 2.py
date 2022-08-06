maxsum = -1
prev = 0
for i in range(10):
    a,b = map(int,input().split())

    cur = b - a + prev
    maxsum = max(maxsum,cur)
    prev = cur

print(maxsum)