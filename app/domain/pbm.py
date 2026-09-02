from dataclasses import dataclass
from enum import Enum

class ClaimStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    REJECTED = "rejected"

@dataclass(frozen=True)
class Member:
    member_id: str
    plan_id: str

@dataclass(frozen=True)
class Claim:
    claim_id: str
    member_id: str
    status: ClaimStatus
