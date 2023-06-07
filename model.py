from typing import List

from pydantic import BaseModel
from re import match

class Vehicle(BaseModel):
    registration: str
    category: str
    owner: str
    quotation: float


class BillItem(BaseModel):
    registration: str
    quotation: float
    surcharge: float
    total: float
@app.get("/bills/{owner}")
async def get_bill_for_owner(owner: str) -> Bill:
    bill = next(bill for bill in bills if bill.owner == owner)
    
    # Calculate bill items
    for vehicle in vehicles:
        if vehicle.owner == owner:
            surcharge = vehicle.quotation * 0.1  # 10% surcharge
            total = vehicle.quotation + surcharge
            item = BillItem(registration=vehicle.registration, quotation=vehicle.quotation, surcharge=surcharge, total=total)
            bill.items.append(item)
            bill.total += total
    
    return bill
class Vehicle(BaseModel):
    registration: str
    category: str
    owner: str
    quotation: float
    
    @validator("registration")
    def validate_registration(cls, value: str) -> str:
        pattern = r"^[A-Z]{2}-\d{3}-[A-Z]{2}$"
        if not match(pattern, value):
            raise ValueError("Invalid registration number")
        return value

