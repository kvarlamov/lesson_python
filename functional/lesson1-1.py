from pymonad.tools import curry

# part 1
@curry(2)
def concat(a: str, b: str) -> str:
    return a + b

greet = concat("Hello, ")

print(greet("World"))
print(greet("Petya"))

# part 2
@curry(4)
def make_greeting(firstword: str, comma: str, name: str, end: str) -> str:
    return f"{firstword}{comma} {name}{end}"

first_step = make_greeting("Hello")(",")
final = first_step("!") 


result = final("Petya")
print(result) # Hello, Petya!