from pydantic import BaseModel

class InsuranceRequest(BaseModel):
    car_value: float
    car_age: int
    deductible_percentage: float
    broker_fee: float
    coverage_percentage: float = 1.0