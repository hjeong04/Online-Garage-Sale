from colorama import Fore
from infrastructure.switchlang import switch
import infrastructure.state as state


def run():
    print(' *********** Welcome to HOGS *************')
    print()

    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case('c', create_account)
            s.case('l', login_to_account)
            s.case('h', host_gs)
            s.case('v', visit_gs)
            s.case('p', view_past_gs)
            s.case('x', exit_app)
            s.case('', lambda: None)
            s.default(unknown_commnad)

        if action:
            print()


def show_commands():
    print("Would you like to:")
    print("[C] Create an account")
    print("[L] Login to your account")
    print("[H] Host a new garage sale")
    print("[V] Visit a garage sale")
    print("[P] View past garage sales")
    print("[X] Exit app")
    print()


def create_account():
    """ Allows the user to create a new account
    """


def login_to_account():
    """ Allows the user to login to their account
    """


def host_gs():
    """ Allows the user to host a garage sale
    """


def visit_gs():
    """ Allows the user to visit a garage sale
    """


def view_past_gs():
    """ Allows the user to view past garage sales they hosted / attended
    """


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}'

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def unknown_commnad():
    print("Sorry we didn't understand that command")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
