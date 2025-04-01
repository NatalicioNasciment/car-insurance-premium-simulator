from decimal import Decimal
from pydantic import BaseModel
from datetime import datetime


class FactorRisk(BaseModel):
    value : Decimal
    year : int

    def calculate_age_car(self):
        current_year = datetime.now().year
        age = current_year - self.year
        return age

    class Config:
        frozen = True