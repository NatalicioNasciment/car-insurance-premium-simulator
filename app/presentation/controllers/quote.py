from fastapi import HTTPException, Depends
from app.application.use_cases.quote import QuoteUseCase
from app.application.dto.insurence import InsuranceRequest

class QuoteController:
    def __init__(self, use_case: QuoteUseCase = Depends()):
        self.use_case = use_case

    def generate(self, dto: InsuranceRequest):
        try:
            quote = self.use_case.generate(dto)
            return quote
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))