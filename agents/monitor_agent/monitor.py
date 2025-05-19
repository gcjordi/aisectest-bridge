from utils.logger import log_event

def monitor_activity():
    log_event("Monitor Agent", "Suspicious login pattern detected from unusual device")
    return {"anomaly": True, "details": "Login from unrecognized device, high location variance"}
