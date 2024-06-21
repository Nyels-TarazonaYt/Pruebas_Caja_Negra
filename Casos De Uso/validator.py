import re

def validar_password(password):
    # Verificar longitud
    if not (8 <= len(password) <= 10):
        return False, "Longitud incorrecta"
    
    # Verificar al menos 2 letras
    if len(re.findall(r'[a-zA-Z]', password)) < 2:
        return False, "Faltan letras"
    
    # Verificar al menos una letra mayúscula
    if not re.search(r'[A-Z]', password):
        return False, "Falta letra mayúscula"
    
    # Verificar al menos una letra minúscula
    if not re.search(r'[a-z]', password):
        return False, "Falta letra minúscula"
    
    # Verificar al menos un número
    if not re.search(r'\d', password):
        return False, "Falta número"
    
    # Verificar al menos un carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Falta carácter especial"
    
    return True, "password válida"


