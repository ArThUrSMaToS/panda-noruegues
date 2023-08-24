# variaveis
idatot = 0
media = 0
velho = 0
nomeh = ""
totmulher20 = 0

# entrada dos dados : nome idade e sexo
for c in range(1,5):
    print("-----{}° pessoa-----".format(c))
    nome = str(input("escreva seu nome: ")).strip()
    idade =int(input("escreva sua idade: "))
    sexo =str(input("escreva seu sexo[M/F]: ")).strip()

    # soma das idades
    idatot += idade
    # aqui eu acho o homem mais velho e seu nome
    if c == 1 and sexo in 'Mm':
        velho = idade
        nomeh = nome
    if idade > velho and sexo in 'Mm':
        velho = idade
        nomeh = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

# média de idade do grupo
media = idatot / 4

print("a média das idades é de {} anos".format(media))
print("o {} é o homem mais velho e tem a idade de {} anos".format(nomeh,velho))
print("o numero de mulheres com menos de 20 anos é {}".format(totmulher20))
