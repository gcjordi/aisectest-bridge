from utils.logger import log_event

def analyze_anomaly(data):
    risk_score = 0.91
    log_event("Analysis Agent", f"Risk score: {risk_score}")
    return {"risk_score": risk_score, "verdict": "high_risk" if risk_score > 0.8 else "low_risk"}
