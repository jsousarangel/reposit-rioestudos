palavra = input("digite uma palavra:  ")
vezes = 0

for i in palavra:
    print(i)
    if i =="a":
        vezes = vezes + 1
print(' quantidade de vezes que a letra a apareceu foi: ', vezes)
