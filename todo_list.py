def add_a_task(task_number, task_text):
    task_list[task_number] = task_text

def add_a_completed_task(task_number):

    if task_number not in completed_tasks:
        completed_tasks.add(task_number) 
        print("You added a task.")
    else:
        print("This task has already been completed.")


def delete_a_task(task_number):
    if task_number in task_list:
        task_list.pop(task_number)
    else:
        print("Invalid task number.")


menu = """
Welcome to the To Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Show completed tasks
5. Delete a task
6. Quit

"""
task_list = {}
completed_tasks = set()
task_number = 1  # Initialize the task number counter
completed_task_number = 1

while True:
    print(menu)
    user_choice = int(input("What would you like to do? "))
    if user_choice == 1:
        task = input("Enter your task: ")
        add_a_task(task_number, task)  # Add task number along with the task
        task_number += 1  # Increment task number
    elif user_choice == 2:
         if task_list == {}:
             print("Your task list is empty.")
         else:
            print("Your tasks are:")
         for task_num, task in task_list.items():
            print(f"{task_num}. {task}")
    elif user_choice == 3:
        completed_task = int(input("Enter the task number you completed: "))
        add_a_completed_task(completed_task)
        completed_task_number += 1
    elif user_choice == 4:
        print("Your completed tasks are: ")
        for completed_task in completed_tasks:
            print(completed_task, task_list[completed_task])
    elif user_choice == 5:
        task_number_to_delete = int(input("Enter the task number you want to delete: "))
        delete_a_task(task_number_to_delete)
        print('You deleted a task.')
    else:
        break




    