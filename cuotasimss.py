from typing import Counter
from imss import CalculoIMSSObrero, CalculoIMSSPatron


class CuotasImss(CalculoIMSSObrero, CalculoIMSSPatron):
    def __init__(self):
        CalculoIMSSObrero.__init__(self)
        CalculoIMSSPatron.__init__(self)

    # Cuota fija
    @classmethod
    def function_cuota_fija_patronal(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.cuotas_pres_especie_enf_mat_cuot()

    # Excedente
    @classmethod
    def function_excedente_patronal(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.cuotas_pres_especie_enf_mat()

    @classmethod
    def function_excedente_obrero(cls, x):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(x)
        return cuota.cuotas_pres_especie_enf_mat()

    # Prestaciones en dinero
    @classmethod
    def function_prestaciones_patronal(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.cuotas_pres_dinero_enf_mat()

    @classmethod
    def function_prestaciones_obrero(cls, x):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(x)
        return cuota.cuotas_pres_dinero_enf_mat()

    # Gastos medicos pensionados
    @classmethod
    def function_gastos_medicos_patronal(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.gastos_medicos_pencionados()

    @classmethod
    def function_gastos_medicos_obrero(cls, x):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(x)
        return cuota.gastos_medicos_pencionados()

    # Riesgo de trabajo
    @classmethod
    def function_riesgo_trabajo(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.riesgo_de_trabajo()

    # Invalidez y vida
    @classmethod
    def function_invalidez_patronal(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.cuota_invalidez()

    @classmethod
    def function_invalidez_obrero(cls, x):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(x)
        return cuota.cuota_invalidez()

    # Guarderias y prestaciones sociales
    @classmethod
    def function_guarderia_patronal(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.guarderia()

    # Sutotal seguros imss
    @classmethod
    def function_subtotal_imss_patronal(cls, x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        subtotal = (
            cuota.cuotas_pres_especie_enf_mat_cuot() +
            cuota.cuotas_pres_especie_enf_mat() +
            cuota.cuotas_pres_dinero_enf_mat() +
            cuota.gastos_medicos_pencionados() +
            cuota.riesgo_de_trabajo() +
            cuota.cuota_invalidez() +
            cuota.guarderia()
        )
        return subtotal

    @classmethod
    def function_subtotal_imss_obrero(cls, x):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(x)
        subtotal = (
            cuota.cuotas_pres_especie_enf_mat() +
            cuota.cuotas_pres_dinero_enf_mat() +
            cuota.gastos_medicos_pencionados() +
            cuota.cuota_invalidez()
        )
        return subtotal

    # Retiro, Cesantia en edad avanzada y vejez
    # Retiro
    @classmethod
    def function_retiro_patronal(cls,x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.retiro()
    
    # Cesantia en edad avanzada y vejez
    @classmethod
    def function_ceav_patronal(cls,x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        return cuota.cuota_cesantia_vejez()

    @classmethod
    def function_ceav_obrero(cls,x):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(x)
        return cuota.cuota_cesantia_vejez()

    @classmethod
    def function_rcv_patronal(cls,x):
        cuota = CalculoIMSSPatron()
        cuota.set_sdi(x)
        subtotal = (
            cuota.retiro() +
            cuota.cuota_cesantia_vejez()
        )
        return subtotal

    @classmethod
    def function_rcv_obrero(cls,x):
        cuota = CalculoIMSSObrero()
        cuota.set_sdi(x)
        subtotal = (
            cuota.cuota_cesantia_vejez()
        )
        return subtotal

