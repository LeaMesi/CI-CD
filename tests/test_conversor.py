import pytest

from conversor import convertir_temperatura


def test_celsius_a_fahrenheit():
    assert convertir_temperatura(0, "C", "F") == pytest.approx(32)


def test_fahrenheit_a_celsius():
    assert convertir_temperatura(212, "F", "C") == pytest.approx(100)


def test_acepta_escalas_en_minuscula():
    assert convertir_temperatura(25, "c", "f") == pytest.approx(77)


def test_misma_escala_devuelve_el_mismo_valor():
    assert convertir_temperatura(18, "C", "C") == pytest.approx(18)


@pytest.mark.parametrize(
    ("valor", "origen"),
    [(-273.16, "C"), (-459.68, "F")],
)
def test_rechaza_valores_menores_al_cero_absoluto(valor, origen):
    with pytest.raises(ValueError, match="cero absoluto"):
        convertir_temperatura(valor, origen, "C")


def test_acepta_el_cero_absoluto():
    assert convertir_temperatura(-273.15, "C", "C") == pytest.approx(-273.15)


def test_rechaza_escalas_no_soportadas():
    with pytest.raises(ValueError, match="escalas válidas"):
        convertir_temperatura(20, "K", "C")
