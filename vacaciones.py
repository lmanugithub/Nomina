# coding: utf-8

# In[1]:

__author__ = 'lguerrero'


class Vacaciones():

    def __init__(self) -> None:
        self.vacaciones = {
            '1': [12, 1.0493],
            '2': [14, 1.0506],
            '3': [16, 1.0520],
            '4': [18, 1.0534],
            '5': [20, 1.0547], 
            '6': [22, 1.0561], '7': [22, 1.0561], '8': [22, 1.0561], '9': [22, 1.0561], '10': [22, 1.0561], 
            '11': [24, 1.0575], '12': [24, 1.0575], '13': [24, 1.0575], '14': [24, 1.0575], '15': [24, 1.0575], 
            '16': [26, 1.0589], '17': [26, 1.0589], '18': [26, 1.0589], '19': [26, 1.0589], '20': [26, 1.0589], 
            '21': [28, 1.0602], '22': [26, 1.0602], '23': [28, 1.0602], '24': [28, 1.0602], '25': [28, 1.0602], 
            '26': [30, 1.0616], '27': [30, 1.0616], '28': [30, 1.0616], '29': [30, 1.0616], '30': [30, 1.0616], 
            '31': [32, 1.0630], '32': [32, 1.0630], '33': [32, 1.0630], '34': [32, 1.0630], '34': [32, 1.0630],
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
