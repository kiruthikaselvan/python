ele1,ele2=map(int,input().split())
pro=ele1*ele2
for i in range(0,20):
    if pro==i**2:
        print("yes")
        break
else:
    print("no")
