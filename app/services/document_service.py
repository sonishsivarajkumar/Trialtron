# app/services/document_service.py
import json
from models.document import Document
from config import settings

class DocumentService:
    def __init__(self):
        self.data_file = settings.DATA_FILE

    def get_all_documents(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return [Document(**doc) for doc in data]
        except FileNotFoundError:
            return []

    def create_document(self, document: Document):
        documents = self.get_all_documents()
        document.id = str(len(documents) + 1)
        documents.append(document)
        self._save_documents(documents)

    def update_document(self, document: Document):
        documents = self.get_all_documents()
        for i, doc in enumerate(documents):
            if doc.id == document.id:
                documents[i] = document
                break
        self._save_documents(documents)

    def _save_documents(self, documents):
        with open(self.data_file, 'w') as f:
            json.dump([doc.dict() for doc in documents], f)
