num=int(input())
temp=num
res=0
while(num>0):
    r=num%10
    res=res+r**3
    num=num//10
if res==temp:
    print("yes")
else:
    print("no")
