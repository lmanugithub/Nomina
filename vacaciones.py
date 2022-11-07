# coding: utf-8

# In[1]:

__author__ = 'lguerrero'


class Vacaciones():

    def __init__(self) -> None:
        self.vacaciones = {
            '1': [12, 1.0452],
            '2': [14, 1.0466],
            '3': [16, 1.0479],
            '4': [18, 1.0493],
            '5': [20, 1.0507], '6': [20, 1.0507], '7': [20, 1.0507], '8': [20, 1.0507], '9': [20, 1.0507],
            '10': [22, 1.0521], '11': [22, 1.0521], '12': [22, 1.0521], '13': [22, 1.0521], '14': [22, 1.0521],
            '15': [24, 1.0534], '16': [24, 1.0534], '17': [24, 1.0534], '18': [24, 1.0534], '19': [24, 1.0534],
            '20': [26, 1.0548], '21': [26, 1.0548], '22': [26, 1.0548], '23': [26, 1.0548], '24': [26, 1.0548],
            '25': [28, 1.0562], '26': [28, 1.0562], '27': [28, 1.0562], '28': [28, 1.0562], '29': [28, 1.0562],
            '30': [30, 1.0575], '31': [30, 1.0575], '32': [30, 1.0575], '33': [30, 1.0575], '34': [30, 1.0575],
        }

    def dias_vacacion(self, ano: str) -> int:
        return self.vacaciones[str(ano)][0]

    def factor_integration(self, ano: str) -> float:
        return self.vacaciones[str(ano)][1]

    @classmethod
    def fac_int(cls, ano: str) -> float:
        factor = Vacaciones()
        return factor.factor_integration(ano)

    @classmethod
    def dia_vac(cls, ano: str) -> float:
        factor = Vacaciones()
        return factor.dias_vacacion(ano)


if __name__ == '__main__':
    prueba = Vacaciones()
    anos = input('Digite el numero de años: ')
    print(prueba.dias_vacacion(anos))
