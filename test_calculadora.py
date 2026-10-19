import os
import sys

# Agregar la ruta actual al path del sistema
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Intentar importar según el nombre de archivo existente
try:
    from Calculadora import calcular_total
except ModuleNotFoundError:
    from calculadora import calcular_total

def test_calcular_total():
    assert calcular_total(100, 0.10) == 110.0
