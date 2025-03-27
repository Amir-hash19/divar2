from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserAccountManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email")
        else:
            email = self.normalize_email(email)
            user = self.model(email = email, name = name)
            user.set_password(password)
            user.save()

            return user
        

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    age = models.PositiveIntegerField(default=0)
    is_superuser = models.BooleanField(default=False)



    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(age__gte=18), name="age_gte_18")
        ]

    class Meta:
        unique_together =[["email", "name"]]

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]    
        


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = UserAccountManager()


    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.name