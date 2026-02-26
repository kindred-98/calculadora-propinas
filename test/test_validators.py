import pytest
from src.validators import (
    validar_monto,
    validar_porcentaje,
    validar_propina_fija,
    validar_personas,
)


# -------------------
# VALIDAR MONTO
# -------------------

def test_validar_monto_valido():
    validar_monto(100)


def test_validar_monto_cero():
    with pytest.raises(ValueError):
        validar_monto(0)


def test_validar_monto_negativo():
    with pytest.raises(ValueError):
        validar_monto(-10)


# -------------------
# VALIDAR PORCENTAJE
# -------------------

def test_validar_porcentaje_valido():
    validar_porcentaje(10)


def test_validar_porcentaje_cero():
    validar_porcentaje(0)


def test_validar_porcentaje_negativo():
    with pytest.raises(ValueError):
        validar_porcentaje(-5)


# -------------------
# VALIDAR PROPINA FIJA
# -------------------

def test_validar_propina_fija_valida():
    validar_propina_fija(20)


def test_validar_propina_fija_cero():
    validar_propina_fija(0)


def test_validar_propina_fija_negativa():
    with pytest.raises(ValueError):
        validar_propina_fija(-10)


# -------------------
# VALIDAR PERSONAS
# -------------------

def test_validar_personas_valido():
    validar_personas(3)


def test_validar_personas_cero():
    with pytest.raises(ValueError):
        validar_personas(0)


def test_validar_personas_negativo():
    with pytest.raises(ValueError):
        validar_personas(-2)


def test_validar_personas_no_entero():
    with pytest.raises(ValueError):
        validar_personas(2.5)