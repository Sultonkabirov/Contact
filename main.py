contacts = {}


def see():
    print("1.Qoshish")
    print("2.O'zgartirish")
    print("3.Qidirish")
    print("4.O'chirish")
    print("5.Ko'rish")


def add_to_contact():
    try:
        name = input("Name: ")
        number = input("Phone number: ")
        contacts[name] = number
        print("Qushildi!!")
    except Exception as e:
        print(f"Error: {e}")


def change_contact():
    try:
        name = input("Name: ")
        number = input("Phone number: ")
        contacts[name] = number
        print("O'zgartirildi!!")
    except Exception as e:
        print(f"Error: {e}")


def find_contact():
    try:
        name = input("Name: ")
        print(name, contacts[name])
    except Exception as e:
        print(f"Error: {e}")


def remove_contact():
    try:
        name = input("Name: ")
        del (contacts[name])
        print("O'chirildi!! ")
    except Exception as e:
        print(f"Error: {e}")


def see_contacts():
    try:
        for k, v in contacts.items():
            print(k, v)
    except Exception as e:
        print(f"Error: {e}")


while True:
    see()
    num = int(input("\nTanlovni kiriting:"))
    match num:
        case 1:  add_to_contact()
        case 2:  change_contact()
        case 3:  find_contact()
        case 4:  remove_contact()
        case 5:  see_contacts()
        case _:
            print("Warning !!!")
            break
    print("\n")