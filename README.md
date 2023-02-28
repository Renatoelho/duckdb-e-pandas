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

```bash
   id    name  age            city
0   1    João   25       São Paulo
1   2   Maria   30  Rio de Janeiro
2   3   Pedro   18  Belo Horizonte
3   4     Ana   40    Porto Alegre
4   5   Luiza   27        Curitiba
```

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

