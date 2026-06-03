from pymonad.tools import curry

@curry(4)
def make_greeting(firstword: str, comma: str, name: str, end: str) -> str:
    return f"{firstword}{comma} {name}{end}"

first_step = make_greeting("Hello")(",")
final = first_step("!") 


result = final("Petya")
print(result) # Hello, Petya!