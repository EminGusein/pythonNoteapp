import menuTemplates as m

def menu_console():
        m.printNenuTitle("ЖУРНАЛ ЗАМЕТОК")
        print("1 - Вывод журнала \n2 - Вывод заметки по id \n3 - Выбор заметки по дате\n4 - Редактировать заметку"
              " \n5 - Добавить заметку\n6 - Удалить заметку\n7 - Выход")
        m.printMenuLine()
        print("\nВведите пункт из меню: ")