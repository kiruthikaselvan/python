str=list(map(str,input().split()))
s1=str[0]
s2=str[1]
if len(s1)==len(s2):
    print(s1)
else:
    if len(s1)>len(s2):
        print(s1)
    else:
        print(s2)
