from datetime import datetime
def write_diary():
    entry = input("Enter your diary entry here:")
    today = datetime.today()

    with open("diary.txt" , "a") as f:
        f.write(entry +"\n")
        f.write(f"\n{today}\n")
        f.write("-"*30)
        

        print("Diary saved!")


def read_diary():

    try:
        with open("diary.txt" , "r") as s:
            print("\n---Your Diary---")
            print(s.read())
    except FileNotFoundError:
        print("No diary entries found")
while True:
    print("\n Personal Diary")
    print("1) Write diary")
    print("2) Read diary")
    print("3) Exit")
    choice = int(input("Enter a choice to read or write (1 or 2):"))

    if choice == 1:
        write_diary()
    elif choice == 2:
        read_diary()
    elif choice == 3:
        print("Bye Bye")
        break
    else:
        print("invalid choice")
