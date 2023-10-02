from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def Hash(password):
    return passwd_context.hash(password)
