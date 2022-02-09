class TresPorciento:

    def __init__(self):
        self._base = 0

    # getter method
    def get_base(self):
        return self._base

    # setter method
    def set_base(self, base):
        self._base = base

    def calculo_tres(self):
        return round(((self._base / 1) * 0.03), 2)

    @classmethod
    def function_tresporciento(cls, x):
        calculo = TresPorciento()
        calculo.set_base(x)
        return calculo.calculo_tres()
