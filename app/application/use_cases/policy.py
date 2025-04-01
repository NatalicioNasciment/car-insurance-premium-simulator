from decimal import Decimal
from domain.services.policy import ServicePolicy

class PolicyUseCase:
    def __init__(self, service_policy: ServicePolicy):
        self.service_policy = service_policy

    def calculate_policy_limit(self, car_value: Decimal, coverage_percentage: Decimal, deductible_percentage: Decimal) -> Decimal:
        """
        Orchestrates the calculation of the policy limit.
        Calls the policy service to calculate the final policy limit.
        """
        return self.service_policy.calculate_policy_limit(car_value, coverage_percentage, deductible_percentage)
