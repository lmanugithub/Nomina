# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# libraries
from isr import ISR
from dataimss import DataImss


class Aguinaldo(DataImss):
    def __init__(self) -> None:
        super().__init__()
        self._aguinaldo = 0

    # getter method
    def get_aguinaldo(self) -> float:
        return self._aguinaldo

    # setter method
    def set_aguinaldo(self, aguinaldo: float) -> float:
        self._aguinaldo = aguinaldo

    def aguinaldo_grabado(self) -> float:
        excento = self._uma * 30
        if (self._aguinaldo - excento) > 0:
            return self._aguinaldo - excento
        else:
            return 0


class Ley(ISR, Aguinaldo):
    def __init__(self):
        super().__init__()

    def ordinario_aguinaldo(self) -> float:
        remunaracion = self.get_sueldo_base() + self.aguinaldo_grabado()
        nueva_base = ISR()
        nueva_base.set_sueldo_base(remunaracion)
        return round(nueva_base.impuesto_a_retener(), 2)
    
    def impuesto_aguinaldo_ley(self) -> float:
        return round(self.ordinario_aguinaldo() - self.impuesto_a_retener(), 2) 


class Reglamento(ISR, Aguinaldo):
    def __init__(self):
        super().__init__()
        # self._aguinaldo = 0

    def fracc_i(self) -> float:
        return round(self.aguinaldo_grabado() / 365, 2)

    def fracc_ii(self) -> float:
        remuneracion = self.get_sueldo_base() + self.fracc_i()
        ingreso_aguinaldo = ISR()
        ingreso_aguinaldo.set_sueldo_base(remuneracion)
        return round(ingreso_aguinaldo.calculo_impuesto(), 2)

    def fracc_iii(self) -> float:
        return round(self.fracc_ii() - self.calculo_impuesto(), 4)

    def fracc_v(self) -> float:
        if self.fracc_i() > 0:
            return round(self.fracc_iii() / self.fracc_i(), 4)
        else:
            return 0

    def fracc_iv(self) -> float:
        return round(self.aguinaldo_grabado() * self.fracc_v(), 2)
    

class Imuesto_Aguinaldo(Ley, Reglamento):
    def __init__(self):
        super().__init__()

    def impuesto_aguinaldo(self) -> float:
        if self.fracc_iv() > self.impuesto_aguinaldo_ley():
            return self.impuesto_aguinaldo_ley()
        else:
            self.fracc_iv()


# if __name__ == '__main__':
#     calculo = Imuesto_Aguinaldo()
#     calculo.set_aguinaldo(3526.04)
#     print(calculo.fracc_i())
#     calculo.set_sueldo_base(19500)
#     print(calculo.get_sueldo_base())
#     print(calculo.fracc_ii())
#     print(calculo.fracc_iii())
#     print(calculo.fracc_v())
#     print(calculo.fracc_iv())
#     print(calculo.aguinaldo_grabado())
#     print(calculo.impuesto_aguinaldo_ley())
#     print(calculo.impuesto_aguinaldo())
