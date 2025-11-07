import requests
import json

from src.github_client import GitHubClient
from src.event_utils import EventUtils

def get_github_data_for_user():
    events = GitHubClient().get_events_for_user("terrencetuy")
    print(EventUtils.group_by_repo(events))

    repos = EventUtils.get_repos_owned_by_user(events, "terrencetuy")

