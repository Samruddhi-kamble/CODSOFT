todo=[]
while True:
    print("\n...To-Do Lists...")
    print("1.Add Task")
    print("2.View Task")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Exit")
    
    ch=input("Enter your choice(1-5):")

    if ch=='1':
        task=input("Enter your task:")
        todo.append(task)
        print("Task added successfully")

    elif ch=='2':
        if len(todo)==0:
            print("No tasks available")
        else:
            print("Your Tasks:")
            for i in range(len(todo)):
                print(i+1,".",todo[i])
    
    elif ch=='3':
        if len(todo)==0:
            print("No tasks to update")
        else:
            n=int(input("Enter task number to update:"))
            if n>=1 and n<=len(todo):
                new_task=input("Enter new task:")
                todo[n-1]=new_task
                print("Task updated")
            else:
                print("Invalid task number")
    
    elif ch=='4':
        if len(todo)==0:
            print("No tasks to delete")
        else:
            n=int(input("Enter task number to delete:"))
            if n>=1 and n<=len(todo):
                todo.pop(n-1)
                print("Task deleted")
            else:
                print("Invalid task number")
    
    elif ch=='5':
        print("Thank you!")
        break
    else:
        print("Please enter a valid choice")