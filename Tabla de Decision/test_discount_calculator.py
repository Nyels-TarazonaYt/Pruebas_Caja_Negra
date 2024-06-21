import pytest
from discount_calculator import calcular_descuento

@pytest.mark.parametrize("categoria, cantidad, promocion, esperado", [
    ("Regular", 5, False, 0),  # Caso 1
    ("Regular", 5, True, 5),   # Caso 2
    ("Regular", 15, False, 5), # Caso 3
    ("Regular", 15, True, 10), # Caso 4
    ("Regular", 25, False, 10),# Caso 5
    ("Regular", 25, True, 15), # Caso 6
    ("VIP", 5, False, 10),     # Caso 7
    ("VIP", 5, True, 15),      # Caso 8
    ("VIP", 15, False, 15),    # Caso 9
    ("VIP", 15, True, 20),     # Caso 10
    ("VIP", 25, False, 20),    # Caso 11
    ("VIP", 25, True, 25),     # Caso 12
    ("Regular", 0, False, 0),  # Caso 13: Cantidad en el borde inferior
    ("Regular", 10, True, 10), # Caso 14: Cantidad en el borde medio
    ("VIP", 20, False, 15),    # Caso 15: Cantidad en el borde superior medio
    ("VIP", 21, True, 25)      # Caso 16: Cantidad justo por encima del borde superior
])
def test_calcular_descuento(categoria, cantidad, promocion, esperado):
    assert calcular_descuento(categoria, cantidad, promocion) == esperado
