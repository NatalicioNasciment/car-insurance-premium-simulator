from fastapi import APIRouter, Depends
from app.presentation.controllers.quote import QuoteController
from app.application.dto.insurence import InsuranceRequest
from app.domain.entities.quotation import Quotation
router = APIRouter(prefix="/quote", tags=["Quote"])

@router.post("/generate", response_model=Quotation)
def generate_quote(dto: InsuranceRequest, controller: QuoteController = Depends()) -> Quotation:
    return controller.generate(dto)
