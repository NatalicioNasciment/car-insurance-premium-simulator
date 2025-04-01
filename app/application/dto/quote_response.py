from pydantic import BaseModel
from decimal import Decimal

class QuoteResponse(BaseModel):
    premium: Decimal
    policy_limit: Decimal
    applied_rate: Decimal