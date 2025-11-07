from src.event import Event
from src.repo import Repo


def group_by_repo(events: list[Event]) -> dict[str, list[Event]]:
    grouped_events:dict[str, list[Event]] = {}
    for event in events:
        if not event.repo.name in grouped_events:
            grouped_events[event.repo.name] = []
        grouped_events[event.repo.name].append(event)
    return grouped_events

def get_event_type_counts(events: list[Event]) -> dict[str, int]:
    counts:dict[str, int] = {}
    for event in events:
        if event.type in counts:
            counts[event.type] += 1
        else:
            counts[event.type] = 1
    
    return counts
    

def get_repos_owned_by_user(events: list[Event], username: str) -> set[Repo]:
    repos = [event.repo for event in events if event.repo.get_owner() == username]
            
    return set(repos)
    
    
