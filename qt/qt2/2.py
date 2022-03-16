class UserException(Exception):
    pass


class InvaliUserNameException(UserException):
    pass


def user_name(name):
    if name.isdigit():
        raise InvaliUserNameException("Неверное имя пользователя")
    else:
        pass


while True:
    try:
        name = input()
        user_name(name)
        break
    except InvaliUserNameException:
        print("Неверное имя")