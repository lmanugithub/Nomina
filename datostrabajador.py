# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

from dataimss import DataImss
# Importación de librerias
from fechas import WorkingTime


class DatosTrabajador(WorkingTime,DataImss):
    def __init__(self) -> None:
        WorkingTime.__init__(self)
        DataImss.__init__(self)
        WorkingTime.__init__(self)
        self.salario_diario_minimo = 248.93 #207.44
        self.prima_vacacional = 0.25
        self.dias_agunaldo = 15.2

    # getter method
    def get_sueldo_mensual(self):
        return self._sueldo_mensual

    # setter method
    def set_sueldo_mensual(self,sueldo=0):
        self._sueldo_mensual=sueldo

    def sueldo_diario(self):
        return self.get_sueldo_mensual()/30.4

    # getter method
    def get_dias_vacaciones(self)->int:
        return self._dias_vacaciones

    # setter method
    def set_dias_vacaciones(self,dias=0):
        self._dias_vacaciones = dias

    # # getter method
    # def get_dias_vacaciones_faltantes(self)->int:
    #     return self._dias_vacaciones_faltantes

    # # setter method
    # def set_dias_vacaciones_faltantes(self,dias=0):
    #     self._dias_vacaciones_faltantes = dias

    def anos_trabajados(self):
        return round(self.dias_trabajados()/365,2)

    # getter method
    def get_seg_gtos_med_mayor(self):
        return self._seg_gtos_med_mayor

    # setter method
    def set_seg_gtos_med_mayor(self,importe=0):
        self._seg_gtos_med_mayor=importe

    # getter method
    def get_seg_gtos_med(self):
        return self._seg_gtos_med

    # setter method
    def set_seg_gtos_med(self,importe=0):
        self._seg_gtos_med=importe

    # getter method
    def get_vales_despensa(self):
        return self._vales_despensa

    # setter method
    def set_vales_despensa(self,importe=0):
        self._vales_despensa=importe

    # getter method
    def get_gratificacion_extra(self):
        return self._gratificacion_extra

    # setter method
    def set_gratificacion_extra(self,importe=0):
        self._gratificacion_extra=importe

