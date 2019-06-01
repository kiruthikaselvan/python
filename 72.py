w=input()
l=["a","e","i","o","u","A","E","I","O","U"]
for i in w:
    if i in l:
        print("yes")
        break
else:
    print("no")
