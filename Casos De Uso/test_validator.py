import pytest
from validator import validar_password

@pytest.mark.parametrize("password, esperado", [
    # Caso 1: Cuando Supere 10 caracteres retorna:
    ("Abcdefghijk1@", (False, "Longitud incorrecta")), 
    
    # Caso 2: Cuando sea Menor a 8 caracteres retorna:
    ("Abc1@23", (False, "Longitud incorrecta")), 
    
    # Caso 3: Cuando sea Entre 8 a 10 caracteres, válido retorna:
    ("A1b2@3456", (True, "Passsword válida")), 
    
    # Caso 4: Cuando se quiere Verificar que exista letra mayúscula retorna:
    ("abcdefgh1@", (False, "Falta letra mayúscula")), 
    
    # Caso 5: Cuando se quiere Verificar que exista alguna letra retorna:
    ("12345678@", (False, "Faltan letras")), 
    
    # Caso 6: Cuando se quiere Verificar que exista un carácter especial retorna:
    ("Abcdefgh1", (False, "Falta carácter especial")), 
    
    # Caso 7: Cuando se quiere Verificar que exista un número retorna:
    ("Abcdefgh@", (False, "Falta número")), 
    
    # Caso 8: Cuando se quiere Verificar que exista letra minúscula retorna:
    ("ABCDEFGH1@", (False, "Falta letra minúscula")), 
    
    # Caso 9: Cuando se quiere Verificar que cumpla todas las condiciones retorna:
    ("A1b@cDeFg", (True, "Passsword válida")),   
    
    # Caso 10: Cuando Cumple con el mínimo de 8 caracteres y todos los requisitos retorna:
    ("A1@bCdef", (True, "Passsword válida")),
    
    # Caso 11: Cuando Solo tiene letras y números, sin caracteres especiales retorna:
    ("Abcdefgh1", (False, "Falta carácter especial")),
    
    # Caso 12: Cuando Solo tiene letras y caracteres especiales, sin números retorna:
    ("Abcdefgh@", (False, "Falta número")),
    
    # Caso 13: Cuando Tiene longitud correcta pero solo una letra retorna:
    ("A1@345678", (False, "Faltan letras")),
    
    # Caso 14: Cuando Tiene letras, números, y caracteres especiales, pero menos de 8 caracteres retorna:
    ("A1@bC7", (False, "Longitud incorrecta")),
    
    # Caso 15: Cuando Tiene todo correcto pero sin letra mayúscula retorna:
    ("a1@bcdefg", (False, "Falta letra mayúscula")),
    
    # Caso 16: Cuando Tiene todo correcto pero sin letra minúscula retorna:
    ("A1@BCDEFG", (False, "Falta letra minúscula")),
    
    # Caso 17: Cuando Solo tiene números y caracteres especiales, sin letras retorna:
    ("12345678@", (False, "Faltan letras")),
    
    # Caso 18: Cuando Exactamente 10 caracteres, cumple con todos los requisitos retorna:
    ("A1b2@Cdefg", (True, "Passsword válida")),
    
    # Caso 19: Cuando Solo tiene caracteres especiales y letras, sin números retorna:
    ("Abcdefgh@", (False, "Falta número")),
    
    # Caso 20: Cuando Solo tiene caracteres especiales y números, sin letras retorna:
    ("12345678@", (False, "Faltan letras")),
    
    # Caso 21: Cuando Solo tiene letras mayúsculas y caracteres especiales, sin letras minúsculas ni números retorna:
    ("ABCDEFGH@", (False, "Falta letra minúscula")),
    
    # Caso 22: Cuando Solo tiene letras minúsculas y caracteres especiales, sin letras mayúsculas ni números retorna:
    ("abcdefgh@", (False, "Falta letra mayúscula")),
    
    # Caso 23: Cuando Tiene todas letras, números y caracteres especiales pero empieza con un número retorna:
    ("1Abcdefg@", (True, "Passsword válida")),
    
    # Caso 24: Cuando Tiene todas letras, números y caracteres especiales pero empieza con un carácter especial retorna:
    ("@Abcdefg1", (True, "Passsword válida")),
    
    # Caso 25: Cuando Tiene todas letras, números y caracteres especiales pero termina con un número retorna:
    ("Abcdefg1@", (True, "Passsword válida")),
    
    # Caso 26: Cuando Tiene todas letras, números y caracteres especiales pero termina con un carácter especial retorna:
    ("Abcdefg@1", (True, "Passsword válida")),
])
def test_validar_password(password, esperado):
    assert validar_password(password) == esperado
