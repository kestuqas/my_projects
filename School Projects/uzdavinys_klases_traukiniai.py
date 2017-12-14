"""
Traukinį sudaro lokomotyvai ir vagonai. Sukurti klases lokomotyvui,
vagonui ir traukiniui (sąstatui).
Kiekvienas vagonas turi savitąją masę,vežamo krovinio masę,maksimalią
krovinio masę ir unikalų vagono numerį.
Lokomotyvas turi savo masę ir maksimalią tempiamą masę.
Parašyti klases darbui su traukiniu, lokomotyvui ir vagonais.
Parašyti programą klasių veikimo demonstravimui.

Reikalavimai:

Pašalinti pagal ID
Objektai ir metodai dokumentuoti
Galimybė traukinio duomenis įrašyti į failą json formatu
(failo struktūrą pasirinkite)
Galimybė duomenis įkelti iš failo json formatu.
Turi teisingai nuskaityti failą, kurį sukūrė įrašant duomenis
Įrašymui bei nuskaitymas gali būti paduodamas falio pavadinimas
arba atidarytas failas
Traukiniui ir jei reikia vagonams bei lokomotyvams turi būti
aprašyti prasmingi __add__, __sub__, __repr__, __str__/__unicode__,
__len__, __bool__ metodai
Sukūrus kelis traukinius juos galima surūšiuoti (galite pasirinkti pagal ką).
Esant klaidoms - turi būti sukuriami programuotojo aprašyti objektai
paveldėję iš exception klasės.
Turi būti įgyvendintas klaidų gaudymas.
Programa turi tenkinti PEP8 standartą.
Turi būti aprašyta bent viena savybė (property) darbui su atributais
(gali būti aprašytas reikšmių validavimas, reikšmių perskaičiavimas ar kita)
Programa turi būti išskaidyta į modulius
Programos kodas turi būti tvarkingas ir sistemingas.
Prie programos pateikiamos naudojimo instrukcijos
Programą galima atsiskaityti iki gegužės 26 imtinai.
Po šios datos šios programos atsiskaitymai nepriimami.
"""
from pprint import pprint


class Objektas():

    def __init__(self, numeris, mase, tipas):
        self.tipas = tipas
        self.numeris = numeris
        self.mase = mase

    def __repr__(self):
        return "{} Nr. {}, masė {} t".format(
            self.tipas, self.numeris, self.mase)


class Vagonas(Objektas):

    def __init__(self, numeris, maks_svoris, mase,
                 krovinio_svoris, tipas='Vagonas', *args):
        super(Vagonas, self).__init__(numeris, mase, tipas)
        self.numeris = numeris
        self.maks_svoris = maks_svoris
        self.mase = mase
        self.krovinio_svoris = krovinio_svoris
        self.tipas = tipas

    @property
    def krovinio_svoris(self):
        return self._krovinio_svoris

    @krovinio_svoris.setter
    def krovinio_svoris(self, value):
        if int(self.maks_svoris) < (int(self.mase) + int(value)):
            print('Vagono Nr. {} krovinys per sunkus!'.format(self.numeris))
        self._krovinio_svoris = value


class Loko(Objektas):

    def __init__(self, numeris, galia, mase,
                 tipas='Lokomotyvas'):
        super(Loko, self).__init__(numeris, mase, tipas)
        self.numeris = numeris
        self.galia = galia
        self.mase = mase
        self.tipas = tipas


class Sastatas(Vagonas, Loko):

    def __init__(self, vardas):
        self.visi = []
        self.vardas = vardas

    def __add__(self, other):
        self.visi.append(other)
        return self

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        self.visi.remove(other)
        return self

    def __rsub__(self, other):
        if other == 0:
            return self
        else:
            return self.__sub__(other)

    # Objekto pašalinimas iš sąstato pgl. jo numerį
    def remove_by_id(self, object_id):
        for x in self.visi:
            if object_id == x.numeris:
                self.visi.remove(x)
        return self

    # Objektų vnt. skaičiavimas
    def count(self):
        vagonai = 0
        loko = 0
        for item in self.visi:
            if item.__class__.__name__ == 'Loko':
                loko += 1
            else:
                vagonai += 1
        return loko, vagonai

    # Sąstato galios skaičiavimas
    def galia(self):
        sast_galia = 0
        for item in self.visi:
            if item.__class__.__name__ == 'Loko':
                sast_galia += int(item.galia)
        return sast_galia

    # Sąstato masės skaičiavimas
    def viso_mase(self):
        mase = 0
        for item in self.visi:
            mase += int(item.mase)
            if item.__class__.__name__ == 'Vagonas':
                mase += int(item.krovinio_svoris)
        return mase

    # Sąstato būsenos tikrinimas
    def busena(self):
        sast_busena = None
        if int(self.galia()) >= int(self.viso_mase()):
            sast_busena = 'OK'
        else:
            sast_busena = 'Perkrautas'
        return sast_busena

    # Sąstato objektų rūšiavimas pagal pasirinktą objekto parametrą
    def rusiuok(self, a):
        self.visi.sort(key=lambda x: getattr(x, a))
        pprint(self.visi)

    # Sąstato sąrašo vaizdavimo metodas
    def __repr__(self):
        return "\nSąstatas: {}\n\tViso objektų: {} vnt. {}\n\tViso masė: {} t\n\tViso galia: {} t\n\n\tBūsena: {}".format(self.vardas, len(self.visi), self.count(), self.viso_mase(), self.galia(), self.busena())


v1 = Vagonas('PI-125846', 120, 52, 50)
v2 = Vagonas('AN-127846', 140, 56, 57)
v3 = Vagonas('TR-837846', 160, 59, 75)
v4 = Vagonas('KE-837846', 160, 62, 87)

l1 = Loko('127846-BZ', 5000, 159)
l2 = Loko('897846-BZV', 4000, 139)

s1 = Sastatas('Vilnius-Minskas 20171201')
s2 = Sastatas('Vilnius-Maskva 20171202')

s1 + l1 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 - v1 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4 + v4 + v1 + v2 + v3 + v4 + v1 + v2 + v3 + v4
s2 + l2 + v1 + v2 + v3 + v4 + v1 + v3 + v4 + v1 + v3 + v4 + v1 + v2 - v4

s1.remove_by_id('PI-125846')
s2.remove_by_id('AN-127846')
s2.remove_by_id('AN-127846')

s1.rusiuok('numeris')
s2.rusiuok('mase')

print(s1)
print(s2)


