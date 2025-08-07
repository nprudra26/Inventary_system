# models/employee.py
from . import db

class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(50), nullable=False)
    handover_date = db.Column(db.Date, nullable=True)
    model_name = db.Column(db.String(50), nullable=True)
    laptop_name = db.Column(db.String(50), nullable=True)
    processor = db.Column(db.String(50), nullable=True)
    windows = db.Column(db.String(50), nullable=True)
    ssd = db.Column(db.String(20), nullable=True)
    ram = db.Column(db.String(20), nullable=True)
    device_id = db.Column(db.String(50), nullable=True)
    product_serial_no = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=True)
    hostname = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    dlp = db.Column(db.String(20), nullable=True)
    option_type = db.Column(db.String(10), nullable=False, default='New')

    def __repr__(self):
        return f"<Employee {self.emp_name}>"
