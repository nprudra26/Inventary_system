from . import db

class OfficeStationary(db.Model):
    __tablename__ = 'office_stationary'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    activation_date = db.Column(db.Date, nullable=True)
    expiry_date = db.Column(db.Date, nullable=True)
    mail_id = db.Column(db.String(50), nullable=True)
    warranty_years = db.Column(db.Integer, nullable=False)
    make_in = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<OfficeStationary {self.product_name} ({self.make_in})>"
