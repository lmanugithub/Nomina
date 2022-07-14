# coding: utf-8

# In[1]:

# Importando librerias
import os
import pandas as pd
import numpy as np
# Insert the directory


class Proyecto_base():

    def load_files(self, ruta):
        files = [file for file in os.listdir(ruta)]
        files.sort()
        all_files = pd.DataFrame()
        for file in files:
            df = pd.read_excel(ruta + file)
            all_files = pd.concat([all_files, df])
        return all_files

    def clean_files(self, r_1, r_2, r_3, r_4, r_5, r_6):

        cta_donantes = self.load_files(r_1)
        cta_donantes.drop(columns=['Auditoría orig.',
                                   'Referencia de distribución', 'Crédito'], inplace=True)
        cta_donantes.rename(columns={'Núm. maestro orig.': 'Folio_d',
                                     'Núm. Diario': 'Diario_d'}, inplace=True)
        self.preprocessed_cta_donantes = cta_donantes.copy()

        cta_ingresos = self.load_files(r_2)
        cta_ingresos.drop(columns=['Fecha trans.', 'Auditoría orig.',
                                   'Referencia de distribución', 'Núm. maestro orig.',
                                   'Nombre maestro orig.', 'Débito', ], inplace=True)
        cta_ingresos.rename(columns={'Núm. Diario': 'Diario_i'}, inplace=True)
        self.preprocessed_cta_ingresos = cta_ingresos.copy()

        centro_ctos = self.load_files(r_3)
        centro_ctos.drop(columns=['Número de cuenta', 'Descripción cuenta', 'Fecha contab. Contabilidad',
                                  'Referencia', 'Monto débito', 'Monto de crédito',
                                  'Id. de proveedor', 'COMUNICACION'], inplace=True)
        centro_ctos.rename(
            columns={'Entrada de diario': 'Diario_c'}, inplace=True)
        self.preprocessed_centro_ctos = centro_ctos.copy()

        smart_donan = self.load_files(r_4)
        smart_donan.drop(columns=['Tipo de documento', 'Fecha del documento', 'Nombre de cliente',
                                  'Monto de ventas', 'Estado anulado', 'Estado del documento',
                                  'Id. usuario contabilizado'], inplace=True)
        smart_donan.rename(columns={'Número de cliente': 'Id_cliente',
                                    'Número de documento': 'Folio_s'}, inplace=True)
        self.preprocessed_smart_donan = smart_donan.copy()

        
        donantes = self.load_files(r_5)
        donantes.drop(columns=['Nombre de cliente', 'Teléfono 1', 'Node',
                               'Número registro de impuestos', 'Núm. cuenta COGS',
                               'Núm. cuenta cuentas por cobrar', 'Núm. cuenta de inventario',
                               'Núm. cuenta de ventas', 'Núm. cuenta cancelación',
                               'Cancelaciones año actual', ], inplace=True)
        donantes['direccion'] = donantes['Dirección 1']+" "+donantes['Dirección 2'] + \
                                " "+donantes['Ciudad']+" " + \
                                donantes['Estado o provincia']+" "+donantes['Postal']
        donantes.drop(columns=['Dirección 1', 'Dirección 2',
                       'Ciudad', 'Estado o provincia', 'Postal',],inplace=True)
        donantes.rename(columns={'Número de cliente':'Id_cliente',
                         'Número de cliente de empresa':'Id_cta_nacional'},inplace=True)
        self.preprocessed_donantes = donantes.copy()


        elcfdi = self.load_files(r_6)
        idx_filtro = elcfdi['Tipo'].isin(['ingreso'])
        elcfdi = elcfdi[idx_filtro]
        elcfdi['Funcional'] = elcfdi.apply(lambda x: x['Total']* x['Tipo de Cambio'], axis=1)
        elcfdi.drop(columns=['XML','Rfc Emisor','Nombre Emisor','Descuento'] ,inplace=True)
        elcfdi.drop(columns=['Total impuesto Trasladado','Nombre Impuesto',
                     'Total impuesto Retenido','Nombre Impuesto','Versión',
                     'Régimen Fiscal','Estado','Estatus',
                     'Validación EFOS','Fecha Consulta','Conceptos'] ,inplace=True)
        elcfdi['Regimen Fiscal'] = elcfdi['Rfc Receptor'].apply(lambda x : 'Persona Fisica' if len(x)==13 else 'Persona Moral' )
        elcfdi['Nacionalidad'] = elcfdi['Rfc Receptor'].apply(lambda x : 'extranjero' if x=='XEXX010101000' else 'nacional' )
        elcfdi['Proyecto'] = elcfdi['Folio'].apply(lambda x : 'Socios UNETE' if len(x)==10 else 'Normal' )
        elcfdi['Identificado'] = elcfdi['Rfc Receptor'].apply(lambda x : 'Publico General' if x=='XAXX010101000' else 'Particular' )
        self.preprocessed_elcfdi = elcfdi.copy()

        temp_1 = pd.merge(cta_donantes, cta_ingresos, how='left', left_on='Diario_d', right_on='Diario_i')
        temp_2 = pd.merge(temp_1, centro_ctos, how='left', left_on='Diario_d', right_on='Diario_c')
        temp_3 = pd.merge(temp_2, smart_donan, how='left', left_on='Folio_d', right_on='Folio_s')
        temp_4 = pd.merge(temp_3, donantes, how='left', left_on='Id_cliente', right_on='Id_cliente')
        base = pd.merge(temp_4, elcfdi, how='left', left_on='Folio_d', right_on='Folio')
        base.drop(columns=['Diario_d', 'Diario_i', 'Crédito', 'Diario_c', 'Folio_s',
                   'Nombre Receptor', 'Tipo', 'Folio', 'Fecha', 'Sub Total',
                   'Nombre Impuesto.1', 'Total', 'Moneda', 'Tipo de Cambio',
                   'Funcional', 'Identificado'], inplace=True)
        base = base[['Id_cliente', 'Id_cta_nacional', 'Cuenta_donors', 'Cuenta_incomes',
             'Serie', 'Folio_d', 'Fecha trans.', 'Nombre maestro orig.',
             'Rfc Receptor', 'SEGMENTO', 'direccion', 'UUID', 'Método de Pago','Uso CFDI',
             'Forma de Pago', 'Nacionalidad', 'Regimen Fiscal', 'Débito', 'Proyecto']]

        self.processed_base_recibos = base.copy()
        


    def putout_cta_donantes(self):
        return self.preprocessed_cta_donantes

    def putout_cta_ingresos(self):
        return self.preprocessed_cta_ingresos

    def putout_centro_ctos(self):
        return self.preprocessed_centro_ctos

    def putout_smart_donan(self):
        return self.preprocessed_smart_donan

    def putout_donantes(self):
        return self.preprocessed_donantes

    def putout_elcfdi(self):
        return self.preprocessed_elcfdi

    def putout_base_recibos(self):
        return self.processed_base_recibos
