s=input()
l=["a","e","i","o","u","A","E","I","O","U"]
if s.isalpha():
    if s in l:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
