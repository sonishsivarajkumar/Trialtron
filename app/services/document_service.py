# app/services/document_service.py
import json
from models.document import Document

class DocumentService:
    def __init__(self, file_path="documents.json"):
        self.file_path = file_path

    def get_all_documents(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Document.from_dict(doc) for doc in data]
        except FileNotFoundError:
            return []

    def create_document(self, document):
        documents = self.get_all_documents()
        documents.append(document)
        self._save_documents(documents)

    def update_document(self, updated_document):
        documents = self.get_all_documents()
        for i, doc in enumerate(documents):
            if doc.id == updated_document.id:
                documents[i] = updated_document
                break
        self._save_documents(documents)

    def _save_documents(self, documents):
        with open(self.file_path, "w") as f:
            json.dump([doc.to_dict() for doc in documents], f, indent=2)
