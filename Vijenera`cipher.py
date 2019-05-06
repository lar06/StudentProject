a=input("Enter a English word: ")
k=input("Enter a key word: ")
k=k*(len(a)//len(k)+1)
for i in range(len(a)):
    if a[i]!=" ":
       b=chr((ord(a[i])-96+(ord(k[i])-97))%26+96)
       print(b)
    else:
       print(" ", end="")
