from yc import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    founders = db.relationship('Founder', backref='company', lazy=True)


    def __repr__(self):
        return f"Company('{self.name}')"


class Founder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    twitter = db.Column(db.String(200), unique=False, nullable=True)
    linkedin = db.Column(db.String(200), unique=False, nullable=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
