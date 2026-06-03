from pymonad.tools import curry

@curry(2)
def concat(a: str, b: str) -> str:
    return a + b

greet = concat("Hello, ")

print(greet("World"))
print(greet("Petya"))