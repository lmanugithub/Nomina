# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

from dataimss import DataImss
# Importación de librerias
from isr import ISR
from sbc import SBC

class Reglamento(ISR):
    def __init__(self):
        super().__init__()
        self._sueldo_base = 0



