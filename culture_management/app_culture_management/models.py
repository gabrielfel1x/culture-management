from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Evento(models.Model):
    TIPOS_EVENTO = [
        ('show', 'Show musical'),
        ('teatro', 'Apresentação teatral'),
        ('orquestra', 'Orquestra'),
        ('musical', 'Musical'),
        ('humor', 'Show de humor'),
    ]

    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPOS_EVENTO)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    entrada_gratuita = models.BooleanField(default=False)
    vagas = models.PositiveIntegerField(null=True, blank=True, help_text="")

    def __str__(self):
        return self.titulo

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('O Email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, name, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']