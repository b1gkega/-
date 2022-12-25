'''from itertools import product
cab = product('ABCX', repeat=5)
spisk = []
for i in cab:
    s = ''.join(i)
    if (s[0] == 'X' and s.count('X') == 1) or s.count('X') == 0:
        spisk.append(s)
print(len(spisk))'''

'''from itertools import product
cab = product('НРТУ', repeat=4)
coun = 0
for i in cab:
    coun += 1
    s = ''.join(i)
    if coun == 215:
        print(s)'''

'''from itertools import product
cab = product('ABCDXYZ', repeat=4)
spisk = []
t = 'XYZ'
for i in cab:
    s = ''.join(i)
    if s[0] in t and s.count('X') + s.count('Y') + s.count('Z') == 1:
        spisk.append(s)
print(len(spisk), *spisk)'''



'''from itertools import product
cab = product('ЛЕТО', repeat=4)
coun = 0
sgl = 'ЛТ'
for i in cab:
    s = ''.join(i)
    if s[0] in sgl:
        coun += 1
print(coun)
'''






















spisk = []
coun = 0
from itertools import product
cab = product('ЯУНОПТИА', repeat=16)
for i in cab:
    s = ''.join(i)
    if s.count('АНТИУТОПИЯ') == 1 and s.count('Н') + s.count('П') + s.count('Т') <= 6:
        coun += 1
print(coun)
