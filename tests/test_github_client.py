from src.github_client import GitHubClient

# todo: patch with mock request
def test_get_events_for_valid_user():
    ghc = GitHubClient()
    events = ghc.get_events_for_user("terrencetuy")
    assert len(events) == 7
    
# todo: test for invalid user

