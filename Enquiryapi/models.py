from django.db import models
from django.core.validators import RegexValidator


status =(
    ("Not Contacted", "Not Contacted"),
    ("Converted", "Converted"),
    ('Junk', "Junk")
)


# Create your models here.

class Conferencedata(models.Model):
    Name = models.CharField(max_length=50)



class product(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class enquiryDatas(models.Model):
    Name = models.CharField(max_length=50)
    OrganizationName = models.CharField(max_length=200)
    Email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    status = models.CharField(max_length=50, choices=status)
    MobileNumber = models.CharField(validators=[phone_regex], max_length=17)
    Location = models.CharField(max_length=200)
    message = models.CharField(max_length=500, blank=True)
    Interesteds = models.ManyToManyField(product)
    conferencedata = models.ForeignKey(Conferencedata, on_delete=models.SET_NULL , null=True , blank=True)
