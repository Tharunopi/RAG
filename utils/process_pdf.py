from typing import Optional
from langchain_community.document_loaders import PDFMinerLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
import tempfile

class processPDF():
    def __init__(self, embedding_model:CohereEmbeddings):
        self.__embedding_model = embedding_model

    def load_pdf(self, pdf) -> Optional[list]:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(pdf.read())
                tmp_pdf_path = tmp_file.name
                pdf_loader = PDFMinerLoader(tmp_pdf_path)
                pdf_load = pdf_loader.load()
                print(f"load_pdf: PDF loaded {tmp_pdf_path}")
                return pdf_load

        except Exception as e:
            print(f"load_pdf: {e}")
            return None

    def pdf_splitter(self, single_docs:list) -> Optional[list]:
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            splitted_pdf = splitter.split_documents(single_docs)
            page_content = [i.page_content for i in splitted_pdf]
            return page_content

        except Exception as e:
            print(f"pdf_splitter: {e}")
            return None
        
    def convert_to_embeddings(self, splitted_docs:list) -> Optional[list]:
        try:
            result = self.__embedding_model.embed_documents(splitted_docs)
            return result

        except Exception as e:
            print(f"convert_to_embeddings: {e}")
            return None
        
    def pdf_to_embeddings(self, pdf) -> Optional[list]:
        try:
            loaded_pdf = self.load_pdf(pdf)
            splitted_pdf = self.pdf_splitter(loaded_pdf)
            final_embeddings = self.convert_to_embeddings(splitted_pdf)
            return final_embeddings, splitted_pdf
        
        except Exception as e:
            print(f"pdf_to_embeddings: {e}")
            return None