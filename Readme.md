
# Python&gRPC

Container docker basico com python e gRPC

## Instalação

#### Instalando a biblioteca python virtualenv:
```bash
  python -m pip install virtualenv
```
#### Criando o ambiente virtual venv:
```bash
  virtualenv venv
```
#### Iniciando o ambiente virtual:
```bash
  source venv/bin/activate
```
#### Instalando as dependencias:
```bash
  pip install -r requirements.txt
```
#### Gerando os metodos proto:
```bash
  python -m grpc_tools.protoc -I ./proto --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated ./proto/server.proto
```

Legenda do comando `grpc_tools.proto`:

`-I`: Aponta para diretorio do arquivo proto;

`--python_out`: Define onde os arquivos python serão gerados;

`--pyi_out`: Define onde os arquivos pyi serão gerados;

`--grpc_python_out`: Define onde os arquivos grpc serão gerados;
    
## Iniciando o servidor

### Caso queira rodar o servidor sem o docker siga o passo abaixo.

```bash
  python ./grpc_server.py
```

### Caso queira rodar o servidor com docker execute os passos abaixo.


Para rodar esse projeto com o docker, você vai precisar configurar as variaveis `PROJETO` `PROJETO_DIR` `SERVER` `PORTAS` do arquivo .env que se encontra na pasta [/docker](/docker)

#### Apos configurar as variaveis do arquivo .env basta seguir os passos abaixo:

#### Rodando o container docker:
```bash
  cd docker
  docker compose up -d
```

#### Acessando o container docker (Só funciona com o container rodando)

```bash
  docker exec -it grpc_python bash
```

## Testando requisições rpc com o insomnia

Utilizando insomnia crie uma nova gRPC request, adicione o caminho '127.0.0.1:50051' selecione o proto file presente na pasta /proto/server.proto e selecione o metodo SayHello adicione no body  `{"name":"Teste"}` e clique em "send" sera retornado a resposta:

```
{
	"message": "Hello Teste"
}
```

## Adicionais

Gerar o arquivo requirements caso não tenha:
```bash
source venv/bin/activate
pip freeze > requirements.txt
```