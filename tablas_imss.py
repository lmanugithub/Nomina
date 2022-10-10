# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from dataimss import DataImss

class Tablas_Imss(DataImss):
    def __init__(self) -> None:
        super().__init__()

        self.ceav = {
            '2023': (0.03150,	0.03281,	0.03575,	0.03751,	0.03869,	0.03953,	0.04016,	0.04241),
            '2024': (0.03150,	0.03413,	0.04000,	0.04353,	0.04588,	0.04756,	0.04882,	0.05331),
            '2025': (),
            '2026': (),
            '2027': (), 
            '2028': (), 
            '2029': (), 
            '2030': () 
        }

        self.index_ceav = (
            1.01, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 10.00 
        )

    def dias_vacacion(self, ano: str) -> int:
        return self.ceav[str(ano)][0]
    
