# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from typing import Tuple


class Tablas:
    def __init__(self):

        Tablas = Tuple[
            float, float, float, float, float, float,
            float, float, float, float, float, float
        ]
        # tarifas 2023
        self.limite_inferior: Tablas = (
            0.01, 746.05, 6332.06, 11128.02, 12935.83, 15487.72,
            31236.50, 49233.01, 93993.91, 125325.21, 375975.62
        )
        # tarifas 2023
        self.limite_superior: Tablas = (
            746.04, 6332.05, 11128.01, 12935.82, 15487.71, 31236.49, 
            49233.00, 93993.90, 125325.20, 375975.61, 2000000000.00
        )
        # tarifas 2023
        self.cuota_fija: Tablas = (
            0.00, 14.32, 371.83, 893.63, 1182.88, 1640.18, 5004.12,
            9236.89, 22665.17, 32691.18, 117912.32
        )
        # tarifas 2023
        self.por_excedente_limite_inferior: Tablas = (
            0.0192, 0.0640, 0.1088, 0.1600, 0.1792, 0.2136, 0.2352,
            0.3000, 0.3200, 0.3400, 0.3500
        )
        # tarifas 2023
        self.superior_subsidio: Tablas = (
            1768.96, 2653.38, 3472.84, 3537.87, 4446.15, 4717.18,
            5335.42, 6224.67, 7113.90, 7382.33, 2000000000.00
        )
        # tarifas 2023
        self.cuota_subsidio: Tablas = (
            407.02, 406.83, 406.62, 392.77, 382.46, 354.23, 324.87,
            294.63, 253.54, 217.61, 0.00
        )


class Tablas_Anual:
    def __init__(self):

        Tablas = Tuple[
            float, float, float, float, float, float,
            float, float, float, float, float, float
        ]

        self.limite_inferior_anual: Tablas = (
            0.01, 7735.01, 65651.08, 115375.91, 134119.42, 160577.66, 
            323862.01, 510451.01, 974535.04, 1299380.05, 3898140.13,
        )

        self.limite_superior_anual: Tablas = (
            7735.00, 65651.07, 115375.90, 134119.41, 160577.65, 323862.00, 
            510451.00, 974535.03, 1299380.04, 3898140.12, 389814013.00,
        )

        self.cuota_fija_anual: Tablas = (
            0.00, 148.51, 3855.14, 9265.20, 12264.16, 17005.47, 
            51883.01, 95768.74, 234993.95, 338944.34, 1222522.76,
        )

        self.por_excedente_limite_inferior_anual: Tablas = (
            0.0192, 0.0640, 0.1088, 0.1600, 0.1792, 0.2136, 0.2352,
            0.3000, 0.3200, 0.3400, 0.3500
        )