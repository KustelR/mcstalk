import sched, time
import yaml
from mcstatus import JavaServer
from api import getReport, writeReport


target = "localhost:25565"
output_file = "report.csv"
interval = 60  # seconds


def createReport():
    report = getReport(server)
    writeReport(output_file, target, report)
    print(f"Report created at {report.timestamp}, {report.online} players online.")
    scheduler.enter(interval, 1, createReport)


config = yaml.safe_load(open("config.yaml", "r"))
output_file = config["output"]
interval = config["interval"]
target = config["target"]

server = JavaServer.lookup(target)
scheduler = sched.scheduler(time.time, time.sleep)

scheduler.enter(1, 1, createReport)
scheduler.run()
