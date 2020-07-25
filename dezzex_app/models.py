from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=70)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name

    def isExists(self):
        if Customer.objects.filter(phone=self.phone):
            return True
        return False