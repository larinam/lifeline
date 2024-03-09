from mongoengine import Document, StringField, ReferenceField, DateTimeField, EmbeddedDocument, FloatField, ListField, \
    EmbeddedDocumentField


class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(required=True)
    google_id = StringField()
    google_token = StringField()


class Scenario(EmbeddedDocument):
    description = StringField(required=True)
    probability = FloatField(required=True)


class Objective(Document):
    author = ReferenceField(User, required=True)
    title = StringField(required=True)
    description = StringField()
    target_date = DateTimeField()
    start_date = DateTimeField()
    scenarios = ListField(EmbeddedDocumentField(Scenario))
