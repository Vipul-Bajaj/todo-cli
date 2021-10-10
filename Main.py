from modules.TodoList import TodoList
from modules.TodoListChecker import checker
import threading

# This is a sample intended application of the to-do cli

if __name__ == "__main__":

    while True:
        command = input("Enter Command ('help' to list all commands, 'exit' "
                "to close) : ").lower()

        if command == "exit":
            exit()

        if command == "help":
            print("\nAvailable Commands:", end='\n\n')
            print("'add' - prompts for information about the task and adds it "
                "to the to-do list")
            print("'view' - displays all to-do list items")
            print("'help' - displays this dialogue", end='\n\n')
            exit()

        t= TodoList()

        if command in ("add", "a"):
            task = input("Enter Title of Todo: ")
            description = input("Enter Description of Todo: ")
            try:
                deadline = float(input("Enter Deadline in minutes "
                    "(leave blank if not setting one): " ))
                t.add_todo(task, description, deadline)
            except ValueError:
                t.add_todo(task, description)
            finally:
                print()

        t = TodoList()
        # This will be done via interactive CLI (WIP)
        t.add_todo(
            task='Wash Dishes',
            description="Don't forget to use Vim bar also",
            minute_deadline_offset=1.5)

        t.add_todo(
            task='Hang Clothes',
            description="Also install new hanging rope",
            minute_deadline_offset=0.5)

        t.add_todo(
            task='Run Washing Machine',
            description="Also use Comfort in the end",
            minute_deadline_offset=1)

        # multithreading used here st it doesn't interfere with Future to-do Insertion
        t1 = threading.Thread(target=checker, args=(t,), name='t1')
        # this makes the thread auto close when the parent thread closes
        t1.setDaemon(True)
        t1.start()
