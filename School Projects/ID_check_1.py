

# Gaunam ID ir tikrinam ar int ir ar sudarytas tik iš 11 skaičių
def Ivestis():
    while True:
        try:
            # Prašom ID kodo iš naudotojo
            id_kodas = int(input('\n\tĮveskite asmens kodą: '))
            # Konvertujam gautą įvestį į LIST
            id_list = [int(x) for x in str(id_kodas)]
            # Tikrinam, ar įvestį sudaro 11 ženklų
            if len(id_list) != 11:
                print('\n\tAsmens kodą sudaro 11 skaičių.\
                      \n\tBandykite dar kartą.')
                Ivestis()
            # Jei viskas gerai, priimame įvestą kodą
            # ir paleidžiame tikrinimo algoritmą
            ctrl_int_calc(id_list, id_kodas)
            break
        # Jei įvedamas ne sveikasis skaičius prašome mėginti dar kartą
        except ValueError:
            print('\n\tPriimu tik sveikąjį skaičių.\n\tBandykite dar kartą.')


# Algoritmas kontroliniam asmens kodo skaičiui sužinoti
# ir patikrinti, žr. WIKIPEDIA
def ctrl_int_calc(id_list, id_kodas):
    ctrl_int = 0  # kontrolinis skaičius

    # Skaičiuojam kodo skaičių sandaugų sumą pagal 1 taisyklę
    sum1 = 0  # kodo skaičių sandaugų suma pagal 1 taisyklę
    num1 = 1  # pagalbinis kintamasis leidžiantis iteruoti sąrašą
    ctrl_int_1 = 0  # kontrolinio skaičiaus versija pagal 1 taisyklę

    for x in id_list[0:-1]:
        if num1 < 10:
            sum1 = sum1 + x * num1
            num1 += 1
        else:
            num1 = 1
            sum1 = sum1 + x * num1
            num1 += 1
    ctrl_int_1 = sum1 % 11

    # Skaičiuojam kodo skaičių sandaugų sumą pagal 2 taisyklę
    sum2 = 0  # kodo skaičių sandaugų suma pagal 2 taisyklę
    num2 = 3  # pagalbinis kintamasis leidžiantis iteruoti sąrašą
    ctrl_int_2 = 0  # kontrolinio skaičiaus versija pagal 1 taisyklę

    for x in id_list[0:-1]:
        if num2 < 10:
            sum2 = sum2 + x * num2
            num2 += 1
        else:
            num2 = 1
            sum2 = sum2 + x * num2
            num2 += 1
    ctrl_int_2 = sum2 % 11

    # Tikrinam kokią taisyklę atitinka paskaičiuoti kontroliniai skaičiai
    # ir pritaikome, kad gautime tikrąjį kontrolinį skaičių
    if ctrl_int_1 != 10:
        ctrl_int = ctrl_int_1
    elif ctrl_int_2 != 10:
        ctrl_int = ctrl_int_2
    else:
        ctrl_int = 0

    # Tikrinam ar paskutinis kodo skaičius atitinka kontrolinį skaičių,
    # t. y. ar įvestas asmens kodas teisingas ir vėl paleidžiam programą
    if ctrl_int == id_list[-1]:
        print('\tGali būti, kad asmens kodas {} yra teisingas'.format(id_kodas))
        Ivestis()
    else:
        print('\tAsmens kodas {} yra neteisingas'.format(id_kodas))
        Ivestis()


# Paleidžiam programą
if __name__ == '__main__':
    Ivestis()

print
