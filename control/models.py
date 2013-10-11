from django.db import models

# Create your models here.

class user(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField(blank=True,verbose_name='e-mail')
    group = models.SmallIntegerField()
    enable = models.SmallIntegerField()

    class Admin:
        pass

class user_login_history(models.Model):
    ip = models.GenericIPAddressField()
    user = models.CharField(max_length=30)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()
    success = models.SmallIntegerField()

class competence(models.Model):
    user = models.CharField(max_length=30)
    group = models.SmallIntegerField()
    access_machine = models.CharField(max_length=1024)
    deny_machine = models.CharField(max_length=1024)
    access_cmd = models.CharField(max_length=1024)
    deny_cmd = models.CharField(max_length=1024)

class machine(models.Model):
    ip = models.GenericIPAddressField()
    desc = models.CharField(max_length=1024)
    cpu = models.CharField(max_length=100)
    mem = models.CharField(max_length=100)
    disk = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    def __unicode__(self):
        return self.ip


class cmd(models.Model):
    cmd = models.CharField(max_length=100)
    cmd_desc = models.CharField(max_length=1024)
    group_cmd = models.CharField(max_length=100)
    group_cmd_desc = models.CharField(max_length=1024)
    file = models.CharField(max_length=200)
    def __unicode__(self):
        return self.cmd

class cmd_history(models.Model):
    ip = models.GenericIPAddressField()
    user = models.CharField(max_length=30)
    cmd = models.CharField(max_length=100)
    success = models.SmallIntegerField()



