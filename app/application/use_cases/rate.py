from decimal import Decimal
from domain.value_objects.factor_risk import FactorRisk
from domain.services.rate import ServiceRate

class RateUseCase:
    def __init__(self, service_rate: ServiceRate):
        self.service_rate = service_rate

    def calculate(self, factor_risk: FactorRisk) -> Decimal:
        """
        Orchestrates the calculation of the insurance rate based on the age and value of the car.   
        Calls the rate service to calculate the rate.
        """
        return self.service_rate.calculate(factor_risk)
