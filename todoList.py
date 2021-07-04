
x="[x]"
ListTodo = []
while True:
    print("Welcome to Todo List program")
    print("enter 1:show todo list")
    print("enter 2:add todo list")
    print("enter 3:delete todo list")
    print("enter 4:Tick it done")
    print("enter 0:Exit")
    choice = input("enter your number:")

    if choice=="1":
        print(ListTodo)
        i = 0
        for data in ListTodo:
            i = i + 1
            print(i, data['name'], "     ", data['isDone'])

    elif choice=="2":
        name=input("Note:")
        DictTodo = {'name': name, 'isDone': x}
        ListTodo.append(DictTodo)

    elif choice=="3":
        i=0
        for data in ListTodo:
            i=i+1
            print(i,data['name'],"     ",data['isDone'])
        print("Enter number for delete:")
        DeleteData = int(input('Enter number:'))-1
        ListTodo.remove(ListTodo[DeleteData])

    elif choice=="4":
        i = 0
        for data in ListTodo:
            i = i + 1
            print(i, data['name'], "     ", data['isDone'])
        print("ใส่ข้อที่ต้องการบอกว่าทำแล้ว")
        w = int(input("Enter number:"))-1
        ListTodo[w]['isDone']="[/]"

    elif choice=="0":
        break
    else:
        print("invalid number ")



