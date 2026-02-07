def calculate_risk(tx: dict):
    """
    Calculates fraud risk using explainable rule-based logic.
    Returns risk level, numeric risk score, and reasons.
    """

    score = 0
    reasons = []

    amount = tx.get("amount", 0)
    payee_type = tx.get("payee_type", "known")
    urgency = tx.get("urgency", 0)
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
    if urgency == 1:
        score += 20
        reasons.append("Urgency or pressure detected")

    # Rule 4: Unusual transaction time
    if time_of_day == "night":
        score += 10
        reasons.append("Unusual transaction time")

    # ===== BEHAVIORAL ANALYSIS =====
    input_time = tx.get("input_time", 0)
    pasted_upi = tx.get("pasted_upi", False)
    switch_count = tx.get("switch_count", 0)
    hesitation_score = tx.get("hesitation_score", 0)

    # Rule 5: Suspiciously fast input (bot-like behavior)
    if input_time < 5 and input_time > 0:
        score += 25
        reasons.append("Suspiciously fast form completion (possible bot)")

    # Rule 6: UPI ID was pasted (common in scam scenarios)
    if pasted_upi:
        score += 15
        reasons.append("UPI ID was pasted (possibly from scam message)")

    # Rule 7: Multiple tab switches (copying from external source)
    if switch_count >= 3:
        score += 10
        reasons.append("Multiple tab switches detected")

    # Rule 8: Excessive hesitation (uncertainty or coercion)
    if hesitation_score >= 10:
        score += 10
        reasons.append("High hesitation detected (possible coercion)")

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
