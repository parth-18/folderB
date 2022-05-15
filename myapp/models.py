from django.db import models

# Create your models here.
class S_Data(models.Model):
    u_type = models.CharField(max_length=50,default='')
    f_name = models.CharField(max_length=50,default='')
    u_name = models.CharField(max_length=50,default='')
    e_mail = models.EmailField(max_length=50,default='')
    phone = models.CharField(max_length=10,default='')
    gender = models.CharField(max_length=10,default='')
    dob = models.DateField(blank=True,null=True)

    # def __str__(self):
    #     return self.f_name

class T_Data(models.Model):
    u_type = models.CharField(max_length=50,default='')
    f_name = models.CharField(max_length=50,default='')
    e_mail = models.EmailField(max_length=50,default='')
    phone = models.CharField(max_length=10,default='')
    dob = models.DateField(blank=True,null=True)
    locality = models.CharField(max_length=30,default='')
    overview = models.TextField(default='')
    qualification = models.TextField(default='')
    expertise = models.TextField(default='')
    def partial(self):
        return self.expertise.split(',')
    languages = models.TextField(default='')
    rate = models.CharField(max_length=5,default='')
    mode = models.CharField(max_length=30,default='')

class Batch(models.Model):
    student = models.CharField(max_length=50,default='')
    tutor = models.CharField(max_length=50,default='')