from flask_sqlalchemy import SQLalchemy
db = SQLalchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True, nullable=False)
    slug = db.Column(db.String(255),unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(255))

    def __repr__(self):
        return f'<book {self.id} {self.name}'

    def serializer(self):
        return {
            'id':self.id,
            'name':self.name,
            'slug':self.slug,
            'price':self.price,
            'image':self.image,
        }
