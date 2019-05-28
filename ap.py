l1=list(map(int,input().split()))
n=l1[0]
s=l1[1]
d=l1[2]
l=[s]
c=s
for i in range(n-1):
    c=c+d
    l.append(c)
print(sum(l))
