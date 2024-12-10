import datetime
from .database import db
from sqlalchemy import Column, Integer, String

word_collection_association = db.Table(
    'word_collection_association',
    db.Model.metadata,
    Column('word_id', Integer, db.ForeignKey('word.id')),
    Column('collection_id', Integer, db.ForeignKey('collection.id'))
)

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    words = db.relationship('Word', secondary=word_collection_association, back_populates='collections')
    story = db.Column(db.Text)
    root = db.Column(db.String(100))

    def __repr__(self):
        return f"Collection('{self.name}')"

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.Text)
    example = db.Column(db.Text)
    root = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    collections = db.relationship('Collection', secondary=word_collection_association, back_populates='words')

    def __repr__(self):
        return f"Word('{self.word}')"

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    story = db.Column(db.Text, nullable=False)  # Markdown content
    author_name = db.Column(db.String(100), nullable=False)
    author_email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Article('{self.title}')"