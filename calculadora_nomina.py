# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from datetime import datetime
import pandas as pd
from isr import ISR
from cuotasimss import CuotasImss
from vacaciones import Vacaciones


class Proyectos():


    def dias_proyectados(self, num):
        calculo = Vacaciones()
        if num < 0:
            return calculo.dias_vacacion(str(1))
        elif num == 0:
            return calculo.dias_vacacion(str(num+2))
        else:
            return calculo.dias_vacacion(str(num+1))


    def factor_sdi(self, vacation):
        propossional_vacation = vacation * 0.25
        return round((365 + 15 + propossional_vacation)/365, 4)


    def triangulacion(self, valor_1, valor_2, valor_agg):
        '''
        valor: valor de la base segunda quincena que es la suma de dos quincenas + fondo
        valor_agg: fondo fijo
        '''
        objetivo = valor_1 - ISR.function_isr(valor_1*2)/2
        cuenta = 0
        isr = ISR.function_isr(valor_2)/2 
        dato = (valor_2/2) - isr - valor_agg

        while dato < objetivo:
            cuenta += 1
            isr = ISR.function_isr(valor_2 + cuenta)/2 
            dato = ((valor_2/2)+cuenta) - isr - valor_agg
        return cuenta


    def clean_and_load_data(self, data_file):
        '''
        data_file: Archivo a imortar
        num_meses: Número de meses a proyectar
        '''
        # Esto es para dar un poco de formato
        pd.options.display.max_rows = None
        pd.options.display.max_columns = None
        pd.options.display.float_format = '$ {:,.2f}'.format

        # Llamamos el archivo de excel
        dataframe = pd.read_excel(data_file)

        # Es muy importante dar correcto formato a la columna de fecha
        dataframe['date'] = pd.to_datetime(dataframe['date'])

        # Establecemos la fecha base para los calculos
        fecha_base = pd.to_datetime('2021/12/31', format='%Y/%m/%d')

        dataframe['suma'] = dataframe.sum(axis=1)

        # Todo este codigo es para calcular el SDI en base a la fecha de ingreso
        years_working = ((dataframe['date'].apply(
            lambda x: fecha_base-x)).dt.days//365)
        dias_vacaciones = years_working.apply(self.dias_proyectados)
        factor_to_apply = dias_vacaciones.apply(self.factor_sdi)
        sueldo_diario = dataframe['suma'].apply(lambda x: x/30.4)
        dataframe['salarioDiario'] = sueldo_diario.multiply(factor_to_apply)

        # Calculo carga laboral mensual normal

        # Proyeccion de la carga laboral por meses

        # Base para calculo de 3% sobre nomina proyectado

        # Carga laboral proyectado

        # Costo del Proyecto

        # Recibo nomina normal
        dataframe['ISR Q1'] = ((dataframe['a'].apply(lambda x: x*2)
                                ).apply(ISR.function_isr)).apply(lambda x: x/2)
        dataframe['IMSS Q1'] = (dataframe['salarioDiario'].apply(
            CuotasImss.function_imss_obrero)).apply(lambda x: x/2)
        retenciones = dataframe.loc[:, [
            'ISR Q1', 'IMSS Q1']].sum(axis=1)
        dataframe['sueldo Q1'] = dataframe['a'].sub(retenciones)

        isr_q1 = ((dataframe['a'].apply(lambda x: x*2)
                   ).apply(ISR.function_isr)).apply(lambda x: x/2)
        isr_q2 = (dataframe['suma'].apply(
            ISR.function_isr)).apply(lambda x: x/2)

        dataframe['ISR Q2'] = (dataframe['suma'].apply(
            ISR.function_isr)).apply(lambda x: x/2)
        dataframe['IMSS Q2'] = (dataframe['salarioDiario'].apply(
            CuotasImss.function_imss_obrero)).apply(lambda x: x/2)
        retenciones = dataframe.loc[:, [
            'ISR Q2', 'IMSS Q2']].sum(axis=1)
        dataframe['sueldo Q2'] = (dataframe['suma'].apply(
            lambda x: x/2)).sub(retenciones).sub(dataframe['f'])

        dataframe['Objetivo'] = dataframe['a'].sub(isr_q1)

        dataframe['gratificación'] = dataframe.apply(
            lambda x: self.triangulacion(x['a'], x['suma'], x['f']), axis=1)

        base_q3 = dataframe.loc[:,['suma','gratificación']].sum(axis=1)

        isr_q3 = (base_q3.apply(ISR.function_isr)).apply(lambda x: x/2)

        dataframe['ISR Q3'] = (base_q3.apply(ISR.function_isr)).apply(lambda x: x/2)
        dataframe['IMSS Q3'] = (dataframe['salarioDiario'].apply(
            CuotasImss.function_imss_obrero)).apply(lambda x: x/2)
        retenciones = dataframe.loc[:, [
            'ISR Q3', 'IMSS Q3']].sum(axis=1)
        dataframe['sueldo Q3'] = (dataframe['suma'].apply(
            lambda x: x/2)).sub(retenciones).sub(dataframe['f'])

        # resta = dataframe['sueldo neto'].apply(lambda x: x - 6000)
        # resultado = dataframe['suma'].apply(lambda x: x * 0.32)
        # resultado_1 = resta - resultado
        # dataframe['ahorro'] = resultado_1

        self.preprocessed_data = dataframe.copy()

    def putout_data(self):
        return self.preprocessed_data
