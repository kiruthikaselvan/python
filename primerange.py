l=list(map(int,input().split()))
start=l[0]
end=l[1]
if start==1:
    start=start+1
for x in range(start,end+1):
    count=0
    for y in range(1,x+1):
        if x%y==0:
            count=count+1
    if count==2:
        print(x,end=" ")
