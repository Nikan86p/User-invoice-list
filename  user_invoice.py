import os, time, string


def delete():
    os.system("cls" if os.name == "nt" else "clear")


def animation(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.06)


def int_check():
    while True:
        animation("Enter employee's age (int): ")
        age = input("").strip()

        try:
            age = int(age)

            if age <= 0 or age > 110:
                delete()
                animation("Please enter a valid age!!")
                time.sleep(1)
                delete()
            else:
                break

        except ValueError:
            delete()
            animation("Please write a valid number!!")
            time.sleep(1)
            delete()

    return age


def string_check(srt):
    invalids = string.punctuation + "0123456789"

    while True:
        animation("Enter employee's")
        str = input(f" {srt}: ").capitalize().strip()

        if not str:
            delete()
            animation(f"=== {srt} CANNOT BE EMPTY!!! ===")
            time.sleep(1)
            delete()
            continue

        if any(char in invalids for char in str):
            delete()
            animation(f"=== PLEASE ENTER {srt} WITHOUT PUNCTUATION OR NUMBERS ===")
            time.sleep(1)
            delete()

            continue
        else:
            break
    return str


def main():

    delete()
    list1 = []

    animation("***** Hello Welcome *****\n")

    counter = 0
    while True:

        try:
            y = [1, 2, 3]
            animation(
                "Type (1) for ...Adding user...\nType (2) for ...Showing users...\nType (3) for ...Exit...\n\n"
            )
            x = int(input(":"))
            if x not in y:
                delete()
                animation("Please enter a valid number(1-3)!!!")
                time.sleep(1)

        except ValueError:
            delete()
            animation("Please enter a valid number!!!")
            time.sleep(1)
            delete()
            continue

        delete()

        if x == 1:

            counter += 1
            delete()
            name = string_check(srt="NAME")
            delete()
            last_name = string_check(srt="LAST NAME")
            delete()
            age = int_check()
            delete()
            occupation = string_check(srt="OCCUPATION")
            delete()
            animation("Enter employee's EMAIL: ")
            gmail = input("")

            list1.append(
                {
                    "user": counter,
                    "name": name,
                    "last": last_name,
                    "age": age,
                    "occupation": occupation,
                    "email": gmail,
                }
            )
            delete()

            animation(f"\n{name}'s user has been added successfully!!!")
            time.sleep(1.5)
            delete()

        elif x == 2:
            delete()

            if not list1:
                animation("No information stored yet!!!!\n\n")
                time.sleep(2)
                delete()

            else:
                # print(list1)
                print(
                    "____________________________________________ list _____________________________________________"
                )
                print("User\tName\tLast-name\tAge\tOccupation\t\tEmail-Address")
                for a in list1:
                    print(
                        f"\n{a['user']}\t{a['name']}\t{a['last']}\t{a['age']}\t{a['occupation']}\t\t{a['email']}"
                    )
                    print(
                        "_______________________________________________________________________________________________\n"
                    )

        elif x == 3:
            delete()

            break


if __name__ == "__main__":
    main()
