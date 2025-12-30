import sched, time
import yaml
from mcstatus import JavaServer
from api import get_report, write_report, read_report


def createReport():
    report = get_report(server)
    write_report(TARGET, report)
    if report.available:
        print(f"Report created at {report.timestamp}, {report.online} players online.")
    else:
        print(f"Report created at {report.timestamp}, server unavailable")
    scheduler.enter(INTERVAL, 1, createReport)


TARGET = "localhost:25565"
INTERVAL = 60  # seconds


config = yaml.safe_load(open("config.yaml", "r"))
INTERVAL = config["interval"]
TARGET = config["target"]

server = JavaServer.lookup(TARGET)

reports = read_report(TARGET);
for report in reports:
    print(report)

scheduler = sched.scheduler(time.time, time.sleep)

scheduler.enter(1, 1, createReport)
scheduler.run()

