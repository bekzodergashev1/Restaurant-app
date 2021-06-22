from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reservations(models.Model):
    place_choices = (
        ('LUX-1', 'LUX-1'),
        ('LUX-2', 'LUX-2'),
        ('LUX-3', 'LUX-3'),
        ('LUX-4', 'LUX-4'),
        ('LUX-5', 'LUX-5'),
        ('Ordinary places-1', 'Ordinary places-1'),
        ('Ordinary places-2', 'Ordinary places-2'),
        ('Ordinary places-3', 'Ordinary places-3'),
        ('Ordinary places-4', 'Ordinary places-4'),
        ('Ordinary places-5', 'Ordinary places-5'),
    )
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    people = models.CharField(max_length=2, blank=True)
    place = models.CharField(max_length = 20, choices = place_choices, default = '1')

    def __str__(self):
        return f'Name: {self.name}'


class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    messages = models.CharField(max_length=225)

    def __str__(self):
        return self.name
