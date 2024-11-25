from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from assistant.pdf_reader import pdf_extract
from assistant.db_embeddings import create_db_embeddings, query_vector_db
from assistant.context import rag_model
from assistant.schema import Query
from dotenv import load_dotenv
import numpy as np
import pickle
import os

load_dotenv()

VECTOR_STORE_PATH = "db"
DOC_PATH = "data/Codigo-de-Etica-e-de-Conduta.pdf"
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET", "POST"],
    allow_credentials=True,
    allow_origins=["*"], 
    allow_headers=["*"]
)

@app.get("/")
async def root():
    """
    Provides information about the API.

    Returns
    -------
    JSONResponse
        A JSON object containing a brief description of the API's purpose.
    """
    return JSONResponse(
        status_code=200,
        content={
            "info": """
            Esta API tem como objetivo oferecer uma aplicação que utiliza a técnica de Retrieval Augmented Generation (RAG) para responder 
            a perguntas específicas sobre o código de ética e conduta para funcionários e servidores da Caixa Econômica Federal (CEF), 
            com base no documento público disponível no Caixa Asset.
            """
        },
    )

@app.get("/create_vector_db")
async def create_vector_db():
    """
    Creates a vector database by extracting text from a PDF document and embedding it.

    Returns
    -------
    JSONResponse
        A success message if the vector database is created successfully.
    JSONResponse
        An error message if an exception occurs.
    """
    try:
        pages = pdf_extract(DOC_PATH)
        create_db_embeddings(pages, OPENAI_API_KEY, VECTOR_STORE_PATH)
        return JSONResponse(
            status_code=200,
            content={"message": "Banco de dados vetorial criado com sucesso."}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"error": str(e)}
        )

@app.post("/ask_question")
async def ask_question(query: Query):
    """
    Answers a question based on the content of a PDF document using a RAG-based model.

    Parameters
    ----------
    query : Query
        The query object containing the question to be answered.

    Returns
    -------
    JSONResponse
        The answer to the query if processed successfully.
    JSONResponse
        An error message if an exception occurs.
    """
    try:
        question = query.question
        docs_faiss = query_vector_db(question, OPENAI_API_KEY, VECTOR_STORE_PATH)
        context_text = "\n\n".join([doc.page_content for doc, _score in docs_faiss])
        answer, conversation = rag_model(context_text, question)
        return JSONResponse(
            status_code=200,
            content={
                'question': question,
                'answer': answer,
                'history': conversation
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
