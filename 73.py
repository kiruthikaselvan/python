ele=int(input())
l,u=map(int,input().split())
for i in range(l,u+1):
    if i==ele:
        print("yes")
        break
else:
    print("no")
