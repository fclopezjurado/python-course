import re

REG_EXP_FOR_STRING = r"^.+$"
REG_EXP_FOR_PHONE_NUMBER = r"^\+?(6\d{2}|7[1-9]\d{1})\d{6}$"
REG_EXP_FOR_MAIL = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$"
REG_EXP_FOR_DATES = (r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1["
                     r"6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|["
                     r"13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?["
                     r"1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
REG_EXPR_FOR_SPANISH_ID = r"^[0-9]{8}[A-Z]$"
REG_EXPR_FOR_BOOLEANS = r"^(yes|no)$"
YES = "yes"

clients = {}


def add_client():
    surname = take_input_value(str, "Enter the client's surname: ")

    if not is_valid_value(REG_EXP_FOR_STRING, surname):
        print("Invalid surname!")
        return

    name = take_input_value(str, "Enter the client's name: ")

    if not is_valid_value(REG_EXP_FOR_STRING, name):
        print("Invalid name!")
        return

    address = take_input_value(str, "Enter the client's address: ")

    if not is_valid_value(REG_EXP_FOR_STRING, address):
        print("Invalid address!")
        return

    phone = take_input_value(str, "Enter the client's phone number: ")

    if not is_valid_value(REG_EXP_FOR_PHONE_NUMBER, phone):
        print("Invalid phone number!")
        return

    email = take_input_value(str, "Enter the client's email: ")

    if not is_valid_value(REG_EXP_FOR_MAIL, email):
        print("Invalid email!")
        return

    spanish_id = take_input_value(str, "Enter the client's ID: ")

    if not is_valid_value(REG_EXPR_FOR_SPANISH_ID, spanish_id):
        print("Invalid ID!")
        return

    regular_client = take_input_value(str, "Is the client a regular client? (yes/no): ")

    if not is_valid_value(REG_EXPR_FOR_BOOLEANS, regular_client):
        print("Invalid boolean expression!")
        return

    regular_client = regular_client == YES
    created_at = take_input_value(str, "Enter the date when the client was created (dd/mm/yyyy): ")

    if not is_valid_value(REG_EXP_FOR_DATES, created_at):
        print("Invalid created at date!")
        return

    clients[spanish_id] = {"surname": surname, "name": name, "address": address, "phone": phone, "email": email,
                           "regular_client": regular_client, "created_at": created_at}

    print("Client added successfully!")


def delete_client():
    spanish_id = take_input_value(str, "Enter the client's ID: ")

    if not is_valid_value(REG_EXPR_FOR_SPANISH_ID, spanish_id):
        print("Invalid ID!")
        return

    if spanish_id not in clients:
        print("Client not found!")
        return

    del clients[spanish_id]
    print("Client deleted!")


def print_client():
    spanish_id = take_input_value(str, "Enter the client's ID: ")

    if not is_valid_value(REG_EXPR_FOR_SPANISH_ID, spanish_id):
        print("Invalid ID!")
        return

    if spanish_id not in clients:
        print("Client not found!")
        return

    print(clients[spanish_id])


def print_clients():
    print(clients)


def print_regular_clients():
    for spanish_id, client in clients.items():
        if client["regular_client"]:
            print("\"{0}\": {1}".format(spanish_id, client))


def run_sixth_option():
    print("You chose the sixth option!")


def execute_menu():
    exit_menu = False

    while not exit_menu:
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Option 5")
        print("6. Exit")

        option = take_input_value(int, "Choose an option: ")

        if option == 1:
            add_client()
        elif option == 2:
            delete_client()
        elif option == 3:
            print_client()
        elif option == 4:
            print_clients()
        elif option == 5:
            print_regular_clients()
        elif option == 6:
            run_sixth_option()
            exit_menu = True
        else:
            print("Invalid option!")


def take_input_value(data_type, message):
    try:
        return data_type(input(message))
    except ValueError:
        return None


def is_valid_value(reg_exp, value):
    return value is not None and bool(re.match(reg_exp, value))


execute_menu()
