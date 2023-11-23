FROM python:3.9.18-slim-bookworm

# Cria os diretórios para proto e generated
WORKDIR /app

# Atualiza o pip e instala o virtualenv
RUN python -m pip install --upgrade pip && python -m pip install virtualenv

# Cria e ativa o ambiente virtual
RUN virtualenv venv

# Copia os requisitos e instala as dependências
COPY ./requirements.txt ./
# Instala as dependências contidas no requirements
RUN venv/bin/pip install -r requirements.txt
# Cria a pasta prot
RUN mkdir proto

COPY models /app/models

COPY services /app/services
# Copia o arquivo proto
COPY ./proto/server.proto /app/proto

# Gera os arquivos python/grpc a partir do arquivo .proto
RUN venv/bin/python -m grpc_tools.protoc -I ./proto --python_out=. --pyi_out=. --grpc_python_out=. ./proto/server.proto

# Copia o servidor gRPC
COPY ./grpc_server.py /app
