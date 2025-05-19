from utils.logger import log_event

def take_action(analysis):
    if analysis["verdict"] == "high_risk":
        log_event("Response Agent", "Triggering AWS Lambda to lock account")
    else:
        log_event("Response Agent", "Recording event in DynamoDB")
