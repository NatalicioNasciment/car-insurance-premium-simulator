from pydantic import BaseModel
from decimal import Decimal

class PolicyLimitResponse(BaseModel):
    final_policy_limit: Decimal
