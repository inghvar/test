from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.core.mail import send_mail


class Company(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'Компании'



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)
    username = models.CharField('Ник', max_length=50)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    is_custom_role_1 = models.BooleanField(default=False)
    is_custom_role_2 = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def email_user(self, *args, **kwargs):
        send_mail(
            '{}'.format(args[0]),
            '{}'.format(args[1]),
            '{}'.format(args[2]),
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
