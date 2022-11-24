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
from fechas import WorkingTime
pd.options.display.float_format = '{:,.2f}'.format


class Proyectado():
    def __init__(self) -> None:
        self.years = ['2023','2024','2025','2026','2027','2028','2029','2030']
        self.date_2022 = pd.to_datetime('2022/12/31')
        self.date_2023 = pd.to_datetime('2023/12/31')
        
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

    def dias_laborados(self, base_date, begining_date, mensual):
        time = WorkingTime()
        time.set_fecha_base(base_date)
        time.set_fecha_ingreso(begining_date)
        dias = (time.get_fecha_base() - time.get_fecha_ingreso()).days
        if dias > 365:
            return (mensual/30.4) * 365
        else:
            return (mensual/30.4) * (dias + 1) 


    def clean_load(self, data):
        pd.options.display.float_format = '{:,.2f}'.format 
        df = pd.read_excel(data, sheet_name='Hoja1')
        df.head()
        df['Fecha Ingreso'] = pd.to_datetime(df['Fecha Ingreso'], format='%Y-%m-%d')

        # SECCION DEL 2022

        ## POSIBLE AUMENTO

        df['Sueldo 2022'] = df['Sueldo mensual'].apply(lambda x: x * self.aumento(0))
        df['Vales 2022'] = df.apply(lambda x: self.vales(x['Vales'], 0), axis=1)

        # Datos mensuales
        df['SDI 2022'] = df.apply(lambda x: SBC.funcion_sdi(sueldo = x['Sueldo 2022'], a = x['Fecha Ingreso'], b = self.date_2022), axis=1)
        df['SBC 2022'] = df.apply(lambda x: SBC.funcion_sbc(sueldo = x['Sueldo 2022'], vales = x['Vales 2022'], a = x['Fecha Ingreso'], b = self.date_2022), axis=1)
        df['ISR 2022'] = df['Sueldo 2022'].apply(lambda x: ISR.function_isr(x))
        df['IMSS Ob 2022'] = df.apply(lambda x: self.imss_ob(x['SBC 2022'], index=0), axis=1)
        df['IMSS Pt 2022'] = df.apply(lambda x: self.imss_pt(sal_diario= x['SBC 2022'], date=self.date_2022, index=0), axis=1)
        df['ISN 2022'] = df['Sueldo 2022'] * 0.03
        _isr_ = df['Sueldo 2022'].apply(lambda x: ISR.function_isr(x))
        df['Neto'] = df['Sueldo 2022'] - _isr_ - df['IMSS Ob 2022']
        df['Aguinaldo 2022'] = df.apply(lambda x: SBC.funcion_aguinaldo(sueldo = x['Sueldo 2022'], a = x['Fecha Ingreso'], b = self.date_2022), axis=1)
        # df['Impto Aguinaldo 2022'] = df.apply(lambda x: impto_ag(x['Sueldo mensual'], x['Aguinaldo']) ,axis=1)
        df['Prima Vacacional 2022'] = df.apply(lambda x: SBC.funcion_pv(sueldo = x['Sueldo 2022'], date_ingreso = x['Fecha Ingreso'], date_base = self.date_2022), axis=1)
        df['Carga 2022'] = df.loc[:,['IMSS Pt 2022','ISN 2022']].sum(axis = 1)
        # Datos anualisados en base a los dias trabajados
        prestaciones = df.loc[:,['Aguinaldo 2022','Prima Vacacional 2022']].sum(axis = 1)
        sueldo_anual = df.apply(lambda x: self.dias_laborados(base_date = self.date_2022, begining_date = x['Fecha Ingreso'], mensual = x['Sueldo 2022']), axis = 1)
        df['Sueldo 2022 anual'] = prestaciones + sueldo_anual
        df['Vales 2022 anual'] = (df.apply(lambda x: self.dias_laborados(base_date = self.date_2022, begining_date = x['Fecha Ingreso'], mensual = x['Vales 2022']), axis = 1)).astype('int')
        df['Carga 2022 anual'] = df.apply(lambda x: self.dias_laborados(base_date = self.date_2022, begining_date = x['Fecha Ingreso'], mensual = x['Carga 2022']), axis = 1)



        # SECCION DEL 2023

        ## POSIBLE AUMENTO

        df['Sueldo 2023'] = df['Sueldo mensual'].apply(lambda x: x * self.aumento(1))
        df['Vales 2023'] = df.apply(lambda x: self.vales(x['Vales'], index=1), axis=1)

        # Datos mensuales
        df['SDI 2023'] = df.apply(lambda x: SBC.funcion_sdi(sueldo = x['Sueldo 2023'], a = x['Fecha Ingreso'], b = self.date_2023), axis=1)
        df['SBC 2023'] = df.apply(lambda x: SBC.funcion_sbc(sueldo = x['Sueldo 2023'], vales = x['Vales 2023'], a = x['Fecha Ingreso'], b = self.date_2023), axis=1)
        df['ISR 2023'] = df['Sueldo 2023'].apply(lambda x: ISR.function_isr(x))
        df['IMSS Ob 2023'] = df.apply(lambda x: self.imss_ob(x['SBC 2023'], index=1), axis=1)
        df['IMSS Pt 2023'] = df.apply(lambda x: self.imss_pt(sal_diario= x['SBC 2023'], date=self.date_2023, index=1), axis=1)
        df['ISN 2023'] = df['Sueldo 2023'] * 0.03
        _isr_ = df['Sueldo 2023'].apply(lambda x: ISR.function_isr(x))
        df['Neto'] = df['Sueldo 2023'] - _isr_ - df['IMSS Ob 2023']
        df['Aguinaldo 2023'] = df.apply(lambda x: SBC.funcion_aguinaldo(sueldo = x['Sueldo 2023'], a = x['Fecha Ingreso'], b = self.date_2023), axis=1)
        # df['Impto Aguinaldo 2023'] = df.apply(lambda x: impto_ag(x['Sueldo mensual'], x['Aguinaldo']) ,axis=1)
        df['Prima Vacacional 2023'] = df.apply(lambda x: SBC.funcion_pv(sueldo = x['Sueldo 2023'], date_ingreso = x['Fecha Ingreso'], date_base = self.date_2023), axis=1)
        df['Carga 2023'] = df.loc[:,['IMSS Pt 2023','ISN 2023']].sum(axis = 1)
        # Datos anualisados en base a los dias trabajados
        prestaciones = df.loc[:,['Aguinaldo 2023','Prima Vacacional 2023']].sum(axis = 1)
        sueldo_anual = df.apply(lambda x: self.dias_laborados(base_date = self.date_2023, begining_date = x['Fecha Ingreso'], mensual = x['Sueldo 2023']), axis = 1)
        df['Sueldo 2023 anual'] = prestaciones + sueldo_anual
        df['Vales 2023 anual'] = (df.apply(lambda x: self.dias_laborados(base_date = self.date_2023, begining_date = x['Fecha Ingreso'], mensual = x['Vales 2023']), axis = 1)).astype('int')
        df['Carga 2023 anual'] = df.apply(lambda x: self.dias_laborados(base_date = self.date_2023, begining_date = x['Fecha Ingreso'], mensual = x['Carga 2023']), axis = 1)

 
 
        self.preprocessed_data = df.copy()

    def put_out(self):
        return self.preprocessed_data


        # Testing


    def test(self, data):
        pd.options.display.float_format = '{:,.2f}'.format 
        df = pd.read_excel(data, sheet_name='Hoja1')
        df.head()
        df['Fecha Ingreso'] = pd.to_datetime(df['Fecha Ingreso'], format='%Y-%m-%d')
        df['Sueldo 2022'] = df['Sueldo mensual'].apply(lambda x: x * self.aumento(0))
        df['Vales 2022'] = df.apply(lambda x: self.vales(x['Vales'], 0), axis=1)
        df['SBC 2022'] = df.apply(lambda x: self.func_sdi(sueldo = x['Sueldo 2022'], ingreso = x['Fecha Ingreso'], base = self.date_2022), axis=1)

        self.sueldo = df.copy()

    def put_out_test(self):
        return self.sueldo


if __name__=='__main__':
    test = Proyectado()
    print(test.aumento(1))
    print(test.aumento(4))
    for i in range(8+1):
        print(test.aumento(i), end=",")

