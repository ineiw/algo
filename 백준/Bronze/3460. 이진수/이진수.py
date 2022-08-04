import sys
length = int(input())

data = []
for i in range(length):
    data.append(int(sys.stdin.readline()))

for i in range(length):
    case = data[i]
    moc = case
    cnt = 0
    for j in range(case):

        if moc%2 == 1:
            print(cnt,end=" ")

        moc = moc//2
        if(moc == 0):
            break

        cnt+=1

