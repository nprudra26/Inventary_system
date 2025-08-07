from . import db

class Repair(db.Model):
    __tablename__ = 'repair'

    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String(50))
    emp_name = db.Column(db.String(100))
    device_id = db.Column(db.String(50))
    outward_date = db.Column(db.Date, nullable=True)
    inward_date = db.Column(db.Date, nullable=True)
    purpose_of_repair = db.Column(db.Text)
    client_name = db.Column(db.String(100))

    def __repr__(self):
        return f"<Repair {self.device_type} - {self.device_id}>"
