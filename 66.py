w=int(input())
c=1
for i in range(2,w+1):
    if w%i==0:
        c=c+1
if c==2:
    print("yes")
else:
    print("no")
