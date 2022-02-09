from isr import ISR
from imss import CalculoIMSSObrero


class TaxRetencion(ISR, CalculoIMSSObrero):
    factor = 1.0452

    def __init__(self):
        ISR.__init__(self)
        CalculoIMSSObrero.__init__(self)

    def salario_diario_integrado(self, sueldo: float) -> float:
        '''
        Parameter: float -> float
        Hace un calculo breve del impuesto quincenal 
        de  una persona
        '''
        calculo = ISR()
        calculo.set_sueldo_base(sueldo)
        sdi_mensual = (calculo.get_sueldo_base() * TaxRetencion.factor)
        return round(sdi_mensual/30.4, 4)


if __name__ == '__main__':
    calculo = TaxRetencion()
    # sueldo = float(input(f'Ingrese su sueldo mensual: '))
    sueldos = [13238.28, 13900.19,14073.7]
    for sueldo in sueldos:
        calculo.set_sueldo_base(sueldo)
        sdi = calculo.salario_diario_integrado(sueldo)
        calculo.set_sdi(sdi)
        importe_neto = (sueldo/2) - (calculo.impuesto_a_retener()/2+calculo.total_imss()/2)

        print(f'\n')
        print(f'Salario Diario Integrado: $ {calculo.get_sdi():,.2f}')
        print(f'Su sueldo quincenal: .....$ {sueldo/2:,.2f}')
        print('\n\t.:Deduciones:.')
        print(f'Impuesto sobre la renta:..$ {calculo.impuesto_a_retener()/2:,.2f}')
        print(f'Seguro social: ...........$ {calculo.total_imss()/2:,.2f}')
        print(
            f'Suma retenciones taxes.....$ {calculo.impuesto_a_retener()/2+calculo.total_imss()/2:,.2f}')
        print(f'\n')
        print(f'Importe a pagar:.........$ {importe_neto:,.2f}')
        print(f'{calculo.get_sueldo_base()-(calculo.impuesto_a_retener()):,.2f}')
        print('\t.:GRACIAS:.')
