class Repo:
    def __init__(self, name: str) -> None:
        self.name = name

    # operating under the assumption that the owner is the first part of the name
    def get_owner(self) -> str:
        return self.name.split("/")[0]
