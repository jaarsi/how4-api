# Sistema de Pedidos

how4-api é o componente que representa o back-end do projeto HoW4 (Hands on Work 4), disciplina contida no curso de sistemas da informação da UNIVALI;

## Resumo

Para executar este projeto, as seguintes tecnologias são necessárias:

- Python 3.8+
- Pip e Pipenv (gerenciadores de pacote)
- Flask (web framework)
- Peewee (orm)

## Instalação

Este guia tem como base o sistema operacional Linux Ubuntu 20.04.
Começaremos instalando os pacotes necessários:

```bash
sudo apt update
sudo apt install -y python3-pip sqlite3
pip3 install pipenv
```

Agora é o momento de clonar o repositório:

```bash
git clone https://github.com/jaarsi/how4-challenge-api
cd how4-challenge-api
```

A partir da pasta clonada, instalaremos as dependências do projeto. Para tal tarefa, usaremos o pipenv:

```bash
pipenv install
```

O utilitário pipenv se encarregará de criar o ambiente virtual e instalar as dependências do projeto.
O proximo passo é criar uma arquivo ".env". Esse arquivo contém toda as configurações inerentes ao ambiente de desenvolvimento.

```text
FLASK_ENV=development
FLASK_DEBUG=1
DATABASE_URL=sqlite:///database.db
```

Uma breve explicação:

- FLASK_ENV: Indica o ambiente na qual o sistema será executado. Util para detectar quando a api está rodando em modo de testes, desenvolvimento ou produção.
- FLASK_DEBUG: Indica se o projeto será executado em modo debug. Este modo permite inspecionar a execução interna do programa e é bem util no diagnóstico de bugs.
- DATABASE_URL: Contém a connection string que identifica o repositório de dados.

Em seguida, vamos criar as tabelas do banco de dados, para tal tarefa, 2 comandos estão disponíveis:

```bash
pipenv run flask create-database
pipenv run flask seed-database
```

Importante notar que estamos executando os comandos precedidos de "pipenv run". Isso acontece porque o python e as dependências do projeto estão num ambiente virtual, como mencionado anteriormente, portanto, estão num ambiente separado do sistema operacional. Prefixando com "pipenv run", podemos rodar os comandos utilizando o contexto do ambiente virtual. Sem esse prefixo, os comandos retornarão com erro. Dito isto, vamos às explicações:

- flask create-database: Cria um banco de dados (database.db) e cria as tabelas segundo a modelagem definida no arquivo models.py.
- flask seed-database: Partindo do principio que o banco já está criado, este comando povoa-o com uma massa de dados de exemplo.

E, finalmente, para executar o projeto:

```bash
pipenv run flask run
```

### Endpoints

A api expõe algumas rotas que permite aplicações externas interagirem com a mesma, vamos à elas:

#### GET /cliente

Retorna uma lista com todos os clientes.

#### GET /cliente/<int:id>

Retorna um cliente, baseado no id informado na url.

#### POST /cliente

Salva um cliente no banco de dados.

```text
    no_cliente: str
    nu_cpf: str
    de_email: str
    st_inativo: bool
```

#### PUT /cliente/<int:id>

Atualiza um cliente, baseado no id informado na url.

```text
    no_cliente: str
    nu_cpf: str
    de_email: str
    st_inativo: bool
```

#### DELETE /cliente/<int:id>

Deleta um cliente.

#### GET /produto

Retorna uma lista com todos os produtos.

#### GET /produto/<int:id>

Retorna o produto identificado pelo id indicado na url.

#### POST /produto

Grava um produto no banco de dados.

```text
    no_produto: str
    de_produto: str
    qt_estoque: int
    st_inativo: bool
```

#### PUT /produto/<int:id>

Atualiza o produto identificado pelo id indicado na url.

```text
    no_produto: str
    de_produto: str
    qt_estoque: int
    st_inativo: bool
```

#### DELETE /produto/<int:id>

Exclui o produto identificado pelo id indicado na url.

#### GET /pedido

Retorna a lista de pedidos

#### GET /pedido/<int:id>

Retorna um pedido identificado pelo id indicado na url.

#### POST /pedido

Grava um pedido.

```text
    cliente: int
    vr_pedido: float
    itens: list[item]
```

Formato do item
```
    nu_ordem: int
    produto: int
    qt_produto_item: float
    vr_unitario: float
```

#### PUT /pedido/<int:id>

Atualiza um pedido identificado pelo id indicado na url.

```text
    cliente: int
    vr_pedido: float
    itens: list[item]
```

Formato do item
```
    nu_ordem: int
    produto: int
    qt_produto_item: float
    vr_unitario: float
```

#### DELETE /pedido/<int:id>

Exclui um pedido identificado pelo id indicado na url.
