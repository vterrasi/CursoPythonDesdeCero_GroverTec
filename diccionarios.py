persona = {'Nombre': 'Velia', 
            'Edad': 38, 
            'Estatura': 1.62, #Esto es un diccionario
            'Gadgets': ['Laptop', 'Smartphone','Auriculares']} #Lista dentro de un diccionario

#print(persona['Nombre'])  # Imprime el nombre usando la clave del diccionario
#print(persona['0'])    # Arroja un error ya que esta no es la sintaxis para imprimir la posicion '0'.
#print(persona['gadgets'])
persona['Dirección'] = 'Madrid'  # Agrega una nueva clave 'Dirección' al diccionario  
#persona.clear()  # Limpia el diccionario, eliminando todos sus elementos

# print(persona.keys())  # Imprime todas las claves del diccionario
# print(persona.values())  # Imprime todos los valores del diccionario   
# print(persona.items())  # Imprime todos los pares clave-valor (tuplas) del diccionario 
#persona.pop('Estatura')  # Elimina la clave 'Estatura' y su valor asociado del diccionario
persona.update({'Mascota': True, 'Estatura': 1.70 })  # Actualiza el diccionario con el par-valor especificado
# print(persona)

# for dato in persona:
#     print(dato)  # Imprime cada clave del diccionario

#Tupla
tupla = (123, 'Velia', 38, 1.62, 123)

print(tupla.index(38))