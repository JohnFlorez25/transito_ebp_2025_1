def calcular_valor_multa(tipo_infraccion, grado_infraccion):
    valor_multa = 0
    if(tipo_infraccion == 1):
        if grado_infraccion == 1:
            valor_multa = 600000
        elif grado_infraccion == 2:
            valor_multa = 1200000
        elif grado_infraccion == 3:
            valor_multa = 2000000
    elif(tipo_infraccion == 2):
        valor_multa = 400000
    elif(tipo_infraccion == 3):
        valor_multa = 1000000
    return valor_multa