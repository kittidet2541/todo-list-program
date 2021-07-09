def showListTodo():
    i = 0
    for data in listTodo:
        i = i + 1
        print(i, data['name'], "     ", data['isDone'])

def deleteListTodo():

    print("Enter number for delete:")
    deleteData = int(input('Enter number:')) - 1
    listTodo.remove(listTodo[deleteData])

def addListTodo():
    name = input("Note:")
    dictTodo = {'name': name, 'isDone': []}
    listTodo.append(dictTodo)

def doneListTodo():
    print("ใส่ข้อที่ต้องการบอกว่าทำแล้ว")
    w = int(input("Enter number:")) - 1
    listTodo[w]['isDone'] = "[x]"

listTodo = []
while True:
    print("Welcome to Todo List program")
    print("enter 1:show todo list")
    print("enter 2:add todo list")
    print("enter 3:delete todo list")
    print("enter 4:Tick it done")
    print("enter 0:Exit")
    choice = input("enter your number:")

    if choice=="1":
        showListTodo()

    elif choice=="2":
        showListTodo()
        addListTodo()

    elif choice=="3":
        showListTodo()
        deleteListTodo()

    elif choice=="4":
        showListTodo()
        doneListTodo()

    elif choice=="0":
        break

    else:
        print("invalid number ")
        ################################
