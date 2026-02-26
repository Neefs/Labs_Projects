

class Foo:
    def __init__(self, name: str, profession: str) -> None:
        self.name = name
        self.profession = profession

    def speak(self) -> str:
        return self.name + " says hello!"
    
    def __repr__(self):
        return f"Foo({self.name}, {self.profession})"