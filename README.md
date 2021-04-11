# Python + Clean Arch
Projeto protótipo baseado em um mini curso para utilização de clean architecture juntamente com aplicações Python.

## Instalação do Projeto
Após realizar o clone do projeto, é indicado que os seguintes passos sejam seguidos:

### Criação do Ambiente Virtual
Ao clonar e entrar na pasta do projeto, devemos criar o ambiente virtual onde todos os packages necessários para o funcionamento do projeto serão instalados. 

O ambiente virtual utilizado neste projeto será o venv (virtualenv) e caso você já não tenha instalado em seu computador, instale-o rodando `pip install virtualenv`.

Após a instalação, execute o código `virtualenv -p python3 venv` para executar a criação do ambiente virtual na pasta do projeto.

### Acesso ao Ambiente Virtual
Para entrar em seu ambiente virtual, execute o código `. venv/bin/activate` no bash do linux ou `venv\Scripts\activate.bat` no cmd do windows.

### Instalação dos Packages
Como ultimo requerimento, execute o código `venv/bin/pip3 install -r requirements.txt` para linux ou `venv\Scripts\pip3.exe install -r requirements.txt` para windows para instalar todos os packages necessários para o funcionamento da aplicação.

## Criação e Instanciação do Banco de Dados (SQLite)
Para a criação do banco os seguintes passos devem ser seguidos via linha de comando:

1. ``` python ```

O passo 1 iniciará o python e você deverá executar os seguintes códigos:

2. ``` from src.repositories.config import * ```
3. ``` from src.entities import * ```
4. ``` db_conn = DBConnectionHandler() ```
5. ``` engine = db_conn.get_engine() ```
6. ``` Base.metadata.create_all(engine) ```

Após o passo 6, um arquivo chamado `storage.db` será criado com as configurações do seu banco de dados.

## Packages Utilizadas no Projeto

### Pylint
Linter da linguagem Python, neste projeto, está sendo utilizada de acordo com o code style PEP 8.

### Black
Formatador de códigos Python de acordo com o code style PEP 8.

### Flake8
Verificador de código para saber se o que está sendo commitado está dentro dos padrões do code style.

### Pre-Commit
Realiza o lint, formatação e teste nos códigos antes de qualquer commit.

### SQL Alchemy
ORM do banco de dados. Neste projeto, será utilizado o SQLite.

## Informações Úteis

### Salva as packages do venv no requeriments.txt

*Linux:*
``` venv/bin/pip3 freeze > requirements.txt ``` 

*Windows:*
``` venv/Scripts/pip3.exe freeze > requirements.txt ```

### Reconfigurar Git ao clonar o repositório
Caso você receba um erro ao clonar o repositório e tentar realizar um commit, sendo o erro ```/usr/bin/env: ‘python3.8’: No such file or directory``` no windows, você deve desinstalar o pre-commit e instalá-lo novamente com os seguintes comandos:

```pre-commit uninstall```

```pre-commit install```

## Créditos
Créditos ao youtuber Programador Lhama.