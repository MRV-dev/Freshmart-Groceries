from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    full_name: str
    date_of_birth: date
    address: str
    contact_number: str
    emergency_contact: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
