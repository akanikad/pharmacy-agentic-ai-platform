CLAIMS = {
    "M1001": {"claim_id": "CLM10001", "status": "paid"},
    "M1002": {"claim_id": "CLM10002", "status": "pending"},
}

def get_claim_status(member_id: str):
    return CLAIMS.get(
        member_id,
        {"claim_id": "UNKNOWN", "status": "not_found"},
    )
