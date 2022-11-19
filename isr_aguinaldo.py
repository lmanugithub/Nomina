# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# libraries
from isr import ISR


class Reglamento(ISR):
    def __init__(self):
        super().__init__()
        self._aguinaldo = 0

    # getter method
    def get_aguinaldo(self) -> float:
        return self._aguinaldo

    # setter method
    def set_aguinaldo(self, aguinaldo: float) -> float:
        self._aguinaldo = aguinaldo


    def fracc_i(self):
        return round(self._aguinaldo / 365, 2)
    
    def fracc_ii(self):
        remuneracion = self.get_sueldo_base() + self.fracc_i()
        ingreso_aguinaldo = ISR()
        ingreso_aguinaldo.set_sueldo_base(remuneracion)
        return round(ingreso_aguinaldo.calculo_impuesto(),2)
    
    def fracc_iii(self):
        return round(self.fracc_ii() - self.calculo_impuesto() , 4)
    
    def fracc_v(self):
        if self.fracc_i() > 0:
            return round(self.fracc_iii() / self.fracc_i(), 4)
        else:
            return 0 
        
    def fracc_iv(self):
        return round(self._aguinaldo * self.fracc_v(), 2)
    
if __name__=='__main__':
    calculo = Reglamento()
    calculo.set_aguinaldo(639.44)
    print(calculo.fracc_i())
    calculo.set_sueldo_base(19500)
    print(calculo.get_sueldo_base())
    print(calculo.fracc_ii())
    print(calculo.fracc_iii())
    print(calculo.fracc_v())
    print(calculo.fracc_iv())


