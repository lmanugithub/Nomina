from tablas import Tablas


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

# if __name__=='__main__':
#     calculo = ISR()
#     calculo.set_sueldo_base(35000)

#     print(calculo.impuesto_a_retener()/2)
#     # print(calculo.total_imss())
