import psycopg2


def ask_user():
    print("Please choose from the following options.")
    print("1. View the Artist Database")
    print("2. Add a row to the Artist Database")
    print("3. Search the Artist Database")
    response = input("What would you like to do? Type 1, 2, or 3 ")
    if response in ['1', '2', '3']:
        return int(response)
    else:
        print("\nThat was not a valid input. \n")
        ask_user()


def view_database(cur):
    cur.execute("SELECT * FROM artists;")
    for row in cur:
        print("Artist: {}, Title of Piece: {}, Year: {}, Medium: {}, Subject: {}, Collection: {}\n".format(row[1], row[2], row[3], row[4], row[5], row[6]))


def add_row(cur):
    pass


def main():
    conn = psycopg2.connect("dbname=artists user=shannon")
    cur = conn.cursor()
    user_choice = ask_user()
    if user_choice == 1:
        view_database(cur)
    if user_choice == 2:
        add_row(cur)
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
