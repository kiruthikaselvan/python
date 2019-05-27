l=list(map(int,input().split()))
s=l[0]
e=l[1]
for i in range(s+1,e):
    if i%2!=0:
        print(i,end=" ")
        
