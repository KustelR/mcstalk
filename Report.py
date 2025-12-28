from datetime import datetime


class Report:
    def __init__(self, timestamp: datetime, players: list[str], online: int):
        self.timestamp = timestamp
        self.players = players
        self.online = online

    def __str__(self):
        return f"Report(timestamp={self.timestamp}, players={self.players}, online={self.online})"
    timestamp: datetime
    players: list[str]