def calculate_risk(tx: dict):
    """
    Calculates fraud risk using explainable rule-based logic.
    Returns risk level, numeric risk score, and reasons.
    """

    score = 0
    reasons = []

    amount = tx.get("amount", 0)
    payee_type = tx.get("payee_type", "known")
    urgency = tx.get("urgency", "no")
    time_of_day = tx.get("time_of_day", "day")

    # Rule 1: High transaction amount
    if amount >= 10000:
        score += 40
        reasons.append("High transaction amount")

    # Rule 2: New / first-time payee
    if payee_type == "new":
        score += 30
        reasons.append("Payment to a new payee")

    # Rule 3: Urgency or pressure
    if urgency == "yes":
        score += 20
        reasons.append("Urgency or pressure detected")

    # Rule 4: Unusual transaction time
    if time_of_day == "night":
        score += 10
        reasons.append("Unusual transaction time")

    # ===== BEHAVIORAL BIOMETRICS RULES =====
    input_time = tx.get("input_time", 0)
    pasted_upi = tx.get("pasted_upi", False)
    switch_count = tx.get("switch_count", 0)
    hesitation_score = tx.get("hesitation_score", 0)

    # Rule 5: UPI ID was pasted (common scam pattern)
    if pasted_upi:
        score += 25
        reasons.append("UPI ID was pasted — common scam pattern")

    # Rule 6: Fast confirmation (less than 3 seconds)
    if input_time < 3 and input_time > 0:
        score += 15
        reasons.append("Fast confirmation suggests urgency or pressure")

    # Rule 7: Multiple app/tab switches (suspicious behavior)
    if switch_count > 2:
        score += 15
        reasons.append("User switched apps multiple times — suspicious behavior")

    # Rule 8: Hesitation detected during input
    if hesitation_score > 5:
        score += 10
        reasons.append("Hesitation detected during input")

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
