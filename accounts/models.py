from django.apps import apps
from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given phone, email, and password.
        """
        if not phone:
            raise ValueError('The given phone must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    STUDENT = 1
    TEACHER = 2
    STAFF = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (STAFF, 'staff'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    username = None
    phone_regex = RegexValidator(
        regex=r'^9\d{9}', message="Enter a valid phonenumber 9XXXXXXXXX")
    phone = models.CharField(
        validators=[phone_regex], max_length=10, unique=True)
    role = models.ManyToManyField(Role, blank=True)

    otp = models.CharField(max_length=6, blank=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)

    otp_reset = models.CharField(max_length=6, blank=True)
    otp_reset_expiry = models.DateTimeField(blank=True, null=True)

    reset_token = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = "phone"

    objects = UserManager()

    @property
    def is_student(self):
        return self.role.id == Role.STUDENT

    @property
    def is_teacher(self):
        return self.role.id == Role.TEACHER

    @property
    def is_manager(self):
        return self.role.id == Role.STAFF

    @property
    def is_admin(self):
        return self.role.id == Role.ADMIN

    @property
    def is_otp_time_valid(self):
        return self.otp_expiry > timezone.now()

    @property
    def is_otp_reset_time_valid(self):
        return self.otp_reset_expiry > timezone.now()

    def validate_otp(self, value):
        return int(self.otp) == value

    def validate_otp_reset(self, value):
        return int(self.otp_reset) == value

    def __str__(self):
        return f"{self.phone}({self.get_full_name()})"


def image_upload_location(instance, filename):
    return f'profile/{instance.user.phone}/{filename}'


class Profile(models.Model):
    # it is imported here due to the ciruclar dependency
    # Course model contains user get which is imported above this import.
    from courses.models import CourseCategory
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=image_upload_location, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    college_name = models.CharField(max_length=100, null=True, blank=True)
    faculty = models.CharField(max_length=100, null=True, blank=True)
    admission_year = models.DateField(null=True, blank=True)
    interests = models.ManyToManyField(CourseCategory, blank=True)
    extra_content = models.JSONField(default=dict, blank=True, null=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.phone
