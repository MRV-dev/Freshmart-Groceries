from sqlalchemy import Column, Integer, String, Date
from database.db import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    emergency_contact = Column(String, nullable=False)
