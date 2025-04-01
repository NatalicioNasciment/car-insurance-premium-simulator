from fastapi import Depends
from decimal import Decimal
from pydantic import BaseModel
from app.domain.value_objects.factor_risk import FactorRisk
from app.domain.entities.quotation import Quotation
from app.domain.services.rate import ServiceRate
from app.domain.services.premium import ServicePremium
from app.domain.services.policy import ServicePolicy

class ServiceQuote:

    def __init__(self, service_policy: ServicePolicy = Depends(), service_premium: ServicePremium = Depends(), service_rate: ServiceRate = Depends()):
        self.service_rate = service_rate
        self.service_premium = service_premium
        self.service_policy = service_policy

    def generate(self, broker_fee: Decimal, car_age: int,  car_value: Decimal, deductible_percentage: Decimal, coverage_percentage: Decimal) -> Quotation:
        
        applied_rate = self.service_rate.calculate(car_age, car_value)

        final_premium = self.service_premium.calculate(applied_rate, broker_fee, car_value, deductible_percentage)

        final_policy_limit = self.service_policy.calculate_policy_limit(car_value, coverage_percentage, deductible_percentage)

        return  Quotation(applied_rate=applied_rate, policy_limit=final_policy_limit, premium=final_premium)

