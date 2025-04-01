from pydantic import BaseModel

class Quotation(BaseModel):
    applied_rate: float
    policy_limit: float
    premium: float