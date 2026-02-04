from risk_engine import calculate_risk

tx = {
    "amount": 25000,
    "new_payee": 1,
    "urgent": 1,
    "time_of_day": "night"
}

print(calculate_risk(tx))
