from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from risk_engine import calculate_risk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    amount: float
    new_payee: int
    time_of_day: str
    urgent: int

@app.post("/check-transaction")
def check_transaction(tx: Transaction):
    risk_level, reasons = calculate_risk(tx.dict())
    return {"risk_level": risk_level, "reasons": reasons}
