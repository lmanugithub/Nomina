# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from datostrabajador import DatosTrabajador
from isr import ISR


class CalculoFiniquito(DatosTrabajador, ISR):
    def __init__(self) -> None:
        DatosTrabajador.__init__(self)
        ISR.__init__(self)

    def dias_proporcional_vacaciones(self):
        if self.dias_vacaciones_trabajadas() > 0:
            return (self.get_dias_vacaciones() * self.dias_vacaciones_trabajadas()/365)
        else:
            return 0

    def parte_proporcional_vacacion(self):
        '''
        Vacaciones proporcional
        '''
        return self.dias_proporcional_vacaciones() * self.sueldo_diario()

    def parte_proporcional_prima_vac(self):
        return self.parte_proporcional_vacacion() * self.prima_vacacional

    def dias_proporcional_aguinaldo(self):
        dias_aguinaldo = 15
        return (dias_aguinaldo/365) * self.dias_ano_trabajados()

    def parte_proporcional_aguinaldo(self):
        return self.dias_proporcional_aguinaldo() * self.sueldo_diario()

    def vacaciones_pendientes(self):
        return self.sueldo_diario() * self.get_dias_vacaciones()

    def persepciones_x_cubrir(self):
        quincena = int(self.get_fecha_baja().strftime('%d'))
        if quincena > 16:
            return (
                (self.get_sueldo_mensual()) +
                self.parte_proporcional_vacacion() +
                self.parte_proporcional_prima_vac() +
                self.parte_proporcional_aguinaldo() +
                self.parte_proporcional_aguinaldo() +
                self.get_gratificacion_extra() +
                self.vacaciones_pendientes()
            )
        else:
            return (
                (self.get_sueldo_mensual()/2) +
                self.parte_proporcional_vacacion() +
                self.parte_proporcional_prima_vac() +
                self.parte_proporcional_aguinaldo() +
                self.parte_proporcional_aguinaldo() +
                self.get_gratificacion_extra() +
                self.vacaciones_pendientes()
            )

    def excencion_s_parte_aguinaldo(self):
        if self.parte_proporcional_aguinaldo() > (self._uma * 30):
            return (self._uma * 30)
        else:
            return self.parte_proporcional_aguinaldo()

    def excencion_s_parte_prima_vac(self):
        if self.parte_proporcional_prima_vac() > (self._uma * 15):
            return (self._uma * 15)
        else:
            return self.parte_proporcional_prima_vac()

    def base_impto_finiq(self):
        return (
            self.persepciones_x_cubrir() -
            (self.excencion_s_parte_aguinaldo() +
             self.excencion_s_parte_prima_vac())
        )

    def isr_finiquito(self):
        calculo = ISR()
        calculo_ant = ISR()
        calculo_ant.set_sueldo_base(self.get_sueldo_mensual()/2)
        calculo.set_sueldo_base(self.base_impto_finiq())
        quincena = int(self.get_fecha_baja().strftime('%d'))
        if quincena > 16:
            return calculo.impuesto_a_retener() - (calculo_ant.impuesto_a_retener()/2)
        else:
            return calculo.impuesto_a_retener()
