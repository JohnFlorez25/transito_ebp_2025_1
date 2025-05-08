# Datos de entrada
tipo_infraccion = 0
grado_infraccion  = 0
valor_multa = 0


print("Ingrese el tipo de infracción:")
print("1. Embriaguez")
print("2. Pico y Placa")
print("3. Semaforo")
tipo_infraccion = int(input("Seleccione el tipo de infracción (1-3): "))

# print(type(tipo_infraccion))
if(tipo_infraccion == 1):
    grado_infraccion=int(input("Ingrese el grado de la infraccion 1- 3:"))
    if grado_infraccion == 1:
        valor_multa = 600000
    elif grado_infraccion == 2:
        valor_multa = 1200000
    elif grado_infraccion == 3:
        valor_multa = 2000000

print("El tipo de infraccón seleccionado es: ", tipo_infraccion)
print("El grado de infracción seleccionado es: ", grado_infraccion)
print("El valor de la multa es: ", valor_multa)
      
        

