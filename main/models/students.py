from ..extensions.database import db

class Student(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(),nullable=False)
    age=db.Column(db.Integer,nullable=False)


    def __repr__(self):
        return f"{self.name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
