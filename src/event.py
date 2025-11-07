from src.repo import Repo


class Event:
    def __init__(self, type: str, repo: Repo) -> None:
        self.type=type
        self.repo=repo
        
