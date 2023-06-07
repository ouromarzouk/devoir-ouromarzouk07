from fastapi import FastAPI
from typing import List
from .models import Vehicle, Bill


app = FastAPI()

# Dummy data
vehicles = [
    Vehicle(registration="AA-111-AA", category="car", owner="Sister Mary", quotation=1000.0),
    Vehicle(registration="BB-222-BB", category="motorcycle", owner="Convent of Saint Clare", quotation=500.0),
    Vehicle(registration="CC-333-CC", category="car", owner="Sister Agatha", quotation=1500.0),
    Vehicle(registration="DD-444-DD", category="motorcycle", owner="Sister Teresa", quotation=800.0),
]

bills = [
    Bill(owner="Sister Mary", items=[], total=0.0),
    Bill(owner="Convent of Saint Clare", items=[], total=0.0),
    Bill(owner="Sister Agatha", items=[], total=0.0),
    Bill(owner="Sister Teresa", items=[], total=0.0)
]
