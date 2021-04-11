# Python + Clean Arch
Projeto protótipo baseado em um mini curso para utilização de clean architecture juntamente com aplicações Python.

## Instalação do Projeto
Após realizar o clone do projeto, é indicado que os seguintes passos sejam seguidos:

### Criação do Ambiente Virtual
Ao clonar e entrar na pasta do projeto, devemos criar o ambiente virtual onde todos os packages necessários para o funcionamento do projeto serão instalados. 

O ambiente virtual utilizado neste projeto será o venv (virtualenv) e caso você já não tenha instalado em seu computador, instale-o rodando `pip install virtualenv`.

Após a instalação, execute o código `virtualenv -p python3 venv` para executar a criação do ambiente virtual na pasta do projeto.

### Acesso ao Ambiente Virtual
Para entrar em seu ambiente virtual, execute o código `. venv/bin/activate` no bash do linux.

### Instalação dos Packages
Como ultimo requerimento, execute o código `venv/bin/pip3 install -r requirements.txt` para instalar todos os packages necessários para o funcionamento da aplicação.

## Packages Utilizadas no Projeto

### Pylint
Linter da linguagem Python, neste projeto, está sendo utilizada de acordo com o code style PEP 8.

### Black
Formatador de códigos Python de acordo com o code style PEP 8.

### Flake8
Verificador de código para saber se o que está sendo commitado está dentro dos padrões do code style.

### Pre-Commit
Realiza o lint, formatação e teste nos códigos antes de qualquer commit.

## Códigos Necessários / Úteis

### Salva as packages do venv no requeriments.txt

``` pylint --generate-rcfile > .pylintrc ``` 

## Créditos
Créditos ao youtuber Programador Lhama.