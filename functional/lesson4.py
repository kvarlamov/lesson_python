from pymonad.maybe import Maybe, Just, Nothing
from pymonad.tools import curry

MAX_BIRDS_DIFF=3

# посадка птиц на левую сторону
@curry(2)
def to_left(n, pole):
    left, right = pole
    new_left = left + n
    if abs(new_left - right) > MAX_BIRDS_DIFF:
        return Nothing
    return Just((new_left, right))

# посадка птиц на правую сторону
@curry(2)
def to_right(n, pole):
    left, right = pole
    new_right = right + n
    if abs(left - new_right) > MAX_BIRDS_DIFF:
        return Nothing
    return Just((left, new_right))

# банановая кожура
def banana(pole):
    return Nothing

# отображение результата
def show(maybe, label):
    if maybe == Nothing:
        print(f"{label}. Канатоходец УПАЛ!")
    else:
        left, right = maybe.value
        print(f"{label}. Держится! Птиц слева: {left}, справа: {right}")


show(
    Just((0,0))
        .bind(to_left(2))
        .bind(to_right(5))
        .bind(to_left(-2)), # канатоходец упадёт тут
        "Тест 1: перевес справа"
)

show(
    Just((0,0))
        .bind(to_left(2))
        .bind(to_right(1))
        .bind(to_left(-1)),
    "Тест 2: Равновесие"
) # в данном случае всё ок

show(
    Just((0,0))
        .bind(to_left(2))
        .bind(banana) # кожура всё испортит
        .bind(to_right(5)), # уже упали и не вызывается
    "Тест 3: Падение на кожуре"
)