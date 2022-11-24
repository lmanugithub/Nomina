# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
import pandas as pd
from cuotasimss import CuotasImss
from imss import CalculoIMSSObrero, CalculoIMSSPatron
from isr import ISR
from datetime import datetime
from sbc import SBC
from isr_aguinaldo import Impuesto_Aguinaldo
pd.options.display.float_format = '{:,.2f}'.format


class Proyectado():
    def __init__(self) -> None:
        self.years = ['2023','2024','2025','2026','2027','2028','2029','2030']
        
    def aumento(self, index):
        i = 1
        aumento = [1]
        for _ in self.years:
            i += 0.09
            aumento.append(round(i,2))
        return aumento[index]

    def vales(self, vale, index):
        if (vale * self.aumento(index)) > 1500:
            return 1500.0
        else:
            return (vale * self.aumento(index))

    def imss_pt(self, sal_diario, date, index):
        nomina = CalculoIMSSPatron()
        nomina.set_fecha_base(date)
        nomina.set_sdi(sal_diario)
        nomina._uma = 96.22 * self.aumento(index)
        return nomina.total_imss()


    def imss_ob(self, sal_diario, index):
        nomina = CalculoIMSSObrero()
        nomina.set_sdi(sal_diario)
        nomina._uma = 96.22 * self.aumento(index)
        return nomina.total_imss()


    def clean_load(self, data):
        pd.options.display.float_format = '{:,.2f}'.format 
        df = pd.read_excel(data, sheet_name='Hoja1')
        df.head()
        df['Fecha Ingreso'] = pd.to_datetime(df['Fecha Ingreso'], format='%Y-%m-%d')

if __name__=='__main__':
    test = Proyectado()
    print(test.aumento(1))
    print(test.aumento(4))
    for i in range(8+1):
        print(test.aumento(i), end=",")

