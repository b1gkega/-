'''for x in range(46):
    for y in range(46):
        for z in range(46):
            a ='0' + x*'1' + y*'2' + z*'3'
            while '01' in a or '02' in a or '03' in a:
                a = a.replace('01', '30', 1)
                a = a.replace('02', '3103', 1)
                a = a.replace('03', '1201', 1)
            if a.count('1') == 31 and a.count('2') == 24 and a.count('3') == 46:
                print(x, y, z)'''


for m in range(500):
    coun = 0
    spisk = []
    a = '>' + 15 * '1' + 35 * '2' + m * '3'
    while '>1' in a or '>2' in a or '>3' in a:
        a = a.replace('>1', '2>')
        a = a.replace('>2', '3>')
        a = a.replace('>3', '11>')
    for pumpum in range(2, (a.count('2')*2 + a.count('1') + a.count('3')*3)):
        if (a.count('2')*2 + a.count('1') + a.count('3')*3) % pumpum == 0:
            coun += 1
    if coun == 3:
        print(m)
        break


