from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator 

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
    )

    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Enter a valid email address.")],
        error_messages={'unique': "A user with this email already exists."},
    )
    password = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(8, message="Password must be at least 8 characters long."),
            RegexValidator(r'[A-Z]', message="Password must contain at least one uppercase letter."),
            RegexValidator(r'[a-z]', message="Password must contain at least one lowercase letter."),
        ],
    )
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(1)], verbose_name="First Name")
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(1)], verbose_name="Last Name")
    phone = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(r'^\d{10}$', message="Phone number must be exactly 10 digits."),
        ],
        verbose_name="Phone Number",
    )
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="City")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="State")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Country")
    pincode = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(r'^\d{6}$', message="Pincode must be exactly 6 digits."),
        ],
        verbose_name="Pincode",
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='author')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'pincode', 'role']

    def __str__(self):
        return self.email

