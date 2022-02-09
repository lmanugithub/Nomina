from sueldodiariofiniq import SueldoDiarioIntegrado
from isr import ISR 

class CalculoSeparacion(SueldoDiarioIntegrado,ISR):
    def __init__(self) -> None:
        SueldoDiarioIntegrado.__init__(self)
        ISR.__init__(self)

    def tres_meses_sueldo(self):
        '''
        (Salario Diario Integrado X 30 dias ) X 3 meses
        '''
        return (self.salario_integrado_separacion() * 30) * 3

    def veinte_dias_x_ano(self):
        '''
        ((Salario Diario Integrado X 20 dias ) / 365 ) X Días Trabajados
        '''
        return ((self.salario_integrado_separacion() * 20) / 365) * self.dias_trabajados()

    def doce_dias_x_año(self):
        '''
        ( 12 dias X cada año de servicio hasta por el doble del SMGDF 80.04)
        '''
        return (((self.salario_diario_minimo * 2)*12)/365) * self.dias_trabajados()

    def monto_separacion(self):
        return (self.tres_meses_sueldo() +
                self.veinte_dias_x_ano() +
                self.doce_dias_x_año() )

    def parte_exenta(self):
        '''
        Parte excenta por separación ( 90 dias de SMGDF)
        ( SMGDF x 90 dias ) X Años Trabajados
        '''
        return (self._uma * 90) * self.anos_trabajados()

    def tasa_efectiva(self):
        calculo = ISR()
        calculo.set_sueldo_base(self.get_sueldo_mensual())
        return (calculo.impuesto_a_retener()/self.get_sueldo_mensual())

    def isr_separacion(self):
        return (self.monto_separacion()-
                self.parte_exenta()) * self.tasa_efectiva()
