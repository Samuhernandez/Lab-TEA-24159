# Tendencias e Innovacion de Tecnologia Agricola
def calcularSalario(horas, tarifa):
    horas_extras = horas - max_horas_semanales
    if (horas_extras > 0):
        pago = (max_horas_semanales * tarifa) + (horas_extras * (tarifa * 1.5))
    else:
        pago = horas * tarifa
    return pago

try:
    max_horas_semanales = 40
    horas = int(input("cuantas horas trabajo?"))
    Tarifa = float(input ("Tarifa por hora?"))
    salario = calcularSalario(horas, Tarifa)
    print(salario)
except:
    print("Error, deber ingresar un valor numerico")
