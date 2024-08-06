from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI

def rag_model(context_text: str, query: str, OPENAI_API_KEY: str) -> str:
    """
    Gera uma resposta baseada em um contexto fornecido, utilizando o modelo OpenAI.

    Parametros
        - context_text (str): Texto do contexto baseado no qual a resposta será gerada.
        - query (str): Pergunta a ser respondida com base no contexto fornecido.
        - OPENAI_API_KEY (str): Chave API necessária para acessar o modelo OpenAI.

    Retorna (str):
        - Resposta gerada pelo modelo.
    """

    PROMPT_TEMPLATE = """
    A partir de agora você é um consultor sênior de RH da Caixa Econômica Federal (CEF). 
    Responda as perguntas baseado apenas no contexto a seguir:
    {context}
    Responda à pergunta com base no contexto acima: {question}.
    Forneça uma resposta detalhada.
    Não justifique suas respostas.
    Não forneça informações não mencionadas nas INFORMAÇÕES DE CONTEXTO.
    Não diga “de acordo com o contexto” ou “mencionado no contexto” ou similar.
    """

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)
    
    model = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=OPENAI_API_KEY)
    return model.predict(prompt)