carrinho = []
carrinho.append(('Produto 1', 'R$ ',30))
carrinho.append(('Produto 2','R$ ', 20))
carrinho.append(('Produto 3','R$ ', 50))
total = 0
for produto in carrinho:
    total += produto[2]
print(f'R$',total)

# USANDO LIST COMPREHENSION

t= [for produto in carrinho += produto[2] ]