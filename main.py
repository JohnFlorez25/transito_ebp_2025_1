from multa import calcular_valor_multa 
# Datos de entrada
tipo_infraccion = 0
grado_infraccion  = 0
valor_multa = 0

print("Ingrese el tipo de infracción:")
print("1. Embriaguez")
print("2. Pico y Placa")
print("3. Semaforo")
tipo_infraccion = int(input("Seleccione el tipo de infracción (1-3): "))

if(tipo_infraccion == 1):
    grado_infraccion=int(input("Ingrese el grado de la infraccion 1- 3:"))

valor_multa = calcular_valor_multa(tipo_infraccion, grado_infraccion);


print("El tipo de infraccón seleccionado es: ", tipo_infraccion)
print("El grado de infracción seleccionado es: ", grado_infraccion)
print("El valor de la multa es: ", valor_multa)