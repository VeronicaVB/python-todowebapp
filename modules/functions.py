import os

FILEPATH: str = "todos.txt"


def check_exist():
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, "w") as file:
            pass


def get_todos(filepath=FILEPATH):
    check_exist()
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

    check_exist()
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)


print(__name__)
# Only execute this function when I want to.
if __name__ == '__main__':
    print("Hello from functions!")
