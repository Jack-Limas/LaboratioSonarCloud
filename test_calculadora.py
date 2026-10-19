import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importa el archivo según el nombre con el que se creó originalmente
try:
    from Calcudora import calcular_total
except ModuleNotFoundError:
    from Calculadora import calcular_total

def test_calcular_total():
    assert calcular_total(100, 0.10) == 110.0
