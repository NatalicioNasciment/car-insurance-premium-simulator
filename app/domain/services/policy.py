from decimal import Decimal

class ServicePolicy:
    """ Service responsible for calculating the insurance policy limit. """

    def calculate_policy_limit(self, car_value: Decimal, coverage_percentage: Decimal, deductible_percentage: Decimal) -> Decimal:
        base_policy_limit = self._calculate_base_policy_limit(car_value, coverage_percentage)
        deductible_value = self._calculate_deductible_value(base_policy_limit, deductible_percentage)
        final_policy_limit = base_policy_limit - deductible_value
        return final_policy_limit
    
    def _calculate_base_policy_limit(self, car_value: Decimal, coverage_percentage: Decimal):
        return car_value * coverage_percentage

    def _calculate_deductible_value(self, base_policy_limit: Decimal, deductible_percentage: Decimal) -> Decimal:
        return base_policy_limit * deductible_percentage
    

