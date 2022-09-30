# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

class DataImss():
    _uma = 96.22 # <- apartir de 1 febrero 2022. 89.62 - 2021
    dias = 30.4
    _prima_de_riesgo = 0.54355

    def __init__(self) -> None:
        self._sdi = 0

    # getter method
    def get_sdi(self):
        return self._sdi

    # setter method
    def set_sdi(self, sdi):
        self._sdi = sdi
