def calculate_risk(tx: dict):
    """
    Calculates fraud risk for a transaction using explainable rules.
    Returns risk level and reasons.
    """

    score = 0
    reasons = []

    # Rule 1: High transaction amount
    if tx.get("amount", 0) >= 10000:
        score += 40
        reasons.append("High transaction amount")

    # Rule 2: First-time payee
    if tx.get("new_payee") == 1:
        score += 30
        reasons.append("Payment to a new payee")

    # Rule 3: Urgency or pressure signal
    if tx.get("urgent") == 1:
        score += 20
        reasons.append("Urgency or pressure detected")

    # Rule 4: Unusual time of transaction
    if tx.get("time_of_day") == "night":
        score += 10
        reasons.append("Unusual transaction time")

    risk_score = min(score, 100)

    # Final risk decision
    if risk_score >= 70:
        risk_level = "HIGH"
    elif score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return risk_level, reasons
