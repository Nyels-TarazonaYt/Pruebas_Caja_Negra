def calcular_descuento(categoria, cantidad, promocion):
    if categoria == "Regular":
        if cantidad < 10:
            if promocion:
                return 5
            else:
                return 0
        elif 10 <= cantidad <= 20:
            if promocion:
                return 10
            else:
                return 5
        elif cantidad > 20:
            if promocion:
                return 15
            else:
                return 10
    elif categoria == "VIP":
        if cantidad < 10:
            if promocion:
                return 15
            else:
                return 10
        elif 10 <= cantidad <= 20:
            if promocion:
                return 20
            else:
                return 15
        elif cantidad > 20:
            if promocion:
                return 25
            else:
                return 20
    return 0


#Categoría	Cantidad	Promoción	Descuento
#Regular	< 10	        No	        0%
#Regular	< 10	        Sí	        5%
#Regular	10 - 20	        No	        5%
#Regular	10 - 20	        Sí	        10%
#Regular	> 20	        No	        10%
#Regular	> 20	        Sí	        15%
#VIP	    < 10	        No	        10%
#VIP	    < 10	        Sí	        15%
#VIP	    10 - 20	        No	        15%
#VIP	    10 - 20	        Sí	        20%
#VIP	    > 20	        No	        20%
#VIP	    > 20	        Sí	        25%