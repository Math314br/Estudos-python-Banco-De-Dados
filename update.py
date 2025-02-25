#atualizar banco de dados!!!!!
import sqlite3 as conector

conexao = conector.connect('./meu_banco.db')
cursor = conexao.cursor()

comando = '''UPDATE Pessoa SET oculos= ? WHERE cpf=13308809919;'''
#ira executar um  comando para atulzar oculos agr ele usa oculos.
# SE EU QUISER DELETAR UMA PESSOA USARIA DELETE Pessoa WHERE cpf=COLOCO CPF DA PESSOA E EXECUTO PESSOA SERIA DELETADA
cursor.execute(comando,(True,))

conexao.commit()

cursor.close()
conexao.close()
print("conexao fechada")