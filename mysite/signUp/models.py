from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    user_name = models.CharField(max_length = 200, default = 'old_user')
    email = models.EmailField()
    password =  models.CharField(max_length = 200)

    def __str__(self):
        return self.email

