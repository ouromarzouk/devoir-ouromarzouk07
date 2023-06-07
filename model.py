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


