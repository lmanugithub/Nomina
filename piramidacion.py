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
        self.with_vouchers = 0


    # getter method
    def get_gross_salary(self) -> float:
        return self.gross_salary

    # setter method
    def set_gross_salary(self, gross_salary: float) -> float:
        self.gross_salary = gross_salary  

    # getter method
    def get_with_vouchers(self) -> bool:
        return self.with_vouchers

    # setter method
    def set_with_vouchers(self, with_vouchers: bool) -> bool:
        self.with_vouchers = with_vouchers

    # getter method
    def get_goal(self) -> bool:
        return self.goal

    # setter method
    def set_goal(self, goal: float) -> float:
        self.goal = goal

    def calculo_vales(self) -> int:
        return int(self.gross_salary * 0.05 if self.gross_salary * 0.05 <= 1500 else 1500)
    
    def get_net_salary(self) -> float:
        vales = self.calculo_vales(self.gross_salary)
        isr = ISR.function_isr(self.gross_salary)
        sbc = SBC.funcion_sbc(sueldo=self.gross_salary, vales=vales, admission_date=self.fecha_inicio_tranajador, base_date=self.fecha_fin_ejercicio)
        imss = CalculoIMSSObrero.function_imss_obrero(sbc)

        if self.with_vouchers == 1:
            neto = self.gross_salary - isr - imss + vales
        else:
            neto = self.gross_salary - isr - imss  

        return round(neto,2) 

    def get_approch_to_gross_salary(self) -> float:
        approach = Piramidacion()
        inicio = self.goal * 1.42
        approach.set_gross_salary(inicio)
        
        while  self.goal > self.get_net_salary():
            inicio -= 1
            approach.set_gross_salary(inicio)
        return inicio
    
if __name__=='__main__':
    valor_a_buscar = 13_000
    approach = Piramidacion()
    approach.set_goal(valor_a_buscar)
    print(approach.get_approch_to_gross_salary())
    




