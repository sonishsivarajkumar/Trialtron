# app/models/document.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from uuid import uuid4

class Document(BaseModel):
    id: Optional[str] = None
    title: str
    content: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    version: int = 1
    comments: List[str] = []

class Document:
    def __init__(self, title, content, id=None, created_at=None, updated_at=None):
        self.id = id or str(uuid4())
        self.title = title
        self.content = content
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"])
        )
