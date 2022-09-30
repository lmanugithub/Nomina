# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from datostrabajador import DatosTrabajador


class SueldoDiarioIntegrado(DatosTrabajador):
    def __init__(self) -> None:
        DatosTrabajador.__init__(self)

    def vacacion_anual(self):
        return (self.sueldo_diario() * self.get_dias_vacaciones())/365

    def sueldo_anual(self):
        return ((self.sueldo_diario() * 365) - (self.vacacion_anual()*365))/365

    def prima_vaca_anual(self):
        return (self.vacacion_anual() * self.prima_vacacional)/365

    def aguinaldo(self):
        return (self.sueldo_diario() * self.dias_agunaldo)/365

    def bono_anual(self):
        return (self.sueldo_diario() * self.dias_agunaldo)/365

    def vales_anuales(self):
        return (self.get_vales_despensa() * 12.5)/365

    def seg_gtos_mayor_anual(self):
        return self.get_seg_gtos_med_mayor()/365

    def seg_gtos_anual(self):
        return self.get_seg_gtos_med()/365

    def salario_integrado_separacion(self):
        return (self.vacacion_anual() +
                self.sueldo_anual() +
                self.prima_vaca_anual() +
                self.aguinaldo() +
                self.bono_anual() +
                self.seg_gtos_mayor_anual() +
                self.seg_gtos_anual() +
                self.vales_anuales())
