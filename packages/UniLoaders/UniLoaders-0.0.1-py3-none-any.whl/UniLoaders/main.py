

from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import UnstructuredPowerPointLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders.image import UnstructuredImageLoader


def all_loaders(path_or_url: str):
    filters = ["https", "http", "docx", "ppt", "pdf", "jpg", "png"]
    for string not in filters:
        return "TypeError"
    if "https" or "http" in path_or_url:
        url = [path_or_url]
        loader = UnstructuredURLLoader(urls=url)
        data = loader.load()
        return data
    
    if "docx" in path_or_url:
        loader = Docx2txtLoader(path_or_url)
        data = loader.load()
        return data

    if "ppt" in path_or_url:
        loader = UnstructuredPowerPointLoader(path_or_url)
        data = loader.load()
        return data
    
    if "pdf" in path_or_url:
        loader = PyPDFLoader(path_or_url)
        data = loader.load()
        return data
    
    if "jpg" or "png" in path_or_url:
        loader = UnstructuredImageLoader(path_or_url, mode="elements")
        data = loader.load()
        return data
