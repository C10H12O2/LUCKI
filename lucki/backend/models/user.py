from backend.app import db, ma
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
#Profile fields
display_name = db.Column(db.String(100))
tagline = db.Column(db.String(200))
avatar_url = db.Column(db.String(300))
