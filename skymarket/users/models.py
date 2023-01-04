from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    ADMIN = "admin", _("admin")
    USER = "user", _("user")


class User(AbstractBaseUser):
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    first_name = models.CharField(
        max_length=20,
        verbose_name="Имя",
        help_text="Введите свое имя",
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name="Фамилия",
        help_text="Введите свою фамилию",
    )
    phone = PhoneNumberField(
        unique=True,
        verbose_name="номер телефона",
        help_text="Введите свой номер телефона",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="адрес эл. почты",
        help_text="Введите свой адрес эл. почты",
    )
    role = models.CharField(
        max_length=5,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Выберите роль пользователя",
    )
    image = models.ImageField(
        upload_to="photos/",
        verbose_name="Фото",
        help_text="Загрузите вашу фотографию",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="Активен ли аккаунт",
        help_text="Укажите, активен ли ваш аккаунт",
    )

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
