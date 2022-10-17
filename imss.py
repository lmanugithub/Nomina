# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from dataimss import DataImss
from fechas import WorkingTime
from tablas_imss import Tablas_Imss


class CalculoIMSSObrero(DataImss):
    def __init__(self):
        super().__init__()

    def salario_diario(self):
        if (self._uma * 25) > self._sdi:
            return (1) * self._sdi
        else:
            return self._uma * 25

    # 02 ENFERMEDAD Y MATERNIDAD _EXCEDENTE
    def cuotas_pres_especie_enf_mat(self):
        exento = self._uma * 3
        diferencia = self.salario_diario() - exento

        if diferencia >= 0:
            return round((diferencia * self.dias * 0.0040), 4)
        else:
            return 0

    # 03 ENFERMEDAD Y MATERNIDAD _GM
    def gastos_medicos_pencionados(self):
        return round((self.salario_diario() * self.dias * 0.00375), 4)

    # 04 ENFERMEDAD Y MATERNIDAD _PD
    def cuotas_pres_dinero_enf_mat(self):
        return round((self.salario_diario() * self.dias * 0.0025), 4)

    # II_ENFERMEDAD Y MATERNIDAD
    def cuota_enfermedad_maternidad(self):
        return round(self.cuotas_pres_dinero_enf_mat() +
                     self.gastos_medicos_pencionados() +
                     self.cuotas_pres_especie_enf_mat(), 4)

    # III_INVALIDEZ Y VIDA _IV
    def cuota_invalidez(self):
        return round((self.salario_diario() * self.dias * 0.00625), 4)

    # IV_RETIRO CESANTIA Y VEJEZ 02
    def cuota_cesantia_vejez(self):
        return round((self.salario_diario() * self.dias * 0.01125), 4)

    def total_imss(self):
        return round((self.cuota_enfermedad_maternidad() +
                      self.cuota_invalidez() +
                      self.cuota_cesantia_vejez()), 2)  # self.cuota_gastos_medicos()

    @classmethod
    def function_imss_obrero(cls, x):
        calculo = CalculoIMSSObrero()
        calculo.set_sdi(x)
        return calculo.total_imss()


class CalculoIMSSPatron(DataImss, WorkingTime, Tablas_Imss):
    def __init__(self):
        super().__init__()
        
        self.ceav = {
            '2023': (0.03150,	0.03281,	0.03575,	0.03751,	0.03869,	0.03953,	0.04016,	0.04241),
            '2024': (0.03150,	0.03413,	0.04000,	0.04353,	0.04588,	0.04756,	0.04882,	0.05331),
            '2025': (0.03150,	0.03544,	0.04426,	0.04954,	0.05307,	0.05559,	0.05747,	0.06422),
            '2026': (0.03150,	0.03676,	0.04851,	0.05556,	0.06026,	0.06361,	0.06613,	0.07513),
            '2027': (0.03150,	0.03807,	0.05276,	0.06157,	0.06745,	0.07164,	0.07479,	0.08603), 
            '2028': (0.03150,	0.03939,	0.05701,	0.06759,	0.07464,	0.07967,	0.08345,	0.09694), 
            '2029': (0.03150,	0.04070,	0.06126,	0.07360,	0.08183,	0.08770,	0.09211,	0.10784), 
            '2030': (0.03150,	0.04202,	0.06552,	0.07962,	0.08902,	0.09573,	0.10077,	0.11875) 
        }

    def salario_diario(self):
        if (self._uma * 25) > self._sdi:
            return (1) * self._sdi
        else:
            return self._uma * 25

    # I_RIESGO
    def riesgo_de_trabajo(self):
        return round(((self._prima_de_riesgo/100) * self.salario_diario() * self.dias), 4)

    # 01 ENFERMEDAD Y MATERNIDAD _CF
    def cuotas_pres_especie_enf_mat_cuot(self):
        # cuota_fija = self._uma * 3
        return round((self._uma * self.dias * 0.2040), 4)

    # 02 ENFERMEDAD Y MATERNIDAD _EXCEDENTE
    def cuotas_pres_especie_enf_mat(self):
        exento = self._uma * 3
        diferencia = self.salario_diario() - exento

        if diferencia >= 0:
            return round((diferencia * self.dias * 0.0110), 4)
        else:
            return 0

    # 03 ENFERMEDAD Y MATERNIDAD _GM
    def gastos_medicos_pencionados(self):
        return round((self.salario_diario() * self.dias * 0.0105), 4)

    # 04 ENFERMEDAD Y MATERNIDAD _PD
    def cuotas_pres_dinero_enf_mat(self):
        return round((self.salario_diario() * self.dias * 0.0070), 4)

    # II_ENFERMEDAD Y MATERNIDAD
    def cuota_enfermedad_maternidad(self):
        return round(self.cuotas_pres_dinero_enf_mat() +
                     self.cuotas_pres_especie_enf_mat() +
                     self.gastos_medicos_pencionados() +
                     self.cuotas_pres_especie_enf_mat_cuot(), 4)

    # III_INVALIDEZ Y VIDA _IV
    def cuota_invalidez(self):
        return round((self.salario_diario() * self.dias * 0.0175), 4)

    # IV_RETIRO CESANTIA Y VEJEZ 01
    def retiro(self):
        return round((self.salario_diario() * self.dias * 0.0200), 4)

    # IV_RETIRO CESANTIA Y VEJEZ 02
    def veces_uma(self):
        return round(self.salario_diario() / self._uma , 2)

    def get_year(self):
        year = self.get_fecha_base().year
        return year

    def index(self) -> int:
        lista = [1.01, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.01, 35]
        elements = [i for i in lista if i <= self.veces_uma()]
        indice = lista.index(elements[-1])
        return indice

    def method_ceav(self):
        if self.get_year() < 2030:
            year = str(self.get_year())
            return self.ceav[year][self.index()]
        else:
            year = '2030'
            return self.ceav[year][self.index()]


    def cuota_cesantia_vejez(self):
        if self.get_year() < 2023:
            return round((self.salario_diario() * self.dias * 0.03150), 4)
        else:
            return round((self.salario_diario() * self.dias * self.method_ceav()), 4)

    # V_GUARDERIA Y PRESTACIONES
    def guarderia(self):
        return round(self.salario_diario() * self.dias * 0.0100, 4)

    # INFONAVIT
    def infonavit(self):
        return round((self.salario_diario() * self.dias * 0.05), 2)

    def imss(self):
        return round((self.riesgo_de_trabajo() +
                     self.cuota_enfermedad_maternidad() +
                     self.cuota_invalidez() +
                     self.guarderia() + 0
                      ), 2)  # self.cuota_gastos_medicos()

    def total_afore(self):
        return round((self.retiro() +
                      self.cuota_cesantia_vejez()), 2)

    def total_imss(self):
        subtotal = (
            self.imss() +
            self.infonavit() +
            self.total_afore()
        )
        return round(subtotal, 2)

    # Funciones provisionales para posible manejo facil de pandas
    @classmethod
    def function_imss_patron(cls, x, date):
        calculo = CalculoIMSSPatron()
        calculo.set_fecha_base(date)
        calculo.set_sdi(x)
        return calculo.imss()

    @classmethod
    def function_infonavit(cls, x, date):
        calculo = CalculoIMSSPatron()
        calculo.set_fecha_base(date)
        calculo.set_sdi(x)
        return calculo.infonavit()

    @classmethod
    def function_afore(cls, x, date):
        calculo = CalculoIMSSPatron()
        calculo.set_fecha_base(date)
        calculo.set_sdi(x)
        return calculo.total_afore()

    @classmethod
    def function_imss_patronal(cls, x, date):
        '''
        Función que suma las funciones anteriores patronales
        '''
        calculo = CalculoIMSSPatron()
        calculo.set_fecha_base(date)
        calculo.set_sdi(x)
        subtotal = (
            calculo.imss() +
            calculo.infonavit() +
            calculo.total_afore()
        )
        return subtotal
