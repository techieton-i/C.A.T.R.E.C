from django.contrib.auth.models import BaseUserManager
# from . import constants as user_constants


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, reg_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            reg_number=reg_number,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.is_active = True
        # user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        # user.user_type = user_constants.SUPERUSER
        user.set_password(password)
        user.save()
        return user
