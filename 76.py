ele1=int(input())
c=0
for i in range(1,ele1+1):
    if ele1%i==0:
        c=c+1
if c>2:
    print("yes")
else:
    print("no")
