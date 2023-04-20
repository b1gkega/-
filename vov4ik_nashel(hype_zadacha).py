


def do_math(stroka):
    spisk_from_stroka = stroka.split()
    new_spisk = []
    str_usd_bukv = ""
    vse_ENG = "abcdefghijklmnopqrstuvwxyz"
    for chislo_v_spiske in spisk_from_stroka:
        for element_v_chisle in range(len(chislo_v_spiske)):
            if 97 <= ord(chislo_v_spiske[element_v_chisle]) <= 122:
                bukva = chislo_v_spiske[element_v_chisle]
                cocojumbo = chislo_v_spiske[:element_v_chisle] + chislo_v_spiske[element_v_chisle + 1:]
                cocojumbo = bukva + vse_ENG[str_usd_bukv.count(bukva)] + cocojumbo
                new_spisk.append(cocojumbo)
                str_usd_bukv += bukva
    sortirovan = sorted(new_spisk)
    bebra = int(sortirovan[0][2:])
    for chislo in range(1, len(sortirovan)):
        match (chislo-1) % 4:
            case 0:
                bebra += int(sortirovan[chislo][2:])
            case 1:
                bebra -= int(sortirovan[chislo][2:])
            case 2:
                bebra *= int(sortirovan[chislo][2:])
            case 3:
                bebra /= int(sortirovan[chislo][2:])
    print(round(bebra))

do_math("24z6 1z23 z369 89z 9z 96z 950z 600z 907z 900z 900z 900z 900z 900z 900z 900z 900z 900z 900z 900z 900z")
