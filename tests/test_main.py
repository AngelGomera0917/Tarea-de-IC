# tests/test_main.py
from main import saludo

def test_saludo():
    assert saludo() == "Hola, mundo!"
