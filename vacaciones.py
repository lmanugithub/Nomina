class Vacaciones():

    def __init__(self) -> None:
        self.vacaciones = {
            '1':6,
            '2':8,
            '3':10,
            '4':12,
            '5':14, '6':14,'7':14,'8':14,'9':14,
            '10':16, '11':16,'12':16,'13':16,'14':16,
            '15':18, '16':18,'17':18,'18':18,'19':18,
            '20':20, '21':20,'22':20,'23':20,'24':20,
        }

    def dias_vacacion(self,ano: str) -> int:
        return self.vacaciones[str(ano)]

if __name__=='__main__':
    prueba = Vacaciones()
    anos = input('Digite el numero de años: ')
    print(prueba.dias_vacacion(anos))