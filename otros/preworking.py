# coding: utf-8

# In[1]:

# Importando librerias
import os
import pandas as pd
import numpy as np
# Insert the directory


class Proyecto_f2f():

    def load_files(self, ruta):
        files = [file for file in os.listdir(ruta)]
        files.sort()
        all_files = pd.DataFrame()
        for file in files:
            df = pd.read_excel(ruta + file)
            all_files = pd.concat([all_files, df])
        return all_files

    def clean_solicitados(self, ruta, ruta_2, ruta_3):

        df_rec = self.load_files(ruta)

        df_rec['Fecha Recibo'] = pd.to_datetime(df_rec['Fecha Recibo'], errors='coerce',
                                                format='%Y-%m-%d %H:%M:%S')
        df_rec.drop(columns=['Total comision', 'Total liquidado',
                    'Total(D+E)', 'Fecha Liquidación', 'FILTRO', 'MES'], inplace=True)
        df_rec['TR'] = df_rec['TR'].astype('category')

        self.preprocessed_data_solicitados = df_rec.copy()

        dfliq = self.load_files(ruta_2)

        dfliq[['Monto_procesado', 'Comisión_BanWire', 'Comisión_Fija_Sin_IVA', 'IVA', 'IVA_Comisión_Fija']] = dfliq[[
            'Monto_procesado', 'Comisión_BanWire', 'Comisión_Fija_Sin_IVA', 'IVA', 'IVA_Comisión_Fija']].astype('float64')

        dfliq['sin Contracargos'] = dfliq['Liquidación'].apply(
            lambda x: x if x > 0 else 0)

        dfliq['Contracargos'] = dfliq['Liquidación'].apply(
            lambda x: 0 if x > 0 else x)

        self.preprocessed_data_liquidaciones_banwire = dfliq.copy()

        df_cobros = self.load_files(ruta_3)

        self.preprocessed_data_cobrados = df_cobros.copy()

        # Merge por la izquierda de los recibos solicitados contra sus cobros
        df_mer_left = pd.merge(df_rec, df_cobros, how='left',
                               left_on='Folio', right_on='Aplicar al documento')

        # Merge del datafrane liquidaciones con el dataframe del merge anterior
        df_union = pd.merge(dfliq, df_mer_left, how='left',
                            left_on='referencia', right_on='TR')

        df_union.duplicated(subset=['ID trans'])

        df_uni_01 = df_union[(df_union.duplicated(subset=[
                              'ID trans']) & df_union['Comisión_Fija_Sin_IVA'].apply(lambda x: True if x == 0 else False))]

        df_uni_02 = df_union.drop_duplicates(subset=['ID trans'])

        df_union = pd.concat([df_uni_01, df_uni_02])

        self.data_union = df_union.copy()

        df2021 = df_union[(df_union['R.F.C.'].notna())
                          & (df_union['Cobro'].isna())]

        df2021.set_index('Fecha_Liquidación', inplace=True)

        df2021.drop(columns=['Comisión_BanWire', 'IVA', 'Comisión_Fija_Sin_IVA', 'IVA_Comisión_Fija', 'Comisión MSI', 
                            'IVS MSI', 'Total_Comisión', 'Tasa', 'C/IVA', 'codigo_aut', 'ext_ref_cliente', 'Card', 'telefono',
                            'Comercio', 'Mese_Financiados', 'Utilidad', 'NaN', 'Cobro', 'Aplicar al documento', 'Tipo', 'Fecha', 
                            'Descuento tomado', 'Cancelación', 'Aplicar al monto', 'Pérdidas/ganancias', 'Etiqueta', 'mes'], inplace=True)

        self.data_por_cobrar = df2021.copy()

        liquidaciones = df_union.groupby(pd.Grouper(key='Fecha_Liquidación',))[
            ['Monto_procesado', 'Comisión_BanWire', 'Comisión_Fija_Sin_IVA', 'IVA', 'IVA_Comisión_Fija', 'sin Contracargos', 'Contracargos', 'Liquidación', 'Monto']].sum()

        self.data_liquidaciones = liquidaciones.copy()

    def putout_data_solicitados(self):
        return self.preprocessed_data_solicitados

    def putout_data_liq_ban(self):
        return self.preprocessed_data_liquidaciones_banwire

    def putout_data_cobros(self):
        return self.preprocessed_data_cobrados

    def putout_data_union(self):
        return self.data_union

    def putout_data_por_cobrar(self):
        return self.data_por_cobrar

    def putout_data_liquidaciones(self):
        return self.data_liquidaciones
