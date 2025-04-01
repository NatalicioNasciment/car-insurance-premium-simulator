from fastapi import APIRouter, Depends
from app.presentation.controllers.quote import QuoteController
from app.application.dto.insurence import InsuranceRequest
from app.application.dto.quote_response import QuotationResponse

router = APIRouter(prefix="/quote", tags=["Quote"])

@router.post("/generate", response_model=QuotationResponse)
def generate_quote(dto: InsuranceRequest, controller: QuoteController = Depends()) -> QuotationResponse:
    return controller.generate(dto)
