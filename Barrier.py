while True:
    print('Enter value of height')
    space = int(input())
    if space>0 and space<24:
       print('height: ', space)
       a = '##'
       print(' '*(space),a)
       while space>1:
         print(" "*(space-1),a+'#')
         space -= 1
         a = a + '#'
       break
