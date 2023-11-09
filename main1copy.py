def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        # todos = get_todos(filepath="todos.txt")
        todos = get_todos("todos.txt")

        todos.append(todo)
        todos.append('\n')

        write_todos("todos.txt", todos)

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()


    elif user_action.startswith('show'):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos("todos.txt")

        # new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            # item = item.title()
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos("todos.txt")
            print('Here is todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            print('Here is how it will be', todos)

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.:")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
        # case _:
        #     print("Hey, you entered an unknown command")
    else:
        print("Command is not valid")

print("Bye!")