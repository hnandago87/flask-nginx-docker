from mongoengine import Document, DateTimeField,ListField,PointField, EmbeddedDocumentField

from src.models.users import User

class Location(Document):
    userId = EmbeddedDocumentField(User)
    location = ListField(PointField())
    createdAt = DateTimeField(required=True)
    meta = {'collection': 'locations'}