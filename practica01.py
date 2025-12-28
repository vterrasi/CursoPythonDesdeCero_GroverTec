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
<<<<<<< HEAD
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
>>>>>>> cd7f0c4 (Práctica01_primera_version)
=======


#ya quiero subir este archivo a github
>>>>>>> c27ecba (quise agregar otros dos archivos de la carpeta en este punto y no salió :()
