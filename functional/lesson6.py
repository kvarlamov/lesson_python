## ДЛЯ САМОСТОЯТЕЛЬНОГО РЕШЕНИЯ ЗАДАЧИ НЕ ХВАТИЛО НАВЫКОВ PYTHON и ФП, РЕШАЛ С ПОМОЩЬЮ llm


from pymonad.tools import curry
from pymonad.state import State
import itertools


def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    total_cells = N * M

    # ───────────────────────────────────────────
    # ШАГ 1: Начальная расстановка
    # Парсим battalion в неизменяемое множество координат
    # ───────────────────────────────────────────
    initial_captured = frozenset(
        map(lambda i: (battalion[i * 2], battalion[i * 2 + 1]), range(L))
    )

    # ───────────────────────────────────────────
    # Вспомогательная функция: соседи клетки в пределах поля N×M
    # @curry(2) — карринг позволяет зафиксировать границы поля заранее
    # ───────────────────────────────────────────
    @curry(2)
    def get_neighbors(bounds, pos):
        n, m = bounds
        x, y = pos
        return frozenset(filter(
            lambda p: 1 <= p[0] <= n and 1 <= p[1] <= m,
            [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        ))

    # Фиксируем размеры поля один раз
    cell_neighbors = get_neighbors((N, M))

    # ───────────────────────────────────────────
    # ШАГ 2: Моделирование одного дня захвата — монада State
    #
    # Монада State(run):  run :: day -> (new_captured, new_day)
    #   • значение монады  = frozenset захваченных клеток
    #   • состояние монады = счётчик дней
    #
    # chain.from_iterable(map(cell_neighbors, captured))
    #   — разворачивает соседей всех клеток в один плоский итератор
    # ───────────────────────────────────────────
    def conquest_step(captured):
        def run(day):
            new_captured = captured | frozenset(
                itertools.chain.from_iterable(
                    map(cell_neighbors, captured)
                )
            )
            return new_captured, day + 1

        return State(run)

    # ───────────────────────────────────────────
    # ШАГ 3: «whileTrue» — функциональный аналог условного цикла
    #
    # itertools.repeat(None)     — бесконечная последовательность «тиков»
    # itertools.accumulate(...)  — применяет шаг симуляции к каждому тику,
    #                              накапливая (captured, day)
    #
    # Это семантически эквивалентно хвостовой рекурсии:
    #   loop(state) = if done(state) then state else loop(step(state))
    # ───────────────────────────────────────────
    conquest_states = itertools.accumulate(
        itertools.repeat(None),
        lambda state, _: conquest_step(state[0]).run(state[1]),
        initial=(initial_captured, 1)   # день 1 — высадка десанта
    )

    # ───────────────────────────────────────────
    # ПРОВЕРКА НА ОКОНЧАНИЕ
    # filter ищет первое состояние, где захвачены все клетки поля
    # ───────────────────────────────────────────
    return next(filter(
        lambda state: len(state[0]) == total_cells,
        conquest_states
    ))[1]   # [1] — возвращаем номер дня


# ═══════════════════════════════════════════════
# Тесты
# ═══════════════════════════════════════════════

# Пример из условия задачи
r1 = ConquestCampaign(3, 4, 2, [2, 2, 3, 4])
print(f"Тест 1 — N=3, M=4, старт (2,2),(3,4):  день {r1}  (ожидается 3)")

# Поле 1×1 — захвачено сразу в день 1
r2 = ConquestCampaign(1, 1, 1, [1, 1])
print(f"Тест 2 — N=1, M=1, старт (1,1):         день {r2}  (ожидается 1)")

# Поле 3×3, старт из угла (1,1) — BFS расходится 5 ходов
r3 = ConquestCampaign(3, 3, 1, [1, 1])
print(f"Тест 3 — N=3, M=3, старт (1,1):         день {r3}  (ожидается 5)")

# Поле 5×5, старт из центра (3,3)
r4 = ConquestCampaign(5, 5, 1, [3, 3])
print(f"Тест 4 — N=5, M=5, старт (3,3):         день {r4}  (ожидается 3)")

# Дублирование координат не ломает логику
r5 = ConquestCampaign(3, 4, 3, [2, 2, 3, 4, 2, 2])
print(f"Тест 5 — дублированные координаты:      день {r5}  (ожидается 3)")