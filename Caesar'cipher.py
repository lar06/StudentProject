s1={
    "Guido van Rossum": "Python",
    "Kenneth Eugene Iverson": "APL",
    "John Warner Backus": "Fortran",
    "James Gosling": "Java",
    "Andrei Alexandrescu": "C++",
    "Ole-Johan Dahl": "Simula",
    "Roberto Ierusalimschy": "Lua",
    "Don Syme": "F",
    "Larry Wall": "Perl",
    "Dr. Konrad Ernst Otto Zuse": "Plankalkül",
}
a=input("Enter Sort or Search: ")
if a=="Sort":
    sortName=sorted(s1.keys())
    for lang in sortName:
        print(lang," - ",s1[lang])
elif a=="Search":
    searchName=input("Enter a name: ")
    for name, value in s1.items():
        if name==searchName:
            print(searchName, "created language", s1[name])
            break
    else:
         print("not in the list")
else:
    print("Command is not correct")
