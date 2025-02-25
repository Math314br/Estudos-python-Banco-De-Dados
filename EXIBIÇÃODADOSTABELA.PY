import sqlite3 as conector
from  classes import Pessoa

conexao = conector.connect('./meu_banco.db')
cursor = conexao.cursor()

# essa função ira converter dados bolean inves de aparecer numero aparece TRUE OU FALSE
def converter(dado):
    return True if dado == 1 else False
# aqui pasara regristro da conversao para conector
conector.register_converter('BOOLEAN', converter)
comando = '''SELECT * FROM Pessoa WHERE oculos = ?;'''
cursor.execute(comando,(True,))

#puxando todos dados
registros  = cursor.fetchall()
for registro in registros:
    #aqui pega todos registros das pessoas  e printa tipo e oq esta insirido
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.oculos), pessoa.oculos)

cursor.close()
conexao.close()
