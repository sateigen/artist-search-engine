def ask_user():
    print("Please choose from the following options.")
    print("1. View the Artist Database")
    print("2. Add a row to the Artist Database")
    print("3. Search the Artist Database")
    response = input("What would you like to do? Type 1, 2, or 3 ")
    if int(response) in [1, 2, 3]:
        return int(response)
    else:
        print("\nThat was not a valid input. \n")
        ask_user()


def view_database():
        


def main():
    if ask_user == 1:
        view_database()


if __name__ == '__main__':
    main()
