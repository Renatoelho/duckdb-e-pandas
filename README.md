# Como utilizar o duckDB e o pandas para executar queries em um Dataframe

Este guia irá ensiná-lo a utilizar o duckDB e pandas para executar consultas em um dataframe.

#### Pré-requisitos

Para seguir este guia, você precisará ter o duckDB e o pandas instalados em seu ambiente de desenvolvimento.

Você pode instalar o duckDB executando o seguinte comando no terminal:

```bash
pip install duckdb
```

E para instalar o pandas, basta executar o seguinte comando:

```bash
pip install pandas
```

#### Criando o dataframe

Para este exemplo, vamos criar um dataframe de clientes usando o pandas. Execute o seguinte código em seu ambiente de desenvolvimento:

```python
import pandas as pd

# Importando o arquivo de clientes no Pandas
df_clientes = pd.read_csv("BaseClientes.csv", sep=",")

print(df_clientes)
```

Este código criará um dataframe com cinco colunas: nome, sobrenome, idade, ultimo_salario e empresa_atual.

A saída no console será a seguinte:

|   |nome|sobrenome|idade|ultimo_salario|empresa_atual|
|-----|-----|-----|-----|-----|-----|
|0|Enrico|Rushmare|31.0|NaN|Skinte|
|1|Ivett|Pettiward|31.0|5249.72|NaN|
|2|Stillmann|Budnik|NaN|13738.43|Tagchatx|
|3|Zondra|Lille|18.0|15998.02|Roomm|
|4|Eldon|Normansell|32.0|NaN|NaN|
|...|...|...|...|...|...|
|995|Darrel|Finders|19.0|19447.05|Jaxnation|
|996|Nelson|Pedel|20.0|3112.77|NaN|
|997|Emmanuel|Trevithick|NaN|4383.58|Twinder|
|998|Alfy|Ilyunin|46.0|NaN|Vinder|
|999|Phaidra|Dolley|20.0|NaN|Bubblemix|

#### Conectando-se ao duckDB

Agora que temos nosso dataframe de clientes, vamos conectar-nos ao duckDB para realizar algumas consultas. Execute o seguinte código em seu ambiente de desenvolvimento:

```python
import duckdb

# Criando conexão com DuckDB
conexao = duckdb.connect(database=":memory:", read_only=False)

# Registrando o DataFrame como uma tabela no DuckDB
conexao.register("clientes", df_clientes)
```

Este código criará uma conexão com o duckDB e registrará o dataframe de clientes como uma tabela chamada clientes.

#### Executando consultas

Agora que estamos conectados ao duckDB, podemos executar consultas em nosso dataframe de clientes. Execute o seguinte código em seu ambiente de desenvolvimento:

```python
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
```

Este código executará três consultas em nosso dataframe de clientes. A primeira consulta conta os clientes, a segunda consulta seleciona apenas clientes com idade igual ou superior a 50 anos e a terceira consulta conta o número de clientes por idade, em grupos de idades onde tem de mais de 30 clientes.

As saídas no console serão as seguintes:

- (Query 1) Contando os clientes.

|     |quantidade_clientes|
|-----|-----|
|0|1000|

- (Query 2) Selecionando apenas clientes com idade igual ou superior a 50 anos.

|     |nome|sobrenome|idade|ultimo_salario|empresa_atual|
|-----|-----|-----|-----|-----|-----|
|0|Egbert|Guisot|50.0|17009.68|Roombo|
|1|Manon|Oaker|50.0|13766.00|NaN|
|2|Marylou|Simonassi|50.0|11604.18|Camimbo|
|3|Carr|Surridge|50.0|9595.53|NaN|
|4|Karyn|Sibille|50.0|NaN|NaN|
|5|Gabrila|Baudins|50.0|2655.76|NaN|
|6|Lucina|Bedboro|50.0|7884.42|Edgeclub|
|7|Carmon|Dulin|50.0|NaN|Wikivu|
|8|Ashien|Dobell|50.0|3311.35|Mynte|
|9|Maison|Spikings|50.0|6330.74|NaN|
|10|Roi|Fuge|50.0|6093.19|InnoZ|
|11|Jodi|Surman-Wells|50.0|18373.74|Yodo|
|12|Riobard|Heppner|50.0|19755.22|Dabshots|
|13|Alessandra|Francklin|50.0|8639.67|Flipopia|

- (Query 3) Contando o número de clientes por idade, em grupos de idades onde tem de mais de 30 clientes.

|     |idade|quantidade|
|-----|-----|-----|
|0|NaN|109|
|1|23.0|33|
|2|26.0|37|
|3|29.0|37|
|4|38.0|39|
|5|45.0|34|
|6|46.0|36|
|7|47.0|33|

***Referência:*** https://duckdb.org/docs/guides/python/sql_on_pandas

***Observação:*** É importante mencionar que o código apresentado acima pode não funcionar corretamente no ambiente Jupyter. Para garantir o funcionamento correto do duckDB em um notebook do Jupyter, é recomendado que se consulte a documentação oficial do duckDB para instruções específicas sobre como utilizá-lo nesse ambiente. A documentação pode ser encontrada em https://duckdb.org/docs.
