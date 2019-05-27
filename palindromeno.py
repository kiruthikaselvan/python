num=int(input())
temp=num
res=0
while(num>0):
    rem=num%10
    res=res*10+rem
    num=num//10
if temp==res:
    print("yes")
else:
    print("no")
    
