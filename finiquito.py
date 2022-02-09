from calculofiniquito import CalculoFiniquito
from calculoseparacion import CalculoSeparacion
from isr import ISR


class Finiquito(CalculoFiniquito,CalculoSeparacion):
    def __init__(self) -> None:
        super().__init__()


if __name__=="__main__":
    finiquito = Finiquito()
    finiquito.set_sueldo_mensual(19033.74)
    finiquito.set_dias_vacaciones(18)
    finiquito.set_vales_despensa(600)
    finiquito.set_seg_gtos_med_mayor(23449.14)
    finiquito.set_seg_gtos_med(1431.19)
    finiquito.set_fecha_ingreso(2004,2,11)
    finiquito.set_fecha_baja(2021,3,31)
    finiquito.set_gratificacion_extra((258.50+951.69))

    print('\n')
    print(f'Salario diario                $ {finiquito.get_sueldo_mensual()/30.4:,.2f}')
    print(f'Salario quincenal             $ {finiquito.get_sueldo_mensual()/2:,.2f}')
    print(f'Salario mensual               $ {finiquito.get_sueldo_mensual():,.2f}')
    print(f'Años trabajados                 {finiquito.anos_trabajados():,.2f}')
    print(f'Dias del año trabajados         {finiquito.dias_ano_trabajados():,.2f}')
    print(f'Dias trabajados vacaciones      {finiquito.dias_vacaciones_trabajadas():,.2f}')
    print(f'Parte proporcional aguinaldo dias      {finiquito.dias_proporcional_aguinaldo():,.2f}')
    print(f'Parte proporcional vacaciones dias      {finiquito.dias_proporcional_vacaciones():,.2f}')
    print('\n')
    # print(f'{finiquito.vacacion_anual():,.2f}')
    # print(f'{finiquito.sueldo_anual():,.2f}')
    print(f'Liquidacion                 $ {finiquito.tres_meses_sueldo():,.2f}')
    print(f'Indemnización               $ {finiquito.veinte_dias_x_ano():,.2f}')
    print(f'Prima antigüedad            $ {finiquito.doce_dias_x_año():,.2f}')
    print('\n')
    print(f'ISR separación              $ {finiquito.isr_separacion():,.2f}')
    print('\n')
    print(f'ISR finiquito              $ {finiquito.isr_finiquito():,.2f}')