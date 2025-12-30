import csv
from os import mkdir
from datetime import datetime, UTC
from dateutil.parser import parse
from mcstatus import JavaServer
from mcstatus.responses import JavaStatusResponse

from Report import Report


def get_player_list(status: JavaStatusResponse) -> list[str]:
    if status.players.sample is None:
        return []

    return list(map(lambda player:  player.name, status.players.sample))


def get_online(status: JavaStatusResponse) -> int:
    return status.players.online

def get_report(server: JavaServer) -> Report:
    timestamp = datetime.now(UTC)
    availability = True
    status: JavaStatusResponse = None
    online: int = 0
    players: list[str] = []

    try:
        status = server.status()
        players = get_player_list(status)
        online = get_online(status)
    except Exception as e:
        availability = False
        print(f"During report collection exception was caught: {e}")
    
    return Report(timestamp, players, availability, online)

def write_report(target: str, report: Report):
    try:
        mkdir("./reports")
    except FileExistsError:
        pass

    with open(f"./reports/{target.replace(":", "")}.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(report.get_writable())

def deserialize_report(serialized: list[str]) -> Report:
    report: Report
    if (len(serialized) == 1):
        report = Report(parse(serialized[0].replace(" UNAVAILABLE", "")), [], False, 0)
    else:
        report = Report(parse(serialized[0]), serialized[2:], True, int(serialized[1]))
    return report


def read_report(target: str) -> list[Report]:
    result: list[Report] = []
    try:
        with open(f"./reports/{target.replace(":", "")}.csv", "r", newline="") as file:
            reader = csv.reader(file)
            result = list(map(lambda row: deserialize_report(row), list(reader))) #
    except FileNotFoundError:
        print(f"Reports of {target} were not found")

    return result