'''
import sys,random
n=int(sys.argv[1])
for i in range(n):
    print(random.randrange(0,100))
'''
def return_values():
    D={}
    L=[5,[4,'myself'],(1,2,4),'learn']
    for i ,m in zip(L,['a','b','c','d']):
        D.setdefault(m,i)
    return D

print(return_values())