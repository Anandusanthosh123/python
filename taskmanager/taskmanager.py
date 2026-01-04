
tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1.View Tasks")
    print("2.Add Tasks")
    print("3.Delete Tasks")
    print("4.Exit")
    
    
def view_tasks():
    if not tasks:
        print("No tasks yet !")
    else:
        print("\n  Your Tasks:")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}. {task}")
          
          
def add_tasks():
      task = input("Enter a new task: ")
      tasks.append(task)
      print(f"Task '{task}' added!")
      
def delete_task():
    view_tasks()                
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num -1)
        print(f"Task '{removed}' deleted! ")
    except(ValueError,IndexError):
        print("Invalid task number!")
 # main loop
while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
           print("Goodbye!")
           break
        else:
            print("Invalid choice,try again.")             
            
            
                
    