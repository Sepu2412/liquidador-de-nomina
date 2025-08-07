
def calcular_nomina(salario_base, dias_laborados, horas_extras):

    if salario_base <= 0 or dias_laborados < 0 or dias_laborados > 30 or horas_extras < 0:
        return None  

    salario_dia = salario_base / 30
    valor_hora = salario_base / 240  
    salario = salario_dia * dias_laborados
    extras = horas_extras * valor_hora * 1.25  
    total = salario + extras

    return round(total, 2)

def prueba_normal_1():
    salario = 1500000
    dias = 30
    horas = 5
    resultado = calcular_nomina(salario, dias, horas)
    esperado = 1639062.5

    if resultado == round(esperado, 2):
        print("exitosa")
    else:
        print(" falló. ", resultado)


def prueba_extraordinaria_1():
    salario = 10000000
    dias = 30
    horas = 50
    resultado = calcular_nomina(salario, dias, horas)
    esperado = 11354166.67

    if resultado == round(esperado, 2):
        print(" exitosa")
    else:
        print("falló.", resultado)



def prueba_error_1():
    salario = 1500000
    dias = 37  
    horas = 5
    resultado = calcular_nomina(salario, dias, horas)

    if resultado is None:
        print(" no sirve  ")
    else:
        print("sirve", resultado)

prueba_normal_1()
prueba_extraordinaria_1()
prueba_error_1()

