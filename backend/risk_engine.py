def calculate_risk(tx: dict):
    """
    Calculates fraud risk using explainable rule-based logic.
    Returns risk level, numeric risk score, and reasons.
    """

    score = 0
    reasons = []

    amount = tx.get("amount", 0)
    new_payee = tx.get("new_payee", 0)
    urgent = tx.get("urgent", 0)
    time_of_day = tx.get("time_of_day", "day")
    rapid_tx = tx.get("rapid_transactions", 0)  # simulated signal

    # Rule 1: High transaction amount
    if amount >= 10000:
        score += 40
        reasons.append("High transaction amount")

    # Rule 2: New / first-time payee
    if new_payee == 1:
        score += 30
        reasons.append("Payment to a new payee")

    # Rule 3: Urgency or pressure
    if urgent == 1:
        score += 20
        reasons.append("Urgency or pressure detected")

    # Rule 4: Unusual transaction time
    if time_of_day == "night":
        score += 10
        reasons.append("Unusual transaction time")

    # Rule 5: Multiple transactions in short time (simulated)
    if rapid_tx == 1:
        score += 15
        reasons.append("Multiple transactions in a short time")

    # Cap score at 100
    risk_score = min(score, 100)

    # Risk level mapping
    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "reasons": reasons
    }
