from itertools import groupby


def minion_game(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    a = 0
    b = 0
    for i, c in enumerate(s):
        if c in vowels:
            print(c)
            b += len(s) - i
        else:
            print('-'+c)
            a += len(s) - i
            
    if a == b:
        print ("Draw")
    elif a > b:
        print ('Stuart {}'.format(a))
    else:
        print ('Kevin {}'.format(b))
     
minion_game('BANANA')
# print(sorted('HACK'))
# print([(len(list(k)), i) for i, k in groupby('1222311')])