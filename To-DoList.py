def task():
    print("----Welcome to the To-Do List---- ")
    tasks = []
    total_tasks = int(input("How many tasks do you want to add? "))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
        
    print(f"Today's total tasks: {tasks}")
    
    while True:
        operation = int(input("Enter1-Add\n2-Update\n3-Delete\n4-View,5-Exit/Stop/"))
        if operation == 1:
            new_task = input("Enter the task you want to add: ")
            if new_task in tasks:
                print("Already exist")
            else:
                tasks.append(new_task)
            print(f"Your task {new_task} succesfully added...")

        elif operation == 2:
            upd_task = input("Enter the task you want to update: ")
            if upd_task in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(upd_task)
                tasks[ind] = up
                print (f"Updated Task: {up}")
        
        elif operation == 3:
            del_task = input("Enter the task you want to delete: ")
            if del_task in tasks:
                ind = tasks.index(del_task)
                del tasks[ind]
                print(f"Your task {del_task} has been deleted...")
        
        elif operation == 4:
            print(tasks)
        
        elif operation == 5:
           break 


task()