import os
import sys

# Asegurar que Python busque en el directorio actual
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Intenta importar con mayúscula y, si no lo encuentra, en minúscula
try:
    from Calculadora import calcular_total
except ModuleNotFoundError:
    from calculadora import calcular_total

def test_calcular_total():
    assert calcular_total(100, 0.10) == 110.0
