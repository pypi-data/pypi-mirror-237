from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import UnstructuredPDFLoader


def all_loaders(path: str):
    if path.endswith("docx"):
        data=Docx2txtLoader(path)
        return data.load()
    
    if path.endswith("pdf"):
        data=UnstructuredPDFLoader(path, mode='elements')
        return data.load()