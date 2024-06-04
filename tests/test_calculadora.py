import sys
import os

# Añadir el directorio 'src' al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from calculadora import suma, resta, multiplicacion, division, exponenciacion, raiz_cuadrada

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 0) == 0
    assert resta(-1, 1) == -2

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(0, 5) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(-1, 1) == -1
    assert division(0, 1) == 0
    with pytest.raises(ValueError):
        division(1, 0)

def test_exponenciacion():
    assert exponenciacion(2, 3) == 8
    assert exponenciacion(5, 0) == 1
    assert exponenciacion(1, -1) == 1

def test_raiz_cuadrada():
    assert raiz_cuadrada(4) == 2
    assert raiz_cuadrada(0) == 0
    with pytest.raises(ValueError):
        raiz_cuadrada(-1)

if __name__ == "__main__":
    pytest.main()
