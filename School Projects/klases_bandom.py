from datetime import datetime
from pprint import pprint
import os
import json

with open('darb_sarasas.json', 'r') as f:
    a = f.read()
zmogai = json.loads(a)


class Zmogus:
    def __init__(self, ref_id, name, surname, pid):
        self.ref_id = ref_id
        self.name = name
        self.surname = surname
        self.pid = pid

    @property
    def pilnas_vardas(self):
        pv = self.name + ' ' + self.surname
        return pv

    @pilnas_vardas.setter
    def pilnas_vardas(self, vardas_pavarde):
        name, surname = vardas_pavarde.split(' ')
        self.name = name
        self.surname = surname

    def dob(self, pid):
        if 0 < int(str(self.pid)[0]) < 3:
            simtmetis = '18'
        elif 2 < int(str(self.pid)[0]) < 5:
            simtmetis = '19'
        elif 4 < int(str(self.pid)[0]) < 7:
            simtmetis = '20'
        else:
            simtmetis = '21'

        dob_str = str(pid)[1:7]
        self.dob = str(datetime.strptime(simtmetis + dob_str, '%Y%m%d').date())
        return self.dob

    @property
    def rodyti(self):
        print("\n\t{} {}, a/k {}, gim. data {}".format(self.name, self.surname, self.pid, self.dob(self.pid)))

    @property
    def saugoti(self):
        # tikrinti()
        zmogai[self.ref_id] = [self.name, self.surname, self.pid]
        with open('darb_sarasas.json', 'w') as f:
            f.write(json.dumps(zmogai))

    @property
    def tikrinti(self):
        from ID_check_1 import ctrl_int_calc
        ctrl_int_calc(self.pid)


z1 = Zmogus('DDB_001', 'Petras', 'Petraitis', 37503051220)
z1.rodyti
z1.tikrinti
print('\t' + z1.pilnas_vardas)
z1.saugoti

z2 = Zmogus('DDB_002', 'Antanas', 'Antanaitis', 50002051520)
z2.rodyti
z2.tikrinti
print('\t' + z2.pilnas_vardas)
z2.saugoti

z2.name = 'Antanukas'
z2.pid = 38502010010
z2.saugoti

z3 = Zmogus('DDB_003', 'Kęstutis', 'Kęstaitis', 37503071220)
z3.rodyti
z3.tikrinti
print('\t' + z3.pilnas_vardas)
z3.saugoti

z3.pilnas_vardas = 'Kestutis Reimeris'
z3.rodyti
print('\t' + z3.pilnas_vardas)
z3.saugoti

pprint(zmogai)
os.startfile('darb_sarasas.json')
