from __future__ import unicode_literals
from django.db import models
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#first name = letters only < 2
#last name same
# email valid format 
# more than 8 characters and match confirmation

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must have more than two characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must have more than two characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please follow correct email format'
        if postData['password'] != postData['password_conf']:
            errors['password'] = 'Passwords need to match'
        if len(postData['password']) < 2:
            errors['password'] = 'Password needs to be at least 8 characters'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
