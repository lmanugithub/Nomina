from datetime import datetime, date

class WorkingTime():
    def __init__(self):
        # datetime.__init__(self)
        # date.__init__(self)
        self.fecha_base = date(year=2021, month=1, day=1)

    # getter method
    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    # setter method
    def set_fecha_ingreso(self,ano=0,mes=0,dia=0):
        self.fecha_ingreso = date(year=ano, month=mes, day=dia)

    # getter method
    def get_fecha_baja(self):
        return self.fecha_actual

    # setter method
    def set_fecha_baja(self,ano=0,mes=0,dia=0):
        self.fecha_actual = date(year=ano, month=mes, day=dia)

    def dias_trabajados(self):
        diferencia = self.get_fecha_baja() - self.get_fecha_ingreso()
        dias = str(diferencia).split()
        return int(dias[0])+1

    def dias_ano_trabajados(self):
        diferencia = self.get_fecha_baja() - self.fecha_base
        dias = str(diferencia).split()
        return int(dias[0])+1

    def aniversario_vacaciones_actual(self):
        ano_base = self.fecha_base.strftime('%Y')
        mes_ingreso = self.get_fecha_ingreso().strftime('%m')
        dia_ingreso = self.get_fecha_ingreso().strftime('%d')        
        ano = int(ano_base)
        mes = int(mes_ingreso)
        dia = int(dia_ingreso)
        fecha_aniversario = date(year=ano,month=mes,day=dia)
        return fecha_aniversario

    def dias_vacaciones_trabajadas(self):
        diferencia = self.get_fecha_baja() - self.aniversario_vacaciones_actual()
        dias = str(diferencia).split()
        if int(dias[0]) > 0:
            return int(dias[0])+1
        else:
            return 0

# if __name__=="__main__":

#     testing = WorkingTime()
#     ano = int(input('Digite el año:'))
#     mes = int(input('Digite el mes:'))
#     dia = int(input('Digite el día:'))
#     testing.set_fecha_ingreso(ano,mes,dia)
#     print(testing.get_fecha_ingreso())



