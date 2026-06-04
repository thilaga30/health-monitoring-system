import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from typing import List, Tuple

class RAGService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
        self.vectorstore = None
        self.qa_chain = None
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=self.api_key
        )
    
    def initialize_vectorstore(self, persist_directory: str = "./chroma_db"):
        """Initialize or load existing vector store"""
        try:
            self.vectorstore = Chroma(
                embedding_function=self.embeddings,
                persist_directory=persist_directory
            )
            print(f"Loaded existing vectorstore from {persist_directory}")
        except Exception as e:
            print(f"Creating new vectorstore: {e}")
            self.vectorstore = Chroma(
                embedding_function=self.embeddings,
                persist_directory=persist_directory
            )
    
    def add_documents(self, documents: List[str], persist_directory: str = "./chroma_db"):
        """Add documents to the vector store"""
        from langchain.schema import Document
        
        # Convert strings to Document objects
        docs = [Document(page_content=doc) for doc in documents]
        
        if self.vectorstore is None:
            self.initialize_vectorstore(persist_directory)
        
        self.vectorstore.add_documents(docs)
        self.vectorstore.persist()
        print(f"Added {len(documents)} documents to vectorstore")
    
    def setup_qa_chain(self):
        """Setup the QA chain"""
        if self.vectorstore is None:
            raise ValueError("Vectorstore not initialized. Call initialize_vectorstore first.")
        
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
    
    def query(self, question: str) -> Tuple[str, List[str]]:
        """Query the RAG system"""
        if self.qa_chain is None:
            self.setup_qa_chain()
        
        result = self.qa_chain({"query": question})
        
        answer = result.get("result", "")
        sources = [doc.page_content[:100] for doc in result.get("source_documents", [])]
        
        return answer, sources
