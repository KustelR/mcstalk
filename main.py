import sched, time
import yaml
from mcstatus import JavaServer
from api import getReport, writeReport


def createReport():
    report = getReport(server)
    writeReport(OUTPUT_FILE, TARGET, report)
    if report.available:
        print(f"Report created at {report.timestamp}, {report.online} players online.")
    else:
        print(f"Report created at {report.timestamp}, server unavailable")
    scheduler.enter(INTERVAL, 1, createReport)


TARGET = "localhost:25565"
OUTPUT_FILE = "report"
INTERVAL = 60  # seconds


config = yaml.safe_load(open("config.yaml", "r"))
OUTPUT_FILE = config["output"]
INTERVAL = config["interval"]
TARGET = config["target"]

server = JavaServer.lookup(TARGET)
scheduler = sched.scheduler(time.time, time.sleep)

scheduler.enter(1, 1, createReport)
scheduler.run()
