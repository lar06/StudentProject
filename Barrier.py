space = int(input())
print('height: ', space)
a='**'
if space>0 and space<24:
     print(a)
     while space>1:
         print(a+'*')
         space -= 1
         a = a + '*'

