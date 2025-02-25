import sqlite3 as conector
# importando classe pessoa do arquivo classes.py
from classes import Pessoa
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#criação do objeto pessoa aonde dados seram mandado para banco de dados
pessoa = Pessoa(13308809919,"jose lima","1999-12-30",False)
pessoa2 = Pessoa(12467807913,"maria","2008-08-07",True)
#pessoa 3 sera enviado dados por dicionario fica mais facil para entender os dados.
pessoa3 = Pessoa(13814887918,"isabella","2005-11-28",True)
comando2 = '''INSERT INTO Pessoa(cpf,nome,nascimento,oculos) VALUES (
        :cpf, :nome, :data_nascimento, :oculos);'''

cursor.execute(comando2,{
    'cpf':pessoa3.cpf,
    'nome':pessoa3.nome,
    'data_nascimento':pessoa3.data_nascimento,
    'oculos':pessoa3.oculos
    })

conexao.commit()

# comando para enviar banco de dados com query parameter
comando = '''INSERT INTO Pessoa(cpf,nome,nascimento,oculos) VALUES (?,?,?,?);'''
#ENVIANDO DADOS PARA TABELA
cursor.execute(comando,(pessoa.cpf, pessoa.nome,pessoa.data_nascimento,pessoa.oculos))
cursor.execute(comando,(pessoa2.cpf, pessoa2.nome,pessoa2.data_nascimento,pessoa2.oculos))

conexao.commit()

cursor.close()
conexao.close()
print("conexao FECHADA")