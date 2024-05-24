# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# Importación de librerias
from typing import Counter
from imss import CalculoIMSSObrero, CalculoIMSSPatron


class CuotasImss(CalculoIMSSObrero, CalculoIMSSPatron):
    def __init__(self):
        CalculoIMSSObrero.__init__(self)
        CalculoIMSSPatron.__init__(self)

    # Cuota fija
    @classmethod
    def mensual_cuota_fija_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.cuotas_pres_especie_enf_mat_cuot() / cuota.dias * days

    # Excedente patronal
    @classmethod
    def mensual_excedente_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.cuotas_pres_especie_enf_mat() / cuota.dias * days

    @classmethod
    def mensual_excedente_obrero(cls, sbc, days):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(sbc)
        return cuota.cuotas_pres_especie_enf_mat() / cuota.dias * days

    # Prestaciones en dinero
    @classmethod
    def mensual_prestaciones_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.cuotas_pres_dinero_enf_mat() / cuota.dias * days

    @classmethod
    def mensual_prestaciones_obrero(cls, sbc, days):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(sbc)
        return cuota.cuotas_pres_dinero_enf_mat() / cuota.dias * days

    # Gastos medicos pensionados
    @classmethod
    def mensual_gastos_medicos_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.gastos_medicos_pencionados() / cuota.dias * days

    @classmethod
    def mensual_gastos_medicos_obrero(cls, sbc, days):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(sbc)
        return cuota.gastos_medicos_pencionados() / cuota.dias * days

    # Riesgo de trabajo
    @classmethod
    def mensual_riesgo_trabajo(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.riesgo_de_trabajo() / cuota.dias * days

    # Invalidez y vida
    @classmethod
    def mensual_invalidez_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.cuota_invalidez() / cuota.dias * days

    @classmethod
    def mensual_invalidez_obrero(cls, sbc, days):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(sbc)
        return cuota.cuota_invalidez() / cuota.dias * days

    # Guarderias y prestaciones sociales
    @classmethod
    def mensual_guarderia_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.guarderia() / cuota.dias * days

    # # Sutotal seguros imss mensual
    # @classmethod
    # def function_subtotal_imss_patronal(cls, x):
    #     cuota = CalculoIMSSPatron()
    #     cuota.set_sdi(x)
    #     subtotal = (
    #         cuota.cuotas_pres_especie_enf_mat_cuot() +
    #         cuota.cuotas_pres_especie_enf_mat() +
    #         cuota.cuotas_pres_dinero_enf_mat() +
    #         cuota.gastos_medicos_pencionados() +
    #         cuota.riesgo_de_trabajo() +
    #         cuota.cuota_invalidez() +
    #         cuota.guarderia()
    #     )
    #     return subtotal

    # @classmethod
    # def function_subtotal_imss_obrero(cls, x):
    #     cuota = CalculoIMSSObrero()
    #     cuota.set_sdi(x)
    #     subtotal = (
    #         cuota.cuotas_pres_especie_enf_mat() +
    #         cuota.cuotas_pres_dinero_enf_mat() +
    #         cuota.gastos_medicos_pencionados() +
    #         cuota.cuota_invalidez()
    #     )
    #     return subtotal

    # Retiro, Cesantia en edad avanzada y vejez
    # Retiro
    @classmethod
    def bimestral_retiro_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.retiro() / cuota.dias * days
    
    # Cesantia en edad avanzada y vejez
    @classmethod
    def bimestral_ceav_patronal(cls, sbc, base_date, days):
        cuota = CalculoIMSSPatron()
        cuota.set_fecha_base(base_date)
        cuota.set_sdi(sbc)
        return cuota.cuota_cesantia_vejez() / cuota.dias * days

    @classmethod
    def bimestral_ceav_obrero(cls, sbc, days):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(sbc)
        return cuota.cuota_cesantia_vejez() / cuota.dias * days

    # @classmethod
    # def function_rcv_patronal(cls,x):
    #     cuota = CalculoIMSSPatron()
    #     cuota.set_sdi(x)
    #     subtotal = (
    #         cuota.retiro() +
    #         cuota.cuota_cesantia_vejez()
    #     )
    #     return subtotal

    # @classmethod
    # def function_rcv_obrero(cls,x):
    #     cuota = CalculoIMSSObrero()
    #     cuota.set_sdi(x)
    #     subtotal = (
    #         cuota.cuota_cesantia_vejez()
    #     )
    #     return subtotal
    
    @classmethod
    def bimestral_aportaciones_infonavit(cls, sbc, base_date, days):
        calculo = CalculoIMSSPatron()
        calculo.set_fecha_base(base_date)
        calculo.set_sdi(sbc)
        return calculo.infonavit() / calculo.dias * days

