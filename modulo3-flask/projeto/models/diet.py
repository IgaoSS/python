from database import db
from datetime import datetime

class Diet(db.Model):
    def __init__(self, name, description, date_time, is_on_diet=False, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.date_time = date_time
        self.is_on_diet = is_on_diet
    
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date_time': self.date_time.strftime("%d/%m/%Y %H:%M") if self.date_time else None,
            'is_on_diet': self.is_on_diet
        }

    # id (int), name (string), description (string), datetime (datetime), isOnDiet (boolean)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    is_on_diet = db.Column(db.Boolean, default=False)

