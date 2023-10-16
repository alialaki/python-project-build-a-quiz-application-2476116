# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# pyquiz.py -- Main starting point of the program


class QuizApp:
    def __init__(self):
        self.username = ""

    def startup(self):
        # print the greeting at startup
        self.greeting()

        # TODO: ask the user for their name
        self.username = input("What is your user name? ")
        print(f"Wecome, {self.username}!")

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Welcome to PyQuiz! ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()

        # TODO: get the user's selection and act on it. This loop will
        # run until the user exits the app
        selection = ""
        while(True):
            selection = input("Selection? ")

            if len(selection) == 0:
                self.menu_error()
                # We don't want to break out just yet
                continue

            selection = selection.upper()
            if selection[0] == 'E':
                self.goodbye()
                break
            elif selection[0] == 'M':
                self.menu_header()
                continue
            elif selection[0] == 'L':
                print("\nAvailable Quizzes Are: ")
                #! TODO list the quizzes

    # This is the entry point to the program

    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program menu and run until the user exits
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
