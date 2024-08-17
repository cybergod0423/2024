from . import db


class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    # Add a comment or a new field to trigger schema change
    comment = db.Column(db.String(100))

    def to_json(self):
        return {
            'isbn': self.isbn,
            'author': self.author,
            'title': self.title,
            'price': self.price
        }
