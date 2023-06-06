def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')


    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def find_by_name(data:list, lastname: str) -> str:
    for el in data:
        if el.get("Фамилия") == lastname:
            return el.get("Телефон")
    return "Такой абонент отсутствует"

def find_by_number(data: list, phonenumber: str) -> str:
    for el in data:
        if el.get("Телефон") == phonenumber:
            return f'{el.get("Фамилия")},{el.get("Имя")}'
    return "Такой абонент отсутствует"

def add_user(data:list, user: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user.split(',')))
    data.append(record)

def print_result(data: list):
    print(data)

def get_search_name():
    return input('Введите фамилию: ')

def get_search_number():
    return input('Введите номер телефона: ')

def get_new_user():
    return input('Введите фамилию, имя, номер телефона и описание через запятую: ')

def get_file_name():
    return input('Введите название файла: ')

work_with_phonebook()