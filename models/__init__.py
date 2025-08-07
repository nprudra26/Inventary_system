# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .employee import Employee
from .repair import Repair
from .office_stationary import OfficeStationary
