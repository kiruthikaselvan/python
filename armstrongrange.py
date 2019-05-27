l=list(map(int,input().split()))
s=l[0]
e=l[1]
for num in range(s+1,e):
    temp=num
    res=0
    while(num>0):
        r=num%10
        res=res+r**3
        num=num//10
    if res==temp:
       print(res,end=" ")
