from mongoengine import EmbeddedDocument, ObjectIdField, DateField, StringField, EmailField, DictField

class User(EmbeddedDocument):
    name = StringField(max_length=40,min_length=5)
    email = EmailField()
    createdAt = DateField()
    token = DictField()
    password = StringField(max_length=64)
    meta = {'collection': 'users'}