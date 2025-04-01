from pydantic import BaseModel
from decimal import Decimal
from app.domain.services.premium import ServicePremium

class PremiumUseCase(BaseModel):
    def __init__(self, service_premium: ServicePremium):
        self.service_premium = service_premium

    def calculate(self, applied_rate: Decimal, broker_fee: Decimal, car_value: Decimal, deductible_percentage: Decimal) -> Decimal:
        """
        Orchestrates the calculation of the insurance premium.
        Calls the premium service to calculate the final prize.
        """
        return self.service_premium.calculate(applied_rate, broker_fee, car_value, deductible_percentage)