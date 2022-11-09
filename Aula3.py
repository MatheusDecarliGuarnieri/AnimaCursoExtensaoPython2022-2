print ("Início da aula 3 (09/11/2022) ")

contador = 1

#Exibir de 1 até 10 repedidamente 
while(contador <= 10):
  print(contador)
  contador = contador + 1 #ou contador += 1

#Laço for(python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#Lista
frutas = ["morango", "laranja","pêra" ]

#Mostra todas
print (frutas)

#Quero exibir apenas a 3 fruta (pêra)
print (frutas[2])

#Exibir quantas frutas têm na minha tela?
print(len(frutas)) # length = tamanho

#Quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) # length = tamanho
print (frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

#i = 0
#while(i<4):
#  print(frutas[i])
#  i += 1
  
print ("Exemplo das frutas com while")
frutas.append("uva")

i = 0 # (i de index)
while(i<len(frutas)):
  print(frutas[i])
  i += 1

print("Exemplo das Frutas com FOR")
for fruta in frutas: 
  print(fruta)