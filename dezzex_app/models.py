from django.db import models
from django.utils import timezone

class Customer(models.Model):
    full_name = models.CharField(max_length=70)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    image = models.ImageField(upload_to='upload/customers/',default='',null=True)
    registration_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

    def isExists(self):
        if Customer.objects.filter(phone=self.phone):
            return True
        return False

class LogFile(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='logs')
    login_time = models.DateTimeField(default=timezone.now)