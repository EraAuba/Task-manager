import datetime as dt
import calendar
from tkinter import * 
from tkinter import ttk

# списки приоритетов где сохраняются задачи по приоритету
important = []
notImportant = []
useless = []

# добавление задачи
def add_task_to_list(name_entry, tasks_table, priority_combo, day_entry):
    '''Бұл функция словарьді списокқа қосады, осы жерде словарь бізде бір задача,
    ал список болса, задачалардың қосындысы'''
    task = {}
    now = dt.datetime.now()

    # имя задачи и описание его
    taskname = name_entry.get()
    priority = priority_combo.get()

    # выбрать дедлайн из календаря
    now_ded = dt.datetime.now()
    year = now_ded.year
    month = now_ded.month
    day = int(day_entry.get())

    # если дата дедлайна старая чем дата создания проверка
    if day>=now_ded.day: 
        if priority == 'маңызды':
            task['аты'] = taskname
            task['приоритет'] = priority
            task['дата'] = now.strftime("%d-%m-%Y")
            task['дедлайн'] = '{}-{}-{}'.format(day, month, year)
            important.append(task)
            # обновляем Listbox
            tasks_table.insert("", "end", values=(
                task['аты'],
                task['приоритет'],
                task['дедлайн']
            ))
            return important
        elif priority == 'маңызды емес':
            task['аты'] = taskname
            task['приоритет'] = priority
            task['дата'] = now.strftime("%d-%m-%Y")
            task['дедлайн'] = '{}-{}-{}'.format(day, month, year)
            notImportant.append(task)
            # обновляем Listbox
            tasks_table.insert("", "end", values=(
                task['аты'],
                task['приоритет'],
                task['дедлайн']
            ))
            return notImportant
        elif priority == 'керек жоқ':
            task['аты'] = taskname
            task['приоритет'] = priority
            task['дата'] = now.strftime("%d-%m-%Y")
            task['дедлайн'] = '{}-{}-{}'.format(day, month, year)
            useless.append(task)
            # обновляем Listbox
            tasks_table.insert("", "end", values=(
                task['аты'],
                task['приоритет'],
                task['дедлайн']
            ))
            return useless
        else:
            print('Приоритетті дұрыс енгізіңіз!')
    else:
        print('Дедлайн датасы ескі болмау керек')

def change_task(tasks_table, name_entry, priority_combo, day_entry):

    selected = tasks_table.selection()
    if not selected:
        return

    item = tasks_table.item(selected)
    old_values = item["values"]

    new_name = name_entry.get()
    new_priority = priority_combo.get()
    new_day = day_entry.get()

    # если пусто — оставляем старое
    if not new_name:
        new_name = old_values[0]

    if not new_priority:
        new_priority = old_values[1]

    if not new_day:
        new_deadline = old_values[2]
    else:
        now = dt.datetime.now()
        new_deadline = f"{new_day}-{now.month}-{now.year}"

    # обновляем строку в таблице
    tasks_table.item(selected, values=(
        new_name,
        new_priority,
        new_deadline
    ))

def delete_task(tasks_table):
    selected = tasks_table.selection()

    if not selected:
        return

    tasks_table.delete(selected)

def main():
    root = Tk()
    root.title('Task-manager')
    root.geometry('270x350')
    
    label = ttk.Label(root, text='Тапсырмалар')
    label.grid(row=0, column=0, columnspan=3, sticky="ew")

    # поле ввода
    name_entry = ttk.Entry(root)
    name_entry.grid(row=1, column=0, sticky="ew")

    priority_combo = ttk.Combobox(
        root,
        values=['маңызды', 'маңызды емес', 'керек жоқ']
    )
    priority_combo.grid(row=1, column=1, sticky="ew")

    day_entry = ttk.Entry(root)
    day_entry.grid(row=1, column=2, sticky="ew")

    # список задач
    columns = ("name", "priority", "deadline")

    tasks_table = ttk.Treeview(root, columns=columns, show="headings")

    tasks_table.heading("name", text="Аты")
    tasks_table.heading("priority", text="Приоритет")
    tasks_table.heading("deadline", text="Дедлайн")

    tasks_table.column("name", anchor="center")
    tasks_table.column("priority", anchor="center")
    tasks_table.column("deadline", anchor="center")

    tasks_table.grid(row=2, column=0, columnspan=3, sticky="nsew")

    # делаем строки и колонки растягиваемыми
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(2, weight=1)

    # кнопки
    btn_delete = ttk.Button(root, text="Удалить", command=lambda: delete_task(tasks_table))
    btn_delete.grid(row=3, column=0, sticky="ew")

    btn_add = ttk.Button(
        root,
        text="Добавить",
        command=lambda: add_task_to_list(
            name_entry,
            tasks_table,
            priority_combo,
            day_entry
        )
    )
    btn_add.grid(row=3, column=1, sticky="ew")

    btn_edit = ttk.Button(root, text="Редактировать", command=lambda: change_task(
        tasks_table,
        name_entry,
        priority_combo,
        day_entry
    ))
    btn_edit.grid(row=3, column=2, sticky="ew")
    root.mainloop()

if __name__=='__main__':
    main()











