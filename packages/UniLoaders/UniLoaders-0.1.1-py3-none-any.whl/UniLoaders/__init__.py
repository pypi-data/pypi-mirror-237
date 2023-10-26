from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import UnstructuredPowerPointLoader
from langchain.document_loaders import unstructuredURLLoader


def all_loaders(path: str):
    if path.endswith("docx"):
        data=Docx2txtLoader(path)
        return data.load()
    
    if path.endswith("pdf"):
        data=UnstructuredPDFLoader(path)
        return data.load()
    
    if path.endswith("ppt"):
        data=UnstructuredPowerPointLoader(path)
        return data.load()
    
    if "https" in path:
        urls = [path]
        loader=unstructuredURLLoader
        return data.load()