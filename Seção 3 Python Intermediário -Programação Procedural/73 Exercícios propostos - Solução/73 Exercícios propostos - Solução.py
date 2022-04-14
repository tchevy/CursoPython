carrinho = []
carrinho.append(('Produto 1', 'R$ ',30))
carrinho.append(('Produto 2','R$ ', 20))
carrinho.append(('Produto 3','R$ ', 50.8))
total = [(x,y,z) for x, y,z in carrinho]
print(total)
total = [float(z) for x, y,z in carrinho]
print(total)

# SOLUÇÂO DO DESAFIO
total = sum([float(z) for x,y,z in carrinho])
print(f'R$',total)