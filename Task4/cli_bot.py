# Декоратор для обробки можливих помилок вводу
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Give me name and phone please."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid number of arguments."
    return inner

# Розбирає введення користувача на команду та аргументи
def parse_input(user_input):
    cmd, *args = user_input.split()  # Розділяє введення на команду та аргументи
    cmd = cmd.strip().lower()  # Очищує команду від пробілів та переводить у нижній регістр
    return cmd, *args  # Повертає команду та аргументи

# Додає контакт до списку контактів
@input_error
def add_contact(args, contacts):
    name, phone = args # Розпаковує аргументи на ім'я та телефон
    contacts[name] = phone # Додає контакт до словника
    return "Contact added."

# Змінює контакт у списку контактів
@input_error
def change_contact(args, contacts):
    name, phone = args # Розпаковує аргументи на ім'я та телефон
    if name in contacts:
        contacts[name] = phone # Оновлює телефон контакту
        return "Contact updated."
    else:
        return "Contact not found."
    
# Показує телефонний номер контакту
@input_error
def show_phone(args, contacts):
    name = args[0] # Отримує ім'я контакту з аргументів
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# Показує всі контакти
def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])# Формує рядок з усіма контактами
    else:
        return "No contacts."

def main():
    contacts = {}  # Ініціалізація словника для зберігання контактів

    while True:  # Нескінченний цикл для обробки команд користувача
        input_string = input('\n'+"Enter a command => ").strip().lower()  # Зчитування та обробка введення користувача
        try:
            command, *args = parse_input(input_string)  # Розбір введення на команду та аргументи
        except ValueError:  # Якщо виникає помилка при розборі, продовжуємо цикл
            continue
        if command in ["exit", "close"]:  # Якщо команда на вихід, завершуємо програму
            print("Goodbye!")
            break
        elif command == "hello":  # Обробка команди привітання
            print("How can I help you?")
        elif command == "add":  # Додавання нового контакту
            print(add_contact(args, contacts))
        elif command == "change":  # Зміна існуючого контакту
            print(change_contact(args, contacts))
        elif command == "phone":  # Показ телефонного номера контакту
            print(show_phone(args, contacts))
        elif command == "all":  # Виведення всіх контактів
            print(show_all(contacts))
        else:  # Якщо команда не відома
            print("Invalid command.")

if __name__ == "__main__":
    main()  # Запуск головної функції програми