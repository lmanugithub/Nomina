
from datetime import datetime

class Honorarios():
    def __init__(self, importe: float):
        self.importe = importe

    def ret_isr(self):
        return self.importe * 0.10

    def ret_iva(self):
        return self.importe * (2/3) * (0.16)

    def iva(self):
        return self.importe * 0.16

    def total(self):
        return self.importe - self.ret_isr() - self.ret_iva() + self.iva()

    @classmethod
    def func_total(cls, x):
        calculo = Honorarios(x)
        return calculo.total()

initia_time = datetime.now()
objetivo = 12000
cuenta = 0
iteraciones = 0

while Honorarios.func_total(objetivo + cuenta) <= objetivo:
    cuenta = cuenta + 0.00001
    # print(Honorarios.func_total(objetivo + cuenta),end=' ')
    iteraciones += 1
    


if Honorarios.func_total(objetivo + cuenta) == objetivo:
    print(f'La raiz cuadrada de {Honorarios.func_total(objetivo + cuenta)} es {objetivo}')
else:
    print(f'{Honorarios.func_total(objetivo + cuenta)} {iteraciones} {objetivo+cuenta} no tiene una raiz cuadrada exacta')


final_time = datetime.now()
time_elapsed = final_time - initia_time
print(f'Pasaron {time_elapsed.total_seconds()} segundos')