

lt_vienetai_kas = {1: 'vienas', 2: 'du', 3: 'trys', 4: 'keturi', 5: 'penki',
                   6: 'šeši', 7: 'septyni', 8: 'aštuoni', 9: 'devyni'}

# lt_vienetai_ko = {1: 'vieno', 2: 'dviejų', 3: 'trijų', 4: 'keturių',
#                   5: 'penkių', 6: 'šešių', 7: 'septynių', 8: 'aštuonių',
#                   9: 'devynių'}

# lt_vienetai_kam = {1: 'vienam', 2: 'dviem', 3: 'trim', 4: 'keturiem',
#                    5: 'penkiem', 6: 'šešiem', 7: 'septyniem', 8: 'aštuoniem',
#                    9: 'devyniem'}

# lt_vienetai_ka = {1: 'vieną', 2: 'du', 3: 'tris', 4: 'keturis',
#                   5: 'penkis', 6: 'šešis', 7: 'septynis', 8: 'aštuonis',
#                   9: 'devynis'}

# lt_vienetai_kuo = {1: 'vienu', 2: 'dviem', 3: 'trim', 4: 'keturiais',
#                    5: 'penkiais', 6: 'šešiais', 7: 'septyniais',
#                    8: 'aštuoniais', 9: 'devyniais'}

# lt_vienetai_kame = {1: 'viename', 2: 'dviejuose', 3: 'trijuose',
#                     4: 'keturiuose', 5: 'penkiuose', 6: 'šešiuose',
#                     7: 'septyniuose', 8: 'aštuoniuose', 9: 'devyniuose'}

lt_desimtys_kas = {1: 'dešimt', 2: 'dvidešimt', 3: 'trisdešimt',
                   4: 'keturiasdešimt', 5: 'penkiasdešimt',
                   6: 'šešiasdešimt', 7: 'septyniasdešimt',
                   8: 'aštuoniasdešimt', 9: 'devyniasdešimt'}

lt_specialus_kas = {10: 'dešimt', 11: 'vienuolika', 12: 'dvylika', 13: 'trylika',
                    14: 'keturiolika', 15: 'penkiolika', 16: 'šešiolika',
                    17: 'septyniolika', 18: 'aštuoniolika', 19: 'devyniolika'}

lt_dideli_kas = {0: ['šimtas', 'šimtai', 'šimtų'],
                 1: ['tūkstantis', 'tūkstančiai', 'tūkstančių'],
                 2: ['milijonas', 'milijonai', 'milijonų'],
                 3: ['milijardas', 'milijardai', 'milijardų'],
                 4: ['trilijonas', 'trilijonai', 'trilijonų'],
                 5: ['kvadrilijonas', 'kvadrilijonai', 'kvadrilijonų'],
                 6: ['kvintilijonas', 'kvintilijonai', 'kvinilijonų'],
                 7: ['sikstilijonas', 'sikstilijonai', 'sikstilijonų'],
                 8: ['septilijonas', 'septilijonai', 'septilijonų'],
                 9: ['oktilijonas', 'oktilijonai', 'oktilijonų'],
                 10: ['nonilijonas', 'nonilijonai', 'nonilijonų']}

skaicius_zodziais = []


def main():
    """Paleidimo ir duomenų įvesties funkcija"""
    while True:
        try:
            print('\n\n\t(q – išeiti)')
            ivestis = input('\tĮveskite skaičių: ')
            if ivestis == 'q':
                break
            else:
                skaicius = int(ivestis)
                int_to_words(skaicius)

        except ValueError:
            print('\n\tĮvesties klaida, laukiau skaičiaus.')


def int_to_words(skaicius):
    """Pagrindinis konvertavimo algoritmas"""
    sr = str(skaicius)  # pasidarom skaičiaus stringą
    liekana = len(sr) % 3  #
    blokai = len(sr) // 3
    pastumti_blokai = (len(sr) + 2) // 3

    if len(sr) == 1:
        if sr == '0':
            skaicius_zodziais.append('nulis')
        else:
            vienetai(sr)
    elif len(sr) == 2:
        desimtys(sr)
    elif len(sr) == 3:
        simtai(sr)

    else:
        if liekana == 1:
            vienetai(sr[0])
            zodis(sr[0], blokai)
        elif liekana == 2:
            desimtys(sr[0:2])
            zodis(sr[0:2], blokai)
        elif liekana != 0:
            simtai(sr[0:3])
            zodis(sr[0:3], blokai)
        else:
            pass

        for x in range(blokai):

            a = len(sr) - liekana - x * 3
            b = a - 3
            if b == 0:
                srr = sr[-a:]
            else:
                srr = sr[-a:-b]

            # print('liekana: ')
            # print(liekana)
            # print('Blokai: ')
            # print(blokai)
            # print('Pastumti blokai: ')
            # print(pastumti_blokai)
            # print('a ir b: ')
            # print(a)
            # print(str(b) + '\n')
            # print('srr: ')
            # print(srr)

            if srr == '000':
                pass
            else:

                if srr[0] == '0' and srr[1] == '0':
                    vienetai(srr[2])
                    if b == 0:
                        pass
                    else:
                        zodis(srr[2], blokai - x - 1)
                elif srr[0] == '0':
                    desimtys(srr[1:3])
                    if b == 0:
                        pass
                    else:
                        zodis(srr[0:3], blokai - x - 1)
                        # zodis(srr[1:3], blokai - x - 1)
                else:
                    simtai(srr)
                    if b == 0:
                        pass
                    else:
                        zodis(srr, blokai - x - 1)

    # spausdinam gautą sąrašą
    skaicius_zodziais[0] = skaicius_zodziais[0].capitalize()
    for item in skaicius_zodziais:
        print(item, end=' ')
    skaicius_zodziais.clear()


def zodis(srr, blokai):
    """Nustato kurį skaitvardinį linksnį naudoti"""
    if len(srr) == 1:
        if srr == '1':
            skaicius_zodziais.append(lt_dideli_kas[blokai][0])
        else:
            skaicius_zodziais.append(lt_dideli_kas[blokai][1])
    elif len(srr) == 2:
        if srr[0] == '1':
            skaicius_zodziais.append(lt_dideli_kas[blokai][2])
        elif srr[1] == '1':
            skaicius_zodziais.append(lt_dideli_kas[blokai][0])
        else:
            skaicius_zodziais.append(lt_dideli_kas[blokai][1])
    elif srr[1] == '1' or srr[2] == '0':
        skaicius_zodziais.append(lt_dideli_kas[blokai][2])
    elif srr[2] == '1':
        skaicius_zodziais.append(lt_dideli_kas[blokai][0])
    else:
        skaicius_zodziais.append(lt_dideli_kas[blokai][1])

def vienetai(sr):
    """Konvertuojam vienetus į žodžius"""
    if int(sr[-1]) == 0:
        pass
    else:
        skaicius_zodziais.append(lt_vienetai_kas[int(sr)])


def desimtys(sr):
    """Konvertuojam dešimtis į žodžius"""
    if sr == '00':
        pass
    elif sr[0] == '1':
        skaicius_zodziais.append(lt_specialus_kas[int(sr)])
    elif sr[0] == '0':
        vienetai(sr[1])
    elif sr[1] == '0':
        skaicius_zodziais.append(lt_desimtys_kas[int(sr[0])])
    else:
        skaicius_zodziais.append(lt_desimtys_kas[int(sr[0])])
        vienetai(sr[1])


def simtai(sr):
    """Konvertuoja šimtus į žodžius"""
    if sr == '000':
        pass
    elif sr[0] != '0':
        vienetai(sr[0])
        if sr[0] == '1':
            skaicius_zodziais.append(lt_dideli_kas[0][0])
        else:
            skaicius_zodziais.append(lt_dideli_kas[0][1])
        desimtys(sr[1:])
    else:
        desimtys(sr[1:])


if __name__ == '__main__':
    main()
