# 🌌 42 Constellation Tracker (Radar de Constelações)
Este projeto utiliza a API pública da 42 para rastrear em tempo real quais membros de uma determinada constelação estão online no campus do Rio de Janeiro.

## Descrição dos arquivos
`oAuth2.py`: gera o token de atenticação com a API da 42.

`campusId.py`: esse script busca o ID de um campus através do nome da cidade.

`constellations.py`: dicionário das constelações de um determinado campus (RJ - BRASIL).

`exercicio2.py`: o script principal que identifica a constelação do usuário e lista quais colegas do mesmo grupo estão logados no campus, detalhando inclusive se estão em máquinas Mac ou Dell.

## Configuração
É preciso criar um **App** na Intra da 42 para gerar as credenciais `UID` e `SECRET`, necessárias pra gerar o token de autenticação.

### 1. Instale as dependências
`pip install -r requirements.txt`

### 2. Configure as variáveis de ambiente
#### 2.1. Crie um arquivo .env na raiz do seu projeto e adicione:

`MY_AWESOME_UID=seu_uid_aqui`

`MY_AWESOME_SECRET=seu_secret_aqui`

#### 2.2. Execute o script oAuth2.py para gerar o token de autenticação da API da Intra

#### 2.3. Adicione o token gerado ao arquivo .env no seguinte formato:

`access_token=seu_token_aqui`

### Execute o script principal

#### Windows
`python exercicio2.py`

#### Linux
`python3 exercicio2.py`

## Bônus
`bonus.py` é uma atualização do script para enviar os dados formatados no discord via webhook.
<img width="511" height="447" alt="image" src="https://github.com/user-attachments/assets/d94cd48e-e4be-4c12-962e-d506bc63d885" />

## Notebook de estudo
Além dos scripts principais, este repositório inclui um arquivo .ipynb, que funciona como um laboratório pessoal de testes e exploração. É importante notar que este arquivo **não possui caráter de documentação oficial**, servindo apenas como um registo dos meus primeiros testes com a API da 42 e das fases iniciais de desenvolvimento. Nele é possível notar como o projeto evoluiu à medida que aprofundei o meu entendimento sobre os métodos de manipulação de dados em Python e as funcionalidades da API, adaptando a lógica para o que fazia mais sentido no contexto da comunidade.

O objetivo inicial era criar um ranking dos cinco alunos que mais realizaram avaliações num campus durante uma semana. No entanto o escopo foi alterado para o atual sistema de rastreio de constelações.

## O que eu aprendi
- Conceitos básicos em Python
  - Laços de repetição e condicionais
  - Estruturas de dados (listas e dicionários)
  - Manipulação de JSON
  - Funções para organização da lógica
  - Filtragem e validação de dados em tempo de execução
- Uso prático da biblioteca `requests`
  - Métodos HTTP
  - Passagem de parâmetros de filtragem
- Mudança de escopo conforme necessidade
  - o projeto evoluiu conforme novas ideias e limitações técnicas apareceram

