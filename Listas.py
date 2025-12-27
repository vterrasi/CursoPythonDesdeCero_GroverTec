productos =['notebook', 'smartphone', 'tablet', 'monitor', 'teclado']

new_products = productos.copy()
new_products.append('mouse')


#new_products.extend(productos)
productos.insert(1, 'iPad')

#productos.clear()
#productos.pop(2)
productos.remove('monitor')

#print(productos)
#print(productos.index('teclado'))
#print(productos.count('teclado'))
new_products.sort()
print(new_products)
