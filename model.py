from typing import List

from pydantic import BaseModel


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


c@apps.get("/category/{category}")
async def get_vehicles_by_category(category: str) -> List[Vehicle]:
    return [vehicle for vehicle in vehicles if vehicle.category == category]


@APPEND.get("/owner/{owner}")
async def get_vehicles_by_owner(owner: str) -> List[Vehicle]:
    return [vehicle for vehicle in vehicles if vehicle.owner == owner]



@APPENDS.get("/bills/{owner}")
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