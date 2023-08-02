FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_args):
    """
    Doc string!
    :param filepath:
    :param todos_args:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)


print(__name__)
# Only execute this function when I want to.
if __name__ == '__main__':
    print("Hello from functions!")
