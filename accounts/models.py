



from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save, post_delete
from django.conf import settings


# Create your models here.
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, password=None,**extra_fields):
        if not email:
            raise ValueError("User must have an Email Address")
        if not username:
            raise ValueError("User must have a Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,**extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # to create superuser(admin)
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_whitelisted=True
        user.save(using=self._db)
        return user
    



# before run, create media directory in project root,
def get_profile_image_file_path(self, filename):
    return f'profile_images/{self.username}/profile_image.png'


# add default profile in there
def default_profile_image_path():
    return 'default_profile/default_profile.png'


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", unique=True, null=False,blank=False)
    username = models.CharField(max_length=30, unique=True, verbose_name="username", null=False,blank=False)
    is_active = models.BooleanField(default=True)
    is_whitelisted=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(
        max_length=255, blank=True, null=True,
        upload_to=get_profile_image_file_path,
        default=default_profile_image_path
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.get_or_create(user=instance)


# @receiver(post_delete, sender=settings.AUTH_USER_MODEL)
# def delete_auth_token(sender, instance=None, **kwargs):
#     if instance:
#         Token.objects.filter(user=instance).delete()
