from app import app, db
from models import Student

with app.app_context():
    student1 = Student(name="meerhan munshi", parent_contact="9892690119", qr_code_id="QR123")
    student2 = Student(name="chaitali dhaije", parent_contact="8767920896", qr_code_id="QR124")
    
    db.session.add(student1)
    db.session.add(student2)
    db.session.commit()
    
    print("Data added successfully!")
