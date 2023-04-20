lista_original=[1,2,3,4,5,6,7,8,9,10]
nova_lista=[x**2 for x in lista_original]
nova_lista_withif=[x**2 for x in lista_original if x%2==0]
nova_lista_with_ifelse=[1 if x%2!=0 else 0 for x in lista_original]


print(lista_original) #imprime[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nova_lista) #imprime [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(nova_lista_withif) #imprime [4, 16, 36, 64, 100]
print(nova_lista_with_ifelse) #imprime [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

