from dataimss import DataImss


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


class CalculoIMSSPatron(DataImss):
    def __init__(self):
        super().__init__()

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
    def cuota_cesantia_vejez(self):
        return round((self.salario_diario() * self.dias * 0.03150), 4)

    # V_GUARDERIA Y PRESTACIONES
    def guarderia(self):
        return round(self.salario_diario() * self.dias * 0.0100, 4)

    # INFONAVIT
    def infonavit(self):
        return round((self.salario_diario() * self.dias * 0.05), 2)

    def total_imss(self):
        return round((self.riesgo_de_trabajo() +
                     self.cuota_enfermedad_maternidad() +
                     self.cuota_invalidez() +
                     self.guarderia() + 0
                      ), 2)  # self.cuota_gastos_medicos()

    def total_afore(self):
        return round((self.retiro() +
                      self.cuota_cesantia_vejez()), 2)

    # Funciones provisionales para posible manejo facil de pandas
    @classmethod
    def function_imss_patron(cls, x):
        calculo = CalculoIMSSPatron()
        calculo.set_sdi(x)
        return calculo.total_imss()

    @classmethod
    def function_infonavit(cls, x):
        calculo = CalculoIMSSPatron()
        calculo.set_sdi(x)
        return calculo.infonavit()

    @classmethod
    def function_afore(cls, x):
        calculo = CalculoIMSSPatron()
        calculo.set_sdi(x)
        return calculo.total_afore()
    
    @classmethod
    def function_imss_patronal(cls, x):
        '''
        Función que suma las funciones anteriores patronales
        '''
        calculo = CalculoIMSSPatron()
        calculo.set_sdi(x)
        subtotal = (
            calculo.total_imss() +
            calculo.infonavit() +
            calculo.total_afore() 
        )
        return subtotal
