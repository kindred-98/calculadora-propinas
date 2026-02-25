# Archivo principal de la calculadora de propinas
def calcular_propina_10(monto):
    """
    Calcula el 10% de propina sobre un monto dado.
    Parámetros:
        monto (float): El monto total de la cuenta.
    Retorna:
        float: El valor de la propina (10% del monto).
    """
    return monto * 0.10


# Pruebas manuales (solo para este commit)
if __name__ == "__main__":
    monto_prueba = 100
    print("Monto:", monto_prueba)
    print("Propina (10%):", calcular_propina_10(monto_prueba))
