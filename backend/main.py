from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from risk_engine import calculate_risk

app = FastAPI(title="PAYGUARD AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    amount: float
    payee_type: str
    time_of_day: str
    urgency: str

    # Behavioral fields
    input_time: int
    pasted_upi: bool
    switch_count: int
    hesitation_score: int

@app.post("/check-transaction")
def check_transaction(tx: Transaction):
    if tx.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")

    result = calculate_risk(tx.dict())
    return result
