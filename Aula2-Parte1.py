# comando imput (): quero permitir que
#o usuario digite algo...

# pede o nome
nome = input("Digite seu nome: ")

genero = input("Qual seu Gênero (M - Masculino F - Feminino): ")

# pede idade
idade = int(input("Digite sua idade: "))

#comando de saída..exibir na tela
print ("Olá seu nome é {} e sua idade é {}".format(nome, idade))

#e se eu quisse mostrar o dobro da idade informada?
dobro = idade * 2
print ("o dobro da idade informada é {}".format(dobro))

# estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade , mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"

#if (idade >= 18):
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")

# e se eu quisse pergunatar o gênero (M - Masculino F - Feminino)
# Mostre (... e você também precisa/precisou prestar o serviço militar)
if(genero == "m" or genero == "M" and idade >=18 ):
  print("Você já pode prestar ou já prestou serviço militar")
  
if idade < 18:
  print("Você é menor de idade, ainda falta tempo para poder beber ou dirigir")

else:
  print ("Você não precisa prestar serviço militar")

