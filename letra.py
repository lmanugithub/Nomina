# coding: utf-8

# In[1]:

__author__ = 'lguerrero'


class Letra():

    def __init__(self) -> None:

        self.unidades = ["", "un", "dos", "tres", "cuatro", "cinco",
                         "seis", "siete", "ocho", "nueve", "diez"]

        self.especiales = ["once", "doce", "trece", "catorce", "quince",
                           "diezciseis", "diecisiete", "dieciocho", "diecinueve"]

        self.decenas = ["veinte", "treinta", "cuarenta", "cincuenta", "sesenta",
                        "setenta", "ochenta", "noventa"]

        self.cienes = ["ciento", "docientos", "trescientos", "cuatrocientos", "quinientos",
                       "seicientos", "setecientos", "ochocientos", "novecientos"]

        self.moneda = {'0': ['pesos', '/100 MXN'],
                       '1': ['peso', '/100 MXN']}

    def units(self, index):
        return self.unidades[index]

    def esp(self, index):
        return self.especiales[index]

    def tens(self, index):
        return self.decenas[index]

    def hund(self, index):
        return self.cienes[index]

    def number(self, numero: float):
        num = round(numero, 2)
        # centavos = int(round(num % 1, 2) * 100)
        # num = num - centavos/100
        # num = int(num)
        entero = int(num)
        centavos = int((num-entero)*100)
        return (entero, centavos)

    def centavos(self, numero):
        num, centavos = self.number(numero)
        if num == 1:
            return f"{self.moneda['1'][0]} {str(centavos) if int(centavos) > 9 else f'0{str(centavos)}'}{self.moneda['1'][1]}"
        else:
            return f"{self.moneda['0'][0]} {str(centavos) if int(centavos) > 9 else f'0{str(centavos)}'}{self.moneda['0'][1]}"

    def letra_tens(self, numero):
        num, centavos = self.number(numero)

        if num == 0:
            return 'cero'        
        elif num >= 0 and num < 11:
            return(f"{self.units(num)}")
        elif num < 20:
            return(f"{self.esp(num-11)}")
        elif num == 20:
            return(f"{self.tens(0)}")
        elif num < 30:
            return(f"veinti{self.units(num-20)}")

        elif num < 100:

            unid = num % 10
            dec = int(num//10)

            if unid == 0:
                return(f"{self.tens(dec-2)}")
            else:
                return(f"{self.tens(dec-2)} y {self.units(unid)}")

    def letra_hundreds(self, numero):

        if numero >= 100 and numero < 1000:
            num, centavos = self.number(numero)
            t = num % 100  # tens and units
            h = num // 100  # hundreds
            cien = 'cien'

            if t == 0 and h == 1:
                return(f"{cien}")
            else:
                return(f"{self.hund(h-1)} {self.letra_tens(t)}")
        else:
            return self.letra_tens(numero)

    def letra_thousands(self, numero):
        num, centavos = self.number(numero)
        h = num % 1000  # hundreds, tens and units
        th = num // 1000  # thousands
        mil = 'mil'

        if h == 0 and th == 1:
            return(f"{mil}")
        elif h < 100 and th == 1:
            return(f"{mil} {self.letra_tens(h)}")
        elif h < 1000 and th == 1:
            return(f"{mil} {self.letra_hundreds(h)}")
        else:
            return(f"{self.letra_hundreds(th)} {mil} {self.letra_hundreds(h)}")

    def letra_millions(self, numero):
        num, centavos = self.number(numero)
        m = num // 1000000
        millon = num % 1000000
        h = millon % 1000  # hundreds, tens and units
        th = millon // 1000  # thousands
        mil = 'mil'
        mil_ = 'millones'
        cien = 'cien'

        if m == 1:
            if th == 0 and h == 0:
                return(f"{self.letra_tens(m)} millón")
            elif th == 0 and h < 100:
                return(f"{self.letra_tens(m)} millón {self.letra_tens(h)}")
            else:
                return(f"{self.letra_tens(m)} millón {self.letra_hundreds(th)} {mil} {self.letra_hundreds(h)}")

        elif m < 100:
            if th == 0 and h < 100:
                return(f"{self.letra_tens(m)} {mil_} {self.letra_tens(h)}")
            else:
                return(f"{self.letra_tens(m)} {mil_} {self.letra_hundreds(th)} {mil} {self.letra_hundreds(h)}")

        elif m < 1000:
            if th == 0 and h < 100:
                return(f"{self.letra_hundreds(m)} {mil_} {self.letra_tens(h)}")
            else:
                return(f"{self.letra_hundreds(m)} {mil_} {self.letra_hundreds(th)} {mil} {self.letra_hundreds(h)}")

        # menos de cien mil millones
        elif m < 100000:
            if th == 0 and h == 0:
                if m // 1000 == 1:
                    return(f"{mil} {mil_}")
                else:
                    return(f"{self.letra_tens(m//1000)} {mil} {mil_}")
            else:
                return(f"{self.letra_tens(m//1000)} {mil} {self.letra_hundreds(m % 1000)} {mil_} {self.letra_hundreds(th)} {mil} {self.letra_hundreds(h)}")

        elif m >= 100000 and m < 1000000:
            if th == 0 and h == 0:
                if m // 1000 == 100:
                    return(f"{cien} {mil} {mil_}")
                else:
                    return(f"{self.letra_hundreds(m//1000)} {mil} {mil_}")
            else:
                return(f"{self.letra_hundreds(m//1000)} {mil} {self.letra_hundreds(m % 1000)} {mil_} {self.letra_hundreds(th)} {mil} {self.letra_hundreds(h)}")

    def letra(self, numero):

        if numero < 100:
            return f"{self.letra_tens(numero)} {self.centavos(numero)}"
        elif numero < 1000:
            return f"{self.letra_hundreds(numero)} {self.centavos(numero)}"
        elif numero < 1000000:
            return f"{self.letra_thousands(numero)} {self.centavos(numero)}"
        elif numero < 1000000000000:
            return f"{self.letra_millions(numero)} {self.centavos(numero)}"

    @classmethod
    def numero_letra(cls, numero: float) -> float:
        cifra = Letra()
        return cifra.letra(numero)


if __name__ == '__main__':
    texto = Letra()
    numero = float(input("digite un numero:    "))
    print(texto.letra(numero))
    # numeros = [1001.89,  65254612.19,  62669.18, 1, 71503632.34]
    # numeros = [1,1.01,1.02,1.03,1.04,1.05,1.06,1.07,1.08,1.09,1.1,1.11,1.12,1.13,1.14,1.15,1.16,1.17,1.18,1.19,1.2,1.21,1.22,1.23,1.24,1.25,1.26,1.27,1.28,1.29,1.3,1.31,1.32,1.33,1.34,1.35,1.36,1.37,1.38,1.39,1.4,1.41,1.42,1.43,1.44,1.45,1.46,1.47,1.48,1.49,1.5,1.51,1.52,1.53,1.54,1.55,1.56,1.57,1.58,1.59,1.6,1.61,1.62,1.63,1.64,1.65,1.66,1.67,1.68,1.69,1.7,1.71,1.72,1.73,1.74,1.75,1.76,1.77,1.78,1.79,1.8,1.81,1.82,1.83,1.84,1.85,1.86,1.87,1.88,1.89,1.9,1.91,1.92,1.93,1.94,1.95,1.96,1.97,1.98,1.99,2,2.01,2.02,2.03,2.04,2.05,2.06,2.07,2.08,2.09,2.1,2.11,2.12,2.13,2.14,2.15,2.16,2.17,2.18,2.19,2.2,2.21,2.22,2.23,2.24,2.25,2.26,2.27,2.28,2.29,2.3,2.31,2.32,2.33,2.34,2.35,2.36,2.37,2.38,2.39,2.4,2.41,2.42,2.43,2.44,2.45,2.46,2.47,2.48,2.49,2.5,2.51,2.52,2.53,2.54,2.55,2.56,2.57,2.58,2.59,2.6,2.61,2.62,2.63,2.64,2.65,2.66,2.67,2.68,2.69,2.7,2.71,2.72,2.73,2.74,2.75,2.76,2.77,2.78,2.79,2.8,2.81,2.82,2.83,2.84,2.85,2.86,2.87,2.88,2.89,2.9,2.91,2.92,2.93,2.94,2.95,2.96,2.97,2.98,2.99,3,3.01,3.02,3.03,3.04,3.05,3.06,3.07,3.08,3.09,3.1,3.11,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,3.2,3.21,3.22,3.23,3.24,3.25,3.26,3.27,3.28,3.29,3.3,3.31,3.32,3.33,3.34,3.35,3.36,3.37,3.38,3.39,3.4,3.41,3.42,3.43,3.44,3.45,3.46,3.47,3.48,3.49,3.5,3.51,3.52,3.53,3.54]
    # for numero in numeros:
        # print(texto.letra(numero))
