def calcular_recargo(tipo_infraccion,grado_infraccion):
    grua = 40000
    parqueadero = 20000
    recargo = 0
    if(tipo_infraccion == 3):
        accidente = int(input("¿Hubo accidente? (1. Si, 2. No): "))
        if accidente == 2:
            recargo = 0
        else:
            numero_dias = int(input("Ingrese el número de días que estuvo el vehículo inmovilizado: "))
            recargo = ((numero_dias * parqueadero) + grua)
        return recargo   