from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Home(models.Model):
    email = models.EmailField(max_length=200)
    password = models.TextField(max_length=8)
    con_password = models.TextField(max_length=8)
    fullname = models.TextField(max_length=20)
    username = models.TextField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    message = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name


class Softwares(models.Model):
    names: str = models.CharField(max_length=200)

    def __str__(self):
        return self.names

class SoftwareType(models.Model):     ### this class is for what kind of softwares do the customer want . Business, education etc.
    softName = models.CharField(max_length=200)

    def __str__(self):
        return self.softName

 
class Order(models.Model):
    customer_name = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    soft_name = models.CharField(max_length=120,null=True)
    # software = models.ForeignKey(Softwares, on_delete=models.SET_NULL, null=True)
    software = models.CharField(max_length=200,null=True)
    # soft_type = models.ForeignKey(SoftwareType,on_delete=models.SET_NULL,null=True)
    # soft_time = models.DateTimeField(max_length=120)
    soft_amount = models.DecimalField(max_digits=10, decimal_places=2)
    soft_desc = models.TextField(null=True, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.soft_name


class GetJob(models.Model):
    name = models.CharField(max_length=120)
    UserName = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=13)
    education = models.CharField(max_length=120)
    qualification = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    your_skills = models.CharField(max_length=120)
    ever_worked = models.CharField(max_length=120)
    jobrole = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    describe = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.UserName} {self.name} {self.jobrole}"
