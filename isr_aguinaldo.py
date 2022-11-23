# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

# libraries
from isr import ISR
from dataimss import DataImss


class Aguinaldo(DataImss):
    def __init__(self) -> None:
        super().__init__()
        self._aguinaldo = 0

    # getter method
    def get_aguinaldo(self) -> float:
        return self._aguinaldo

    # setter method
    def set_aguinaldo(self, aguinaldo: float) -> float:
        self._aguinaldo = aguinaldo

    def aguinaldo_grabado(self) -> float:
        '''
        Aguinaldo Exento. Hasta 30 UMAs (96.44* x 30)
        Aguinaldo Gravado (Aguinaldo Total- Aguinaldo Exento)
        '''
        excento = self._uma * 30
        if (self._aguinaldo - excento) > 0:
            return self._aguinaldo - excento
        else:
            return 0


class Ley(ISR, Aguinaldo):
    def __init__(self):
        super().__init__()

    def ordinario_aguinaldo(self) -> float:
        remunaracion = self.get_sueldo_base() + self.aguinaldo_grabado()
        nueva_base = ISR()
        nueva_base.set_sueldo_base(remunaracion)
        return round(nueva_base.impuesto_a_retener(), 2)
    
    def impuesto_aguinaldo_ley(self) -> float:
        return round(self.ordinario_aguinaldo() - self.impuesto_a_retener(), 2) 


class Reglamento(ISR, Aguinaldo):
    def __init__(self):
        super().__init__()
        # self._aguinaldo = 0

    def fracc_i(self) -> float:
        '''
        Art. 174 Fracción I. La remuneración (Aguinaldo GRAVADO) de que se trate 
        se dividirá entre 365 y el resultado se multiplicará por 30.4;
        '''
        return round((self.aguinaldo_grabado() / 365) * 30.4, 2)

    def fracc_ii(self) -> float:
        '''
        Art. 174 Fracción II. A la cantidad que se obtenga conforme a la fracción anterior, se le 
        adicionará el ingreso ordinario por la prestación de un servicio personal subordinado que 
        perciba el trabajador en forma regular en el mes de que se trate y al resultado se le 
        aplicará el procedimiento establecido en el artículo 96 de la Ley;
        '''
        remuneracion = self.get_sueldo_base() + self.fracc_i()
        ingreso_aguinaldo = ISR()
        ingreso_aguinaldo.set_sueldo_base(remuneracion)
        return round(ingreso_aguinaldo.calculo_impuesto(), 2)

    def fracc_iii(self) -> float:
        '''
        Art. 174 Fracción III. El Impuesto que se obtenga conforme a la fracción anterior se 
        disminuirá con el Impuesto que correspondería al ingreso ordinario por la prestación de 
        un servicio personal subordinado a que se refiere dicha fracción, calculando este último 
        sin considerar las demás remuneraciones mencionadas en este artículo.
        '''
        return round(self.fracc_ii() - self.calculo_impuesto(), 4)

    def fracc_v(self) -> float:
        '''
        Art. 174 Fracción V. La tasa a que se refiere la fracción anterior, se calculará dividiendo 
        el Impuesto que se determine en términos de la fracción III de este artículo entre la 
        cantidad que resulte conforme a la fracción I de dicho artículo. El cociente se multiplicará 
        por cien y el producto se expresará en por ciento
        '''
        if self.fracc_i() > 0:
            return round(self.fracc_iii() / self.fracc_i(), 4)
        else:
            return 0

    def fracc_iv(self) -> float:
        '''
        Art. 174 Fracción IV. El Impuesto a retener será el que resulte de aplicar a las 
        remuneraciones a que se refiere este artículo, sin deducción alguna, la tasa a que se 
        refiere la fracción siguiente, y
        '''
        return round(self.aguinaldo_grabado() * self.fracc_v(), 2)
    

class Impuesto_Aguinaldo(Ley, Reglamento):
    def __init__(self):
        super().__init__()

    def impuesto_aguinaldo(self) -> float:
        if self.fracc_iv() > self.impuesto_aguinaldo_ley():
            return self.impuesto_aguinaldo_ley()
        else:
            return self.fracc_iv()

    def texto(self):
        if self.fracc_iv() > self.impuesto_aguinaldo_ley():
            return "Impuesto de Ley"
        else:
            return "Impuesto de Reglamento"


if __name__ == '__main__':
    calculo = Impuesto_Aguinaldo()
    calculo.set_aguinaldo(3526.04)
    # print(calculo.fracc_i())
    # calculo.set_sueldo_base(19500)
    # print(calculo.get_sueldo_base())
    # print(calculo.fracc_ii())
    # print(calculo.fracc_iii())
    # print(calculo.fracc_v())
    # print(calculo.fracc_iv())
    print(calculo.aguinaldo_grabado())
    # print(calculo.impuesto_aguinaldo_ley())
    # print(calculo.impuesto_aguinaldo())
