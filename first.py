
from math import sqrt
# sqrt function is basically finds square rooth of a number 


def prime(w):
    
    if w >= 2: print(2)
        
    for q in range(3,w, 2):
        for b in range (2, int(sqrt(q))+1):
            if q % b == 0 :
                break
        else:
            print(q)
    return 'Finish'

print(prime(1000))

'''
for x in range(2, 101):
        for i in range(2, 101):
            if x % i == 0 and x > i:
                break
        else:
            print(x)
'''




def palind(text):
    if text == text[::-1]:
        print(text + ' ' + 'is a palindrome')
    else:
        print(text + ' ' + 'is not a palindrome')

palind('qwerewq')


