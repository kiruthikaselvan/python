l=list(map(int,input().split()))
start=l[0]
end=l[1]
for x in range(start+1,end):
    if x%2==0:
        print(x,end=" ")
        
