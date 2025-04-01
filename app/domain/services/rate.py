from decimal import Decimal
from app.domain.value_objects.factor_risk import FactorRisk
from app.infra.config.settings import config

class ServiceRate:
    
    def calculate(self, car_age: int, car_value: float ) -> float:
        """
        Calculates the rate based on the age of the car and its value:
        - For each year of the car's age, it adds 0.5%.
        - For every $10,000 worth of the car, you add an additional 0.5%.
        """


        age_rate = car_age * float(config.ANNUAL_RATE)

        value_rate = (car_value // float(config.BASE_VALUE)) * float(config.RATE_PER_VALUE)

        total_rate = age_rate + value_rate
        return total_rate
