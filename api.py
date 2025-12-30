import csv
from os import mkdir
from datetime import datetime, UTC
from mcstatus import JavaServer
from mcstatus.responses import JavaStatusResponse

from Report import Report


def get_player_list(status: JavaStatusResponse) -> list[str]:
    if status.players.sample is None:
        return []

    return list(map(lambda player:  player.name, status.players.sample))


def get_online(status: JavaStatusResponse) -> int:
    return status.players.online

def getReport(server: JavaServer) -> Report:
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

def writeReport(output_file: str, target: str, report: Report):
    try:
        mkdir("./reports")
    except FileExistsError:
        pass

    with open(f"./reports/{output_file}_{target.replace(":", "")}.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(report.get_writable())