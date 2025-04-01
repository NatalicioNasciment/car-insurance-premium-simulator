from pydantic import BaseModel


class CarDetails(BaseModel):
    make: str
    model: str
    year: int
    value: float

class InsuranceRequest(BaseModel):
    car: CarDetails
    broker_fee: float
    coverage_percentage: float = 1.0
    deductible_percentage: float