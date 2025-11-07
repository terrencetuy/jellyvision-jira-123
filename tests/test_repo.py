from src.repo import Repo


def test_get_owner():
    repo = Repo("owner/repo_name")
    assert repo.get_owner() == "owner"