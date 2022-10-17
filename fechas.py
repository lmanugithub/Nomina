# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from datetime import date, datetime

import pandas as pd


class WorkingTime():
    # def __init__(self):
        # datetime.__init__(self)
        # date.__init__(self)
        # self.fecha_base = pd.to_datetime('2021/01/01', format='%Y/%m/%d')

    # getter method
    def get_fecha_base(self):
        return self.fecha_base

    # setter method
    def set_fecha_base(self, date):
        self.fecha_base = pd.to_datetime(date, format='%Y/%m/%d')

    # getter method
    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    # setter method
    def set_fecha_ingreso(self, date):
        self.fecha_ingreso = pd.to_datetime(date, format='%Y/%m/%d')

    # getter method
    def get_fecha_baja(self):
        return self.fecha_actual

    # setter method
    def set_fecha_baja(self, date):
        self.fecha_actual = pd.to_datetime(date, format='%Y/%m/%d')

    def dias_trabajados(self):
        diferencia = self.get_fecha_baja() - self.get_fecha_ingreso()
        dias = (diferencia).days//365
        return int(dias)

    def dias_ano_trabajados(self):
        diferencia = self.get_fecha_baja() - self.fecha_base
        dias = (diferencia).days//365
        return int(dias)

    def aniversario_vacaciones_actual(self):
        ano_base = self.fecha_base.year
        mes_ingreso = self.get_fecha_ingreso().month
        dia_ingreso = self.get_fecha_ingreso().day
        ano = int(ano_base)
        mes = int(mes_ingreso)
        dia = int(dia_ingreso)
        date = (f'{ano}/{mes}/{dia}')
        fecha_aniversario = pd.to_datetime(date, format='%Y/%m/%d')
        return fecha_aniversario

    def dias_vacaciones_trabajadas(self):
        diferencia = self.get_fecha_baja() - self.aniversario_vacaciones_actual()
        dias = (diferencia).days//365
        if int(dias) > 0:
            return int(dias)+1
        else:
            return 0
