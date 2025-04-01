from fastapi import Depends
from decimal import Decimal
from app.domain.services.rate import ServiceRate
from app.domain.services.premium import ServicePremium
from app.domain.services.policy import ServicePolicy
from app.application.dto.insurence import CarDetails
from app.application.dto.quote_response import QuotationResponse

class ServiceQuote:

    def __init__(self, service_policy: ServicePolicy = Depends(), service_premium: ServicePremium = Depends(), service_rate: ServiceRate = Depends()):
        self.service_rate = service_rate
        self.service_premium = service_premium
        self.service_policy = service_policy

    def generate(self, broker_fee: Decimal, car: CarDetails, deductible_percentage: Decimal, coverage_percentage: Decimal) -> QuotationResponse:
        
        applied_rate = self.service_rate.calculate(car.year, car.value)

        calculated_premium, deductible_value = self.service_premium.calculate(applied_rate, broker_fee, car.value, deductible_percentage)

        final_policy_limit = self.service_policy.calculate_policy_limit(car.value, coverage_percentage, deductible_percentage)

        return  QuotationResponse(car_details=car, applied_rate=applied_rate, deductible_value= deductible_value,  calculated_premium=calculated_premium, policy_limit=final_policy_limit,)

