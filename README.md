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

data = {'id': [1, 2, 3, 4, 5],
        'name': ['João', 'Maria', 'Pedro', 'Ana', 'Luiza'],
        'age': [25, 30, 18, 40, 27],
        'city': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba']}
        
df = pd.DataFrame(data)

print(df)
```

Este código criará um dataframe com cinco colunas: id, name, age, city.

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

con = duckdb.connect(database=":memory:", read_only=False)

con.register("clientes", df)
```

Este código criará uma conexão com o duckDB e registrará o dataframe de clientes como uma tabela chamada clientes.

#### Executando consultas

Agora que estamos conectados ao duckDB, podemos executar consultas em nosso dataframe de clientes. Execute o seguinte código em seu ambiente de desenvolvimento:

```python
# Selecionando todos os clientes
query = 'SELECT * FROM clientes'
result = con.execute(query).fetchdf()

print(result)

# Selecionando apenas clientes com idade acima de 25 anos
query = 'SELECT * FROM clientes WHERE age > 25'
result = con.execute(query).fetchdf()

print(result)

# Contando o número de clientes por cidade
query = 'SELECT city, COUNT(*) as count FROM clientes GROUP BY city'
result = con.execute(query).fetchdf()

print(result)
```

Este código executará três consultas em nosso dataframe de clientes. A primeira consulta seleciona todos os clientes, a segunda consulta seleciona apenas os clientes com idade acima de 25 anos e a terceira consulta conta o número de clientes por cidade.

As saídas no console serão as seguintes:

xxx

zzz

ddd


***Referência:*** https://duckdb.org/docs/guides/python/sql_on_pandas

***Observação:*** É importante mencionar que o código apresentado acima pode não funcionar corretamente no ambiente Jupyter. Para garantir o funcionamento correto do duckDB em um notebook do Jupyter, é recomendado que se consulte a documentação oficial do duckDB para instruções específicas sobre como utilizá-lo nesse ambiente. A documentação pode ser encontrada em https://duckdb.org/docs.

