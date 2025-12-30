from datetime import datetime


class Report:
    def __init__(self, timestamp: datetime, players: list[str], available: bool, online: int):
        self.timestamp = timestamp
        self.players = players
        self.available = available
        self.online = online

    def __str__(self):
        if self.available:
            return f"Report(timestamp={self.timestamp}, players={self.players}, online={self.online})"
        else:
            return f"Report(At {self.timestamp} server was unavailable)"
        

    def get_writable(self):
        if not self.available:
            return [f"{self.timestamp} UNAVAILABLE"]
        
        return [self.timestamp, self.online, ", ".join(self.players)]
    

    timestamp: datetime
    available: bool
    players: list[str]
    online: int