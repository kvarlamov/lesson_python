from pymonad.tools import curry
from pymonad.maybe import Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

add10 = add(10)

# Примеры
just = Just(1).map(add10)
print(f"{just}")  # Just 11

nothing = Nothing.map(add10)
print(f"{nothing}")  # Nothing

list = ListMonad(1, 2, 3, 4).map(add10)
print(f"{list}")  # [11, 12, 13, 14]