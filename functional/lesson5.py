from pymonad.tools import curry
from pymonad.state import State

free_hours = 40
sprint_init = {'completed': [], 'hours': 0}

# бэклог зада спринта - название: часы
backlog = {
    'Реализовать api': 16,
    'Согласовать архитектуру': 5,
    'Code review': 4,
    'Экспорт истории для заказчика': 16
}

sprint_state = State.insert(sprint_init['completed'])

@curry(2)
def complete_task(task_name, completed_tasks):
    def calculate_hours(spend_hours):
        return completed_tasks + [task_name], spend_hours + backlog[task_name]
    return State(calculate_hours)

process_sprint = sprint_state.then(complete_task('Реализовать api')).then(complete_task('Согласовать архитектуру')).then(complete_task('Code review')).then(complete_task('Экспорт истории для заказчика'))

result = process_sprint.run(sprint_init['hours'])
completed, hours = result
print(f"выполненные задачи: {completed}, потрачено времени: {hours} из {free_hours} (остаток: {free_hours-hours})")