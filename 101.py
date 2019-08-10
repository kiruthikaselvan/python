stri,n=map(str,input().split())
if int(n)==1:
    print(stri[-1])
else:
    print(stri[:int(n)-1:-1])
