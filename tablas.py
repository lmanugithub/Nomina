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
        # tarifas 2024
        self.limite_inferior: Tablas = ( # type: ignore
            0.01, 746.05, 6332.06, 11128.02, 12935.83, 15487.72,
            31236.50, 49233.01, 93993.91, 125325.21, 375975.62
        )
        # tarifas 2024
        self.limite_superior: Tablas = ( # type: ignore
            746.04, 6332.05, 11128.01, 12935.82, 15487.71, 31236.49, 
            49233.00, 93993.90, 125325.20, 375975.61, 2000000000.00
        )
        # tarifas 2024
        self.cuota_fija: Tablas = ( # type: ignore
            0.00, 14.32, 371.83, 893.63, 1182.88, 1640.18, 5004.12,
            9236.89, 22665.17, 32691.18, 117912.32
        )
        # tarifas 2024
        self.por_excedente_limite_inferior: Tablas = ( # type: ignore
            0.0192, 0.0640, 0.1088, 0.1600, 0.1792, 0.2136, 0.2352,
            0.3000, 0.3200, 0.3400, 0.3500
        )
        # tarifas 2023
        self.superior_subsidio: Tablas = ( # type: ignore
            1768.96, 2653.38, 3472.84, 3537.87, 4446.15, 4717.18,
            5335.42, 6224.67, 7113.90, 7382.33, 2000000000.00
        )
        # tarifas 2023
        self.cuota_subsidio: Tablas = ( # type: ignore
            407.02, 406.83, 406.62, 392.77, 382.46, 354.23, 324.87,
            294.63, 253.54, 217.61, 0.00
        )
        # tarifas mayo 2024
        self.ingresos_mensuales_gravados = 9081.00
        self.spe_mensual = 390.12


class Tablas_Anual:
    def __init__(self):

        Tablas = Tuple[
            float, float, float, float, float, float,
            float, float, float, float, float, float
        ]

        self.limite_inferior_anual: Tablas = ( # type: ignore
            0.01, 8952.50, 75984.56, 133536.08, 155229.81, 185852.58, 
            374837.89, 590796.00, 1127926.85, 1503902.47, 4511707.38, 
        )

        self.limite_superior_anual: Tablas = ( # type: ignore
            8952.49, 75984.55, 133536.07, 155229.80, 185852.57, 374837.88, 
            590795.99, 1127926.84, 1503902.46, 4511707.37, 451170737.00,
        )

        self.cuota_fija_anual: Tablas = ( # type: ignore
            0.00, 171.88, 4461.94, 10723.55, 14194.54, 19682.13, 
            60049.40, 110842.74, 271981.99, 392294.17, 1414947.85, 
        )

        self.por_excedente_limite_inferior_anual: Tablas = ( # type: ignore
            0.0192, 0.0640, 0.1088, 0.1600, 0.1792, 0.2136, 0.2352,
            0.3000, 0.3200, 0.3400, 0.3500
        )
