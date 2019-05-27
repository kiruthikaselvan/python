l=list(map(int,input().split()))
l1=list(map(int,input().split()))
n=l[0]
k=l[1]
sum=0
for i in range(k):
    sum=sum+l1[i]
print(sum)
