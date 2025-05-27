from django.contrib.auth.models import UserManager


class CustomUserManger(UserManager):
    def create_user(self, username, email, phone=None, password=None, **extra_fields):
        user =self.model(
            username = username,
            phone = phone,
            email = email,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, username, email,phone=None, password=None, **extra_fields):
        return self.create_user(username,phone=phone,
                                email=email,
                                password=password,
                                **extra_fields)
