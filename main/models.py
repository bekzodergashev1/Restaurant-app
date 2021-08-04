from django.db import models


class Menu_category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images')
    price = models.FloatField()
    menu_category = models.ForeignKey(Menu_category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    messages = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Table_category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_category = models.ForeignKey(Table_category, on_delete=models.CASCADE)
    people = models.IntegerField(blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.people

class Order(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name