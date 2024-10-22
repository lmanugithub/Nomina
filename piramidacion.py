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
        return int(gross_salary * 0.05 if gross_salary * 0.05 <= 1500 else 1500)
    
    def get_net_salary(self, gross_salary:float, with_vouchers:bool) -> float:
        vales = self.calculo_vales(gross_salary)
        isr = ISR.function_isr(gross_salary)
        sbc = SBC.funcion_sbc(gross_salary, vales=vales, admission_date=self.fecha_inicio_tranajador, base_date=self.fecha_fin_ejercicio)
        imss = CalculoIMSSObrero.function_imss_obrero(sbc)

        if with_vouchers == 1:
            neto = gross_salary - isr - imss + vales
        else:
            neto = gross_salary - isr - imss  

        return round(neto,2) 

    def get_approch_to_gross_salary(self, goal:float, vales=0) -> float:
        
        inicio = goal * 1.42
        
        while  goal < self.get_net_salary(inicio, vales):
            inicio -= 1

        return inicio
    
if __name__=='__main__':
    valor_a_buscar = 13000
    approach = Piramidacion()
    print(approach.get_approch_to_gross_salary(valor_a_buscar,0))
    




