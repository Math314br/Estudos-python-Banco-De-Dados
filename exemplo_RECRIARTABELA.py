#aqui iremos excluir e recriar tabela que ja existe, por ela estar vazia nao ira perder nada, iremos tambem alterar as ordens das colunas que ja estava na tabela
import sqlite3 as conector

 # Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

 # Execução de um comando: SELECT... CREATE ...
comando1 = '''DROP TABLE Veiculo;'''

cursor.execute(comando1)

comando2 = '''CREATE TABLE Veiculo (
               placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
                motor REAL NOT NULL,
               proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
               PRIMARY KEY (placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''

cursor.execute(comando2)


conexao.commit()


cursor.close()
conexao.close()