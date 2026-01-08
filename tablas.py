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
        # tarifas 2026
        self.limite_inferior: Tablas = ( # type: ignore
            0.01, 844.6, 7168.52, 12598.03, 14644.65, 17533.65, 
            35362.84, 55736.69, 106410.51, 141880.67, 425642.00
        )
        # tarifas 2026
        self.limite_superior: Tablas = ( # type: ignore
            844.59, 7168.51, 12598.02, 14644.64, 17533.64, 35362.83, 
            55736.68, 106410.5, 141880.66, 425641.99, 3000000000.00
        )
        # tarifas 2026
        self.cuota_fija: Tablas = ( # type: ignore
            0.00, 16.22, 420.95, 1011.68, 1339.14, 1856.84, 5665.16, 
            10457.09, 25659.23, 37009.69, 133488.54
        )
        # tarifas 2026
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
        self.ingresos_mensuales_gravados = 10171.00  #9081.00
        self.spe_mensual = 475.00 #390.12


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
