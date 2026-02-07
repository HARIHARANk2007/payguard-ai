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
    amount: int
    payee_type: str              # "known" or "new"
    time_of_day: str             # "day" or "night"
    urgency: int                 # 0 or 1
    # Behavioral signals
    input_time: int = 0          # seconds spent filling the form
    pasted_upi: bool = False     # True if UPI was pasted
    switch_count: int = 0        # number of tab switches
    hesitation_score: int = 0    # number of backspaces

@app.post("/check-transaction")
def check_transaction(tx: Transaction):
    if tx.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")

    result = calculate_risk(tx.dict())
    return result
