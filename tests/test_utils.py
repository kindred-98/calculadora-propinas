from src.utils import formatear_moneda


def test_formatear_moneda():
    assert formatear_moneda(10) == "$10.00"


def test_formatear_moneda_decimales():
    assert formatear_moneda(10.456) == "$10.46"


def test_formatear_moneda_grande():
    assert formatear_moneda(1000000) == "$1000000.00"