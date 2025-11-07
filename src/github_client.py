import requests

from src.event import Event
from src.repo import Repo


class GitHubClient:

    def __init__(self) -> None:
       self.base_url = "https://api.github.com/" 
       
    def get_events_for_user(self, username: str) -> list[Event]:
        r = requests.get(f"https://api.github.com/users/{username}/events")
        return [Event(event["type"], Repo(event["repo"]["name"])) for event in r.json()]
        
