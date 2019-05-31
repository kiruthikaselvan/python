l=[".","~","!","@","#","$","%","^","&","*",":","_","+","-"]
c=0
str=input()
for i in str:
    if i in l:
        c=c+1
print(c)
