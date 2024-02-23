import sqlite3

#estabelecendo conexao
conexao = sqlite3.connect('C:/Users/cedma/vs-code-projects/Bootcamp-WomakersCode/Banco-de-dados/banco')
cursor = conexao.cursor()

# 1 Criando uma tabela chamada alunos

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#  2 Inserindo 5 registros

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES( 1, "Cedma", 37, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES( 2, "Natalia", 25, "Programação   ")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES( 3, "Ana", 22, "Contábeis   ")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES( 4, "MAria", 20, "Analista de sistemas   ")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES( 5, "Zoe", 30, "Arquiteta de software   ")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES( 6, "Zuma", 32, "Engenharia")')



# 3 Consultas Básicas

# a selecionar todos os registros de alunos

dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print(alunos)


# b Selecionar o nome e a idade dos alunos com mais de 20 anos

dados2 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for alunos in dados2:
    print(alunos)

# c Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados3 = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for alunos in dados3:
    print(alunos)

# d Contar o número total de alunos na tabela

dados4 = cursor.execute('SELECT COUNT(*) FROM alunos')
myresult = dados4.fetchall()
print(myresult[-1][-1])

# 4 Atualização e Remoção 

#a) Atualize a idade de um aluno específico na tabela.

dados5 = cursor.execute('UPDATE alunos SET idade=38 WHERE nome = "Cedma"')
for alunos in dados5:
    print(alunos)

# b) Remova um aluno pelo seu ID.

dados6 = cursor.execute('DELETE FROM alunos WHERE id = 2')
for alunos in dados6:
    print(alunos)

# 5 Criar uma Tabela e Inserir Dados

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo real);')

#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES( 1, "Cedma", 37, 10)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES( 2, "Natalia", 25, 20)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES( 3, "Ana", 22, 30)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES( 4, "MAria", 20, 40)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES( 5, "Zoe", 30, 20)')

# 6. Consultas e Funções Agregadas
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

dados7 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
myresult = dados7.fetchall()
for clientes in myresult:
    print(clientes)

# b) Calcule o saldo médio dos clientes.


dados8 = cursor.execute("SELECT AVG(saldo) FROM clientes")

myresult  = dados8.fetchone()[0]

print("Saldo médio dos clientes:", myresult)

#) Encontre o cliente com o saldo máximo.

dados9 =  cursor.execute("SELECT nome, idade, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)")
myresult = dados9.fetchall()
for clientes in myresult:
    print(clientes)

# d) Conte quantos clientes têm saldo acima de 1000.


dados10 = cursor.execute(("SELECT COUNT(*) FROM clientes WHERE saldo > 1000"))
myresult = dados10.fetchall()
print(myresult[-1][-1])

# 7. Atualização e Remoção com Condições

#a) Atualize o saldo de um cliente específico.

dados11 = cursor.execute('UPDATE clientes SET saldo =1000 WHERE nome = "Cedma"')
myresult = dados11.fetchall()
for clientes in myresult:
    print(clientes)

#b) Remova um cliente pelo seu ID.

dados12 = cursor.execute('DELETE FROM clientes WHERE id = 2')
myresult = dados12.fetchall()
for clientes in myresult:
    print(clientes)


#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')




#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
#cursor.execute('DROP TABLE produtos')



conexao.commit()
conexao.close