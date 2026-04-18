import datetime as dt
import calendar
from tkinter import * 
from tkinter import ttk

# список всех задач
tasks = []

# списки приоритетов где сохраняются задачи по приоритету
important = []
notImportant = []
useless = []

# добавление задачи
def add_task_to_list():
    '''Бұл функция словарьді списокқа қосады, осы жерде словарь бізде бір задача,
    ал список болса, задачалардың қосындысы'''
    task = {}
    now = dt.datetime.now()

    # имя задачи и описание его
    taskname = input('Тапсырманың атын енгіз: ')
    priority = input('Тапсырма қандай приоритетте (маңызды, маңызды емес, керек жоқ): ')

    # выбрать дедлайн из календаря
    now_ded = dt.datetime.now()
    year = now_ded.year
    month = now_ded.month
    print(calendar.month(year, month))
    day = int(input("Дедлайн күнін еңгізініз: "))

    # если дата дедлайна старая чем дата создания проверка
    if day>=now_ded.day: 
        if priority == 'маңызды':
            task['аты'] = taskname
            task['приоритет'] = priority
            task['дата'] = now.strftime("%d-%m-%Y")
            task['дедлайн'] = '{}-{}-{}'.format(day, month, year)
            important.append(task)
            return important
        elif priority == 'маңызды емес':
            task['аты'] = taskname
            task['приоритет'] = priority
            task['дата'] = now.strftime("%d-%m-%Y")
            task['дедлайн'] = '{}-{}-{}'.format(day, month, year)
            notImportant.append(task)
            return notImportant
        elif priority == 'керек жоқ':
            task['аты'] = taskname
            task['приоритет'] = priority
            task['дата'] = now.strftime("%d-%m-%Y")
            task['дедлайн'] = '{}-{}-{}'.format(day, month, year)
            useless.append(task)
            return useless
        else:
            print('Приоритетті дұрыс енгізіңіз!')
    else:
        print('Дедлайн датасы ескі болмау керек')

# быстрая сортировка
def quick_sort(arr, key):
    """Тез сұрыптау алгоритмі"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][key]  # выбираем опорный элемент (середина)
    left = [x for x in arr if x[key] < pivot]   # элементы меньше опорного
    middle = [x for x in arr if x[key] == pivot]  # равные опорному
    right = [x for x in arr if x[key] > pivot]  # элементы больше опорного
    return quick_sort(left, key) + middle + quick_sort(right, key)

# найти нужную задачу
def find_task(name):
    # находим нужную задачу
    for sublist in tasks:
        for task in sublist:
            if task['аты'] == name:
                return task
    return 'Ондай тапсырма жоқ'

# удаление из старого списка приоритета
def del_old_task(task, new_priority):
    for sublist in tasks:
        if task in sublist:
            sublist.remove(task)
    
    # добавить в новый
    if new_priority == 'маңызды':
        important.append(task)
    elif new_priority == 'маңызды емес':
        notImportant.append(task)
    elif new_priority == 'керек жоқ':
        useless.append(task)

# редактирование задач
def change_task():
    """Тапсырманың атын, датасын, приоритетін өзгерту"""
    print(' ')
    print('Тапсырманың тізімдері:')
    for i in tasks:
        print(i)

    name = input('Қандай атты тапсырманы өзгертесін? ')
    task = find_task(name)

    new_name = input("Жаңа ат (Enter если не менять): ")
    new_priority = input("Жаңа приоритет: ")

    now_ded = dt.datetime.now()
    year = now_ded.year
    month = now_ded.month
    print(calendar.month(year, month))
    new_ded = input("Жаңа дедлайн күні: ")

    if new_name:
        task['аты'] = new_name
    if new_priority:
        del_old_task(task, new_priority)
        task['приоритет'] = new_priority
    if new_ded:
        task['дедлайн'] = '{}-{}-{}'.format(new_ded, month, year)

# удаление задач 
def delete():
    """Тапсырманың атын толығымен жою"""
    print(' ')
    print('Тапсырманың тізімдері:')
    for i in tasks:
        print(i)

    name = input('Қандай атты тапсырманы өшіресіз? ')
    task = find_task(name)

    new_priority = ''
    del_old_task(task, new_priority)

def main():
    root = Tk()
    root.title('Task-manager')
    root.geometry('270x350')
    
    tasks.append(important)
    tasks.append(notImportant)
    tasks.append(useless)

    for i in range(len(tasks)):
        tasks[i] = quick_sort(tasks[i], 'аты')

    print(' ')
    print('Тапсырманың тізімдері:')
    for i in tasks:
        print(i)

    label = ttk.Label(text='Тапсырмалар')
    label.grid(row=0, column=1)

    # интерфейс показывающая список задач
    tasks_var = Variable(value=important)
    tasks_listbox = Listbox(listvariable=tasks_var)
    tasks_listbox.grid(row=1, columnspan=3)

    root.columnconfigure(index=1, weight=1)
    btn = ttk.Button(text="Удалить", command=delete) # кнопка удаление в интерфейсе
    btn.grid(row=2, column=0, ipadx=6, ipady=6, sticky="W")

    root.columnconfigure(index=2, weight=1)
    btn = ttk.Button(text="Добавить", command=add_task_to_list) # кнопка добавление в интерфейсе
    btn.grid(row=2, column=1, ipadx=6, ipady=6)

    root.columnconfigure(index=3, weight=1)
    btn = ttk.Button(text="Редактировать", command=change_task) # кнопка редактирование в интерфейсе
    btn.grid(row=2, column=2, ipadx=6, ipady=6, sticky="E")

    root.mainloop()

if __name__=='__main__':
    main()











