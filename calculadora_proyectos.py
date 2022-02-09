
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

    def clean_and_load_data(self, data_file, num_meses:int = 1):
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
        dataframe['3%_nomina'] = dataframe['suma'].apply(
            lambda x: x*0.03)
        dataframe['Cuota_Imss'] = dataframe['salarioDiario'].apply(
            CuotasImss.function_imss_patron)
        dataframe['Cuotas_RCV'] = dataframe['salarioDiario'].apply(
            CuotasImss.function_rcv_patronal)
        dataframe['Infonavit'] = dataframe['salarioDiario'].apply(
            lambda x: x*0.05*30.4)
        dataframe['Carga_laboral'] = dataframe.loc[:, ['3%_nomina', 'Cuota_Imss',
                                                       'Cuotas_RCV', 'Infonavit']].sum(axis=1)
        dataframe['Carga_laboral_total'] = dataframe.loc[:,
                                                         ['suma', 'Carga_laboral']].sum(axis=1)
        
        # Proyeccion de la carga laboral por meses
        meses = num_meses
        dataframe['Sueldo_proyectado'] = dataframe['suma'].apply(
            lambda x: x * meses)
        dataframe['Aguinaldo'] = dataframe['suma'].apply(
            lambda x: (((x/30.4)*15.2)/12)*meses)
        resultado_a = dias_vacaciones.apply(lambda x: x*meses)
        resultado_b = dataframe['suma'].multiply(resultado_a)
        dataframe['Vacaciones'] = resultado_b.apply(lambda x: x/(30.4*12))
        dataframe['Prima_vac'] = dataframe['Vacaciones'].apply(
            lambda x: (x*0.25)*meses)
        # Base para calculo de 3% sobre nomina proyectado
        base_para_3_preyectado = dataframe.loc[:, ['Sueldo_proyectado', 'Aguinaldo',
                                                   'Vacaciones', 'Prima_vac']].sum(axis=1)
        # Carga laboral proyectado
        dataframe['3%_nomina_proyectado'] = base_para_3_preyectado.apply(
            lambda x: x * 0.03)
        dataframe['Cuota_Imss_proyectado'] = dataframe['Cuota_Imss'].apply(
            lambda x: x * meses)
        dataframe['Cuotas_RCV_proyectado'] = dataframe['Cuotas_RCV'].apply(
            lambda x: x * meses)
        dataframe['Infonavit_proyectado'] = dataframe['Infonavit'].apply(
            lambda x: x * meses)
        dataframe['Carga_laboral_proyectado'] = dataframe.loc[:, ['3%_nomina_proyectado', 'Cuota_Imss_proyectado',
                                                                  'Cuotas_RCV_proyectado', 'Infonavit_proyectado']].sum(axis=1)
        # Costo del Proyecto
        dataframe['Costo_proyecto'] = dataframe.loc[:, [
            'Carga_laboral_proyectado', 'Sueldo_proyectado']].sum(axis=1)

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

# # print((dataframe.iloc[:, 21:]))
# # print(list(dataframe['sueldo neto']))
# print(dataframe)


# def duracion_proyecto(inicio, fin) -> int:
#     difference = fin - inicio
#     dias = str(difference).split()
#     return int(dias[0])//30.4


# def mes_even(inicio) -> bool:
#     mes = inicio.strftime('%m')
#     if int(mes) % 2 == 0:
#         return True
#     else:
#         return False


# if __name__ == '__main__':
#     # values = input('Enter space separed values: ').split()
#     # a, b, c = map(int, values)
#     inicio = datetime(2021, 8, 1)
#     fin = datetime(2022, 6, 1)
#     meses = duracion_proyecto(inicio, fin)
#     print(meses)
#     print(mes_even(inicio))
