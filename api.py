import csv
from os import mkdir
from datetime import datetime, UTC
from mcstatus import JavaServer
from mcstatus.responses import JavaStatusResponse

from Report import Report


def get_player_list(status: JavaStatusResponse) -> list[str]:
    return list(map(lambda player:  player.name, status.players.sample))


def get_online(status: JavaStatusResponse) -> int:
    return status.players.online

def getReport(server: JavaServer) -> Report:
    timestamp = datetime.now(UTC)

    status = server.status()
    players = get_player_list(status)
    online = get_online(status)
    return Report(timestamp, players, online)

def writeReport(output_file: str, target: str, report: Report):
    try:
        mkdir("./reports")
    except FileExistsError:
        pass

    with open(f"./reports/{output_file}_{target.replace(":", "")}", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([str(report.timestamp), *report.players])