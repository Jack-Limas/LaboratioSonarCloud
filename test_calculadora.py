import os
import sys

# Forzar a Python a buscar modulos en la raiz del proyecto
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Intentar importar según las variantes de nombre de archivo
try:
    from Calculadora import calcular_total
except ModuleNotFoundError:
    try:
        from calculadora import calcular_total
    except ModuleNotFoundError:
        from Calcudora import calcular_total

def test_calcular_total():
    assert calcular_total(100, 0.10) == 110.0
