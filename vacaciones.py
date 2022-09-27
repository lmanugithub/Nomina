class Vacaciones():

    def __init__(self) -> None:
        self.vacaciones = {
            '1':[6, 1.0452],
            '2':[8, 1.0466],
            '3':[10, 1.0479],
            '4':[12, 1.0493],
            '5':[14, 1.0507], '6':[14, 1.0507],'7':[14, 1.0507],'8':[14, 1.0507],'9':[14, 1.0507],
            '10':[16, 1.0521], '11':[16, 1.0521],'12':[16, 1.0521],'13':[16, 1.0521],'14':[16, 1.0521],
            '15':[18, 1.0534], '16':[18, 1.0534],'17':[18, 1.0534],'18':[18, 1.0534],'19':[18, 1.0534],
            '20':[20, 1.0548], '21':[20, 1.0548],'22':[20, 1.0548],'23':[20, 1.0548],'24':[20, 1.0548],
            '25':[20, 1.0562], '26':[20, 1.0562],'27':[20, 1.0562],'28':[20, 1.0562],'29':[20, 1.0562],
            '30':[20, 1.0575], '31':[20, 1.0575],'32':[20, 1.0575],'33':[20, 1.0575],'34':[20, 1.0575],
        }

    def dias_vacacion(self,ano: str) -> int:
        return self.vacaciones[str(ano)][0]
    
    
    def factor_integration(self, ano: str) -> float:
        return self.vacaciones[str(ano)][1]
    
    @classmethod
    def fac_int(cls, ano: str) -> float:
        factor = Vacaciones()
        return factor.factor_integration(ano)

if __name__=='__main__':
    prueba = Vacaciones()
    anos = input('Digite el numero de años: ')
    print(prueba.dias_vacacion(anos))
