import numpy as np
from langchain_community.vectorstores import FAISS
import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings

def create_db_embeddings(pages: list, openai_api_key: str, vector_store_path: str):
    """
    Cria um banco de dados vetorial de embeddings a partir de uma lista de páginas de texto.
    Além disso, esta função utiliza a API da OpenAI para gerar embeddings vetoriais de textos extraídos
    de um documento PDF, e armazena esses embeddings em um banco de dados FAISS.

    Parâmetros:
        - pages (list): Lista de strings, onde cada string representa uma página de texto extraída do documento.
        - openai_api_key (str): Chave da API da OpenAI necessária para gerar os embeddings.
        - vector_store_path (str): Caminho do arquivo onde o banco de dados vetorial será salvo.
    """
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db_faiss = FAISS.from_documents(chunks, embeddings)
    db_faiss.save_local(vector_store_path)

def query_vector_db(pages: list, query: str, openai_api_key: str, vector_store_path: str) -> list:
    """
    Consulta um banco de dados vetorial para encontrar os textos mais similares a uma consulta fornecida.
    Além disso, esta função carrega um banco de dados FAISS contendo embeddings vetoriais, e utiliza a API da OpenAI
    para gerar o embedding da consulta. Em seguida, busca os textos mais similares no banco de dados.

    Parâmetros:
        - pages (list): Lista de strings, onde cada string representa uma página de texto extraída do documento.
        - query (str): Consulta para a qual serão buscados os textos mais similares no banco de dados de embeddings.
        - openai_api_key (str): Chave da API da OpenAI necessária para gerar o embedding da consulta.
        - vector_store_path (str): Caminho do arquivo onde o banco de dados vetorial está salvo.

    Retorna(list): 
        - Lista de tuplas contendo o texto mais similar e sua pontuação de similaridade em relação à consulta.
    """

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db_faiss = FAISS.load_local(vector_store_path, embeddings, allow_dangerous_deserialization=True)
    return db_faiss.similarity_search_with_score(query, k=3)