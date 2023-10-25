from langchain.document_loaders import Docx2txtLoader


def all_loaders(path: str):
    if path.endswith("docx"):
        data=Docx2txtLoader(path)
        return data.load()