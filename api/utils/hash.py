from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class Hash:

    @staticmethod
    def hash(key: str):
        return make_password(key)

    @staticmethod
    def checkHash(key: str, hash: str):
        return check_password(key, hash)
