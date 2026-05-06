class User:
    first_name: str
    sur_name: str
    age: int

    def __init__(self, first_name: str, sur_name: str, age: int) -> None:
        self.first_name = first_name
        self.sur_name = sur_name
        self.age = age