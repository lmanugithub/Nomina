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

        self.limite_inferior: Tablas = (
            0.01, 644.59, 5470.93, 9614.67, 11176.63, 13381.48,
            26988.51, 42537.59, 81211.26, 108281.68, 324845.02
        )

        self.limite_superior: Tablas = (
            644.58, 5470.92, 9614.66, 11176.62, 13381.47, 26988.50,
            42537.58, 81211.25, 108281.67, 324845.01, 2000000000.00
        )

        self.cuota_fija: Tablas = (
            0.00, 12.38, 321.26, 772.10, 1022.01, 1417.12, 4323.58,
            7980.73, 19582.83, 28245.36, 101876.90
        )

        self.por_excedente_limite_inferior: Tablas = (
            0.0192, 0.0640, 0.1088, 0.1600, 0.1792, 0.2136, 0.2352,
            0.3000, 0.3200, 0.3400, 0.3500
        )

        self.superior_subsidio: Tablas = (
            1768.96, 2653.38, 3472.84, 3537.87, 4446.15, 4717.18,
            5335.42, 6224.67, 7113.90, 7382.33, 2000000000.00
        )

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