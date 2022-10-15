# coding: utf-8

# In[1]:

__author__ = 'lguerrero'


from imss import CalculoIMSSObrero
from isr import ISR
from sbc import SBC


class Incremento():

    # setter method
    def set_data(self, sueldo, fch_ing, fch_bse, vales, goal):
        self.sueldo = sueldo
        self.fch_ing = fch_ing
        self.fch_bse = fch_bse
        self.vales = vales
        self.goal = goal

    # getter method
    def get_data(self):
        return (self.sueldo, self.fch_ing, self.fch_bse, self.vales, self.goal)
    

    def incremento(self):
        _isr_ = ISR()
        _sbc_ = SBC()
        _imss_ = CalculoIMSSObrero()
        _isr_.set_sueldo_base(self.sueldo)
        _sbc_.set_sueldo_mensual(self.sueldo) # datostrabajador
        _sbc_.set_fecha_ingreso(self.fch_ing)
        _sbc_.set_fecha_base(self.fch_bse)
        _sbc_.set_vales_despensa(self.vales)
        _imss_.set_sdi(_sbc_.salario_base_cotizacion())
        neto = self.sueldo - _isr_.impuesto_a_retener() - _imss_.total_imss()

        temp = 0

        while neto <= self.goal:
            temp += 1

            # re-setting data with the new information
            incrementado = self.sueldo + temp
            _isr_.set_sueldo_base(incrementado)
            _sbc_.set_sueldo_mensual(incrementado)
            _imss_.set_sdi(_sbc_.salario_base_cotizacion())
            neto = incrementado - _isr_.impuesto_a_retener() - _imss_.total_imss()
            # print(neto)

        return round(temp, 2)
    
if __name__=='__main__':
    incremento = Incremento()
    incremento.set_data(17800.00, '2022/02/01', '2022/12/31', 1500, 19500)
    print(incremento.incremento())
    print(incremento.sueldo)

