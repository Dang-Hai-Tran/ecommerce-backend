from ..models.user_model import UserModel


class UserService:
    @staticmethod
    def createUser(username, email, password):
        # Create user in database
        user = UserModel.objects.create(
            username=username, email=email, password=password
        )
        return user
    @staticmethod
    def getUserByUsername(username: str):
        # Get user by username
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            user = None
        return user
    @staticmethod
    def getUserById(userId: str):
        # Get user by id
        try:
            user = UserModel.objects.get(id=userId)
        except UserModel.DoesNotExist:
            user = None
        return user
    @staticmethod
    def updateUserPassword(userId: str, password: str):
        # Update user password
        try:
            user = UserModel.objects.get(id=userId)
        except UserModel.DoesNotExist:
            user = None
        if user:
            user.password = password
            user.save()
        return user
