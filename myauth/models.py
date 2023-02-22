from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_midlevel = models.BooleanField(default=False)
    is_lowlevel = models.BooleanField(default=False)
    is_highlevel = models.BooleanField(default=False)
    def __str__(self):
        return self.username


class Mid_level_User(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.first_name)



class Low_level_User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.first_name)


class High_level_User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.first_name)

class Form(models.Model):
    form_name  = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{}".format(self.form_name)

class Input(models.Model):
    INPUT_TYPES = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio'),
    )
    input_type = models.CharField(choices= INPUT_TYPES, max_length=255)
    def __str__(self):
        return "{}".format(self.input_type)

class Action(models.Model):
    ACTION_TYPES = (
        ('Submit', 'Submit'),
        ('Cancel', 'Cancel'),
    )
    action = models.CharField(choices= ACTION_TYPES, max_length=255)
    def __str__(self):
        return "{}".format(self.action)


class FormStructure(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    input_type = models.ForeignKey(Input, on_delete=models.CASCADE)
    input_name=models.CharField(max_length=255, blank=True, null=True)
    is_required = models.BooleanField(default=False)
    def __str__(self):
        return "{}".format(self.form.form_name)

class FormValues(models.Model):
    form = models.ForeignKey(FormStructure, on_delete=models.CASCADE)
    values = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.form.form.form_name)