
import duckdb
import pandas as pd

# Importando o arquivo de clientes no Pandas
df_clientes = pd.read_csv("BaseClientes.csv", sep=",")

# Criando conexão com DuckDB
conexao = duckdb.connect(database=":memory:", read_only=False)

# Registrando o DataFrame como uma tabela no DuckDB
conexao.register("clientes", df_clientes)

# (Query 1) Contando os clientes
query = "SELECT COUNT(*) as quantidade_clientes FROM clientes;"
resultado = conexao.execute(query).df()

print(resultado)

# (Query 2) Selecionando apenas clientes com idade igual ou superior a 50 anos
query = "SELECT * FROM clientes WHERE idade >= 50;"
resultado = conexao.execute(query).df()

print(resultado)

# (Query 3) Contando o número de clientes por idade, em grupos de idades onde tem de mais de 30 clientes
query = """
SELECT idade, COUNT(*) as quantidade 
FROM clientes
GROUP BY idade
HAVING COUNT(*) > 30
ORDER BY idade;
"""
resultado = conexao.execute(query).df()

print(resultado)
