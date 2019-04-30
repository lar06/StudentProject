a=input("Enter a English word: ")
def data_cheaking(a):
    while a.isdigit():
        a=input("Enter a English word: ")
    else:
        while True:
            try:
                if int(a)<0:
                    a=input("Enter a English word: ")
            except (TypeError, ValueError):
                return cipherofCeasar(a)
def cipherofCeasar(a):
    alphabet=("abcdefghijklmnopqrstuvwxyz")
    i=int(input("Enter a number from 1 to 25: "))
    if i<1:
        i=1
    elif i>25:
        i=25
    cipher=""
    for c in a:
        if c in alphabet:
            cipher+=alphabet[(alphabet.index(c)+i)%(len(alphabet))]
    return print(cipher)
print(data_cheaking(a))
input("To exit enter a number")
