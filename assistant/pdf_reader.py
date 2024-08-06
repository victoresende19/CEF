from langchain_community.document_loaders import PyPDFLoader

def pdf_extract(DOC_PATH: str) -> list:
    """
    Extrai o texto de um documento PDF localizado no caminho especificado.

    Parametros
        - DOC_PATH (str): Caminho para o arquivo PDF do qual o texto será extraído.

    Retorna (list):
        - Lista de strings, onde cada string representa uma página do PDF.
    """

    loader = PyPDFLoader(DOC_PATH)
    return loader.load()