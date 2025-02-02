# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
import pandas as pd

from datostrabajador import DatosTrabajador
from vacaciones import Vacaciones


class SBC(Vacaciones, DatosTrabajador):

    def __init__(self) -> None:
        Vacaciones.__init__(self)
        DatosTrabajador.__init__(self)

    # Antigüedad en años
    def antiguedad(self):
        years = (self.fecha_base - self.fecha_ingreso).days // 365
        return years

    # Antigüedad que se usara para el sbc ya que los que no alcanza el año se pone un año de antigüedad
    def antiguedad_sbc(self):
        year = (self.fecha_base - self.fecha_ingreso).days // 365
        if year > 0:
            return self.antiguedad()
        else:
            return 1

    def vacaciones_dias(self):
        years = self.antiguedad_sbc()
        years = str(years)
        return self.dias_vacacion(years)

    # Metodo creado para la prima vacacional
    def vacaciones_dias_r(self):
        years = self.antiguedad()
        if years > 0:
            years = str(years)
            return self.dias_vacacion(years)
        else:
            return 0

    # Los Vales computan para el sbc pero hasta un tope el cual calcula este metodo 
    # Se va a redondear los calculos del tope de vales de despensa, ya que así se hace en ExM
    def tope_vales(self):
        '''
        Se va a redondear los calculos del tope de vales de despensa, ya que así se hace en ExM
        '''
        tope_diario = self._uma * 0.40
        tope_mensual = tope_diario * self.dias
        if self.get_vales_despensa() > tope_mensual:
            return round((self.get_vales_despensa() - tope_mensual) / self.dias,0)
        else:
            return 0

    # Metodo calcula lo proporcional del aguinaldo para el sbc
    def aguinaldo_sbc(self):
        sd = self.get_sueldo_mensual() / 30
        return round(sd * (15/365), 2)

    # Metodo calcula lo proporcional del la prima vacacional para el sbc
    def prima_vac_sbc(self):
        sd = self.get_sueldo_mensual() / 30
        return round((sd * self.vacaciones_dias() * self.prima_vacacional) / 365, 2)

    def salario_base_cotizacion(self):
        sd = self.get_sueldo_mensual() / 30
        sbc = self.tope_vales() + self.aguinaldo_sbc() + self.prima_vac_sbc() + sd
        if (self._uma * 25) > sbc:
            return sbc
        else:
            return self._uma * 25

    @classmethod
    def funcion_sbc(cls, sueldo, vales, admission_date, base_date):
        nomina = SBC()
        nomina.set_fecha_ingreso(admission_date)
        nomina.set_fecha_base(base_date)
        nomina.set_sueldo_mensual(sueldo)
        nomina.set_vales_despensa(vales)
        return nomina.salario_base_cotizacion()

    # En el primer año de calendario solo se paga el aguinaldo en forma proporcional
    def proporcion_aguinaldo(self):
        dias = (self.fecha_base - self.fecha_ingreso).days
        if dias > 365:
            return (15/365) * 365
        else:
            return (15/365) * (dias + 1) 

    def aguinaldo(self):
        sd = self.get_sueldo_mensual() / 30 
        return round((sd * self.proporcion_aguinaldo()), 2)

    @classmethod
    def funcion_aguinaldo(cls, sueldo, admission_date, base_date):
        nomina = SBC()
        nomina.set_fecha_ingreso(admission_date)
        nomina.set_fecha_base(base_date)
        nomina.set_sueldo_mensual(sueldo)
        return nomina.aguinaldo()

    def prima_vac(self):
        sd = self.get_sueldo_mensual() / 30
        return round((sd * self.vacaciones_dias_r() * 0.25), 2)

    @classmethod
    def funcion_pv(cls, sueldo, admission_date, base_date):
        nomina = SBC()
        nomina.set_fecha_ingreso(admission_date)
        nomina.set_fecha_base(base_date)
        nomina.set_sueldo_mensual(sueldo)
        return nomina.prima_vac()

    def sdi(self):
        sd = self.get_sueldo_mensual() / 30
        return self.aguinaldo_sbc() + self.prima_vac_sbc() + sd

    @classmethod
    def funcion_sdi(cls, sueldo, admission_date, base_date):
        nomina = SBC()
        nomina.set_sueldo_mensual(sueldo)
        nomina.set_fecha_ingreso(admission_date)
        nomina.set_fecha_base(base_date)
        return nomina.sdi()

    # Funcion vacaciones
    @classmethod
    def funcion_dias_vacaciones(cls, admission_date, base_date):
        nomina = SBC()
        nomina.set_fecha_ingreso(admission_date)
        nomina.set_fecha_base(base_date)
        return nomina.vacaciones_dias_r()

