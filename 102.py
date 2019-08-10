def check(num):
    if num%2==0:
        num=num//2
        print(num)
        check(num)
n=int(input())
if n%2==0:
    check(n)
else:
    print(n)
