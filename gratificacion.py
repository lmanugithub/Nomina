from isr import ISR


class Gratificacion():

    # setter method
    def set_data(self, base, monto):
        self.base = base
        self.monto = monto

    # getter method
    def get_data(self):
        return (self.base, self.monto)

    def diferencias(self):
        calculo1 = ISR()
        calculo1.set_sueldo_base(self.base)
        calculo2 = ISR()
        calculo2.set_sueldo_base(self.base+self.monto)
        q_1 = self.base/2 - calculo1.impuesto_a_retener()/2
        q_2 = ((self.base + self.monto) - self.base/2) - \
            (calculo2.impuesto_a_retener() - (calculo1.impuesto_a_retener()/2))
        q_2 = q_2 - self.monto
        return (round(q_1, 2), round(q_2, 2))

    def gratificacion(self):
        calculo1 = ISR()
        calculo1.set_sueldo_base(self.base)
        calculo2 = ISR()
        calculo2.set_sueldo_base(self.base + self.monto)
        primera, segunda = self.diferencias()
        temp = 0
        while primera >= segunda:
            temp += 0.01
            calculo2.set_sueldo_base(self.base + self.monto + temp)
            new_base = self.base + self.monto + temp
            segunda = ((new_base) - self.base/2) - (calculo2.impuesto_a_retener() -
                                                    (calculo1.impuesto_a_retener()/2)) - self.monto
        return round(temp, 2)
