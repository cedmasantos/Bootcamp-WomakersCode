import sqlite3

#estabelecendo conexao
conexao = sqlite3.connect('C:/Users/cedma/vs-code-projects/Bootcamp-WomakersCode/Banco-de-dados/banco')
cursor = conexao.cursor()

#Criando uma tabela
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')


#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
cursor.execute('DROP TABLE produtos')



conexao.commit()
conexao.close