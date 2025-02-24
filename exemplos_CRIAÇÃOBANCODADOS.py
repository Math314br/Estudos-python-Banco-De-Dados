import sqlite3 as conector
#banco de dados sqlite
try:
    #abrindo conexao e aquisição do cursor
    #cria um arquivo de banco de dados importante usar sqlite para coisas simples
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #criando uma tabela e pasasndo os paramentos
    #NOT NULL eh  que nao pode ser nulo os dados.
    comando = '''CREATE TABLE IF NOT EXISTS  Pessoa (cpf INTEGER NOT NULL,nome TEXT NOT NULL,
                nascimento DATE NOT NULL, oculos  BOOLEAN NOT NULL, PRIMARY KEY (cpf));'''

    cursor.execute(comando)
    # segunda tabela
    marca = '''CREATE TABLE IF NOT EXISTS  Marca(id INTEGER NOT NULL, nome TEXT  NOT NULL,
        sigla CHARACTER(2)NOT NULL,  PRIMARY  KEY(id));'''
    cursor.execute(marca)  

    carro = '''CREATE TABLE IF NOT EXISTS  Veiculo(placa CHARACTER(7) NOT NULL, ano  INTEGER NOT NULL,
        cor TEXT NOT NULL, proprietario INTEGER NOT NULL, marca  INTEGER NOT NULL,PRIMARY KEY(placa),
        FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf), FOREIGN KEY(marca) REFERENCES Marca(id));'''
        # coluna proprietario fara referencia na tabela pessoa NUMERO CPF, msm coisa para marca que fara referencia com ID da tabela marca.
        #     
    cursor.execute(carro)

    #efetivação do comando
    conexao.commit()

    # verificar erros
except conector.DatabaseError as erro:
    print(f"Erro no banco de dados:{erro} ")
finally:
    #fechando as conexoes
    if conexao:
        cursor.close()
        conexao.close()
        print("CONEXAO FECHADA!!!")
# 3 TABELAS CRIADAS.



