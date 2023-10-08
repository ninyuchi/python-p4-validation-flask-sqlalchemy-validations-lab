from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())    

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    @validates('name')
    def validate_name(self, key, name):
        names = db.session.query(Author.name).all()
        if not name:
            raise ValueError("Name field is required.")
        elif name in names:
            raise ValueError("Name must be unique.")
        return name 

    @validates('phone_number')
    def validate_phone_number(self, key, address):
        if len(address) != 10:
            raise ValueError("Phone number must be 10 digits")
        return address

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, address):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in address for substring in clickbait):
            raise ValueError("No clickbait found")
        return address

    @validates('content')
    def validate_content(self, key, address):
        if len(address) < 250:
            raise ValueError("failed content length validation")
        return address

    @validates('summary')
    def validate_summary(self, key, address):
        if len(address) >= 250:
            raise ValueError("failed summary length validation")
        return address

    @validates('category')
    def validate_category(self, key, address):
        if address != 'Fiction' and address != 'Non-Fiction':
            raise ValueError("failed category validation")
        return address


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'