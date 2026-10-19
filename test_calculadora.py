from Calculadora import calcular_total

def test_calcular_total():
    # Prueba con precio de 100 e impuesto del 10% (0.10)
    assert calcular_total(100, 0.10) == 110.0
