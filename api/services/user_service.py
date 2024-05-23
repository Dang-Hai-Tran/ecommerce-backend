from api.models.user_model import UserModel
from api.utils.hash import Hash


class UserService:
    @staticmethod
    def createUser(username, email, password):
        # Create user in database
        user = UserModel.objects.create(
            username=username, email=email, password=Hash.hash(password)
        )
        return user

    @staticmethod
    def getUserByUsername(username: str):
        # Get user by username
        user = UserModel.objects.get(username=username)
        return user

    @staticmethod
    def getUserById(userId: str):
        # Get user by id
        user = UserModel.objects.get(id=userId)
        return user

    @staticmethod
    def updateUserPassword(userId: str, password: str):
        # Update user password
        user = UserModel.objects.get(id=userId)
        if user:
            user.password = Hash.hash(password)
            user.save()
        return user
