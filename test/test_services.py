import pytest
from src.services import dividir_cuenta


def test_dividir_cuenta_porcentaje():
    resultado = dividir_cuenta(100, "porcentaje", 10, 2)

    assert resultado["propina"] == 10
    assert resultado["total"] == 110
    assert resultado["por_persona"] == 55


def test_dividir_cuenta_fija():
    resultado = dividir_cuenta(100, "fija", 20, 4)

    assert resultado["propina"] == 20
    assert resultado["total"] == 120
    assert resultado["por_persona"] == 30


def test_dividir_cuenta_monto_negativo():
    with pytest.raises(ValueError):
        dividir_cuenta(-100, "porcentaje", 10, 2)


def test_dividir_cuenta_porcentaje_negativo():
    with pytest.raises(ValueError):
        dividir_cuenta(100, "porcentaje", -10, 2)


def test_dividir_cuenta_propina_fija_negativa():
    with pytest.raises(ValueError):
        dividir_cuenta(100, "fija", -10, 2)


def test_dividir_cuenta_personas_invalidas():
    with pytest.raises(ValueError):
        dividir_cuenta(100, "porcentaje", 10, 0)