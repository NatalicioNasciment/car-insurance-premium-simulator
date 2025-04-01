from pydantic import BaseModel
from app.application.dto.insurence import CarDetails

class QuotationResponse(BaseModel):
    car_details: CarDetails
    applied_rate: float
    calculated_premium : float
    deductible_value: float
    policy_limit: float