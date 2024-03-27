
print('\n')

task_list = []
complete_tasks = []

def add_task():
    # This function adds user input into the 'task_list' list
    while True:
        try:
            task = input("\nWhat would you like to add to your To-do list? Type 'done' to return to the main menu. ")
            if task.isnumeric():
                # this is checking to see if the user_input is an interger, and forcing them to type a string.
                str(task)/0
            if task == "done":
                for item in task_list:
                    print(item)
                break
            task_list.append(task)
            complete_tasks.append("No")
            print(f"\n{task} is now added to the To-do list!")
            print("Task\tCompleted?")
            for item in task_list:
                index = task_list.index(item)
                print(f'{item}\t{complete_tasks[index]}')
        except:
            print("No numbers allowed!!")

def del_task():
    # This function deletes user input from the 'task_list' list
    while True:
        try:
            print("Task\tCompleted?")
            for item in task_list:
                # This is checking to see if user input is int
                index = task_list.index(item)
                print(f"{item}\t{complete_tasks[index]}")
            task = input("\nWhat would you like to remove from your To-do list? Type 'done' to return to the main menu. ")
            if task.isnumeric():
                # this is checking to see if the user_input is an interger, and forcing them to type a string.
                str(task)/0
            if task == "done":
                for item in task_list:
                    print(item)
                break
            task_list.remove(task)
            print(f"\n{task} is now removed from the To-do list!")
        except:
            print("No numbers allowed!!")

def complete_task():
    # This function marks the task in 'complete_tasks' yes to indicate items in 'list_task' complete
    while True:
        print("Task\tCompleted?")
        for item in task_list:
            index = task_list.index(item)
            print(f"{item}\t{complete_tasks[index]}")
        user_input = input("\nWhat tasks have you completed? Type 'done' to return to the main menu. ")
        if user_input == "done":
            break
        elif user_input in task_list:
            index = task_list.index(user_input)
            complete_tasks[index] = "Yes"
            print(f"\nCongrats on completing {user_input}! We'll mark that as done. ")
        else:
            # user enters an item that's not on the list
            print("\nItem not in list.")

def view_task():
    # This function allows users to view their list
    if len(task_list) == 0:
        print("Your list is empty!")
    else:
        print(f"\nHere is your list so far!")
        print("Task\tCompleted?")
        for item in task_list:
            index = task_list.index(item)
            print(f"{item}\t{complete_tasks[index]}")



def function():
    #This is the main function
    while True:
        user_input = str(input(f"\nWelcome, {username}, to Ya Bois To-Do List Extraveganza!! \nHere you can make a To-Do List with all the things you need! \nType 'add' to add an item. \nType 'view' to view list. \nType 'done' to mark a task complete. \nType 'del' to delete an item.\nType 'quit' to quit the application. "))
        if user_input == "quit":
            if len(task_list) == 0:
                print(f"\n{username} has no open tasks.")
            else:
                print(f"\n{username}'s To-do List:\n")
                print("Task\tCompleted?")
                for item in task_list:
                    index = task_list.index(item)
                    print(f"{item}\t{complete_tasks[index]}")
            break
        elif user_input == "add":
            add_task()
        elif user_input == "view":
            view_task()
        elif user_input == "done":
            complete_task()
        elif user_input == "del":
            del_task()
        else:
            print("\nWoops! That's not a valid input. The options are 'add', 'view', 'done', del, and 'quit'")


username = input("Please enter a username: ")
if username == '':
    print("Please enter a name to start!")
else:
    function()
