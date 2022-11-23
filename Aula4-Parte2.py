#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um um objeto do tipo cursor 
cursor = conexao.cursor()

#4o. passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoa (pessoa_id, nome, nome_civil, tipo) VALUES (21, 'The Flash', 'Barry Allen', 'Herói(na)')"

#5o. passo: executar o comando sql no sqllite(no cursor)
cursor.execute(sql)

#6o. passo: confirmar o INSERT com commit() e fechar banco
conexao.commit()
conexao.close()