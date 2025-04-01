from decimal import Decimal
from app.domain.value_objects.factor_risk import FactorRisk


class ServicePremium:

    def calculate(self, applied_rate: Decimal, broker_fee: Decimal,  car_value: Decimal, deductible_percentage: Decimal) -> Decimal:
        base_premium  = self._calculate_base_premium(car_value, applied_rate)
        deductible_discount = self._calculate_deductible_discount(base_premium, deductible_percentage)
        final_premium = base_premium - deductible_discount + broker_fee
        return final_premium

    def _calculate_base_premium(self, car_value: Decimal, applied_rate: Decimal) -> Decimal: 
        return car_value * applied_rate

    def _calculate_deductible_discount(self, base_premium: Decimal, deductible_percentage: Decimal) -> Decimal:
        return base_premium * deductible_percentage
