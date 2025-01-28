# Assistente CEF

Sua plataforma definitiva para tirar dúvidas sobre o Código de ética e conduta da Caixa Asset!

## Acesse 
Para facilitar o teste do Assistente CEF, foi desenvolvido um website que realiza consultas à API criada. A API foi criada através das bibliotecas FastAPI, PyPDF2, FAISS, LangChain e OpenAI, em linguagem Python, e é necessário obter uma API_KEY da OpenAI, a qual você pode criar gratuitamente, basta [clicar aqui](https://openai.com/index/openai-api/). Além disso, visando a acessibilidade, criou-se a plataforma Assistente CEF por meio do framework React, em linguagem JavaScript. 

O deploy da API foi realizado utilizando o [Google Cloud](https://cloud.google.com/?hl=pt-BR), sob o plano gratuito. Devido às limitações deste plano, como o uso de máquinas menos robustas, o tempo de resposta pode ser maior em comparação ao uso local da API. Por fim, o frontend da plataforma teve o deploy através do [Vercel](https://vercel.com/). Para acessar e testar o aplicativo, visite: [https://gravidai.vercel.app/](https://gravidai.vercel.app/).

![image](https://github.com/user-attachments/assets/f6988332-82b0-4cef-9738-b2ae12f54027)


<hr>

## Tecnologias
O agente foi criado a partir da técnica RAG (Retrieval-Augmented Generation), visando respostas mais assertivas sobre o assunto. Além disso, utilizou-se das seguintes tecnologias:
- Python 3.11 (com as respectivas bibliotecas): 
  - LangChain: biblioteca para utilização modular de códigos voltados a agentes de IA;
  - OpenAI (além do OpenAI Key): utilização dos modelos LLM OpenAI para a criação das descrições e títulos. Além disso, utilização do modelo DallE 3 para criação da thumbnail;
  - FAISS: utilização para criação do banco de dados vetorial, alocação e pesquisa dos embeddings.
  - PyPDF2: extração de textos de PDFs;
  - Poetry: pacote para o controle de versões das bibiliotecas.
- MongoDB Atlas: utilizado para alocação e recuperação dos embeddings por meio da Vector Search e distância de cosseno.


## Conteúdos:
Para a utilização da técnica RAG, utilizou-se os conteúdos abaixo visando dar um contexto melhor ao assistente. Assim, as respostas são cada vez mais personalizadas e assertivas:
- [CÓDIGOS DE ÉTICA E DE CONDUTA CAIXA ASSET](https://www.caixa.gov.br/Downloads/caixa-asset/Codigo-de-Etica-e-de-Conduta.pdf)

## API
A API foi escrita em FastAPI através da lingugem Python e as devidas bibliotecas contidas no arquivo requirements.txt.

### Configurações - localmente
Instalação da biblioteca Poetry:
```
pip install poetry
```

Inicialização do Poetry:
```
poetry init
```

Instalação das bibliotecas necessárias:
```
poetry install
```

Ou há a possibilidade de apenas utilizar o comando abaixo para a instalação das bibliotecas:
```
pip install requirements.txt
```

Configuração arquivo .env:
```
OPENAI_API_KEY=
```

Ativação da API:
```
poetry run uvicorn main:app --reload
```

### Endpoints
Para executar a API localmente, os seguintes métodos estarão disponíveis. Utilize ferramentas como o Postman ou Insomnia para realizar as requisições:
- Introdução à API com informações de documentos utilizados:
  - ``` (GET): http://127.0.0.1:8000/ ```
- Criação dos embeddings:
  - ``` (GET):  http://127.0.0.1:8000/create_embeddings/ ```
- Assistente:
  - ``` (POST):  http://127.0.0.1:8000/ask_question/ ```
  - Corpo da Requisição JSON: ```{ "question": "Posso receber presentes sendo funcionário da Caixa Asset?" }```

## Frontend
O frontend foi escrito em React através da linguagem Typescript.

### Configurações - localmente
Instalação das bibliotecas:
```
npm install
```

Caso deseje, troque o endpoint de consulta, caso o teste seja feito local, em: gravidai > src > App.tsx:
```
http://127.0.0.1:8000/ask_question/
```

Ativação da interface:
```
npm start
```

## Arquitetura RAG
![image](https://github.com/user-attachments/assets/9f4ec445-8632-4614-aedb-d3c571283305)

## Arquitetura em camadas
![image](https://github.com/user-attachments/assets/a78f90aa-d18e-4b8c-bb49-4d2430beb658)

<hr>
@Victor Resende
