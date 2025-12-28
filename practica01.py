<<<<<<< HEAD
consumo = float(input("Ingrese el consumo del cliente: "))

if consumo > 0 and consumo <= 100:
    descuento = consumo * 0.10
elif consumo > 100 and consumo <= 200:
    descuento = consumo * 0.20
elif consumo > 200:
    descuento = consumo * 0.30  
else:
    descuento = 0   
    print("Consumo inválido.")
    
total = consumo - descuento
total_a_pagar = total + (total * 0.15)   
                         
print('Descuento: ', descuento)
print('Total: ', total)
print('Total a pagar: ', total_a_pagar)


#ya quiero subir este archivo a github
# :(
#     Yess
# )
=======
consumo = float(input("Ingrese el consumo del cliente: "))

if consumo > 0 and consumo <= 100:
    descuento = consumo * 0.10
elif consumo > 100 and consumo <= 200:
    descuento = consumo * 0.20
elif consumo > 200:
    descuento = consumo * 0.30  
else:
    descuento = 0   
    print("Consumo inválido.")
    
total = consumo - descuento
total_a_pagar = total + (total * 0.15)   
                         
print('Descuento: ', descuento)
print('Total: ', total)
print('Total a pagar: ', total_a_pagar)
>>>>>>> 8100e093bd0f0912f1f50a183cd4948ca4019edb
