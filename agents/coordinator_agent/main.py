from agents.monitor_agent.monitor import monitor_activity
from agents.analysis_agent.analyze import analyze_anomaly
from agents.response_agent.respond import take_action

def run():
    anomaly = monitor_activity()
    analysis = analyze_anomaly(anomaly)
    take_action(analysis)

if __name__ == '__main__':
    run()
