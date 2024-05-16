from ..models.user import UserModel


class UserService:
    def createUser(self, data: dict):
        # Create user in database
        username, email, password = data.values()
        user = UserModel.objects.create(
            username=username, email=email, password=password
        )
        return user

    def getUserByUsername(self, username: str):
        # Get user by username
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            user = None
        return user

    def getUserById(self, userId: str):
        # Get user by id
        try:
            user = UserModel.objects.get(id=userId)
        except UserModel.DoesNotExist:
            user = None
        return user

    def updateUserPassword(self, userId: str, password: str):
        # Update user password
        try:
            user = UserModel.objects.get(id=userId)
        except UserModel.DoesNotExist:
            user = None
        if user:
            user.password = password
            user.save()
        return user
