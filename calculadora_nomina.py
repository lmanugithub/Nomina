
# coding: utf-8

# In[1]:

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
        dataframe['ISR mensual'] = dataframe['suma'].apply(ISR.function_isr)
        dataframe['IMSS mensual'] = dataframe['salarioDiario'].apply(
            CuotasImss.function_imss_obrero)
        retenciones = dataframe.loc[:, [
            'ISR mensual', 'IMSS mensual']].sum(axis=1)
        dataframe['sueldo neto'] = dataframe['suma'].sub(retenciones)

        resta = dataframe['sueldo neto'].apply(lambda x: x - 6000)
        resultado = dataframe['suma'].apply(lambda x: x * 0.32)
        resultado_1 = resta - resultado
        dataframe['ahorro'] = resultado_1

        self.preprocessed_data = dataframe.copy()

    def putout_data(self):
        return self.preprocessed_data

