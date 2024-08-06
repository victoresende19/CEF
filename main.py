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
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET", "POST"],
    allow_credentials=True,
    allow_origins=["*"], 
    allow_headers=["*"]
)

VECTOR_STORE_PATH = "db"
DOC_PATH = "data/Codigo-de-Etica-e-de-Conduta.pdf"
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

@app.get("/")
async def root():
    return JSONResponse(
        status_code = 200,
        content = {
            "info": "Esta API tem como objetivo oferecer uma aplicação que utiliza a técnica de Retrieval Augmented Generation (RAG) para responder a perguntas específicas sobre o código de ética e conduta para funcionários e servidores da Caixa Econômica Federal (CEF), com base no documento público disponível no Caixa Asset."
        },
    )

@app.get("/create_vector_db")
async def create_vector_db():
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
    try:
        question = query.question
        pages = pdf_extract(DOC_PATH)
        docs_faiss = query_vector_db(pages, question, OPENAI_API_KEY, VECTOR_STORE_PATH)
        context_text = "\n\n".join([doc.page_content for doc, _score in docs_faiss])
        answer = rag_model(context_text, question, OPENAI_API_KEY)
        return JSONResponse(
            status_code=200, 
            content={"answer": answer}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"error": str(e)}
        )
