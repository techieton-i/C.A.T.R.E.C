from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from users.managers import UserManager
from . import constants as user_constants
from django.core.exceptions import ValidationError
# from .forms import validate_reg
from .populate import populator

# Create your models here.


def validate_reg(value):
    try:
        x = SignUpAccess.objects.get(reg_key=value)
        if x.is_used == True:
            raise ValidationError(
                message='Your validation number is used already',
            )
    except SignUpAccess.DoesNotExist:
        raise ValidationError(
            message='Your validation number does not exist',
        )


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        max_length=75,
        # db_index=True,
        primary_key=True,
        verbose_name='email address'
    )
    reg_number = models.CharField(
        max_length=12,
        unique=True,
        null=True,
        validators=[validate_reg]
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TYPE_CHOICES, null=True, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name='user_profile')
    phone = models.CharField(max_length=255, blank=True, null=True)
    sex = models.PositiveSmallIntegerField(
        choices=((1, 'Male'), (2, 'Female'),), null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class SignUpAccess(models.Model):
    reg_key = models.CharField(primary_key=True, max_length=12, unique=True)
    user_email = models.EmailField(max_length=100, blank=True, null=True)
    user_first_name = models.CharField(max_length=100, blank=True, null=True)
    user_last_name = models.CharField(max_length=100, blank=True, null=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reg_key


class ContactForm(models.Model):
    sender_email = models.EmailField(max_length=100)
    sender_full_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True, primary_key=True)
    message = models.TextField()

    def __str__(self):
        return self.sender_full_name


# print(SignUpAccess.objects.count())

# z = populator(150)
# for entry in z:
#     print(entry)
#     u = SignUpAccess(reg_key=entry)
#     u.save()


# uuu = User.objects.get(email='toluwalope@gmail.com')
# print(uuu.last_name)
# print(uuu.user_profile.sex)
# print(UserProfile.objects.all())
# r = UserProfile.objects.get(user=uuu)
# print(r)
