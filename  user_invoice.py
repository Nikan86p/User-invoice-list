import os,time,string


def delete() :
    os.system("cls" if os.name == "nt" else "clear")


def int_check() :
    while True :
        age=input("Enter employee's age (int): ").strip()

        try:
            age=int(age) 
            
            if age<=0 or age>110:
                delete()
                print("Please enter a valid age!!")
                time.sleep(1)
                delete()
            else:
                break
            
            

        except ValueError:
            delete()
            print("Please write a valid number!!")
            time.sleep(1)
            delete()

    return age


def string_check(srt):
    invalids=string.punctuation +"0123456789"

    while True:
        str = input(f"Enter employee's {srt}:").capitalize().strip()

        if any(char in invalids for char in str):
            delete()
            print(f"=== PLEASE ENTER {srt} WITHOUT PUNCTUATION OR NUMBERS ===")
            time.sleep(1)
            delete()

            continue
        else:
            break
    return str


def main():

    delete ()
    list1 = [] 

    print ("***** Hello Welcome *****\n")

    counter=0
    while True:

        x = int(input('Type 1️⃣  for Adding user...\nType 2️⃣  for Showing users...\nType 3️⃣  for Exit...\n\n: '))

        delete()

        if x == 1:

            counter+=1
            delete ()
            name = string_check(srt="NAME")
            delete()
            age = int_check()
            delete()
            occupation = string_check(srt="OCCUPATION")

            list1.append({"user": counter,"name": name, "age": age, "occupation": occupation})
            delete()

            print(f"\n{name}'s user has been added successfully.")
            time.sleep(1.5)
            delete()



        elif x == 2:
            delete ()

            if not list1:
                print("No information stored yet\n\n")
                time.sleep(2)
                delete()

            else:
                #print(list1)
                print("_____________ list _____________")
                print("User\tName\tAge\tOccupation")
                for a in list1:
                    print(f"\n{a['user']}\t{a['name']}\t{a['age']}\t{a['occupation']}")
                    print("_______________________________\n")

        elif x == 3:
            delete ()

            break

        else:
            delete ()

            print("Choose something that exists!!!")

if __name__=="__main__":
    main()