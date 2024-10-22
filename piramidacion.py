import pandas as pd
from imss import CalculoIMSSObrero, CalculoIMSSPatron
from isr import ISR
from datetime import datetime
from sbc import SBC

class Piramidacion(CalculoIMSSObrero,ISR,SBC):
    def __init__(self) -> None:
        super().__init__()
        self.fecha_inicio_tranajador = pd.to_datetime('2024-10-15', format='%Y-%m-%d')
        self.fecha_fin_ejercicio = pd.to_datetime('2024/12/31')

    def calculo_vales(self, gross_salary:float) -> int:
        vales = int(gross_salary * 0.05)
        return min(vales, 1500)
    
    def get_net_salary(self, gross_salary:float, with_vouchers:bool) -> float:
        vales = self.calculo_vales(gross_salary)
        isr = ISR.function_isr(gross_salary)
        sbc = SBC.funcion_sbc(gross_salary, vales=vales, admission_date=self.fecha_inicio_tranajador, base_date=self.fecha_fin_ejercicio)
        imss = CalculoIMSSObrero.function_imss_obrero(sbc)

        neto = gross_salary - isr - imss + vales if with_vouchers else gross_salary - isr - imss

        return round(neto,2) 

    def approach_gross_salary(self, goal:float, vales=0) -> float:      
        inicio = goal * 1.42        
        while  goal < self.get_net_salary(inicio, vales):
            inicio -= 1
        return inicio
    
    def df_iteraciones(self, rango:int, incremento:float, approach_income:float, with_vouchers=0):
        
        # first 
        sueldos = []
        for i in range(1,rango):
            approach_income += incremento
            sueldos.append(approach_income)
        
        # second
        vouchers = [int(sueldo * 0.05) if int(sueldo * 0.05) <= 1500 else 1500 for sueldo in sueldos]

        # third
        isrs = list(map(lambda sueldo: ISR.function_isr(sueldo), sueldos))

        # fourth
        sbcs = []
        for sueldo, vale in zip(sueldos,vouchers):
            value_sbc = SBC.funcion_sbc(sueldo=sueldo, vales=vale, admission_date=self.fecha_inicio_tranajador, base_date=self.fecha_fin_ejercicio)
            sbcs.append(value_sbc)
        
        # fifth
        imss_obs = [CalculoIMSSObrero.function_imss_obrero(sbc) for sbc in sbcs] 

        # sixth
        if with_vouchers:
            net_salary = [sueldo - isr - imss + vale for sueldo, vale, isr, imss in zip(sueldos, vouchers, isrs, imss_obs)]
        else:
            net_salary = [sueldo - isr - imss  for sueldo, isr, imss in zip(sueldos, vouchers, isrs, imss_obs)]

        
        data_frame = {'Sueldo':sueldos,'Vales':vouchers,'SBC':sbcs,'ISR':isrs,'IMSS':imss_obs,'Neto':net_salary}

        return pd.DataFrame(data_frame)
    
    def df_ta(self, buscar_valor:float, with_vouchers=0):
        sueldo_inicial = self.approach_gross_salary(buscar_valor, with_vouchers) - 5
        df = self.df_iteraciones(1000, 0.01, sueldo_inicial, with_vouchers)
        margen = 0.01  # Ajuste de margen para mayor precisión
        df = df[(df['Neto'] >= (buscar_valor - margen)) & (df['Neto'] <= (buscar_valor + margen))]
        self.df_approach = df.copy()

    def putout_ta(self):
        return self.df_approach
    


if __name__=='__main__':
    valor_a_buscar = 13000
    approach = Piramidacion()
    print(approach.approach_gross_salary(valor_a_buscar,1))
    approach.df_ta(valor_a_buscar, 1)
    print(approach.putout_ta())
    




