import Aula4_Parte3 as bd

con, cur = bd.conectar()

nome =input("Informe o nome do Herói/Vilão: ")
nome_civil = input("Informe o nome civil  do Herói/Vilão: (Identidade Secreta)")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o)")

#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES({pessoa_id}, '{nome}','{nome_civil}', '{tipo}')"

cur.execute(sql)

#insert pessoas_grupos
#INSERT INTO pessoas_grupos(pessoa_id, grupo_id) VALUES (x,x)

con.commit()
con.close()
