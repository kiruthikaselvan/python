str1=input()
'''l=[]
x=[l.append(str(i)) for i in range(9)]
print(l)
c=0
for i in str1:
    if i in l:
        c=c+1
print(c)'''
c=0
for i in str1:
    if i.isdigit():
        c=c+1
print(c)
