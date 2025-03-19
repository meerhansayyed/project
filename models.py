
from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    parent_contact = db.Column(db.String(15), nullable=False)
    qr_code_id = db.Column(db.String(100), unique=True, nullable=True)
    points = db.Column(db.Integer, default=0)
    streak = db.Column(db.Integer, default=0)
    voiceprint = db.Column(db.LargeBinary, nullable=True)
