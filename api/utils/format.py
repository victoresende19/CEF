import re

def extract_question(text):
    """Função para extrair o texto após a palavra 'Question'."""
    match = re.search(r"Question:\s*(.*)", text)
    return match.group(1).strip() if match else text

def format_chat_history(chat_history, docs):
    """
    Formata o histórico de conversas em uma estrutura adequada.

    Parâmetros
    ----------
    chat_history : list
        Lista de mensagens que contém o histórico da conversa. Cada mensagem é um objeto 
        que tem o papel ('user' ou 'assistant') e o conteúdo.

    Retorna
    -------
    list
        Uma lista de dicionários formatados, onde cada dicionário contém a mensagem 
        do usuário ('human') e a resposta da IA ('ia'), além do datetime da mensagem.
    """

    formatted_history = []
    for i in range(0, len(chat_history), 2):
        raw_human_message = chat_history[i].content if i < len(chat_history) else ""
        human_message = extract_question(raw_human_message)
        ai_message = chat_history[i + 1].content if i + 1 < len(chat_history) else ""
        formatted_history.append({
            "human": human_message,
            "ia": ai_message
        })
    return formatted_history

def format_docs(docs):
    """
    Formata os documentos recuperados concatenando o conteúdo das páginas em uma única string.

    Parâmetros
    ----------
    docs : list
        Lista de objetos de documentos, onde cada documento tem 
        um conteúdo da página ('page_content').

    Retorna
    -------
    str
        Uma string concatenando o conteúdo das páginas dos documentos recuperados.
    """

    return "\n\n".join(doc.page_content for doc in docs)