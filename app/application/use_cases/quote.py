from fastapi import Depends
from app.domain.services.quote import ServiceQuote
from app.application.dto.quote_response import QuotationResponse
from app.application.dto.insurence import InsuranceRequest


class QuoteUseCase:
    def __init__(self, service_quote: ServiceQuote =  Depends()):
        self.service_quote = service_quote

    def generate(self, dto: InsuranceRequest) -> QuotationResponse:
        """
        Orchestrates the calculation of the insurance premium.
        Calls the premium service to calculate the final prize.
        """
        result = self.service_quote.generate(
            broker_fee=dto.broker_fee,
            car=dto.car,
            deductible_percentage=dto.deductible_percentage,
            coverage_percentage=dto.coverage_percentage
        )
        
        return result