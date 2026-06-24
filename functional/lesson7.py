
from functools import reduce

def second_max(lst):
    # result = (1max, 2max)
    result = reduce(
        lambda acc,x: (x, acc[0]) if x >= acc[0] else (acc[0], x) if acc[1] is None or x > acc[1] else acc,
        lst[1:],
        (lst[0], None)
    )
    return result[1]

# проверка:
print(second_max([5, 4, 3, 2, 5]))
print(second_max([3, 1, 4, 1, 5, 9, 2, 6]))
print(second_max([1, 2, 3]))