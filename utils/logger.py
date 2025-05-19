from datetime import datetime

def log_event(agent, message):
    print(f"[{datetime.utcnow()}] [{agent}] {message}")
