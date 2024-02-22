Apple = {'iPhone12', 'iPhone13', 'iPhone13 PRO', 'iPhone14', 'MacBook','TV'}
Samsung = {'GalaxyS10', 'GalaxyS10 Plus', 'GalaxyS24','GalaxyS24 Plus','TV'}

print('Apple:', Apple)

print('Samsung:', Samsung)

print('União entre as lojas:', Apple.union(Samsung))

print('Modelos disponiveis em ambas as lojas: ', Apple & Samsung)