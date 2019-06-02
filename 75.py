ele=input()
mid=len(ele)//2
if len(ele)%2!=0:
    for i in range(len(ele)):
        if i==mid:
            print("*",end="")
        else:
            print(ele[i],end="")
else:
    for i in range(len(ele)):
        if i==mid or i==mid-1:
            print("*",end="")
        else:
            print(ele[i],end="")
                    
