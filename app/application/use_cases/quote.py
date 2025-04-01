from decimal import Decimal
from app.domain.services.quote import ServiceQuote
from pydantic import BaseModel
from fastapi import Depends
from app.domain.entities.quotation import Quotation
from app.application.dto.insurence import InsuranceRequest


class QuoteUseCase:
    def __init__(self, service_quote: ServiceQuote =  Depends()):
        self.service_quote = service_quote

    def generate(self, dto: InsuranceRequest) -> Quotation:
        """
        Orchestrates the calculation of the insurance premium.
        Calls the premium service to calculate the final prize.
        """
        result = self.service_quote.generate(
            broker_fee=dto.broker_fee,
            car_age=dto.car_age,
            car_value=dto.car_value,
            deductible_percentage=dto.deductible_percentage,
            coverage_percentage=dto.coverage_percentage
        )
        
        return result