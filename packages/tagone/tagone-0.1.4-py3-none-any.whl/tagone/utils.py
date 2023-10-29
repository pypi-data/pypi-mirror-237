import re


def check_email(email):
    if not email:
        return False
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    return bool(re.fullmatch(email_regex, email))
