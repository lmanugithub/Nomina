# coding: utf-8

# In[1]:

__author__ = 'lguerrero'

from sbc import SBC

class Aumento(SBC):
    def __init__(self) -> None:
        super().__init__()
        self._uma 
        self.incremento_general = 0.078
        self.incremento_juan = 0.060

    # getter method
    def get_importe(self) -> float:
        return self.importe

    # setter method
    def set_importe(self, importe: float) -> float:
        self.importe = importe

    def fondo_trabajador(self) -> float:
        if self.importe > 150000:
            fondo = self.importe * self.incremento_juan / 2
            limite = (self._uma * 365 * 1.30) / 12
            if fondo < limite:
                return fondo
            else:
                return limite
        else:
            fondo = self.importe * self.incremento_general / 2
            limite = (self._uma * 365 * 1.30) / 12
            if fondo < limite:
                return fondo
            else:
                return limite
    
    @classmethod
    def funcion_fondo(cls,importe) -> float:
        fondo = Aumento()
        fondo.set_importe(importe)
        return fondo.fondo_trabajador()
    

    def excedente_fondo(self) -> float:
        if self.importe > 150000:
            fondo = self.importe * self.incremento_juan / 2
            limite = (self._uma * 365 * 1.30) / 12
            if fondo > limite:
                return (fondo - limite) * 2
            else:
                return 0
        else:
            fondo = self.importe * self.incremento_general / 2
            limite = (self._uma * 365 * 1.30) / 12
            if fondo > limite:
                return (fondo - limite) * 2
            else:
                return 0
    
    @classmethod
    def funcion_excedente(cls, importe) -> float:
        fondo = Aumento()
        fondo.set_importe(importe)
        return fondo.excedente_fondo()
    
    def vales(self) -> int:
        if (self.importe * 0.05) > 1500:
            return int(1500)
        else:
            return int(round(self.importe * 0.05, 0))
        
    @classmethod
    def funcion_vales(cls, importe) -> int:
        vales = Aumento()
        vales.set_importe(importe)
        return vales.vales()

if __name__ == '__main__':
    prueba = Aumento()
    prueba.set_importe(15000)
    print(prueba.fondo_trabajador())
    print(prueba.excedente_fondo())


