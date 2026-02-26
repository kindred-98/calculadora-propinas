# validators.py

def validar_monto(monto):
    if monto <= 0:
        raise ValueError("El monto debe ser positivo.")

def validar_porcentaje(porcentaje):
    if porcentaje < 0:
        raise ValueError("El porcentaje debe ser positivo.")

def validar_propina_fija(propina):
    if propina < 0:
        raise ValueError("La propina fija debe ser positiva.")

def validar_personas(personas):
    if personas <= 0 or not isinstance(personas, int):
        raise ValueError("Las personas deben ser un entero positivo.")