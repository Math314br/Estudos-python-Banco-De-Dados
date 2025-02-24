import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()
#aki ira alterar tabela veiculo add motor na coluna tabelas
comando = '''ALTER TABLE Veiculo ADD motor REAL;'''

cursor.execute(comando)
print('tabela atualizada')
conexao.commit()

cursor.close()
conexao.close()