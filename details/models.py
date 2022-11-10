from django.db import models

# Create your models here.

class person(models.Model):
    POSITIONS = (
        ('founder', 'founder'),
        ('sponsor', 'sponsor'),
        ('ict', 'ict'),
    )
    first_name  = models.CharField(max_length=120)
    last_name   = models.CharField(max_length=120)
    position    = models.CharField(max_length=120, choices=POSITIONS)
    person_image = models.ImageField(upload_to='images/person/')

    def __str__(self):
        return self.last_name
    
class laptop(models.Model):
    NATURE = (
        ('refurbished', 'refurbished'),
        ('new', 'new'),
    )

    name   = models.CharField(max_length=120)
    ram    = models.IntegerField()
    storagge = models.IntegerField()
    condition = models.CharField(max_length=120, choices=NATURE)
    descriptions  = models.TextField()
    image         = models.ImageField(upload_to='images/laptops/')

    def __str__(self):
        return self.name
