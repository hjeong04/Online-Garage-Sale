from data.users import User


def create_account() -> User:
    user = User.objects
    return user


def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user
