#Pede o nome do aulo e sua nota (de 0 a 10) e, se ele tirar nota 10, você é bichão, mesmo...

nome = input ("Informe o nome do aluno: ")

nota = float(input("Insira a nota que tirou (0 a 10): "))

print ("Aluno {} tirou nota {}".format(nome, nota))

if (nota == 10):
  print("Você é bichão, mesmo...")

elif (nota >=6 and nota < 10):
  print("Tá no caminho certo")

else:
  print("Bora estudar!")

