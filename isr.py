# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from tablas import Tablas, Tablas_Anual
from dataimss import DataImss


class ISR(Tablas):
    def __init__(self):
        super().__init__()
        self._sueldo_base = 0

    # getter method
    def get_sueldo_base(self) -> float:
        return self._sueldo_base

    # setter method
    def set_sueldo_base(self, sueldo_base: float) -> float:
        self._sueldo_base = sueldo_base

    def index_limite_superior(self) -> int:
        i = 0
        while self.limite_superior[i] <= self._sueldo_base:
            i += 1
        return i

    def calculo_impuesto(self) -> float:
        execedente_s_limite_inferior = self._sueldo_base - \
            self.limite_inferior[self.index_limite_superior()]

        impuesto_marginal = execedente_s_limite_inferior * \
            self.por_excedente_limite_inferior[self.index_limite_superior()]

        impuesto = impuesto_marginal + \
            self.cuota_fija[self.index_limite_superior()]

        return impuesto

    def index_cuota_subsidio(self) -> int:
        i = 0
        while self.superior_subsidio[i] <= self._sueldo_base:
            i += 1
        return i

    def subsidio(self):
        return (self.cuota_subsidio[self.index_cuota_subsidio()] * 1)

    def impuesto_a_retener(self) -> float:
        impuesto_retener = -1 * \
            (self.cuota_subsidio[self.index_cuota_subsidio()]
             ) + self.calculo_impuesto()
        return round(impuesto_retener, 2)

    @classmethod
    def function_isr(cls, x: float) -> float:
        calculo = ISR()
        calculo.set_sueldo_base(x)
        return calculo.impuesto_a_retener()



class ISR_Anual(Tablas_Anual,DataImss):
    def __init__(self):
        super().__init__()
        self._sueldo_base = 0
        self._ingresos = 0
        self._deducciones = 0

    # getter method
    def get_sueldo_base_anual(self) -> float:
        return self._sueldo_base_anual

    # setter method
    def set_sueldo_base_anual(self, sueldo_base_anual: float) -> float:
        self._sueldo_base_anual = sueldo_base_anual

    def index_limite_superior_anual(self) -> int:
        i = 0
        while self.limite_superior_anual[i] <= self._sueldo_base_anual:
            i += 1
        return i

    def calculo_impuesto_anual(self) -> float:
        execedente_s_limite_inferior_anual = self._sueldo_base_anual - \
            self.limite_inferior_anual[self.index_limite_superior_anual()]

        impuesto_marginal_anual = execedente_s_limite_inferior_anual * \
            self.por_excedente_limite_inferior_anual[self.index_limite_superior_anual()]

        impuesto = impuesto_marginal_anual + \
            self.cuota_fija_anual[self.index_limite_superior_anual()]
        return impuesto

    # getter method
    def get_ingresos_totales(self) -> float:
        return self._ingresos

    # setter method
    def set_ingresos_totales(self, ingresos: float) -> float:
        self._ingresos = ingresos

    # getter method
    def get_deducciones(self) -> float:
        return self._deducciones

    # setter method
    def set_deducciones(self, deducciones: float) -> float:
        self._deducciones = deducciones

    def limite_deducciones(self):
        unidad = self._uma * 5 * 365
        porcentaje = self._ingresos * 0.15
        if unidad > porcentaje:
            return porcentaje
        else:
            return unidad

    def deducciones_autorizadas(self):
        if self._deducciones > self.limite_deducciones():
            return self.limite_deducciones()
        else:
            return self._deducciones      


    @classmethod
    def function_isr_anual(cls, x: float) -> float:
        calculo = ISR_Anual()
        calculo.set_sueldo_base_anual(x)
        return calculo.calculo_impuesto_anual()

# if __name__=='__main__':
#     calculo = ISR_Anual()
#     calculo.set_sueldo_base_anual(35000)

#     print(calculo.calculo_impuesto_anual())
    # print(calculo.total_imss())
