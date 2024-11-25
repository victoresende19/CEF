from utils.format import format_chat_history, format_docs
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv() 
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

OPENAI_MODEL = "gpt-3.5-turbo-0125"
llm_model = ChatOpenAI(model=OPENAI_MODEL)
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

conversation_chain = ConversationChain(
    llm=llm_model,
    verbose=False,
    memory=memory
)

def rag_model(context_text: str, query: str) -> str:
    """
    Gera uma resposta baseada em um contexto fornecido, utilizando o modelo OpenAI.

    Parametros
        - context_text (str): Texto do contexto baseado no qual a resposta será gerada.
        - query (str): Pergunta a ser respondida com base no contexto fornecido.

    Retorna (str):
        - Resposta gerada pelo modelo.
    """

    prompt_template = """
    You are an expert in the Caixa Econômica Federal Ethics Code, with comprehensive knowledge of organizational ethical guidelines, conduct standards, and reporting mechanisms.
    Don't make up information and, if you don't know it, say so explicitly to talk with HR.
    
    **Retrieval:**
    Relevant information from the Caixa Econômica Federal Ethics Code, including:
    {context}
    
    **Instruction:**
    Answer in a clear, precise, and professional manner, adapting the tone to the employee's role and context.
    Your answer should help resolve the ethical query without unnecessary complications or legal jargon.
    
    **Context:**
    The question has been asked by a Caixa Econômica Federal employee seeking clarification on ethical guidelines, conduct expectations, or potential ethical dilemmas in the workplace.
    
    **Explanation:**
    Provide detailed explanations based on the Ethics Code, citing specific sections or articles when relevant.
    Help the employee understand the ethical principles and reasoning behind the guidance.
    If the context provides official references or contact information for the Ethics Committee, include them.
    
    **Attention:**
    Always answer in Portuguese.
    Maintain confidentiality and professionalism in all interactions.

    Question: {question}
    """

    prompt = prompt_template.format(context=context_text, question=query)
    answer = conversation_chain.run(prompt)
    conversation = format_chat_history(conversation_chain.memory.chat_memory.messages, context_text)
    return answer, conversation
