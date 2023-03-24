from django.contrib.auth.base_user import BaseUserManager

class UserModelManager(BaseUserManager):
    use_in_migrations = True




    def _create_user(self, email, password, **extra_data):

        """
        Create and save user with the given email and password
        """

        if not email:
            raise ValueError('The given email must be set!')

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_data)
        user.set_password(password)
        user.save(using=self_.db)
        return user

    def create_user(self, email, password=None, **extra_data):

        if not email:
            raise ValueError('Phone number is required!')

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_data)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_data):
        extra_data.setdefault('is_staff', True)
        extra_data.setdefault('is_superuser', True)
        extra_data.setdefault('is_active', True)

        if extra_data.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')

        if extra_data.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
    

        return self.create_user(email, password, **extra_data)