'''Задача:
Напишите 4 переменных которые буду обозначать следующие данные:
Количество выполненных ДЗ (запишите значение 12)
Количество затраченных часов (запишите значение 1.5)
Название курса (запишите значение 'Python')
Время на одно задание (вычислить используя 1 и 2 переменные)
Выведите на экран(в консоль), используя переменные, следующую строку:
Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.'''

exercises_completed = 12
hours_spent = 1.5
course_name = 'Python'
average_time_per_exercise = hours_spent / exercises_completed
print(f'Курс: {course_name}, всего задач: {exercises_completed}, затрачено часов: {hours_spent}, среднее время выполнения {average_time_per_exercise} часа.')
