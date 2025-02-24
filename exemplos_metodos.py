#exemplo SQLITE3
import sqlite3 as conector
# poderia usar o mysql so precisaria importar biblioteca e mudar URL do conect
import mysql.connector as conector

#iniciando conexão
#essa url pode ser login e senha do banco, usuario etc
conexao = conector.connect("URL  SQLite")#"URL MySQL" usaria o mysql os comandos dps sao os msm

# criando cursor
cursor = conexao.cursor()

#exemplos de comandos SELECT CREATE
cursor.execute("...") # executa algum comando como select ou create etc
cursor.fetchall()#retorna todos itens pesquisados etc

#comitar todos alteração que fez
conexao.commit()

#fechar conexoes
cursor.close()
conexao.close()

# tambem se eu quiser usar o postgreSQL seria a mesma coisa porem importando biblioteca dele e alterando url 


