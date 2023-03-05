# DesafioKonsi

Projeto desenvolvido a partir de desafio feito pela empresa Konsi.

## Descrição

Este projeto tem como objetivo montar um serviço de API que recebe uma requisição de um cliente, contendo um Json, informando seu CPF e credenciais de acesso ao site (http://extratoclube.com.br/). Posteriormente o sistema deve acessar o site e por meio de um Crawler, navegar até a aba de consulta de benefícios, extrair o beneficio retornado pelo servidor e por fim enviar de volta ao requisitante o benefício resultante da busca 

## Iniciando

### Dependencias

* Python 3.9
* PIP
* Pytest: Já está contindo no requirements.txt. (https://docs.pytest.org/en/7.2.x/getting-started.html)
* Uvicorn: Já está contindo no requirements.txt. (https://www.uvicorn.org/)
* Google Chrome: Versão 110.0.5481.178 (Versão oficial) 64 bits. (https://support.google.com/chrome/answer/95346?hl=pt-BR&co=GENIE.Platform%3DDesktop)
* Chromedriver : Uma versão compatível com o Chrome da versão acima já se encontra na raiz do projeto, caso possua outra versão do Google Chrome o Chromedriver compativel deve ser baixado e usado para subistituir o contido no projeto. (https://chromedriver.chromium.org/downloads)
* Postman: Para requisição post com Json de teste (Qualquer ferramenta que execute requisições post pode ser usado). (https://www.postman.com/downloads/)

### Instalação

* Clonar projeto do git.
* Abrir terminal
* Navegar até a pasta para onde desejar importar o projeto
* Executar o comando
```
git clone git@github.com:Pauloh7/DesafioKonsi.git
```

* Subir ambiente virtual.
* Abrir terminal
* Navegar até a pasta para onde desejar criar o ambiente virtual
* Usar comando para criar o ambiente (Exemplo utilizando virtualenv mas é possivel utilizar outro de própria preferencia):
```
virtualenv nome_da_virtualenv
```
* Utilizar primeiro comando em ambientes linux ou segundo comando em ambientes Windows para ativar o ambiente virtual.
* Linux
```
source nome_da_virtualenv/bin/activate
```
* Windows
```
nome_da_virtualenv/Scripts/Activate
```

* Instalar requeriments.txt
* Navegar ate o diretorio contendo o requirements.txt
* Com o ambiente virtual ativo executar o comando:
```
pip install -r requirements.txt
```

### Executando Projeto

* Abrir Terminal ou PowerShell.
* Ativar o ambiente virtual.
* Linux
```
source nome_da_virtualenv/bin/activate
```
* Windows
```
nome_da_virtualenv/Scripts/Activate
```
* Navegar até pasta raiz do projeto.
* Executar uvicorn para subir API (rodar este comando obrigatoriamente na pasta raiz do projeto):
```
uvicorn api.router:app --reload
```
* Uma mensagem "Application startup complete." deve ser exebida no terminal.
* Abrir o Postman.
* Preencher a barra da URL de requisição com o endereço: 127.0.0.1:8000/consultacpf/
* Alterar a opção de envio setada em get para post.
* Selecionar a opção Body.
* Selecionar raw e alterar de text para json, mudando assim o Content-Type.
* Preencher a caixa de texto com seguinte para gerar o json:
```
{
"cpf":"cpf_buscado",
"login":"usuario_de_acesso",
"senha":"senha_de_acesso"
}
```
* Clicar em send
* Na caixa body inferior deve ser exibido o resultado da requisição feita.

### Executando Testes

*Abrir terminal
*Navegar até raiz do projeto
*Executar comando (Executar via python para evitar erro de importação de modulos):
```
python -m pytest tests/
```
##Help

A requisição post deve ser feita por HTTP, provavelmente HTTPS ocorrerá em erro.

## Autor

[Paulo Henrique De Souza Gomes](https://www.linkedin.com/in/paulo-henrique-4a849139/)
