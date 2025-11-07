from src.app import get_github_data_for_user

def test_add():
    print(get_github_data_for_user())
    assert 1 + 1 == 3