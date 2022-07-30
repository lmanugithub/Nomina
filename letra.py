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
        centavos = int(round(num % 1, 2) * 100)
        num = num - centavos/100
        num = int(num)
        return (num, centavos)

    def centavos(self, numero):
        num, centavos = self.number(numero)
        if num == 1:
            return f"{self.moneda['1'][0]} {str(centavos) if int(centavos) > 9 else f'0{str(centavos)}'}{self.moneda['1'][1]}"
        else:
            return f"{self.moneda['0'][0]} {str(centavos) if int(centavos) > 9 else f'0{str(centavos)}'}{self.moneda['0'][1]}"

    def letra_tens(self, numero):
        num, centavos = self.number(numero)

        if num >= 0 and num < 11:
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
    # for numero in numeros:
    #     print(texto.letra(numero))
